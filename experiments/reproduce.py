"""Replay every saved evaluation configuration into a separate output directory."""

from pathlib import Path
import argparse, hashlib, json, subprocess, sys
import yaml
from run_study import ROOT

MANUSCRIPT_SUITES = {
    "evaluation": "results/evaluation_study",
    "newest-wins": "results/followup_study",
    "cue-free-completion": "results/cue_free_completion",
    "prefix-controls": "results/additional_study/prefix_controls",
}
SUPPLEMENTARY_SUITES = {
    "agent-tasks": "supplementary/agent_tasks/results",
}
SUITES = {**MANUSCRIPT_SUITES, **SUPPLEMENTARY_SUITES}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1048576), b""):
            h.update(block)
    return h.hexdigest()


def checkpoints():
    protocol = yaml.safe_load((ROOT / "experiments/evaluation_study.yaml").read_text())
    paths = {int(k): ROOT / v for k, v in protocol["checkpoints"].items()}
    for p in (ROOT / "results/evaluation_study/jobs").rglob("complete.json"):
        receipt = json.loads(p.read_text())
        if receipt["job"]["dataset"] == "train":
            paths[receipt["job"]["training_seed"]] = p.parent / receipt["checkpoint"]
    return paths


def evaluations(suite, paths):
    out = []
    for label, folder in SUITES.items():
        if suite == "manuscript" and label in SUPPLEMENTARY_SUITES:
            continue
        if suite not in ("all", "manuscript", label):
            continue
        for p in sorted((ROOT / folder / "jobs").rglob("complete.json")):
            receipt = json.loads(p.read_text())
            job = receipt["job"]
            if job["dataset"] != "train":
                out.append(
                    (
                        label,
                        p.parent.name,
                        p.parent / "config.yaml",
                        job.get("training_seed", job.get("seed")),
                    )
                )
    if suite in ("all", "historical"):
        for p in sorted((ROOT / "results/historical").rglob("config.yaml")):
            if not (p.parent / "predictions.jsonl").exists():
                continue
            config = yaml.safe_load(p.read_text())
            if config.get("run_kind") == "aggregate":
                continue
            checkpoint = config.get("execution", {}).get("checkpoint", "")
            seed = next(
                (s for s, path in paths.items() if path.parent.parent.name in checkpoint), None
            )
            if seed is None:
                raise ValueError(f"Cannot identify checkpoint for {p}")
            key = hashlib.sha256(p.relative_to(ROOT).as_posix().encode()).hexdigest()[:12]
            out.append(("historical", key, p, seed))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--suite", choices=["all", "manuscript", "historical", *SUITES], default="manuscript")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--output", type=Path, default=ROOT / "results/reproduction")
    ap.add_argument("--train-seed", type=int, choices=[7, 13, 23, 37, 41])
    args = ap.parse_args()
    paths = checkpoints()
    if args.train_seed:
        config_path = paths[args.train_seed].parent.parent / "config.yaml"
        selected = [("training", f"seed_{args.train_seed}", config_path, args.train_seed)]
    else:
        selected = evaluations(args.suite, paths)
    print(f"{len(selected)} jobs")
    source_hash = hashlib.sha256(
        "".join(
            digest(p)
            for directory in ["src", "scripts"]
            for p in sorted((ROOT / directory).rglob("*.py"))
        ).encode()
    ).hexdigest()
    for i, (label, key, original, seed) in enumerate(selected, 1):
        print(
            f"[{i}/{len(selected)}] {label} seed={seed} config={original.relative_to(ROOT)}",
            flush=True,
        )
        if args.plan:
            continue
        folder = args.output.resolve() / label / key
        config = yaml.safe_load(original.read_text())
        config.pop("execution", None)
        config["run"]["output_root"] = str(folder / "runs")
        training = label == "training"
        dataset = config["dataset"]["name"]
        if not training and dataset != "synthetic":
            config["dataset"]["input"] = str(
                ROOT
                / "data/external"
                / (
                    "longmemeval/longmemeval_s_cleaned.json"
                    if dataset == "longmemeval"
                    else "locomo/locomo10.json"
                )
            )
        fingerprint = hashlib.sha256(
            json.dumps(
                {
                    "config": config,
                    "source": source_hash,
                    "checkpoint": None if training else digest(paths[seed]),
                    "input": digest(config["dataset"]["input"])
                    if not training and dataset != "synthetic"
                    else None,
                },
                sort_keys=True,
            ).encode()
        ).hexdigest()
        done = folder / "replayed.json"
        if done.exists():
            receipt = json.loads(done.read_text())
            if receipt["fingerprint"] != fingerprint:
                raise ValueError(f"Replay settings changed; use a new output directory: {folder}")
            for name, expected in receipt["files"].items():
                if digest(folder / name) != expected:
                    raise ValueError(f"Changed replay output: {name}")
            print("[Verified skip]", flush=True)
            continue
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "config.yaml"
        path.write_text(yaml.safe_dump(config))
        if training:
            script_path = ROOT / "scripts/train_liquid.py"
        elif label == "agent-tasks":
            script_path = ROOT / "supplementary/agent_tasks/scripts/run_agent_tasks.py"
        elif dataset == "synthetic":
            script_path = ROOT / "scripts/run_synthetic.py"
        else:
            script_path = ROOT / "scripts/run_real_benchmark.py"
        command = [sys.executable, str(script_path), "--config", str(path)]
        if not training:
            command += ["--checkpoint", str(paths[seed])]
        if not training and dataset == "longmemeval":
            command += ["--start-index", "50"]
        subprocess.run(command, cwd=ROOT, check=True)
        files = {
            p.relative_to(folder).as_posix(): digest(p) for p in folder.rglob("*") if p.is_file()
        }
        done.write_text(json.dumps({"fingerprint": fingerprint, "files": files}, indent=2) + "\n")


if __name__ == "__main__":
    main()
