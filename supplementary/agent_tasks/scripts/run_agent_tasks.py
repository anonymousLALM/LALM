"""Memory-in-the-loop tool selection and argument generation; simulated tools only."""

from pathlib import Path
import argparse, csv, json, re, sys, time, hashlib, yaml

ARCHIVE_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from run_synthetic import build_agents, load_config, observe_sequence
from liquid_memory_agents.datasets.synthetic import generate_examples
from liquid_memory_agents.embeddings import (
    SentenceTransformerEncoder,
    LexicalAugmentedEncoder,
)
from liquid_memory_agents.llm.transformers_reader import TransformersAnswerReader
from liquid_memory_agents.utils import (
    seed_everything,
    create_run_directory,
    write_environment,
)


def task(example):
    person = re.search(r"\b[A-Z][A-Za-z]+-\d{4}\b", example.query).group()
    t = example.question_type
    a = example.answer
    if t in ["correction", "contradictory_update", "paraphrase"]:
        name = "book_trip"
        args = {"person": person, "destination": a}
        request = f"Book the preferred trip for {person}."
    elif t == "stable_fact":
        name = "record_profile"
        args = {"person": person, "hometown": a}
        request = f"Record the hometown of {person}."
    elif t == "repeated_fact":
        name = "reserve_venue"
        args = {"person": person, "venue": a}
        request = f"Reserve the preferred venue for {person}."
    elif t == "boolean":
        name = "set_response_preferences"
        args = {"person": person, "concise": a == "yes"}
        request = f"Set the concise response preference for {person}."
    elif t == "goal":
        name = "set_goal"
        args = {"person": person, "project": a}
        request = f"Set the project goal for {person}."
    elif t == "response_style":
        name = "send_message"
        args = {"person": person, "text_style": a}
        request = f"Send a message to {person} using the preferred text style."
    elif t == "temporal":
        name = "log_meeting"
        args = {"person": person, "collaborator": a}
        request = f"Log the earlier meeting partner of {person}."
    else:
        hometown, project = a.split(" and ")
        name = "update_profile"
        args = {"person": person, "hometown": hometown, "project": project}
        request = f"Record both hometown and current project for {person}."
    return request, {"name": name, "arguments": args}


def scores(raw, expected):
    try:
        r = json.loads(raw)
        tool = isinstance(r, dict) and r.get("name") == expected["name"]
        arguments = isinstance(r, dict) and r.get("arguments") == expected["arguments"]
    except (json.JSONDecodeError, TypeError):
        tool = arguments = False
    return dict(correct_tool=tool, exact_arguments=arguments, full_success=tool and arguments)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--checkpoint", type=Path, required=True)
    a = ap.parse_args()
    c = load_config(a.config)
    seed_everything(c["run"]["seed"])
    out = create_run_directory(c["run"]["output_root"], "agent_tasks")
    (out / "config.yaml").write_text(yaml.safe_dump(c))
    write_environment(out)
    encoder = SentenceTransformerEncoder(c["embedding"]["model"])
    liquid = LexicalAugmentedEncoder(encoder, int(c["liquid"].get("lexical_bytes", 256)))
    reader = TransformersAnswerReader(
        c["answer_llm"]["model"],
        max_input_tokens=c["answer_llm"]["max_input_tokens"],
        max_new_tokens=c["answer_llm"]["max_new_tokens"],
    )
    reader.system_prompt = (ARCHIVE_ROOT / "configs/system_prompt.txt").read_text()
    agents = build_agents(encoder, liquid, reader, c, a.checkpoint)
    schemas = json.loads((ARCHIVE_ROOT / "configs/tool_schemas.json").read_text())
    template = (ARCHIVE_ROOT / "configs/prompt.txt").read_text()
    rows = []
    ids = []
    with (out / "predictions.jsonl").open("w", encoding="utf-8") as f:
        for h in c["dataset"]["turns"]:
            for ex in generate_examples(
                50,
                h,
                c["run"]["seed"],
                c["dataset"].get("correction_style", "original"),
            ):
                request, expected = task(ex)
                query = template.format(schemas=json.dumps(schemas), request=request)
                for agent in agents:
                    agent.reset()
                    started = time.perf_counter()
                    # Use the same public write API and original memory query across methods.
                    observations = [
                        ({"role": role, "content": turn}, stamp, session)
                        for turn, stamp, role, session in zip(
                            ex.turns, ex.timestamps, ex.roles, ex.session_ids
                        )
                    ]
                    observe_sequence(agent, observations)
                    write_ms = (time.perf_counter() - started) * 1000
                    started = time.perf_counter()
                    context, metadata = agent.get_memory_context(ex.query)
                    read_ms = (time.perf_counter() - started) * 1000
                    started = time.perf_counter()
                    if agent.name == "lalm":
                        prediction = reader.answer_with_prefix(
                            query,
                            agent._last_read["prefix"] * agent.lexical_prefix_scale,
                            context=context,
                        )
                    else:
                        prediction = reader.answer(query, context)
                    generation_ms = (time.perf_counter() - started) * 1000
                    row = dict(
                        example_id=ex.example_id,
                        agent=agent.name,
                        horizon=h,
                        question_type=ex.question_type,
                        query=ex.query,
                        action_request=request,
                        reference=expected,
                        prediction=prediction,
                        **scores(prediction, expected),
                        write_ms_per_turn=write_ms / h,
                        read_ms=read_ms,
                        generation_ms=generation_ms,
                        end_to_end_ms=write_ms + read_ms + generation_ms,
                        config_seed=c["run"]["seed"],
                    )
                    rows.append(row)
                    f.write(json.dumps(row) + "\n")
                    f.flush()
                ids.append(ex.example_id)
    for filename, key in [("metrics.csv", None), ("per_type.csv", "question_type")]:
        summaries = []
        for agent in agents:
            for h in c["dataset"]["turns"]:
                types = sorted({x["question_type"] for x in rows}) if key else ["all"]
                for t in types:
                    selected = [
                        r
                        for r in rows
                        if r["agent"] == agent.name
                        and r["horizon"] == h
                        and (not key or r["question_type"] == t)
                    ]
                    if selected:
                        summaries.append(
                            dict(
                                agent=agent.name,
                                horizon=h,
                                question_type=t,
                                n=len(selected),
                                **{
                                    m: sum(float(x[m]) for x in selected) / len(selected)
                                    for m in [
                                        "correct_tool",
                                        "exact_arguments",
                                        "full_success",
                                        "write_ms_per_turn",
                                        "read_ms",
                                        "end_to_end_ms",
                                    ]
                                },
                            )
                        )
        with (out / filename).open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(summaries[0]))
            w.writeheader()
            w.writerows(summaries)
    (out / "dataset_manifest.json").write_text(
        json.dumps(
            {
                "example_ids": ids,
                "sha256": hashlib.sha256(json.dumps(ids).encode()).hexdigest(),
                "tool_schemas_sha256": hashlib.sha256(
                    (ARCHIVE_ROOT / "configs/tool_schemas.json").read_bytes()
                ).hexdigest(),
                "action_prompt_sha256": hashlib.sha256(
                    (ARCHIVE_ROOT / "configs/prompt.txt").read_bytes()
                ).hexdigest(),
                "system_prompt_sha256": hashlib.sha256(
                    (ARCHIVE_ROOT / "configs/system_prompt.txt").read_bytes()
                ).hexdigest(),
            }
        )
    )
    print(out)


if __name__ == "__main__":
    main()
