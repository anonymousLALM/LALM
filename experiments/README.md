# Evaluation and analysis

Run commands from this project root, using the same Python/CUDA environment as the completed runs. No new model dependencies are required.

## Commands

For a published checkout, use `python experiments/reproduce.py --plan` and the [root README](../README.md). The original runners below describe historical commands; completed historical receipts cannot be resumed with edited publication source.

```powershell
python experiments/run_study.py --plan
python experiments/run_study.py --group all
```

Completed jobs are hash-verified and skipped on restart. Interrupted jobs restart from their beginning in a new run folder; partial outputs are never included in summaries. Do not edit source/configs during a suite. If the protocol changes, use `--output results/evaluation_study_v2`. Only one runner should write to a given output directory at a time.

## Scope and optional training

- `cue-free`: 1,000/5,000 turns, evaluation seeds 11/13/17; LALM checkpoints 7/13/23 and shared Lexical-only, Growing RAG, Bounded RAG (18 jobs).
- The deterministic stress variant preserves generated entities, truth traces, timestamps, answer labels and distractors. Destination corrections use three paraphrases; response-style corrections also omit cues. Correction queries omit `currently`. Cue removal applies to correction utterances, not unrelated negative facts. Modified streams receive distinct IDs and are saved as `streams_<horizon>.jsonl`. Per-question-type rows distinguish correction behavior from overall accuracy.
- `ordering`: Growing RAG retains its original dense top-eight membership and clipping, changing only output order to timestamp with insertion-index ties. All horizons, three synthetic evaluation seeds, and both released datasets (5 jobs). Existing released-data batch settings are retained.
- `extra-seeds` is optional and excluded from `all`. Seeds 37 and 41 are fixed prospectively. Each is trained and evaluated on all synthetic horizons, both released datasets, Pure Liquid, and 1K/5K zero/random/permuted-prefix controls.

```powershell
python experiments/run_study.py --group extra-seeds
```

The new seeds are complete and their verified results are included in the five-seed result package. This runner does not silently change the current three-seed study.

## Outputs

```
results/evaluation_study/
  jobs/<12-character-job-id>/
    config.yaml
    command.json
    complete.json
    runs/<run-id>/
      predictions.jsonl
      metrics.csv
      config.yaml
      dataset_manifest.json
      environment.json
      hardware.json
  per_run.csv
  per_seed.csv
  means.csv
  RESULTS.md
  inventory.json
  significance/
    paired_tests.csv
    provenance.json
    RESULTS.md
```

The loaded checkpoint seed and evaluation seed are recorded separately. Each job includes source hashes and artifact hashes. Summaries include per-question-type values, stream means within each training seed, then mean/sample SD across trained seeds. Shared controls have no training-seed SD. Counts identify partial suites; no absent job is filled with zero. Regenerate tables at any point with `python experiments/summarize_results.py`.

## Existing-prediction significance

```powershell
python experiments/paired_significance.py
```

`paired_sources.json` explicitly lists the saved prediction files; analysis refuses mismatched IDs, references, queries, or conflicting duplicates. Reports use 10,000 paired bootstrap resamples for pointwise 95% CIs and two-sided paired sign-randomization p-values, with Holm adjustment across aggregate comparisons only. LoCoMo resamples whole conversations (only ten clusters); other datasets resample questions. Aggregate results average checkpoint scores within each question before inference, conditional on those fitted checkpoints. These tests do not estimate population uncertainty over training seeds. All five checkpoints have matched trained-vs-zero predictions. Methodological context: [Dror et al., ACL 2018](https://aclanthology.org/P18-1128/).

## Verification

`python -m pytest tests/unit/test_evaluation_controls.py -q -p no:cacheprovider` checks retrieval/formula invariants and a synthetic evaluation export with stub models. This is a CPU wiring test, not a full GPU accuracy run. Stub outputs live only in pytest's temporary directory, never in the saved results.

Job directories use compact deterministic IDs to stay below Windows path limits. Human-readable group/dataset/method/seed names remain in terminal output, configs, receipts and the inventory. Previously completed jobs retain their original paths.

After all 63 LALM jobs finish, run `python experiments/summarize_results.py` followed by `python experiments/aggregate_five_seeds.py`. The latter verifies saved artifact hashes and produces `five_seed_per_seed.csv`, `five_seed_means.csv`, `FIVE_SEED_RESULTS.md`, and `artifact_index.csv` with exact prediction/config paths.
