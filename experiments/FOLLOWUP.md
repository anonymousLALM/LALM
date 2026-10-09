# LALM follow-up study

All 48 newest-wins evaluations and six original-rule cue-free completion evaluations are complete. Checkpoint seeds are 7/13/23/37/41; synthetic stream seeds are 11/13/17.

Use `python experiments/reproduce.py --suite newest-wins --output results/reproduction` to replay newest-wins in a fresh directory, or `--suite cue-free-completion` for the added original-rule predictions. Do not resume historical receipts after source edits: their fingerprints describe the original implementation. Original commands and receipts remain provenance.

`python experiments/paired_followup.py` recomputes all 84 per-seed/aggregate rows. Holm adjustment covers its 14 aggregate comparisons only. No prediction or checkpoint is modified by this analysis.

Each run contains config, predictions, overall/per-type metrics, dataset manifest, latency, memory and environment. Suite summaries average evaluation streams within trained seeds before mean/sample SD. Shared baselines are not training replicates. `results/cue_free_completion` supplies missing original-rule cue-free seeds 37/41; all requested comparisons are now complete.
