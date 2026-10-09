import torch
from liquid_memory_agents.agents.rag import RAGMemoryAgent, TurnRecord


class Encoder:
    dimension = 3

    def encode(self, text):
        if isinstance(text, list):
            return torch.stack([self.encode(t) for t in text])
        return torch.tensor([1.0, 0.2 if "apple" in text else 0.7, 0.3])


class Answerer:
    embedding_dimension = 5

    def answer(self, *args, **kwargs):
        return "test"


def test_timestamp_preserves_selected_records_and_orders_ties():
    a = RAGMemoryAgent(Encoder(), Answerer(), top_k=3)
    a.turns = [
        TurnRecord(str(i), torch.tensor([1.0, float(i), 0.0]), t, str(i))
        for i, t in enumerate(["2024-03", "2024-01", "2024-01"])
    ]
    _, before = a.get_memory_context("q")
    a.timestamp_order = True
    context, after = a.get_memory_context("q")
    assert before["turn_indices"] == after["turn_indices"]
    assert (
        context.index("[Session id: 1]")
        < context.index("[Session id: 2]")
        < context.index("[Session id: 0]")
    )


from liquid_memory_agents.datasets.synthetic import generate_examples


def test_cue_free_preserves_truth_and_distractors():
    old = generate_examples(30, 1000, 11)
    new = generate_examples(30, 1000, 11, correction_style="cue_free")
    for a, b in zip(old, new):
        assert (a.answer, a.evidence_indices, a.ground_truth_trace, a.timestamps) == (
            b.answer,
            b.evidence_indices,
            b.ground_truth_trace,
            b.timestamps,
        )
        assert a.example_id != b.example_id
        for i, (x, y) in enumerate(zip(a.turns, b.turns)):
            if x != y:
                assert i == a.evidence_indices[-1]
                assert not any(
                    cue in y.casefold()
                    for cue in [
                        "correction:",
                        "actually",
                        "instead",
                        "not ",
                        "now ",
                        "changed",
                        "currently",
                        "update:",
                    ]
                )


def test_evaluation_exports_with_stub_reader(tmp_path, monkeypatch):
    # This verifies runner wiring and artifact format, not model accuracy.
    import importlib.util, sys, yaml, json
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    sys.path.insert(0, str(root / "scripts"))
    spec = importlib.util.spec_from_file_location(
        "review_smoke_runner", root / "scripts/run_synthetic.py"
    )
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    from liquid_memory_agents.embeddings import LexicalAugmentedEncoder

    class StubEncoder(Encoder):
        def __init__(self, *args, **kwargs):
            pass

    class StubReader(Answerer):
        def __init__(self, *args, **kwargs):
            pass

        def answer_with_prefix(self, *args, **kwargs):
            return "test"

    config = m.load_config(root / "configs/synthetic.yaml")
    config["run"]["output_root"] = str(tmp_path / "runs")
    config["liquid"].update(state_dim=4, slots=2, prefix_tokens=2)
    config["liquid"]["lexical_memory"]["capacity"] = 8
    config["dataset"].update(smoke_examples=2, smoke_horizon=10)
    enc = LexicalAugmentedEncoder(StubEncoder(), config["liquid"]["lexical_bytes"])
    from liquid_memory_agents.agents.liquid import LALMMemoryAgent as Agent

    agent = Agent(enc, StubReader(), state_dim=4, slots=2, prefix_tokens=2)
    config["dataset"]["correction_style"] = "cue_free"
    names = ["lalm", "lexical_only", "rag", "bounded_rag", "rag_timestamp"]
    checkpoint = tmp_path / "test.pt"
    torch.save(
        dict(
            format_version=1,
            modules={
                k: v.state_dict()
                for k, v in [
                    ("cell", agent.memory.cell),
                    ("reader", agent.reader),
                    ("adapter", agent.adapter),
                ]
            },
            config=config,
            seed=13,
            dataset_hashes={},
        ),
        checkpoint,
    )
    config.setdefault("evaluation", {})["agents"] = names
    cfg = tmp_path / "config.yaml"
    cfg.write_text(yaml.safe_dump(config))
    monkeypatch.setattr(m, "SentenceTransformerEncoder", StubEncoder)
    monkeypatch.setattr(m, "TransformersAnswerReader", StubReader)
    monkeypatch.setattr(
        sys,
        "argv",
        ["run_synthetic.py", "--config", str(cfg), "--checkpoint", str(checkpoint), "--smoke"],
    )
    m.main()
    predictions = next((tmp_path / "runs").rglob("predictions.jsonl"))
    rows = [json.loads(x) for x in predictions.read_text().splitlines()]
    assert len(rows) == 2 * len(names)
    assert {x["agent"] for x in rows} == set(names)
    for name in ["metrics.csv", "config.yaml", "dataset_manifest.json"]:
        assert (predictions.parent / name).is_file()
