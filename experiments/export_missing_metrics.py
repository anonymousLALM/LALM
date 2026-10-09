"""Export released-data diagnostics directly from completed metrics/per_type CSVs."""

from pathlib import Path
import csv, json, statistics
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]


def main():
    rows = []
    for receipt in sorted((ROOT / "results/evaluation_study/jobs").rglob("complete.json")):
        d = json.loads(receipt.read_text())
        j = d["job"]
        if j["dataset"] not in ["longmemeval", "locomo"]:
            continue
        if not (
            j["agent"] == "rag_timestamp"
            or (j["training_seed"] in [37, 41] and j["agent"] in ["lalm", "pure_liquid"])
        ):
            continue
        run = receipt.parent / d["result"]
        for name in ["metrics.csv", "per_type.csv"]:
            source = run / name
            for row in csv.DictReader(source.open()):
                for metric in [
                    "diagnostic_token_f1",
                    "diagnostic_exact_match",
                    "locomo_official_qa_score",
                ]:
                    if row.get(metric, "") == "":
                        continue
                    rows.append(
                        dict(
                            dataset=j["dataset"],
                            agent=j["agent"],
                            training_seed=j["training_seed"]
                            if j["agent"] != "rag_timestamp"
                            else "",
                            evaluation_seed=j["evaluation_seed"],
                            question_type=row.get("question_type", "all"),
                            metric=metric,
                            n=row["examples"],
                            value=float(row[metric]),
                            source=str(source.relative_to(ROOT)),
                            config=str((run / "config.yaml").relative_to(ROOT)),
                            predictions=str((run / "predictions.jsonl").relative_to(ROOT)),
                        )
                    )
    out = ROOT / "results/evaluation_study/missing_metrics"
    out.mkdir(exist_ok=True)

    def write(name, data):
        with (out / name).open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(data[0]))
            w.writeheader()
            w.writerows(data)

    write("per_seed.csv", rows)
    groups = defaultdict(list)
    for row in rows:
        groups[tuple(row[k] for k in ["dataset", "agent", "question_type", "metric"])].append(
            row["value"]
        )
    means = [
        dict(
            zip(["dataset", "agent", "question_type", "metric"], k),
            n_checkpoints=len(v) if k[1] != "rag_timestamp" else 0,
            mean=statistics.mean(v),
            sample_sd=statistics.stdev(v) if len(v) > 1 else "",
        )
        for k, v in groups.items()
    ]
    write("means.csv", means)
    text = [
        "# Missing released-data metrics",
        "",
        "Scores below are percentages. LALM/Pure Liquid summaries here cover seeds 37 and 41 only; they are not five-seed summaries. Timestamp RAG has no training checkpoint. Exact match is the existing diagnostic, not the LongMemEval official judge score.",
        "",
        "| Dataset | Method | Type | Metric | Mean +/- sample SD (%) |",
        "|---|---|---|---|---|",
    ]
    for x in means:
        text.append(
            f"| {x['dataset']} | {x['agent']} | {x['question_type']} | {x['metric']} | {100 * x['mean']:.2f}"
            + (f" +/- {100 * x['sample_sd']:.2f}" if x["sample_sd"] != "" else "")
            + " |"
        )
    (out / "RESULTS.md").write_text("\n".join(text) + "\n")
    print(out, len(rows), "metric rows")


if __name__ == "__main__":
    main()
