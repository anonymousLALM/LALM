"""Complete original-rule cue-free predictions for checkpoints 37 and 41."""

import argparse, json, subprocess, sys, yaml
from run_study import ROOT, run, key


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan", action="store_true")
    args = ap.parse_args()
    p = yaml.safe_load((ROOT / "experiments/evaluation_study.yaml").read_text())
    checkpoints = {}
    for receipt in (ROOT / "results/evaluation_study/jobs").rglob("complete.json"):
        d = json.loads(receipt.read_text())
        if d["job"]["dataset"] == "train":
            checkpoints[d["job"]["training_seed"]] = receipt.parent / d["checkpoint"]
    selected = [
        dict(
            group="cue-free-completion",
            dataset="synthetic",
            agent="lalm",
            training_seed=s,
            evaluation_seed=e,
            correction_style="cue_free",
            horizons=[1000, 5000],
            replacement_rule="cue_gated",
        )
        for s in [37, 41]
        for e in [11, 13, 17]
    ]
    for i, j in enumerate(selected, 1):
        print(f"[{i}/6] {key(j)}", flush=True)
        if not args.plan:
            run(j, p, ROOT / "results/cue_free_completion", checkpoints)
    if not args.plan:
        subprocess.run(
            [sys.executable, str(ROOT / "experiments/paired_followup.py")], cwd=ROOT, check=True
        )


if __name__ == "__main__":
    main()
