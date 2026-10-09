# LALM: additional evaluation experiments

All 63 planned jobs completed: 18 cue-free evaluations, 5 timestamp-ordering evaluations, and 40 extra-seed training/evaluation jobs. Saved artifacts were hash-verified during five-seed aggregation.

## Protocol and interpretation

- Reader: frozen Qwen2.5-3B-Instruct; encoder: all-MiniLM-L6-v2. Existing dataset, input/output budgets and operative settings are retained unless the experiment specifies a change.
- Every displayed score is a percentage. **+/- means sample standard deviation, not a confidence interval.**
- Trained-method aggregates first average synthetic evaluation streams 11/13/17 within each checkpoint, then compute mean and sample SD across training checkpoints. Baseline synthetic SD is across evaluation streams; these SDs measure different sources of variation.
- Cue-free LALM uses the original three checkpoints 7/13/23. The standard-protocol five-seed results add 37/41. Seeds 37/41 were not evaluated on cue-free streams.
- Released-data evaluations use local LongMemEval diagnostics and text-only LoCoMo category-aware QA. Single baseline evaluations have no replicate SD.

## 1. Corrections without cue words

The 1K/5K streams preserve entities, answers, truth traces, distractors and timestamps. Destination and response-style updates are paraphrased without the predefined correction cues; destination queries omit currently. This removes cues from correction utterances rather than every occurrence in unrelated facts. Modified stream IDs end in `-cuefree`; exact streams are saved in each run as `streams_1000.jsonl` and `streams_5000.jsonl`.

| Method | 1,000 turns | 5,000 turns | SD source |
| --- | --- | --- | --- |
| LALM | 55.78 +/- 2.69 | 47.56 +/- 4.82 | 3 training checkpoints |
| Lexical-only | 54.00 +/- 2.00 | 47.33 +/- 3.06 | 3 evaluation streams |
| Growing RAG | 50.67 +/- 3.06 | 50.67 +/- 3.06 | 3 evaluation streams |
| Bounded RAG | 24.00 +/- 4.00 | 0.00 +/- 0.00 | 3 evaluation streams |

### Correction-specific accuracy

| Method | Question type | 1,000 turns | 5,000 turns |
| --- | --- | --- | --- |
| LALM | correction | 6.67 +/- 6.67 | 0.00 +/- 0.00 |
| LALM | contradictory_update | 8.89 +/- 3.85 | 0.00 +/- 0.00 |
| LALM | response_style | 60.00 +/- 0.00 | 0.00 +/- 0.00 |
| Lexical-only | correction | 6.67 +/- 11.55 | 6.67 +/- 11.55 |
| Lexical-only | contradictory_update | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Lexical-only | response_style | 60.00 +/- 34.64 | 0.00 +/- 0.00 |
| Growing RAG | correction | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | contradictory_update | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | response_style | 73.33 +/- 11.55 | 46.67 +/- 11.55 |
| Bounded RAG | correction | 53.33 +/- 23.09 | 0.00 +/- 0.00 |
| Bounded RAG | contradictory_update | 73.33 +/- 11.55 | 0.00 +/- 0.00 |
| Bounded RAG | response_style | 46.67 +/- 23.09 | 0.00 +/- 0.00 |

### Every cue-free run

| Method | Training / loaded checkpoint seed | Evaluation seed | Horizon | Accuracy |
| --- | --- | --- | --- | --- |
| Bounded RAG | 7 (unused by baseline) | 13 | 1000 | 28.00 |
| Bounded RAG | 7 (unused by baseline) | 13 | 5000 | 0.00 |
| Bounded RAG | 7 (unused by baseline) | 17 | 1000 | 20.00 |
| Bounded RAG | 7 (unused by baseline) | 17 | 5000 | 0.00 |
| Lexical-only | 7 (unused by baseline) | 13 | 1000 | 54.00 |
| Lexical-only | 7 (unused by baseline) | 13 | 5000 | 48.00 |
| Growing RAG | 7 (unused by baseline) | 17 | 1000 | 48.00 |
| Growing RAG | 7 (unused by baseline) | 17 | 5000 | 50.00 |
| Lexical-only | 7 (unused by baseline) | 17 | 1000 | 56.00 |
| Lexical-only | 7 (unused by baseline) | 17 | 5000 | 44.00 |
| LALM | 23 | 11 | 1000 | 52.00 |
| LALM | 23 | 11 | 5000 | 42.00 |
| Lexical-only | 7 (unused by baseline) | 11 | 1000 | 52.00 |
| Lexical-only | 7 (unused by baseline) | 11 | 5000 | 50.00 |
| LALM | 7 | 13 | 1000 | 58.00 |
| LALM | 7 | 13 | 5000 | 52.00 |
| LALM | 13 | 17 | 1000 | 58.00 |
| LALM | 13 | 17 | 5000 | 50.00 |
| Bounded RAG | 7 (unused by baseline) | 11 | 1000 | 24.00 |
| Bounded RAG | 7 (unused by baseline) | 11 | 5000 | 0.00 |
| LALM | 7 | 17 | 1000 | 56.00 |
| LALM | 7 | 17 | 5000 | 50.00 |
| LALM | 13 | 13 | 1000 | 56.00 |
| LALM | 13 | 13 | 5000 | 50.00 |
| Growing RAG | 7 (unused by baseline) | 11 | 1000 | 50.00 |
| Growing RAG | 7 (unused by baseline) | 11 | 5000 | 54.00 |
| LALM | 23 | 13 | 1000 | 54.00 |
| LALM | 23 | 13 | 5000 | 44.00 |
| Growing RAG | 7 (unused by baseline) | 13 | 1000 | 54.00 |
| Growing RAG | 7 (unused by baseline) | 13 | 5000 | 48.00 |
| LALM | 23 | 17 | 1000 | 52.00 |
| LALM | 23 | 17 | 5000 | 40.00 |
| LALM | 7 | 11 | 1000 | 58.00 |
| LALM | 7 | 11 | 5000 | 50.00 |
| LALM | 13 | 11 | 1000 | 58.00 |
| LALM | 13 | 11 | 5000 | 50.00 |

