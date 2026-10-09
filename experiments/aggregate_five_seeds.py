"""Verify evaluation artifacts and aggregate five trained LALM checkpoints."""

from pathlib import Path
import csv, json, hashlib, statistics as st
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/evaluation_study"


def read(p):
    return list(csv.DictReader(p.open(encoding="utf-8")))


def sha(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1048576), b""):
            h.update(b)
    return h.hexdigest()


def write(name, rows):
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    receipts = list((OUT / "jobs").rglob("complete.json"))
    assert len(receipts) == 63
    files = []
    for p in receipts:
        d = json.loads(p.read_text())
        j = d["job"]
        run = p.parent / d["result"]
        omitted = (
            {
                x["path"]
                for x in json.loads((ROOT / "results/publication_omissions.json").read_text())
            }
            if (ROOT / "results/publication_omissions.json").exists()
            else set()
        )
        for name, digest in d.get("release_artifact_sha256", d["artifacts"]).items():
            artifact = p.parent / name
            if artifact.exists():
                assert sha(artifact) == digest, name
            else:
                assert artifact.relative_to(ROOT).as_posix() in omitted, name
        files.append(
            dict(
                group=j["group"],
                dataset=j["dataset"],
                agent=j["agent"],
                training_seed=j["training_seed"],
                evaluation_seed=j["evaluation_seed"],
                config=str((run / "config.yaml").relative_to(ROOT)),
                predictions=str((run / "predictions.jsonl").relative_to(ROOT))
                if j["dataset"] != "train"
                else "",
                metrics=str((run / "metrics.csv").relative_to(ROOT))
                if j["dataset"] != "train"
                else "",
                receipt=str(p.relative_to(ROOT)),
            )
        )
    write("artifact_index.csv", files)
    rows = []
    for r in read(ROOT / "results/historical/source_measurements.csv"):
        if (
            r["training_seed"] not in {"7", "13", "23"}
            or r["question_type"]
            or r["experiment"]
            not in {"synthetic", "prefix_1000", "prefix_5000", "longmemeval", "locomo"}
        ):
            continue
        rows.append(
            dict(
                experiment=r["experiment"],
                agent=r["agent"],
                training_seed=r["training_seed"],
                horizon=r["horizon"],
                metric=r["metric"],
                value=float(r["value"]),
            )
        )
    for r in read(OUT / "per_seed.csv"):
        if r["group"] != "extra-seeds" or r["question_type"] != "all":
            continue
        agent = r["agent"]
        exp = r["dataset"]
        metric = r["metric"]
        h = r["horizon"]
        if exp == "synthetic":
            if metric != "correct":
                continue
            metric = "accuracy"
            if agent.endswith("_prefix"):
                exp = "prefix_" + h
        elif exp in {"longmemeval", "locomo"}:
            metric = {
                "correct": "diagnostic_exact_match",
                "token_f1_diagnostic": "diagnostic_token_f1",
            }.get(metric, metric)
        rows.append(
            dict(
                experiment=exp,
                agent=agent,
                training_seed=r["training_seed"],
                horizon=h,
                metric=metric,
                value=float(r["value"]),
            )
        )
        if exp == "synthetic" and agent == "lalm" and h in {"1000", "5000"}:
            rows.append(
                dict(
                    experiment="prefix_" + h,
                    agent=agent,
                    training_seed=r["training_seed"],
                    horizon=h,
                    metric=metric,
                    value=float(r["value"]),
                )
            )
    g = defaultdict(lambda: defaultdict(list))
    for r in rows:
        k = (r["experiment"], r["agent"], r["horizon"], r["metric"])
        g[k][r["training_seed"]].append(r["value"])
    summary = []
    for k, streams in sorted(g.items()):
        v = {seed: st.mean(values) for seed, values in streams.items()}
        if set(v) != {"7", "13", "23", "37", "41"}:
            continue
        summary.append(
            dict(
                zip(["experiment", "agent", "horizon", "metric"], k),
                n_training_seeds=5,
                mean=st.mean(v.values()),
                sample_sd=st.stdev(v.values()),
            )
        )
    per_seed = []
    for k, streams in sorted(g.items()):
        for seed, values in sorted(streams.items()):
            per_seed.append(
                dict(
                    zip(["experiment", "agent", "horizon", "metric"], k),
                    training_seed=seed,
                    value=st.mean(values),
                )
            )
    write("five_seed_per_seed.csv", per_seed)
    write("five_seed_means.csv", summary)
    text = [
        "# Five-training-seed results",
        "",
        "Percentages; synthetic evaluation streams are averaged within each training seed before computing mean/sample SD across 7/13/23/37/41. Released-data scores are local diagnostics.",
        "",
        "| Experiment | Method | Horizon | Metric | Mean +/- SD (%) |",
        "|---|---|---:|---|---:|",
    ]
    for r in summary:
        text.append(
            f"| {r['experiment']} | {r['agent']} | {r['horizon']} | {r['metric']} | {100 * r['mean']:.2f} +/- {100 * r['sample_sd']:.2f} |"
        )
    (OUT / "FIVE_SEED_RESULTS.md").write_text("\n".join(text) + "\n")
    print("Verified 63 completed jobs.")
    print("\n".join(text))


if __name__ == "__main__":
    main()
