"""Report matched newest-wins trained/sham prefix predictions and paired inference."""

from pathlib import Path
from collections import defaultdict
import csv, json, statistics, hashlib
import numpy as np
from paired_significance import inference

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/additional_study/prefix_controls"
SEEDS = [7, 13, 23, 37, 41]
CONTROLS = ["lalm_zero_prefix", "lalm_random_prefix", "lalm_permuted_prefix"]


def write(name, rows):
    if not rows:
        return
    with (OUT / name).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    data = defaultdict(dict)
    sources = {}
    runs = []
    for suite in [ROOT / "results/followup_study", OUT]:
        for receipt in sorted((suite / "jobs").rglob("complete.json")):
            d = json.loads(receipt.read_text())
            j = d["job"]
            if j["dataset"] != "synthetic":
                continue
            if suite != OUT and (j["agent"] != "lalm" or not j["group"].startswith("newest-wins")):
                continue
            run = receipt.parent / d["result"]
            path = run / "predictions.jsonl"
            sources[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
            for line in path.open(encoding="utf-8"):
                r = json.loads(line)
                h = r["horizon"]
                style = j["correction_style"]
                agent = r["agent"]
                if h not in ([1000, 5000] if style == "original" else [5000]):
                    continue
                if agent not in ["lalm"] + CONTROLS:
                    continue
                k = (style, h, agent, j["training_seed"])
                v = (
                    float(r["correct"]),
                    r["query"],
                    json.dumps(r["reference"], sort_keys=True),
                )
                old = data[k].get(r["example_id"])
                if old is not None and old != v:
                    raise ValueError("Conflicting prediction")
                data[k][r["example_id"]] = v
            runs.append(
                dict(
                    config=str((run / "config.yaml").relative_to(ROOT)),
                    predictions=str(path.relative_to(ROOT)),
                    training_seed=j["training_seed"],
                    evaluation_seed=j["evaluation_seed"],
                    correction_style=j["correction_style"],
                )
            )
    per_seed = []
    means = []
    tests = []
    for style, h in [("original", 1000), ("original", 5000), ("cue_free", 5000)]:
        for agent in ["lalm"] + CONTROLS:
            values = []
            for seed in SEEDS:
                r = data.get((style, h, agent, seed), {})
                if not r:
                    continue
                value = statistics.mean(x[0] for x in r.values())
                values.append(value)
                per_seed.append(
                    dict(
                        style=style,
                        horizon=h,
                        agent=agent,
                        training_seed=seed,
                        n_questions=len(r),
                        expected_questions=150,
                        value=value,
                        complete=len(r) == 150,
                    )
                )
            if values:
                means.append(
                    dict(
                        style=style,
                        horizon=h,
                        agent=agent,
                        n_training_seeds=len(values),
                        mean=statistics.mean(values),
                        sample_sd=statistics.stdev(values) if len(values) > 1 else "",
                        complete=len(values) == 5
                        and all(len(data.get((style, h, agent, s), {})) == 150 for s in SEEDS),
                    )
                )
        for control in CONTROLS:
            aligned = []
            ids0 = None
            for seed in SEEDS:
                left = data.get((style, h, "lalm", seed), {})
                right = data.get((style, h, control, seed), {})
                if len(left) != 150 or len(right) != 150:
                    continue
                if set(left) != set(right):
                    raise ValueError("Unmatched IDs")
                ids = sorted(left)
                if ids0 is not None and ids != ids0:
                    raise ValueError("Checkpoint question sets differ")
                ids0 = ids
                for k in ids:
                    if left[k][1:] != right[k][1:]:
                        raise ValueError("Query/reference mismatch")
                delta = np.array([left[k][0] - right[k][0] for k in ids])
                aligned.append(delta)
                tests.append(
                    dict(
                        style=style,
                        horizon=h,
                        left="lalm",
                        right=control,
                        training_seed=seed,
                        **inference(delta, ids, "synthetic", 10000, 20261001),
                    )
                )
            if len(aligned) == 5:
                tests.append(
                    dict(
                        style=style,
                        horizon=h,
                        left="lalm",
                        right=control,
                        training_seed="mean",
                        **inference(np.mean(aligned, axis=0), ids0, "synthetic", 10000, 20261001),
                    )
                )
    for r in tests:
        r["p_holm"] = ""
    order = sorted(
        [i for i, r in enumerate(tests) if r["training_seed"] == "mean"],
        key=lambda i: tests[i]["p_raw"],
    )
    prev = 0
    for rank, i in enumerate(order):
        prev = max(prev, min(1, tests[i]["p_raw"] * (len(order) - rank)))
        tests[i]["p_holm"] = prev
    write("per_seed.csv", per_seed)
    write("means.csv", means)
    write("paired_tests.csv", tests)
    write("artifact_index.csv", runs)
    (OUT / "provenance.json").write_text(
        json.dumps(
            dict(
                sources=sources,
                samples=10000,
                seed=20261001,
                holm="aggregate comparisons only; final family contains nine comparisons",
            ),
            indent=2,
        )
        + "\n"
    )
    text = [
        "# Item 1: newest-wins prefix controls",
        "",
        f"Completed new evaluation jobs: {len(list((OUT / 'jobs').rglob('complete.json')))}/30. Each job evaluates zero/random/permuted controls. Trained-prefix predictions are reused from the verified newest-wins study. Partial rows are explicitly marked; final tests require 150 matched questions and all five checkpoints.",
        "",
        "| Stream | Horizon | Method | Seeds | Mean +/- sample SD (%) | Complete |",
        "|---|---|---|---|---|---|",
    ]
    for r in means:
        text.append(
            f"| {r['style']} | {r['horizon']} | {r['agent']} | {r['n_training_seeds']} | {100 * r['mean']:.2f}"
            + (f" +/- {100 * r['sample_sd']:.2f}" if r["sample_sd"] != "" else "")
            + f" | {r['complete']} |"
        )
    text += [
        "",
        "## Per-seed values",
        "",
        "| Stream | Horizon | Method | Seed | Accuracy (%) | Questions | Complete |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in per_seed:
        text.append(
            f"| {r['style']} | {r['horizon']} | {r['agent']} | {r['training_seed']} | {100 * r['value']:.2f} | {r['n_questions']} | {r['complete']} |"
        )
    text += [
        "",
        "## Paired tests",
        "",
        "Differences and CIs below are percentage points. Raw p uses paired sign randomization; 95% CI uses paired bootstrap. Holm covers aggregate comparisons only. Aggregate results condition on the five fitted checkpoints.",
        "",
        "| Stream | Horizon | Control | Seed | Difference | 95% CI | Raw p | Holm p |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in tests:
        text.append(
            f"| {r['style']} | {r['horizon']} | {r['right']} | {r['training_seed']} | {100 * r['delta']:.2f} | [{100 * r['ci_low']:.2f}, {100 * r['ci_high']:.2f}] | {r['p_raw']:.5g} | {r['p_holm']} |"
        )
    (OUT / "LALM_PREFIX_CONTROLS_NEWEST.md").write_text("\n".join(text) + "\n")
    print(
        "Item 1 report refreshed; completed jobs",
        len(list((OUT / "jobs").rglob("complete.json"))),
        flush=True,
    )


if __name__ == "__main__":
    main()
