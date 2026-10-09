"""Verify shipped result bytes and complete saved-study coverage."""

from pathlib import Path
import hashlib, json, csv

ROOT = Path(__file__).resolve().parents[1]


def digest(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()


def main():
    manifest = json.loads((ROOT / "results/publication_manifest.json").read_text())
    actual = {
        p.relative_to(ROOT).as_posix()
        for p in (ROOT / "results").rglob("*")
        if p.is_file()
        and p.name != "publication_manifest.json"
        and not any(x in p.parts for x in ["__pycache__", "reproduction", "smoke"])
    }
    assert actual == set(manifest["files"]), "Result inventory differs from manifest"
    for rel, expected in manifest["files"].items():
        p = ROOT / rel
        if not p.is_file() or digest(p) != expected:
            raise ValueError(f"Missing/changed artifact: {rel}; run git lfs pull if needed")
    original = [
        p
        for p in (ROOT / "results").rglob("best.pt")
        if "additional_study" not in p.relative_to(ROOT / "results").parts
    ]
    assert len(original) == 5
    for suite, n in [
        ("evaluation_study", 63),
        ("followup_study", 48),
        ("cue_free_completion", 6),
        ("additional_study/prefix_controls", 30),
    ]:
        receipts = list((ROOT / "results" / suite / "jobs").rglob("complete.json"))
        assert len(receipts) == n
        for p in receipts:
            d = json.loads(p.read_text())
            run = p.parent / d["result"]
            assert (run / "config.yaml").is_file()
            assert (
                run
                / ("checkpoints/best.pt" if d["job"]["dataset"] == "train" else "predictions.jsonl")
            ).is_file()
            for name, sha in d.get("release_artifact_sha256", {}).items():
                assert digest(p.parent / name) == sha
    rows = list(
        csv.DictReader((ROOT / "results/followup_study/significance/paired_tests.csv").open())
    )
    assert len(rows) == 84
    assert all(r["complete"] == "True" for r in rows)
    assert all(r["p_holm"] == "" for r in rows if r["training_seed"] != "mean")
    for suite, count in [
        ("additional_study/prefix_controls", 54),
    ]:
        tests = list(csv.DictReader((ROOT / "results" / suite / "paired_tests.csv").open()))
        assert len(tests) == count
        assert all(r["p_holm"] == "" for r in tests if r["training_seed"] != "mean")

    # Verify supplementary archive
    supp_files = manifest.get("supplementary_files", {})
    for rel, expected in supp_files.items():
        p = ROOT / rel
        if not p.is_file() or digest(p) != expected:
            raise ValueError(f"Missing/changed supplementary artifact: {rel}")
    supp_receipts = list((ROOT / "supplementary/agent_tasks/results/jobs").rglob("complete.json"))
    assert len(supp_receipts) == 36
    for p in supp_receipts:
        d = json.loads(p.read_text())
        run = p.parent / d["result"]
        assert (run / "config.yaml").is_file()
        assert (run / "predictions.jsonl").is_file()
        for name, sha in d.get("release_artifact_sha256", {}).items():
            assert digest(p.parent / name) == sha
    supp_tests = list(
        csv.DictReader((ROOT / "supplementary/agent_tasks/results/paired_tests.csv").open())
    )
    assert len(supp_tests) == 288
    assert all(r["p_holm"] == "" for r in supp_tests if r["training_seed"] != "mean")

    print(
        "Verified",
        len(manifest["files"]),
        f"manuscript result files; five checkpoints; 147 completed manuscript jobs; 84 complete follow-up test rows; and 36 supplementary agent-task jobs ({len(supp_files)} files).",
    )


if __name__ == "__main__":
    main()
