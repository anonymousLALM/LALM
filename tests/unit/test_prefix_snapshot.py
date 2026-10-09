"""Check that optional prefix snapshots still evaluate all three controls."""

import ast
import importlib.util
from pathlib import Path


def test_prefix_snapshot(tmp_path, monkeypatch):
    root = Path(__file__).resolve().parents[2]
    spec = importlib.util.spec_from_file_location(
        "prefix_preparation", root / "experiments/prepare_prefix_controls.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for directory in ["src", "scripts", "configs", "experiments"]:
        (tmp_path / directory).mkdir()
    (tmp_path / "experiments/run_study.py").write_text(
        (root / "experiments/run_study.py").read_text()
    )
    (tmp_path / "scripts/run_synthetic.py").write_text(
        (root / "scripts/run_synthetic.py").read_text()
    )
    monkeypatch.setattr(module, "ROOT", tmp_path)
    dest = module.ensure_snapshot("prefix_controls")
    tree = ast.parse((dest / "experiments/run_study.py").read_text())
    agents = [
        kw.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        for kw in node.keywords
        if kw.arg == "agents"
    ]
    assert len(agents) == 1
    assert ast.literal_eval(agents[0]) == [
        "lalm_zero_prefix",
        "lalm_random_prefix",
        "lalm_permuted_prefix",
    ]
    spec = importlib.util.spec_from_file_location(
        "prefix_shared", root / "experiments/prefix_shared_memory.py"
    )
    shared = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(shared)
    shared.optimize_snapshot(dest)
    source = (dest / "scripts/run_synthetic.py").read_text()
    compile(source, "shared_prefix_snapshot", "exec")
    assert '"shared_memory_build": True' in source
