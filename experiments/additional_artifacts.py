"""Verify saved jobs independently of checkout location before reusing them."""

from pathlib import Path
import hashlib, json


def verified_receipt(suite, key, job):
    legacy = Path(suite) / "jobs" / key
    short = Path(suite) / "jobs" / hashlib.sha256(key.encode()).hexdigest()[:12]
    folder = legacy if (legacy / "complete.json").exists() else short
    receipt = folder / "complete.json"
    if not receipt.exists():
        return None
    d = json.loads(receipt.read_text())
    if d["job"] != job:
        raise ValueError("Saved job protocol differs: " + str(folder))
    for name, expected in d.get("release_artifact_sha256", d.get("artifacts", {})).items():
        p = folder / name
        if hashlib.sha256(p.read_bytes()).hexdigest() != expected:
            raise ValueError("Saved artifact changed: " + str(p))
    d["_folder"] = folder
    return d
