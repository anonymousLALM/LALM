"""Build the complete LALM evaluation experiment report from saved scores."""

from pathlib import Path
from collections import defaultdict
import csv, json, statistics as st

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/evaluation_study"
LABEL = {
    "lalm": "LALM",
    "pure_liquid": "Pure Liquid",
    "lexical_only": "Lexical-only",
    "rag": "Growing RAG",
    "bounded_rag": "Bounded RAG",
    "rag_timestamp": "Timestamp-ordered Growing RAG",
    "lalm_zero_prefix": "Zero prefix",
    "lalm_random_prefix": "Random prefix",
    "lalm_permuted_prefix": "Permuted prefix",
}


def read(p):
    return list(csv.DictReader(p.open(encoding="utf-8")))


def table(lines, heads, rows):
    lines.extend(
        ["", "| " + " | ".join(heads) + " |", "| " + " | ".join(["---"] * len(heads)) + " |"]
    )
    lines.extend("| " + " | ".join(map(str, row)) + " |" for row in rows)


def fmt(v):
    return (
        f"{100 * st.mean(v):.2f} +/- {100 * st.stdev(v):.2f}"
        if len(v) > 1
        else f"{100 * v[0]:.2f} (single evaluation)"
    )


def main():
    runs = read(OUT / "per_run.csv")
    five = read(OUT / "five_seed_per_seed.csv")
    inventory = read(OUT / "artifact_index.csv")
    lines = [
        "# LALM: additional evaluation experiments",
        "",
        "All 63 planned jobs completed: 18 cue-free evaluations, 5 timestamp-ordering evaluations, and 40 extra-seed training/evaluation jobs. Saved artifacts were hash-verified during five-seed aggregation.",
        "",
        "## Protocol and interpretation",
        "",
        "- Reader: frozen Qwen2.5-3B-Instruct; encoder: all-MiniLM-L6-v2. Existing dataset, input/output budgets and operative settings are retained unless the experiment specifies a change.",
        "- Every displayed score is a percentage. **+/- means sample standard deviation, not a confidence interval.**",
        "- Trained-method aggregates first average synthetic evaluation streams 11/13/17 within each checkpoint, then compute mean and sample SD across training checkpoints. Baseline synthetic SD is across evaluation streams; these SDs measure different sources of variation.",
        "- Cue-free LALM uses the original three checkpoints 7/13/23. The standard-protocol five-seed results add 37/41. Seeds 37/41 were not evaluated on cue-free streams.",
        "- Released-data evaluations use local LongMemEval diagnostics and text-only LoCoMo category-aware QA. Single baseline evaluations have no replicate SD.",
        "",
        "## 1. Corrections without cue words",
        "",
        "The 1K/5K streams preserve entities, answers, truth traces, distractors and timestamps. Destination and response-style updates are paraphrased without the predefined correction cues; destination queries omit currently. This removes cues from correction utterances rather than every occurrence in unrelated facts. Modified stream IDs end in `-cuefree`; exact streams are saved in each run as `streams_1000.jsonl` and `streams_5000.jsonl`.",
    ]

    def aggregate(group, agent, h, typ="all"):
        rr = [
            r
            for r in runs
            if r["group"] == group
            and r["agent"] == agent
            and r["horizon"] == str(h)
            and r["question_type"] == typ
        ]
        if agent == "lalm":
            g = defaultdict(list)
            for r in rr:
                g[r["training_seed"]].append(float(r["value"]))
            return [st.mean(v) for v in g.values()]
        return [float(r["value"]) for r in rr]

    agents = ["lalm", "lexical_only", "rag", "bounded_rag"]
    table(
        lines,
        ["Method", "1,000 turns", "5,000 turns", "SD source"],
        [
            (
                LABEL[a],
                fmt(aggregate("cue-free", a, 1000)),
                fmt(aggregate("cue-free", a, 5000)),
                "3 training checkpoints" if a == "lalm" else "3 evaluation streams",
            )
            for a in agents
        ],
    )
    lines += ["", "### Correction-specific accuracy"]
    table(
        lines,
        ["Method", "Question type", "1,000 turns", "5,000 turns"],
        [
            (
                LABEL[a],
                t,
                fmt(aggregate("cue-free", a, 1000, t)),
                fmt(aggregate("cue-free", a, 5000, t)),
            )
            for a in agents
            for t in ["correction", "contradictory_update", "response_style"]
        ],
    )
    lines += ["", "### Every cue-free run"]
    table(
        lines,
        ["Method", "Training / loaded checkpoint seed", "Evaluation seed", "Horizon", "Accuracy"],
        [
            (
                LABEL[r["agent"]],
                r["training_seed"] or r["loaded_checkpoint_seed"] + " (unused by baseline)",
                r["evaluation_seed"],
                r["horizon"],
                f"{100 * float(r['value']):.2f}",
            )
            for r in runs
            if r["group"] == "cue-free" and r["question_type"] == "all"
        ],
    )
    lines += ["", "### All cue-free question types"]
    types = sorted(
        {
            r["question_type"]
            for r in runs
            if r["group"] == "cue-free" and r["question_type"] != "all"
        }
    )
    table(
        lines,
        ["Method", "Question type", "1,000 turns", "5,000 turns"],
        [
            (
                LABEL[a],
                t,
                fmt(aggregate("cue-free", a, 1000, t)),
                fmt(aggregate("cue-free", a, 5000, t)),
            )
            for a in agents
            for t in types
        ],
    )
    lines += [
        "",
        "The cue-free results expose weak destination correction/update recall, particularly at 5K turns. Overall accuracy includes unchanged fact categories and should not be interpreted as correction accuracy.",
        "",
        "## 2. Growing RAG with timestamp ordering",
        "",
        "Dense retrieval selects the same top eight hits as the existing Growing RAG implementation. Selected hits are presented in ascending timestamp order, using insertion index to break ties. Existing clipping and context budgets are retained.",
    ]
    old = defaultdict(list)
    for line in (
        ROOT / "results/historical/runs/20260709T063916Z_multi_seed/predictions.jsonl"
    ).open(encoding="utf-8"):
        r = json.loads(line)
        if r["agent"] == "rag":
            old[(r["horizon"], r["seed"])].append(float(r["correct"]))
    table(
        lines,
        ["Synthetic horizon", "Original Growing RAG", "Timestamp-ordered Growing RAG"],
        [
            (
                h,
                fmt([st.mean(v) for (hh, _), v in old.items() if hh == h]),
                fmt(aggregate("ordering", "rag_timestamp", h)),
            )
            for h in [100, 500, 1000, 5000]
        ],
    )
    real = []
    for d, run, metric in [
        ("longmemeval", "20260709T103718Z_longmemeval", "token_f1_diagnostic"),
        ("locomo", "20260709T112355Z_locomo", "locomo_official_qa_score"),
    ]:
        vals = [
            json.loads(l)
            for l in (ROOT / "results/historical/runs" / run / "predictions.jsonl").open(
                encoding="utf-8"
            )
        ]
        a = st.mean(r[metric] for r in vals if r["agent"] == "rag")
        b = next(
            float(r["value"])
            for r in runs
            if r["group"] == "ordering" and r["dataset"] == d and r["question_type"] == "all"
        )
        real.append((d, metric, f"{100 * a:.2f}", f"{100 * b:.2f}", f"{100 * (b - a):+.2f}"))
    table(
        lines, ["Dataset", "Metric", "Original RAG", "Timestamp order", "Difference (points)"], real
    )
    lines += [
        "",
        "Released-data rows have one evaluation each; SD is unavailable. Timestamp order improves the synthetic mean at 500/1K/5K turns; released-data changes are small. No paired significance test for this new comparison is included here.",
        "",
        "### Every timestamp-ordering run",
    ]
    table(
        lines,
        ["Dataset", "Evaluation seed", "Horizon", "Score"],
        [
            (
                r["dataset"],
                r["evaluation_seed"],
                r["horizon"] or "--",
                f"{100 * float(r['value']):.2f}",
            )
            for r in runs
            if r["group"] == "ordering" and r["question_type"] == "all"
        ],
    )
    lines += [
        "",
        "## 3. Two additional training seeds: five checkpoints in total",
        "",
        "Seeds 37 and 41 use the existing training recipe. Both are evaluated on standard synthetic streams at all four horizons and on LongMemEval/LoCoMo, for LALM and Pure Liquid. Zero/random/permuted-prefix controls are evaluated at 1K/5K. The random control is deterministic and norm matched. The five checkpoints are 7, 13, 23, 37 and 41.",
        "",
        "### Mean +/- sample SD across five training checkpoints",
    ]
    metrics = defaultdict(dict)
    for r in five:
        metrics[(r["experiment"], r["agent"], r["horizon"], r["metric"])][r["training_seed"]] = (
            float(r["value"])
        )
    table(
        lines,
        ["Experiment", "Method", "Horizon", "Metric", "Mean +/- SD"],
        [
            (k[0], LABEL.get(k[1], k[1]), k[2] or "--", k[3], fmt(list(v.values())))
            for k, v in sorted(metrics.items())
            if len(v) == 5
        ],
    )
    lines += ["", "### Individual training-seed scores"]
    table(
        lines,
        [
            "Experiment",
            "Method",
            "Horizon",
            "Metric",
            "Seed 7",
            "Seed 13",
            "Seed 23",
            "Seed 37",
            "Seed 41",
        ],
        [
            (
                k[0],
                LABEL.get(k[1], k[1]),
                k[2] or "--",
                k[3],
                *[f"{100 * v[s]:.2f}" if s in v else "?" for s in ["7", "13", "23", "37", "41"]],
            )
            for k, v in sorted(metrics.items())
            if len(v) == 5
        ],
    )
    lines += [
        "",
        "LALM exceeds Pure Liquid on the reported aggregates. The trained prefix does not consistently exceed the zero prefix, and LoCoMo varies substantially across checkpoints. These are descriptive comparisons; mean +/- SD alone does not establish statistical significance.",
        "",
        "## 4. Saved files and exact artifact locations",
        "",
        "- [All new per-run scores](per_run.csv)",
        "- [New scores averaged within each training seed](per_seed.csv)",
        "- [New suite aggregates](means.csv)",
        "- [Five-seed individual scores](five_seed_per_seed.csv)",
        "- [Five-seed aggregate scores](five_seed_means.csv)",
        "- [Machine-readable artifact index](artifact_index.csv)",
        "- [Existing-prediction paired tests](significance/paired_tests.csv): the original analysis uses the existing three checkpoints; it has not been expanded to five.",
        "",
        "Each predictions file is JSON Lines, one prediction per line. Configs are YAML; metric tables are CSV. Both training seed and evaluation seed are recorded separately. Completion receipts retain source and artifact hashes. Baseline loaded-checkpoint IDs are bookkeeping and do not imply learned checkpoint dependence. Paths below are relative to this report.",
    ]

    def link(path, label):
        if not path:
            return "--"
        rel = Path(path.replace("\\", "/")).relative_to("results/evaluation_study").as_posix()
        return f"[{label}](<{rel}>)"

    table(
        lines,
        [
            "Group",
            "Dataset / method",
            "Checkpoint seed",
            "Eval seed",
            "Predictions",
            "Config",
            "Metrics",
            "Receipt",
        ],
        [
            (
                r["group"],
                r["dataset"] + " / " + r["agent"],
                r["training_seed"],
                r["evaluation_seed"],
                link(r["predictions"], "JSONL"),
                link(r["config"], "YAML"),
                link(r["metrics"], "CSV"),
                link(r["receipt"], "JSON"),
            )
            for r in inventory
        ],
    )
    lines += [
        "",
        "## Rebuild this report",
        "",
        "From the LALM project root:",
        "",
        "```powershell",
        "python experiments/summarize_results.py",
        "python experiments/aggregate_five_seeds.py",
        "python experiments/build_results_report.py",
        "```",
        "",
        "This report records the completed additional experiments.",
    ]
    dest = OUT / "STUDY_RESULTS.md"
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(dest)


if __name__ == "__main__":
    main()
