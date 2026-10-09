# LALM evaluation guide

The root [README](../README.md) is the maintained installation and reproduction entry point.

## Result editions

1. `results/historical/`: original three-checkpoint study, checkpoints 7/13/23, four synthetic horizons, both prefix-control horizons, LongMemEval and LoCoMo.
2. `results/evaluation_study/`: cue-free stress tests, timestamp-ordered Growing RAG, checkpoints 37/41, five-checkpoint aggregates, missing released-data metrics, original-rule paired tests.
3. `results/followup_study/`: newest-wins evaluations on all five checkpoints and shared Lexical-only; refreshed paired tests.
4. `results/cue_free_completion/`: original-rule cue-free streams for 37/41, completing the matched five-checkpoint comparison.

5. `results/additional_study/prefix_controls/`: newest-wins trained/zero/random/permuted prefix comparisons.
6. `supplementary/agent_tasks/`: supplementary archive of simulated tool selection and argument generation.

## Audit

Run `python experiments/verify_publication.py` after `git lfs pull`. It verifies every public result file, all five checkpoints and completed receipt counts (63 evaluation jobs, 48 newest-wins jobs, six cue-free completion jobs, 30 prefix-control jobs, and 36 supplementary tool-task jobs). Publication receipts include hashes of intermediate files omitted from the public release. The publication manifest verifies the files actually shipped.

`source_measurements.csv` and the historical aggregate manifest identify original measurement provenance. Prediction/config paths use the current neutral directory names. `paired_sources.json` identifies original paired-test inputs; `paired_followup.py` discovers verified completed study receipts and refuses unmatched IDs, queries, references and conflicting duplicate predictions.

## Interpretation

LongMemEval reports diagnostic token F1/exact match on 450 held-out questions, not the official model-judged score. LoCoMo uses its local category-aware QA metric across 1,986 questions in ten conversation clusters. Synthetic accuracy uses the recorded answer matching rule. Released-data type breakdowns are in per-run `per_type.csv` and summary CSVs.

Paired inference averages checkpoints within question and conditions on the fitted checkpoints. LoCoMo bootstraps and sign-randomizes whole conversations. Holm correction covers aggregate comparisons only; seed rows retain raw p-values. Percentile intervals and randomization p-values are distinct procedures and can differ near their decision boundaries.

Full GPU replay is provided by `experiments/reproduce.py`; retraining uses recorded training configs via `--train-seed`. Current code defaults to the original cue-gated sidecar rule; newest-wins is an explicit evaluation config setting. Original hardware was RTX 5080; logical memory size is not VRAM. Library/hardware differences may change generated answers.
