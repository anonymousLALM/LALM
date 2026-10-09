"""Run the completed five-checkpoint agent-task protocol."""

from pathlib import Path
import argparse, json, subprocess, sys, time, yaml, hashlib

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from liquid_memory_agents.utils.config import load_config


def checkpoints():
    p = yaml.safe_load((ROOT / "experiments/evaluation_study.yaml").read_text())
    c = {int(k): ROOT / v for k, v in p["checkpoints"].items()}
    for receipt in (ROOT / "results/evaluation_study/jobs").rglob("complete.json"):
        d = json.loads(receipt.read_text())
        if d["job"]["dataset"] == "train":
            c[d["job"]["training_seed"]] = receipt.parent / d["checkpoint"]
    return c


def jobs(item):
    out = []
    for style in ["original", "cue_free"]:
        for e in [11, 13, 17]:
            for seed in [7, 13, 23, 37, 41]:
                out.append(
                    dict(
                        dataset="synthetic",
                        style=style,
                        horizons=[1000, 5000],
                        e=e,
                        seed=seed,
                        agents=["lalm"],
                    )
                )
            out.append(
                dict(
                    dataset="synthetic",
                    style=style,
                    horizons=[1000, 5000],
                    e=e,
                    seed=7,
                    agents=["lexical_only", "rag", "rag_timestamp", "bounded_rag"],
                )
            )
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--item", type=int, choices=[4], default=4)
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--deadline-unix", type=float)
    a = ap.parse_args()
    selected = jobs(a.item)
    if a.item == 4:
        selected.sort(
            key=lambda j: (
                j["style"] != "original",
                len(j["agents"]) == 1,
                j["seed"] if len(j["agents"]) == 1 else 0,
                j["e"],
            )
        )
    c = checkpoints()
    suite = ROOT / "supplementary/agent_tasks/results"
    interpreter = Path(sys.executable)
    for i, j in enumerate(selected, 1):
        print(f"[Item {a.item} {i}/{len(selected)}]", j, flush=True)
        if a.plan:
            continue
        folder = (
            suite / "jobs" / hashlib.sha256(json.dumps(j, sort_keys=True).encode()).hexdigest()[:12]
        )
        done = folder / "complete.json"
        if done.exists():
            receipt = json.loads(done.read_text())
            pred = folder / receipt["result"] / "predictions.jsonl"
            if hashlib.sha256(pred.read_bytes()).hexdigest() != receipt["predictions_sha256"]:
                raise ValueError("Completed artifact changed: " + str(pred))
            continue
        if a.deadline_unix is not None and time.time() > a.deadline_unix - 600:
            print("Time budget reached; not starting another evaluation job.", flush=True)
            break
        config = load_config(ROOT / "configs" / f"{j['dataset']}.yaml")
        config["run"].update(seed=j["e"], output_root=str(folder / "runs"))
        config["liquid"].setdefault("lexical_memory", {})["replacement_rule"] = "newest_wins"
        config["evaluation"]["agents"] = j["agents"]
        config["dataset"].pop("test_seeds", None)
        config["protocol"] = j
        if j["dataset"] == "synthetic":
            config["dataset"].update(
                turns=j["horizons"],
                correction_style=j["style"],
                examples_by_horizon={1000: 50, 5000: 50},
            )
        else:
            config["dataset"]["input"] = str(ROOT / config["dataset"]["input"])
        # A fresh attempt preserves interrupted predictions, logs and local memory stores.
        from datetime import datetime, timezone

        config["run"]["output_root"] = str(
            folder / "runs" / datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        )
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "config.yaml"
        path.write_text(yaml.safe_dump(config))
        script = ROOT / "supplementary/agent_tasks/scripts/run_agent_tasks.py"
        cmd = [
            str(interpreter),
            str(script),
            "--config",
            str(path),
            "--checkpoint",
            str(c[j["seed"]]),
        ]
        (folder / "command.json").write_text(json.dumps(cmd))
        subprocess.run(cmd, cwd=ROOT, check=True)
        preds = list(Path(config["run"]["output_root"]).rglob("predictions.jsonl"))
        assert len(preds) == 1
        done.write_text(
            json.dumps(
                {
                    "job": j,
                    "result": str(preds[0].parent.relative_to(folder)),
                    "predictions_sha256": hashlib.sha256(preds[0].read_bytes()).hexdigest(),
                }
            )
        )
        subprocess.run(
            [
                sys.executable,
                str(ROOT / "supplementary/agent_tasks/experiments/report_agent_tasks.py"),
                "--item",
                str(a.item),
            ],
            cwd=ROOT,
            check=True,
        )


if __name__ == "__main__":
    main()