### All cue-free question types

| Method | Question type | 1,000 turns | 5,000 turns |
| --- | --- | --- | --- |
| LALM | boolean | 6.67 +/- 6.67 | 2.22 +/- 3.85 |
| LALM | contradictory_update | 8.89 +/- 3.85 | 0.00 +/- 0.00 |
| LALM | correction | 6.67 +/- 6.67 | 0.00 +/- 0.00 |
| LALM | goal | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| LALM | multi_fact | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| LALM | paraphrase | 91.11 +/- 10.18 | 93.33 +/- 11.55 |
| LALM | repeated_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| LALM | response_style | 60.00 +/- 0.00 | 0.00 +/- 0.00 |
| LALM | stable_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| LALM | temporal | 84.44 +/- 15.40 | 80.00 +/- 34.64 |
| Lexical-only | boolean | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Lexical-only | contradictory_update | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Lexical-only | correction | 6.67 +/- 11.55 | 6.67 +/- 11.55 |
| Lexical-only | goal | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| Lexical-only | multi_fact | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Lexical-only | paraphrase | 86.67 +/- 11.55 | 80.00 +/- 0.00 |
| Lexical-only | repeated_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| Lexical-only | response_style | 60.00 +/- 34.64 | 0.00 +/- 0.00 |
| Lexical-only | stable_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| Lexical-only | temporal | 86.67 +/- 23.09 | 86.67 +/- 23.09 |
| Growing RAG | boolean | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | contradictory_update | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | correction | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | goal | 93.33 +/- 11.55 | 100.00 +/- 0.00 |
| Growing RAG | multi_fact | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Growing RAG | paraphrase | 60.00 +/- 20.00 | 66.67 +/- 11.55 |
| Growing RAG | repeated_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| Growing RAG | response_style | 73.33 +/- 11.55 | 46.67 +/- 11.55 |
| Growing RAG | stable_fact | 100.00 +/- 0.00 | 100.00 +/- 0.00 |
| Growing RAG | temporal | 80.00 +/- 20.00 | 93.33 +/- 11.55 |
| Bounded RAG | boolean | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Bounded RAG | contradictory_update | 73.33 +/- 11.55 | 0.00 +/- 0.00 |
| Bounded RAG | correction | 53.33 +/- 23.09 | 0.00 +/- 0.00 |
| Bounded RAG | goal | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Bounded RAG | multi_fact | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Bounded RAG | paraphrase | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Bounded RAG | repeated_fact | 66.67 +/- 11.55 | 0.00 +/- 0.00 |
| Bounded RAG | response_style | 46.67 +/- 23.09 | 0.00 +/- 0.00 |
| Bounded RAG | stable_fact | 0.00 +/- 0.00 | 0.00 +/- 0.00 |
| Bounded RAG | temporal | 0.00 +/- 0.00 | 0.00 +/- 0.00 |

The cue-free results expose weak destination correction/update recall, particularly at 5K turns. Overall accuracy includes unchanged fact categories and should not be interpreted as correction accuracy.

## 2. Growing RAG with timestamp ordering

Dense retrieval selects the same top eight hits as the existing Growing RAG implementation. Selected hits are presented in ascending timestamp order, using insertion index to break ties. Existing clipping and context budgets are retained.

| Synthetic horizon | Original Growing RAG | Timestamp-ordered Growing RAG |
| --- | --- | --- |
| 100 | 66.33 +/- 1.15 | 66.33 +/- 3.79 |
| 500 | 63.11 +/- 5.39 | 68.89 +/- 5.39 |
| 1000 | 58.67 +/- 6.11 | 65.33 +/- 5.77 |
| 5000 | 58.67 +/- 5.03 | 62.00 +/- 3.46 |

| Dataset | Metric | Original RAG | Timestamp order | Difference (points) |
| --- | --- | --- | --- | --- |
| longmemeval | token_f1_diagnostic | 19.53 | 19.30 | -0.23 |
| locomo | locomo_official_qa_score | 31.41 | 32.33 | +0.92 |

Released-data rows have one evaluation each; SD is unavailable. Timestamp order improves the synthetic mean at 500/1K/5K turns; released-data changes are small. No paired significance test for this new comparison is included here.

### Every timestamp-ordering run

| Dataset | Evaluation seed | Horizon | Score |
| --- | --- | --- | --- |
| synthetic | 13 | 100 | 69.00 |
| synthetic | 13 | 500 | 72.00 |
| synthetic | 13 | 1000 | 62.00 |
| synthetic | 13 | 5000 | 64.00 |
| synthetic | 11 | 100 | 62.00 |
| synthetic | 11 | 500 | 62.67 |
| synthetic | 11 | 1000 | 72.00 |
| synthetic | 11 | 5000 | 64.00 |
| locomo | 7 | -- | 32.33 |
| synthetic | 17 | 100 | 68.00 |
| synthetic | 17 | 500 | 72.00 |
| synthetic | 17 | 1000 | 62.00 |
| synthetic | 17 | 5000 | 58.00 |
| longmemeval | 7 | -- | 19.30 |

## 3. Two additional training seeds: five checkpoints in total

Seeds 37 and 41 use the existing training recipe. Both are evaluated on standard synthetic streams at all four horizons and on LongMemEval/LoCoMo, for LALM and Pure Liquid. Zero/random/permuted-prefix controls are evaluated at 1K/5K. The random control is deterministic and norm matched. The five checkpoints are 7, 13, 23, 37 and 41.

