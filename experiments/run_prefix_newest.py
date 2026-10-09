"""Run newest-wins sham-prefix controls using an isolated evaluation snapshot."""

from pathlib import Path
import argparse, json, sys, yaml, subprocess, time

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = (
    ROOT
    / ".runtime"
    / ("prefix_controls_fast" if "--shared-writes" in sys.argv else "prefix_controls")
)
from prepare_prefix_controls import ensure_snapshot
from additional_artifacts import verified_receipt

ensure_snapshot(RUNTIME.name)
sys.path.insert(0, str(RUNTIME / "experiments"))
from run_study import run, key


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument(
        "--shared-writes",
        action="store_true",
        help="Reuse identical write state across sham-prefix controls; predictions verified against serial evaluation.",
    )
    ap.add_argument("--deadline-unix", type=float)
    a = ap.parse_args()
    p = yaml.safe_load((ROOT / "experiments/evaluation_study.yaml").read_text())
    checkpoints = {int(k): ROOT / v for k, v in p["checkpoints"].items()}
    for receipt in (ROOT / "results/evaluation_study/jobs").rglob("complete.json"):
        d = json.loads(receipt.read_text())
        if d["job"]["dataset"] == "train":
            checkpoints[d["job"]["training_seed"]] = receipt.parent / d["checkpoint"]
    selected = [
        dict(
            group="prefix-newest-" + style,
            dataset="synthetic",
            agent="lalm_zero_prefix",
            training_seed=s,
            evaluation_seed=e,
            correction_style=style,
            horizons=[1000, 5000] if style == "original" else [5000],
            replacement_rule="newest_wins",
        )
        for style in ["original", "cue_free"]
        for s in [7, 13, 23, 37, 41]
        for e in [11, 13, 17]
    ]
    for i, j in enumerate(selected, 1):
        print(f"[Item 1 {i}/{len(selected)}]", key(j), "zero/random/permuted", flush=True)
        if not a.plan:
            suite = ROOT / "results/additional_study/prefix_controls"
            if verified_receipt(suite, key(j), j):
                print("[Verified saved job]", key(j), flush=True)
            else:
                if a.deadline_unix is not None and time.time() > a.deadline_unix - 600:
                    print(
                        "Stopping before the time budget expires; completed results are preserved.",
                        flush=True,
                    )
                    break
                run(j, p, suite, checkpoints)
            subprocess.run(
                [sys.executable, str(ROOT / "experiments/report_prefix_newest.py")],
                cwd=ROOT,
                check=True,
            )


if __name__ == "__main__":
    main()
