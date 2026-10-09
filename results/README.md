# LALM results

| Directory | Study |
|---|---|
| `historical/` | Original three-checkpoint measurements and predictions |
| `evaluation_study/` | Five-checkpoint summaries, cue-free/ordering evaluations and original paired tests |
| `followup_study/` | Newest-wins evaluations and 84 paired-test rows |
| `cue_free_completion/` | Original-rule cue-free checkpoints 37/41 |
| `additional_study/prefix_controls/` | Newest-wins prefix controls; 30 jobs, 54 paired-test rows |

Unreported exploratory experiments (including simulated agent tool tasks: 36 jobs, 288 paired-test rows) are archived in [`supplementary/agent_tasks/`](../supplementary/agent_tasks/README.md).

Predictions and five final checkpoints use Git LFS. Intermediate epochs, deterministic stream dumps, duplicate error files and interrupted attempts are excluded. Saved predictions and numerical scores are unchanged; metadata uses neutral paths and relevant dependency versions. Receipts preserve experimental fingerprints and include updated release hashes. Use `python experiments/verify_publication.py` to check shipped files against `publication_manifest.json`. The root README documents replay and retraining.