### Mean +/- sample SD across five training checkpoints

| Experiment | Method | Horizon | Metric | Mean +/- SD |
| --- | --- | --- | --- | --- |
| locomo | LALM | -- | locomo_official_qa_score | 29.05 +/- 5.30 |
| locomo | Pure Liquid | -- | locomo_official_qa_score | 7.44 +/- 4.45 |
| longmemeval | LALM | -- | diagnostic_token_f1 | 20.64 +/- 2.67 |
| longmemeval | Pure Liquid | -- | diagnostic_token_f1 | 8.69 +/- 1.20 |
| prefix_1000 | LALM | 1000 | accuracy | 69.73 +/- 4.61 |
| prefix_1000 | Permuted prefix | 1000 | accuracy | 60.80 +/- 6.72 |
| prefix_1000 | Random prefix | 1000 | accuracy | 62.80 +/- 2.38 |
| prefix_1000 | Zero prefix | 1000 | accuracy | 70.00 +/- 0.00 |
| prefix_5000 | LALM | 5000 | accuracy | 70.53 +/- 6.23 |
| prefix_5000 | Permuted prefix | 5000 | accuracy | 62.53 +/- 6.82 |
| prefix_5000 | Random prefix | 5000 | accuracy | 62.67 +/- 2.49 |
| prefix_5000 | Zero prefix | 5000 | accuracy | 67.87 +/- 0.73 |
| synthetic | LALM | 100 | accuracy | 73.00 +/- 5.24 |
| synthetic | LALM | 1000 | accuracy | 69.73 +/- 4.61 |
| synthetic | LALM | 500 | accuracy | 67.56 +/- 4.92 |
| synthetic | LALM | 5000 | accuracy | 70.53 +/- 6.23 |
| synthetic | Pure Liquid | 100 | accuracy | 12.27 +/- 4.36 |
| synthetic | Pure Liquid | 1000 | accuracy | 10.67 +/- 6.45 |
| synthetic | Pure Liquid | 500 | accuracy | 11.64 +/- 4.44 |
| synthetic | Pure Liquid | 5000 | accuracy | 10.00 +/- 7.48 |

### Individual training-seed scores

| Experiment | Method | Horizon | Metric | Seed 7 | Seed 13 | Seed 23 | Seed 37 | Seed 41 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| locomo | LALM | -- | locomo_official_qa_score | 31.78 | 32.41 | 29.08 | 19.86 | 32.11 |
| locomo | Pure Liquid | -- | locomo_official_qa_score | 4.04 | 15.08 | 5.28 | 7.48 | 5.30 |
| longmemeval | LALM | -- | diagnostic_token_f1 | 20.46 | 20.03 | 17.21 | 24.68 | 20.84 |
| longmemeval | Pure Liquid | -- | diagnostic_token_f1 | 8.07 | 7.84 | 9.07 | 10.64 | 7.84 |
| prefix_1000 | LALM | 1000 | accuracy | 72.00 | 74.67 | 66.67 | 72.00 | 63.33 |
| prefix_1000 | Permuted prefix | 1000 | accuracy | 56.00 | 65.33 | 51.33 | 65.33 | 66.00 |
| prefix_1000 | Random prefix | 1000 | accuracy | 58.67 | 63.33 | 64.67 | 64.00 | 63.33 |
| prefix_1000 | Zero prefix | 1000 | accuracy | 70.00 | 70.00 | 70.00 | 70.00 | 70.00 |
| prefix_5000 | LALM | 5000 | accuracy | 72.00 | 76.67 | 64.00 | 76.00 | 64.00 |
| prefix_5000 | Permuted prefix | 5000 | accuracy | 59.33 | 66.00 | 52.00 | 68.00 | 67.33 |
| prefix_5000 | Random prefix | 5000 | accuracy | 59.33 | 64.00 | 60.67 | 64.67 | 64.67 |
| prefix_5000 | Zero prefix | 5000 | accuracy | 68.67 | 68.67 | 67.33 | 67.33 | 67.33 |
| synthetic | LALM | 100 | accuracy | 73.33 | 80.67 | 73.33 | 71.67 | 66.00 |
| synthetic | LALM | 1000 | accuracy | 72.00 | 74.67 | 66.67 | 72.00 | 63.33 |
| synthetic | LALM | 500 | accuracy | 69.33 | 74.22 | 68.44 | 64.44 | 61.33 |
| synthetic | LALM | 5000 | accuracy | 72.00 | 76.67 | 64.00 | 76.00 | 64.00 |
| synthetic | Pure Liquid | 100 | accuracy | 15.00 | 11.33 | 15.00 | 5.00 | 15.00 |
| synthetic | Pure Liquid | 1000 | accuracy | 16.00 | 3.33 | 16.00 | 4.00 | 14.00 |
| synthetic | Pure Liquid | 500 | accuracy | 14.22 | 10.22 | 14.67 | 4.44 | 14.67 |
| synthetic | Pure Liquid | 5000 | accuracy | 16.00 | 0.00 | 16.00 | 4.00 | 14.00 |

LALM exceeds Pure Liquid on the reported aggregates. The trained prefix does not consistently exceed the zero prefix, and LoCoMo varies substantially across checkpoints. These are descriptive comparisons; mean +/- SD alone does not establish statistical significance.

## 4. Saved files and exact artifact locations

- [All new per-run scores](per_run.csv)
- [New scores averaged within each training seed](per_seed.csv)
- [New suite aggregates](means.csv)
- [Five-seed individual scores](five_seed_per_seed.csv)
- [Five-seed aggregate scores](five_seed_means.csv)
- [Machine-readable artifact index](artifact_index.csv)
- [Existing-prediction paired tests](significance/paired_tests.csv): the original analysis uses the existing three checkpoints; it has not been expanded to five.

