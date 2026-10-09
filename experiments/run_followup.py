"""Evaluation-only follow-up suite; completed prior-study outputs stay unchanged."""

import argparse, json, subprocess, sys, yaml
from run_study import ROOT, run, key


def plan(p):
    seeds = [7, 13, 23, 37, 41]
    out = []

    def add(group, dataset, agent, seed, evaluation_seed, style="original", horizons=None):
        out.append(
            dict(
                group=group,
                dataset=dataset,
                agent=agent,
                training_seed=seed,
                evaluation_seed=evaluation_seed,
                correction_style=style,
                horizons=horizons,
                replacement_rule="newest_wins" if group == "newest-wins" else "cue_gated",
            )
        )

    for style, h in [("original", [100, 500, 1000, 5000]), ("cue_free", [1000, 5000])]:
        for e in [11, 13, 17]:
            for s in seeds:
                add("newest-wins", "synthetic", "lalm", s, e, style, h)
            add("newest-wins", "synthetic", "lexical_only", seeds[0], e, style, h)
    for d in ["longmemeval", "locomo"]:
        for s in seeds:
            add("newest-wins", d, "lalm", s, 7)
        add("newest-wins", d, "lexical_only", seeds[0], 7)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument(
        "--group",
        choices=[
            "all",
            "newest-wins",
            "cue-free",
            "priority",
            "ablations",
            "retrieval",
            "ordering",
        ],
        default="all",
    )
    a = ap.parse_args()
    p = yaml.safe_load((ROOT / "experiments/evaluation_study.yaml").read_text())
    checkpoints = {int(k): ROOT / v for k, v in p["checkpoints"].items()}
    for receipt in (ROOT / "results/evaluation_study/jobs").rglob("complete.json"):
        r = json.loads(receipt.read_text())
        if r["job"]["dataset"] == "train":
            checkpoints[r["job"]["training_seed"]] = receipt.parent / r["checkpoint"]
    selected = [j for j in plan(p) if a.group == "all" or j["group"] == a.group]
    # Rule and stream style must participate in job IDs to prevent collisions.
    for j in selected:
        j["group"] = j["group"] + (
            "-" + j["correction_style"] if j["group"] == "newest-wins" else ""
        )
    suite = ROOT / "results/followup_study"
    if a.plan:
        for i, j in enumerate(selected, 1):
            print(f"[{i}/{len(selected)}] {key(j)}")
        print("No models loaded; evaluation only.")
        return
    for i, j in enumerate(selected, 1):
        print(f"[Job {i}/{len(selected)}; remaining {len(selected) - i}] {key(j)}", flush=True)
        run(j, p, suite, checkpoints)
    subprocess.run(
        [sys.executable, str(ROOT / "experiments/summarize_results.py"), "--output", str(suite)],
        check=True,
    )


if __name__ == "__main__":
    main()
