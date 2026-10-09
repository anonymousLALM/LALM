"""Prepare isolated runtimes without overwriting a running snapshot."""

from pathlib import Path
import hashlib, json, re, shutil

ROOT = Path(__file__).resolve().parents[1]


def ensure_snapshot(name):
    dest = ROOT / ".runtime" / name
    if (dest / "experiments/run_study.py").exists():
        return dest
    dest.mkdir(parents=True, exist_ok=True)
    for directory in ["src", "scripts", "configs"]:
        shutil.copytree(
            ROOT / directory,
            dest / directory,
            ignore=shutil.ignore_patterns("__pycache__"),
            dirs_exist_ok=True,
        )
    text = (ROOT / "experiments/run_study.py").read_text()
    if name.startswith("prefix_controls"):
        text, count = re.subn(
            r"agents=\[j\[['\"]agent['\"]\]\]",
            "agents=['lalm_zero_prefix','lalm_random_prefix','lalm_permuted_prefix']",
            text,
        )
        if count != 1:
            raise ValueError("Expected one agent configuration in the snapshot runner")
    (dest / "experiments").mkdir(exist_ok=True)
    (dest / "experiments/run_study.py").write_text(text)
    if name == "prefix_controls_fast":
        from prefix_shared_memory import optimize_snapshot

        optimize_snapshot(dest)
    hashes = {
        str(p.relative_to(dest)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in dest.rglob("*")
        if p.is_file()
    }
    (dest / "snapshot_manifest.json").write_text(json.dumps(hashes, indent=2))
    return dest


def main():
    ensure_snapshot("prefix_controls")
    print("Prefix-control runtime ready.")


if __name__ == "__main__":
    main()