Each predictions file is JSON Lines, one prediction per line. Configs are YAML; metric tables are CSV. Both training seed and evaluation seed are recorded separately. Completion receipts retain source and artifact hashes. Baseline loaded-checkpoint IDs are bookkeeping and do not imply learned checkpoint dependence. Paths below are relative to this report.

| Group | Dataset / method | Checkpoint seed | Eval seed | Predictions | Config | Metrics | Receipt |
| --- | --- | --- | --- | --- | --- | --- | --- |
| cue-free | synthetic / bounded_rag | 7 | 13 | [JSONL](<jobs/02fe994480ee/runs/20261001T164837Z_synthetic/predictions.jsonl>) | [YAML](<jobs/02fe994480ee/runs/20261001T164837Z_synthetic/config.yaml>) | [CSV](<jobs/02fe994480ee/runs/20261001T164837Z_synthetic/metrics.csv>) | [JSON](<jobs/02fe994480ee/complete.json>) |
| cue-free | synthetic / bounded_rag | 7 | 17 | [JSONL](<jobs/03c1e4bdf7b8/runs/20261001T171104Z_synthetic/predictions.jsonl>) | [YAML](<jobs/03c1e4bdf7b8/runs/20261001T171104Z_synthetic/config.yaml>) | [CSV](<jobs/03c1e4bdf7b8/runs/20261001T171104Z_synthetic/metrics.csv>) | [JSON](<jobs/03c1e4bdf7b8/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 37 | 17 | [JSONL](<jobs/06b841833798/runs/20261001T215250Z_synthetic/predictions.jsonl>) | [YAML](<jobs/06b841833798/runs/20261001T215250Z_synthetic/config.yaml>) | [CSV](<jobs/06b841833798/runs/20261001T215250Z_synthetic/metrics.csv>) | [JSON](<jobs/06b841833798/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 41 | 17 | [JSONL](<jobs/0b803061ad07/runs/20261002T001246Z_synthetic/predictions.jsonl>) | [YAML](<jobs/0b803061ad07/runs/20261002T001246Z_synthetic/config.yaml>) | [CSV](<jobs/0b803061ad07/runs/20261002T001246Z_synthetic/metrics.csv>) | [JSON](<jobs/0b803061ad07/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 37 | 13 | [JSONL](<jobs/117ab5eaf5f0/runs/20261001T213042Z_synthetic/predictions.jsonl>) | [YAML](<jobs/117ab5eaf5f0/runs/20261001T213042Z_synthetic/config.yaml>) | [CSV](<jobs/117ab5eaf5f0/runs/20261001T213042Z_synthetic/metrics.csv>) | [JSON](<jobs/117ab5eaf5f0/complete.json>) |
| extra-seeds | synthetic / lalm | 37 | 11 | [JSONL](<jobs/1493bffeb141/runs/20261001T204103Z_synthetic/predictions.jsonl>) | [YAML](<jobs/1493bffeb141/runs/20261001T204103Z_synthetic/config.yaml>) | [CSV](<jobs/1493bffeb141/runs/20261001T204103Z_synthetic/metrics.csv>) | [JSON](<jobs/1493bffeb141/complete.json>) |
| extra-seeds | synthetic / lalm | 37 | 13 | [JSONL](<jobs/1ec82b4b7ee9/runs/20261001T210829Z_synthetic/predictions.jsonl>) | [YAML](<jobs/1ec82b4b7ee9/runs/20261001T210829Z_synthetic/config.yaml>) | [CSV](<jobs/1ec82b4b7ee9/runs/20261001T210829Z_synthetic/metrics.csv>) | [JSON](<jobs/1ec82b4b7ee9/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 37 | 11 | [JSONL](<jobs/21e9371300b3/runs/20261001T204809Z_synthetic/predictions.jsonl>) | [YAML](<jobs/21e9371300b3/runs/20261001T204809Z_synthetic/config.yaml>) | [CSV](<jobs/21e9371300b3/runs/20261001T204809Z_synthetic/metrics.csv>) | [JSON](<jobs/21e9371300b3/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 41 | 13 | [JSONL](<jobs/21ec68e1f4d6/runs/20261001T235627Z_synthetic/predictions.jsonl>) | [YAML](<jobs/21ec68e1f4d6/runs/20261001T235627Z_synthetic/config.yaml>) | [CSV](<jobs/21ec68e1f4d6/runs/20261001T235627Z_synthetic/metrics.csv>) | [JSON](<jobs/21ec68e1f4d6/complete.json>) |
| cue-free | synthetic / lexical_only | 7 | 13 | [JSONL](<jobs/21ef6970b36d/runs/20261001T164534Z_synthetic/predictions.jsonl>) | [YAML](<jobs/21ef6970b36d/runs/20261001T164534Z_synthetic/config.yaml>) | [CSV](<jobs/21ef6970b36d/runs/20261001T164534Z_synthetic/metrics.csv>) | [JSON](<jobs/21ef6970b36d/complete.json>) |
| ordering | synthetic / rag_timestamp | 7 | 13 | [JSONL](<jobs/25a064f28a86/runs/20261001T171700Z_synthetic/predictions.jsonl>) | [YAML](<jobs/25a064f28a86/runs/20261001T171700Z_synthetic/config.yaml>) | [CSV](<jobs/25a064f28a86/runs/20261001T171700Z_synthetic/metrics.csv>) | [JSON](<jobs/25a064f28a86/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 41 | 17 | [JSONL](<jobs/279b558afcb3/runs/20261002T002809Z_synthetic/predictions.jsonl>) | [YAML](<jobs/279b558afcb3/runs/20261002T002809Z_synthetic/config.yaml>) | [CSV](<jobs/279b558afcb3/runs/20261002T002809Z_synthetic/metrics.csv>) | [JSON](<jobs/279b558afcb3/complete.json>) |
| extra-seeds | locomo / pure_liquid | 41 | 7 | [JSONL](<jobs/2943a130173a/runs/20261002T004854Z_locomo/predictions.jsonl>) | [YAML](<jobs/2943a130173a/runs/20261002T004854Z_locomo/config.yaml>) | [CSV](<jobs/2943a130173a/runs/20261002T004854Z_locomo/metrics.csv>) | [JSON](<jobs/2943a130173a/complete.json>) |
| ordering | synthetic / rag_timestamp | 7 | 11 | [JSONL](<jobs/319ef59dc9de/runs/20261001T171313Z_synthetic/predictions.jsonl>) | [YAML](<jobs/319ef59dc9de/runs/20261001T171313Z_synthetic/config.yaml>) | [CSV](<jobs/319ef59dc9de/runs/20261001T171313Z_synthetic/metrics.csv>) | [JSON](<jobs/319ef59dc9de/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 37 | 11 | [JSONL](<jobs/36d99218b119/runs/20261001T205844Z_synthetic/predictions.jsonl>) | [YAML](<jobs/36d99218b119/runs/20261001T205844Z_synthetic/config.yaml>) | [CSV](<jobs/36d99218b119/runs/20261001T205844Z_synthetic/metrics.csv>) | [JSON](<jobs/36d99218b119/complete.json>) |
| extra-seeds | synthetic / lalm | 41 | 11 | [JSONL](<jobs/3ab6c813eae8/runs/20261001T231227Z_synthetic/predictions.jsonl>) | [YAML](<jobs/3ab6c813eae8/runs/20261001T231227Z_synthetic/config.yaml>) | [CSV](<jobs/3ab6c813eae8/runs/20261001T231227Z_synthetic/metrics.csv>) | [JSON](<jobs/3ab6c813eae8/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 37 | 13 | [JSONL](<jobs/4ab13c55fc40/runs/20261001T211514Z_synthetic/predictions.jsonl>) | [YAML](<jobs/4ab13c55fc40/runs/20261001T211514Z_synthetic/config.yaml>) | [CSV](<jobs/4ab13c55fc40/runs/20261001T211514Z_synthetic/metrics.csv>) | [JSON](<jobs/4ab13c55fc40/complete.json>) |
| extra-seeds | longmemeval / lalm | 41 | 7 | [JSONL](<jobs/5bf7fad02365/runs/20261002T003308Z_longmemeval/predictions.jsonl>) | [YAML](<jobs/5bf7fad02365/runs/20261002T003308Z_longmemeval/config.yaml>) | [CSV](<jobs/5bf7fad02365/runs/20261002T003308Z_longmemeval/metrics.csv>) | [JSON](<jobs/5bf7fad02365/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 41 | 11 | [JSONL](<jobs/5c27f5d4e30e/runs/20261001T232931Z_synthetic/predictions.jsonl>) | [YAML](<jobs/5c27f5d4e30e/runs/20261001T232931Z_synthetic/config.yaml>) | [CSV](<jobs/5c27f5d4e30e/runs/20261001T232931Z_synthetic/metrics.csv>) | [JSON](<jobs/5c27f5d4e30e/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 41 | 13 | [JSONL](<jobs/5c4cfb877809/runs/20261001T234555Z_synthetic/predictions.jsonl>) | [YAML](<jobs/5c4cfb877809/runs/20261001T234555Z_synthetic/config.yaml>) | [CSV](<jobs/5c4cfb877809/runs/20261001T234555Z_synthetic/metrics.csv>) | [JSON](<jobs/5c4cfb877809/complete.json>) |
| ordering | locomo / rag_timestamp | 7 | 7 | [JSONL](<jobs/5e43194d7919/runs/20261001T172841Z_locomo/predictions.jsonl>) | [YAML](<jobs/5e43194d7919/runs/20261001T172841Z_locomo/config.yaml>) | [CSV](<jobs/5e43194d7919/runs/20261001T172841Z_locomo/metrics.csv>) | [JSON](<jobs/5e43194d7919/complete.json>) |
| extra-seeds | longmemeval / pure_liquid | 41 | 7 | [JSONL](<jobs/5fc437b43c4a/runs/20261002T003916Z_longmemeval/predictions.jsonl>) | [YAML](<jobs/5fc437b43c4a/runs/20261002T003916Z_longmemeval/config.yaml>) | [CSV](<jobs/5fc437b43c4a/runs/20261002T003916Z_longmemeval/metrics.csv>) | [JSON](<jobs/5fc437b43c4a/complete.json>) |
| cue-free | synthetic / rag | 7 | 17 | [JSONL](<jobs/62235148b537/runs/20261001T170842Z_synthetic/predictions.jsonl>) | [YAML](<jobs/62235148b537/runs/20261001T170842Z_synthetic/config.yaml>) | [CSV](<jobs/62235148b537/runs/20261001T170842Z_synthetic/metrics.csv>) | [JSON](<jobs/62235148b537/complete.json>) |
| extra-seeds | locomo / lalm | 37 | 7 | [JSONL](<jobs/68233ba278a8/runs/20261001T221431Z_locomo/predictions.jsonl>) | [YAML](<jobs/68233ba278a8/runs/20261001T221431Z_locomo/config.yaml>) | [CSV](<jobs/68233ba278a8/runs/20261001T221431Z_locomo/metrics.csv>) | [JSON](<jobs/68233ba278a8/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 37 | 17 | [JSONL](<jobs/6d5b6ad298a1/runs/20261001T214754Z_synthetic/predictions.jsonl>) | [YAML](<jobs/6d5b6ad298a1/runs/20261001T214754Z_synthetic/config.yaml>) | [CSV](<jobs/6d5b6ad298a1/runs/20261001T214754Z_synthetic/metrics.csv>) | [JSON](<jobs/6d5b6ad298a1/complete.json>) |
| extra-seeds | longmemeval / lalm | 37 | 7 | [JSONL](<jobs/6eebe980f586/runs/20261001T220241Z_longmemeval/predictions.jsonl>) | [YAML](<jobs/6eebe980f586/runs/20261001T220241Z_longmemeval/config.yaml>) | [CSV](<jobs/6eebe980f586/runs/20261001T220241Z_longmemeval/metrics.csv>) | [JSON](<jobs/6eebe980f586/complete.json>) |
| extra-seeds | longmemeval / pure_liquid | 37 | 7 | [JSONL](<jobs/74d662bbcfcd/runs/20261001T220919Z_longmemeval/predictions.jsonl>) | [YAML](<jobs/74d662bbcfcd/runs/20261001T220919Z_longmemeval/config.yaml>) | [CSV](<jobs/74d662bbcfcd/runs/20261001T220919Z_longmemeval/metrics.csv>) | [JSON](<jobs/74d662bbcfcd/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 41 | 17 | [JSONL](<jobs/7e309a14449c/runs/20261002T002316Z_synthetic/predictions.jsonl>) | [YAML](<jobs/7e309a14449c/runs/20261002T002316Z_synthetic/config.yaml>) | [CSV](<jobs/7e309a14449c/runs/20261002T002316Z_synthetic/metrics.csv>) | [JSON](<jobs/7e309a14449c/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 41 | 11 | [JSONL](<jobs/8233db162968/runs/20261001T232434Z_synthetic/predictions.jsonl>) | [YAML](<jobs/8233db162968/runs/20261001T232434Z_synthetic/config.yaml>) | [CSV](<jobs/8233db162968/runs/20261001T232434Z_synthetic/metrics.csv>) | [JSON](<jobs/8233db162968/complete.json>) |
| cue-free | synthetic / lexical_only | 7 | 17 | [JSONL](<jobs/830b6f641ec5/runs/20261001T170609Z_synthetic/predictions.jsonl>) | [YAML](<jobs/830b6f641ec5/runs/20261001T170609Z_synthetic/config.yaml>) | [CSV](<jobs/830b6f641ec5/runs/20261001T170609Z_synthetic/metrics.csv>) | [JSON](<jobs/830b6f641ec5/complete.json>) |
| ordering | synthetic / rag_timestamp | 7 | 17 | [JSONL](<jobs/84d429ae90c4/runs/20261001T172031Z_synthetic/predictions.jsonl>) | [YAML](<jobs/84d429ae90c4/runs/20261001T172031Z_synthetic/config.yaml>) | [CSV](<jobs/84d429ae90c4/runs/20261001T172031Z_synthetic/metrics.csv>) | [JSON](<jobs/84d429ae90c4/complete.json>) |
| ordering | longmemeval / rag_timestamp | 7 | 7 | [JSONL](<jobs/856e25df2b73/runs/20261001T172422Z_longmemeval/predictions.jsonl>) | [YAML](<jobs/856e25df2b73/runs/20261001T172422Z_longmemeval/config.yaml>) | [CSV](<jobs/856e25df2b73/runs/20261001T172422Z_longmemeval/metrics.csv>) | [JSON](<jobs/856e25df2b73/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 41 | 17 | [JSONL](<jobs/85de0594302b/runs/20261002T001818Z_synthetic/predictions.jsonl>) | [YAML](<jobs/85de0594302b/runs/20261002T001818Z_synthetic/config.yaml>) | [CSV](<jobs/85de0594302b/runs/20261002T001818Z_synthetic/metrics.csv>) | [JSON](<jobs/85de0594302b/complete.json>) |
| cue-free | synthetic / lalm | 23 | 11 | [JSONL](<jobs/89ba23de93ba/runs/20261001T161438Z_synthetic/predictions.jsonl>) | [YAML](<jobs/89ba23de93ba/runs/20261001T161438Z_synthetic/config.yaml>) | [CSV](<jobs/89ba23de93ba/runs/20261001T161438Z_synthetic/metrics.csv>) | [JSON](<jobs/89ba23de93ba/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 37 | 11 | [JSONL](<jobs/937e70a10638/runs/20261001T205347Z_synthetic/predictions.jsonl>) | [YAML](<jobs/937e70a10638/runs/20261001T205347Z_synthetic/config.yaml>) | [CSV](<jobs/937e70a10638/runs/20261001T205347Z_synthetic/metrics.csv>) | [JSON](<jobs/937e70a10638/complete.json>) |
| cue-free | synthetic / lexical_only | 7 | 11 | [JSONL](<jobs/96befaf442d6/runs/20261001T162128Z_synthetic/predictions.jsonl>) | [YAML](<jobs/96befaf442d6/runs/20261001T162128Z_synthetic/config.yaml>) | [CSV](<jobs/96befaf442d6/runs/20261001T162128Z_synthetic/metrics.csv>) | [JSON](<jobs/96befaf442d6/complete.json>) |
| extra-seeds | synthetic / lalm | 41 | 13 | [JSONL](<jobs/9782868b52f5/runs/20261001T233919Z_synthetic/predictions.jsonl>) | [YAML](<jobs/9782868b52f5/runs/20261001T233919Z_synthetic/config.yaml>) | [CSV](<jobs/9782868b52f5/runs/20261001T233919Z_synthetic/metrics.csv>) | [JSON](<jobs/9782868b52f5/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 41 | 13 | [JSONL](<jobs/9788924b5cc9/runs/20261001T235129Z_synthetic/predictions.jsonl>) | [YAML](<jobs/9788924b5cc9/runs/20261001T235129Z_synthetic/config.yaml>) | [CSV](<jobs/9788924b5cc9/runs/20261001T235129Z_synthetic/metrics.csv>) | [JSON](<jobs/9788924b5cc9/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 41 | 13 | [JSONL](<jobs/9aaf2c28888b/runs/20261002T000119Z_synthetic/predictions.jsonl>) | [YAML](<jobs/9aaf2c28888b/runs/20261002T000119Z_synthetic/config.yaml>) | [CSV](<jobs/9aaf2c28888b/runs/20261002T000119Z_synthetic/metrics.csv>) | [JSON](<jobs/9aaf2c28888b/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 41 | 11 | [JSONL](<jobs/abe44969d095/runs/20261001T233427Z_synthetic/predictions.jsonl>) | [YAML](<jobs/abe44969d095/runs/20261001T233427Z_synthetic/config.yaml>) | [CSV](<jobs/abe44969d095/runs/20261001T233427Z_synthetic/metrics.csv>) | [JSON](<jobs/abe44969d095/complete.json>) |
| extra-seeds | synthetic / lalm_random_prefix | 37 | 13 | [JSONL](<jobs/ad6e045a37e6/runs/20261001T212546Z_synthetic/predictions.jsonl>) | [YAML](<jobs/ad6e045a37e6/runs/20261001T212546Z_synthetic/config.yaml>) | [CSV](<jobs/ad6e045a37e6/runs/20261001T212546Z_synthetic/metrics.csv>) | [JSON](<jobs/ad6e045a37e6/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 37 | 17 | [JSONL](<jobs/ae066c580181/runs/20261001T215745Z_synthetic/predictions.jsonl>) | [YAML](<jobs/ae066c580181/runs/20261001T215745Z_synthetic/config.yaml>) | [CSV](<jobs/ae066c580181/runs/20261001T215745Z_synthetic/metrics.csv>) | [JSON](<jobs/ae066c580181/complete.json>) |
| cue-free | synthetic / lalm | 7 | 13 | [JSONL](<jobs/b3a641655e50/runs/20261001T162838Z_synthetic/predictions.jsonl>) | [YAML](<jobs/b3a641655e50/runs/20261001T162838Z_synthetic/config.yaml>) | [CSV](<jobs/b3a641655e50/runs/20261001T162838Z_synthetic/metrics.csv>) | [JSON](<jobs/b3a641655e50/complete.json>) |
| cue-free | synthetic / lalm | 13 | 17 | [JSONL](<jobs/bc8b40260241/runs/20261001T165444Z_synthetic/predictions.jsonl>) | [YAML](<jobs/bc8b40260241/runs/20261001T165444Z_synthetic/config.yaml>) | [CSV](<jobs/bc8b40260241/runs/20261001T165444Z_synthetic/metrics.csv>) | [JSON](<jobs/bc8b40260241/complete.json>) |
| cue-free | synthetic / bounded_rag | 7 | 11 | [JSONL](<jobs/bfce993a3cff/runs/20261001T162623Z_synthetic/predictions.jsonl>) | [YAML](<jobs/bfce993a3cff/runs/20261001T162623Z_synthetic/config.yaml>) | [CSV](<jobs/bfce993a3cff/runs/20261001T162623Z_synthetic/metrics.csv>) | [JSON](<jobs/bfce993a3cff/complete.json>) |
| extra-seeds | locomo / lalm | 41 | 7 | [JSONL](<jobs/bff3d541a472/runs/20261002T004424Z_locomo/predictions.jsonl>) | [YAML](<jobs/bff3d541a472/runs/20261002T004424Z_locomo/config.yaml>) | [CSV](<jobs/bff3d541a472/runs/20261002T004424Z_locomo/metrics.csv>) | [JSON](<jobs/bff3d541a472/complete.json>) |
| extra-seeds | synthetic / lalm_zero_prefix | 37 | 13 | [JSONL](<jobs/c0095f01390c/runs/20261001T212050Z_synthetic/predictions.jsonl>) | [YAML](<jobs/c0095f01390c/runs/20261001T212050Z_synthetic/config.yaml>) | [CSV](<jobs/c0095f01390c/runs/20261001T212050Z_synthetic/metrics.csv>) | [JSON](<jobs/c0095f01390c/complete.json>) |
| extra-seeds | synthetic / lalm | 41 | 17 | [JSONL](<jobs/c338fef662b2/runs/20261002T000611Z_synthetic/predictions.jsonl>) | [YAML](<jobs/c338fef662b2/runs/20261002T000611Z_synthetic/config.yaml>) | [CSV](<jobs/c338fef662b2/runs/20261002T000611Z_synthetic/metrics.csv>) | [JSON](<jobs/c338fef662b2/complete.json>) |
| extra-seeds | train / train | 41 | 41 | -- | [YAML](<jobs/c3f6920e4d3e/runs/20261001T222400Z_train_liquid/config.yaml>) | -- | [JSON](<jobs/c3f6920e4d3e/complete.json>) |
| cue-free | synthetic / lalm | 7 | 17 | [JSONL](<jobs/c80107527c45/runs/20261001T164951Z_synthetic/predictions.jsonl>) | [YAML](<jobs/c80107527c45/runs/20261001T164951Z_synthetic/config.yaml>) | [CSV](<jobs/c80107527c45/runs/20261001T164951Z_synthetic/metrics.csv>) | [JSON](<jobs/c80107527c45/complete.json>) |
| extra-seeds | locomo / pure_liquid | 37 | 7 | [JSONL](<jobs/cd68a31991ab/runs/20261001T222032Z_locomo/predictions.jsonl>) | [YAML](<jobs/cd68a31991ab/runs/20261001T222032Z_locomo/config.yaml>) | [CSV](<jobs/cd68a31991ab/runs/20261001T222032Z_locomo/metrics.csv>) | [JSON](<jobs/cd68a31991ab/complete.json>) |
| cue-free | synthetic / lalm | 13 | 13 | [JSONL](<jobs/cff8a674c1ed/runs/20261001T163502Z_synthetic/predictions.jsonl>) | [YAML](<jobs/cff8a674c1ed/runs/20261001T163502Z_synthetic/config.yaml>) | [CSV](<jobs/cff8a674c1ed/runs/20261001T163502Z_synthetic/metrics.csv>) | [JSON](<jobs/cff8a674c1ed/complete.json>) |
| cue-free | synthetic / rag | 7 | 11 | [JSONL](<jobs/d539dfa58c2b/runs/20261001T162359Z_synthetic/predictions.jsonl>) | [YAML](<jobs/d539dfa58c2b/runs/20261001T162359Z_synthetic/config.yaml>) | [CSV](<jobs/d539dfa58c2b/runs/20261001T162359Z_synthetic/metrics.csv>) | [JSON](<jobs/d539dfa58c2b/complete.json>) |
| cue-free | synthetic / lalm | 23 | 13 | [JSONL](<jobs/d882c80278ac/runs/20261001T164033Z_synthetic/predictions.jsonl>) | [YAML](<jobs/d882c80278ac/runs/20261001T164033Z_synthetic/config.yaml>) | [CSV](<jobs/d882c80278ac/runs/20261001T164033Z_synthetic/metrics.csv>) | [JSON](<jobs/d882c80278ac/complete.json>) |
| cue-free | synthetic / rag | 7 | 13 | [JSONL](<jobs/dc7300a4f683/runs/20261001T164717Z_synthetic/predictions.jsonl>) | [YAML](<jobs/dc7300a4f683/runs/20261001T164717Z_synthetic/config.yaml>) | [CSV](<jobs/dc7300a4f683/runs/20261001T164717Z_synthetic/metrics.csv>) | [JSON](<jobs/dc7300a4f683/complete.json>) |
| cue-free | synthetic / lalm | 23 | 17 | [JSONL](<jobs/de6007f077ed/runs/20261001T165947Z_synthetic/predictions.jsonl>) | [YAML](<jobs/de6007f077ed/runs/20261001T165947Z_synthetic/config.yaml>) | [CSV](<jobs/de6007f077ed/runs/20261001T165947Z_synthetic/metrics.csv>) | [JSON](<jobs/de6007f077ed/complete.json>) |
| cue-free | synthetic / lalm | 7 | 11 | [JSONL](<jobs/df1dc1e62ce9/runs/20261001T160312Z_synthetic/predictions.jsonl>) | [YAML](<jobs/df1dc1e62ce9/runs/20261001T160312Z_synthetic/config.yaml>) | [CSV](<jobs/df1dc1e62ce9/runs/20261001T160312Z_synthetic/metrics.csv>) | [JSON](<jobs/df1dc1e62ce9/complete.json>) |
| cue-free | synthetic / lalm | 13 | 11 | [JSONL](<jobs/e60a2c5fac2c/runs/20261001T160914Z_synthetic/predictions.jsonl>) | [YAML](<jobs/e60a2c5fac2c/runs/20261001T160914Z_synthetic/config.yaml>) | [CSV](<jobs/e60a2c5fac2c/runs/20261001T160914Z_synthetic/metrics.csv>) | [JSON](<jobs/e60a2c5fac2c/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 37 | 17 | [JSONL](<jobs/ea52da2eed83/runs/20261001T214217Z_synthetic/predictions.jsonl>) | [YAML](<jobs/ea52da2eed83/runs/20261001T214217Z_synthetic/config.yaml>) | [CSV](<jobs/ea52da2eed83/runs/20261001T214217Z_synthetic/metrics.csv>) | [JSON](<jobs/ea52da2eed83/complete.json>) |
| extra-seeds | synthetic / lalm_permuted_prefix | 37 | 11 | [JSONL](<jobs/f42cfd8a5820/runs/20261001T210335Z_synthetic/predictions.jsonl>) | [YAML](<jobs/f42cfd8a5820/runs/20261001T210335Z_synthetic/config.yaml>) | [CSV](<jobs/f42cfd8a5820/runs/20261001T210335Z_synthetic/metrics.csv>) | [JSON](<jobs/f42cfd8a5820/complete.json>) |
| extra-seeds | synthetic / lalm | 37 | 17 | [JSONL](<jobs/f988f69798ec/runs/20261001T213535Z_synthetic/predictions.jsonl>) | [YAML](<jobs/f988f69798ec/runs/20261001T213535Z_synthetic/config.yaml>) | [CSV](<jobs/f988f69798ec/runs/20261001T213535Z_synthetic/metrics.csv>) | [JSON](<jobs/f988f69798ec/complete.json>) |
| extra-seeds | train / train | 37 | 37 | -- | [YAML](<jobs/fa359ed20613/runs/20261001T195142Z_train_liquid/config.yaml>) | -- | [JSON](<jobs/fa359ed20613/complete.json>) |
| extra-seeds | synthetic / pure_liquid | 41 | 11 | [JSONL](<jobs/fc5de329d026/runs/20261001T231901Z_synthetic/predictions.jsonl>) | [YAML](<jobs/fc5de329d026/runs/20261001T231901Z_synthetic/config.yaml>) | [CSV](<jobs/fc5de329d026/runs/20261001T231901Z_synthetic/metrics.csv>) | [JSON](<jobs/fc5de329d026/complete.json>) |

## Rebuild this report

From the LALM project root:

```powershell
python experiments/summarize_results.py
python experiments/aggregate_five_seeds.py
python experiments/build_results_report.py
```

