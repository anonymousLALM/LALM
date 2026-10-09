"""Export the completed five-checkpoint tool-task study."""

from pathlib import Path
from collections import defaultdict, Counter
import argparse, csv, json, statistics
import numpy as np
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "experiments"))
from paired_significance import inference


def write(path, rows):
    if rows:
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--item", type=int, choices=[4], default=4)
    a = ap.parse_args()
    suite = ROOT / "supplementary/agent_tasks/results"
    suite.mkdir(parents=True, exist_ok=True)
    data = defaultdict(dict)
    cost_counts = Counter()
    artifacts = []
    completed = 0
    for p in sorted((suite / "jobs").rglob("complete.json")):
        receipt = json.loads(p.read_text())
        j = receipt["job"]
        run = p.parent / receipt["result"]
        completed += 1
        artifacts.append(
            dict(
                job=p.parent.name,
                config=str((p.parent / "config.yaml").relative_to(ROOT)),
                predictions=str((run / "predictions.jsonl").relative_to(ROOT)),
                training_seed=j["seed"],
                evaluation_seed=j["e"],
            )
        )
        for line in (run / "predictions.jsonl").open(encoding="utf-8"):
            r = json.loads(line)
            agent = r["agent"]
            seed = j["seed"] if agent == "lalm" else "shared"
            metrics = (
                ["correct_tool", "exact_arguments", "full_success"]
                if a.item == 4
                else ["correct", "token_f1_diagnostic"]
                + (["locomo_official_qa_score"] if j["dataset"] == "locomo" else [])
            )
            metrics += [
                m
                for m in [
                    "write_ms_per_turn",
                    "read_ms",
                    "answer_ms",
                    "end_to_end_ms",
                    "logical_memory_MB",
                    "storage_disk_MB",
                ]
                if m in r
            ]
            for m in metrics:
                # Repeated baseline cost measurements stay separate; they are not training seeds.
                key = (agent, j["dataset"], j["style"], r.get("horizon", ""), seed, m)
                qid = r["example_id"]
                value = (
                    float(r[m]),
                    r["query"],
                    json.dumps(r["reference"], sort_keys=True),
                )
                if (
                    qid in data[key]
                    and m
                    in [
                        "correct",
                        "token_f1_diagnostic",
                        "locomo_official_qa_score",
                        "correct_tool",
                        "exact_arguments",
                        "full_success",
                    ]
                    and data[key][qid] != value
                ):
                    raise ValueError("Repeated shared baseline predictions differ: " + str(key))
                if m not in [
                    "correct",
                    "token_f1_diagnostic",
                    "locomo_official_qa_score",
                    "correct_tool",
                    "exact_arguments",
                    "full_success",
                ]:
                    count_key = (key, qid)
                    n = cost_counts[count_key]
                    if n:
                        value = (
                            (data[key][qid][0] * n + value[0]) / (n + 1),
                            value[1],
                            value[2],
                        )
                    cost_counts[count_key] += 1
                data[key][qid] = value
    rows = []
    means = []
    groups = defaultdict(list)
    tests = []
    for (agent, d, s, h, seed, m), values in sorted(data.items(), key=lambda x: str(x[0])):
        expected = 150 if d == "synthetic" else 450 if d == "longmemeval" else 1986
        complete = len(values) == expected
        value = statistics.mean(x[0] for x in values.values())
        rows.append(
            dict(
                agent=agent,
                dataset=d,
                style=s,
                horizon=h,
                training_seed=seed,
                metric=m,
                n_questions=len(values),
                complete=complete,
                value=value,
            )
        )
        if complete:
            groups[(agent, d, s, h, m)].append(value)
    for (agent, d, s, h, m), values in groups.items():
        means.append(
            dict(
                agent=agent,
                dataset=d,
                style=s,
                horizon=h,
                metric=m,
                n_seeds=len(values) if agent == "lalm" else 0,
                mean=statistics.mean(values),
                sample_sd=statistics.stdev(values) if len(values) > 1 else "",
            )
        )
    if a.item == 4:
        settings = {(d, s, h) for agent, d, s, h, seed, m in data if agent == "lalm"}
        for d, s, h in sorted(settings, key=str):
            for baseline in ["lexical_only", "rag", "rag_timestamp", "bounded_rag"]:
                for m in ["correct_tool", "exact_arguments", "full_success"]:
                    right = data.get((baseline, d, s, h, "shared", m))
                    aligned = []
                    ids0 = None
                    seeds = []
                    if not right:
                        continue
                    for seed in [7, 13, 23, 37, 41]:
                        left = data.get(("lalm", d, s, h, seed, m))
                        if not left or set(left) != set(right) or len(left) != 150:
                            continue
                        ids = sorted(left)
                        if any(left[q][1:] != right[q][1:] for q in ids):
                            raise ValueError("Unmatched question/reference")
                        delta = np.array([left[q][0] - right[q][0] for q in ids])
                        aligned.append(delta)
                        ids0 = ids
                        seeds.append(seed)
                        tests.append(
                            dict(
                                dataset=d,
                                style=s,
                                horizon=h,
                                metric=m,
                                left="lalm",
                                right=baseline,
                                training_seed=seed,
                                **inference(delta, ids, d, 10000, 20261001),
                            )
                        )
                    if len(seeds) == 5:
                        tests.append(
                            dict(
                                dataset=d,
                                style=s,
                                horizon=h,
                                metric=m,
                                left="lalm",
                                right=baseline,
                                training_seed="mean",
                                **inference(np.mean(aligned, axis=0), ids0, d, 10000, 20261001),
                            )
                        )
    for row in tests:
        row["p_holm"] = ""
    ordered = sorted(
        [i for i, r in enumerate(tests) if r["training_seed"] == "mean"],
        key=lambda i: tests[i]["p_raw"],
    )
    previous = 0
    for rank, i in enumerate(ordered):
        previous = max(previous, min(1, tests[i]["p_raw"] * (len(ordered) - rank)))
        tests[i]["p_holm"] = previous
    for name, values in [
        ("per_seed.csv", rows),
        ("means.csv", means),
        ("paired_tests.csv", tests),
        ("artifact_index.csv", artifacts),
    ]:
        write(suite / name, values)
    lines = [
        "# Memory inside simulated tool tasks",
        "",
        f"Completed jobs: {completed}. Shared baselines have no training-seed SD. Holm correction covers aggregate comparisons only.",
        "",
        "| Method | Dataset | Stream | Horizon | Metric | Checkpoints | Mean +/- SD |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in means:
        is_score = r["metric"] in [
            "correct",
            "token_f1_diagnostic",
            "locomo_official_qa_score",
            "correct_tool",
            "exact_arguments",
            "full_success",
        ]
        scale = 100 if is_score else 1
        v = f"{r['mean'] * scale:.3f}"
        v += f" +/- {r['sample_sd'] * scale:.3f}" if r["sample_sd"] != "" else ""
        v += " %" if is_score else ""
        lines.append(
            f"| {r['agent']} | {r['dataset']} | {r['style']} | {r['horizon']} | {r['metric']} | {r['n_seeds'] or 'shared'} | {v} |"
        )
    for title, name in [
        ("Per-seed values", "per_seed.csv"),
        ("Paired tests", "paired_tests.csv"),
        ("Prediction/config files", "artifact_index.csv"),
    ]:
        lines += ["", f"## {title}", ""]
        path = suite / name
        lines += (
            ["```csv", path.read_text(encoding="utf-8"), "```"]
            if path.exists()
            else ["No completed rows yet."]
        )
    (suite / "LALM_AGENT_TASKS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("Report refreshed:", suite, completed)


if __name__ == "__main__":
    main()
