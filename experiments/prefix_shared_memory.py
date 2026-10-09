"""Reuse identical query-independent writes across the three sham-prefix reads."""

from pathlib import Path


def optimize_snapshot(dest):
    path = Path(dest) / "scripts/run_synthetic.py"
    text = path.read_text(encoding="utf-8")
    if "shared_memory_build" in text:
        return
    start = text.index("            for agent in agents:\n                for example in tqdm")
    end = text.index("    metrics = []", start)
    replacement = """            assert all(a.name in {'lalm_zero_prefix','lalm_random_prefix','lalm_permuted_prefix'} for a in agents)
            anchor = agents[0]
            for example in tqdm(examples, desc=f"{horizon} turns / shared writes and three controls"):
                anchor.reset()
                update_started = time.perf_counter()
                observe_sequence(anchor, [
                    ({"role": role, "content": turn}, timestamp, session_id)
                    for turn, role, timestamp, session_id in zip(
                        example.turns, example.roles, example.timestamps, example.session_ids
                    )
                ])
                update_ms = (time.perf_counter() - update_started) * 1000
                for agent in agents:
                    agent.memory = anchor.memory
                    agent.lexical_memory = anchor.lexical_memory
                    record(agent, example, update_ms)
"""
    text = text[:start] + replacement + text[end:]
    text = text.replace(
        'config["execution"] = {',
        'config["execution"] = {\n        "shared_memory_build": True,',
        1,
    )
    path.write_text(text, encoding="utf-8")
