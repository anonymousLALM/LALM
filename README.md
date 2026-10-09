# LALM: Lexically Augmented Liquid Memory

An eight-slot recurrent memory with a bounded 512-entry text sidecar for conversational question answering. This repository provides the implementation, five trained checkpoints, saved predictions, configurations, result tables and paired significance tests.

## Results

| Study | Tables and per-seed results |
|---|---|
| Original rule, five training seeds | [Five-seed results](results/evaluation_study/FIVE_SEED_RESULTS.md) |
| Cue-free corrections and timestamp ordering | [Synthetic and released-data study](results/evaluation_study/STUDY_RESULTS.md) |
| Newest-wins replacement | [Results](results/followup_study/RESULTS.md) |
| Newest-wins prefix controls | [Trained, zero, random and permuted prefixes](results/additional_study/prefix_controls/LALM_PREFIX_CONTROLS_NEWEST.md) |
| Original-rule paired tests | [CSV](results/evaluation_study/significance/paired_tests.csv) |
| Newest-wins paired tests | [CSV](results/followup_study/significance/paired_tests.csv) |

Each study includes per-seed CSVs, means and sample standard deviations, paired-test CSVs and an artifact index. Each completed evaluation run retains its original `predictions.jsonl`, recorded `config.yaml`, metrics, type breakdowns, dataset manifest, relevant package versions and hardware information. Training and evaluation seeds are recorded separately. Unreported exploratory studies (including simulated agent tool tasks) are preserved in [supplementary/agent_tasks/](supplementary/agent_tasks/README.md).

## Structure

```text
LALM/
├── configs/                      # Model/data settings and prompts
├── data/                         # Dataset acquisition instructions
├── docs/PROTOCOL.md               # Metric definitions and interpretation
├── experiments/                  # Reproduction, analysis and paired tests
├── scripts/                      # Training and evaluation entry points
├── src/liquid_memory_agents/      # Memory, reader, encoders and baselines
├── tests/unit/                   # CPU correctness and export checks
├── results/
│   ├── historical/               # Original runs and checkpoints 7/13/23
│   ├── evaluation_study/         # Checkpoints 37/41 and five-seed studies
│   ├── followup_study/           # Newest-wins evaluations
│   ├── cue_free_completion/      # Original-rule cue-free seeds 37/41
│   ├── additional_study/
│   │   └── prefix_controls/
│   └── publication_manifest.json # SHA256 inventory of shipped results
├── supplementary/
│   └── agent_tasks/              # Supplementary archive for unreported agent tasks
├── pyproject.toml
└── requirements.txt
```

## Install

Python 3.12 was used for the saved runs. Full evaluations require a CUDA-capable GPU and model downloads. Install the CUDA-enabled PyTorch build appropriate for your hardware, then install the dependencies. Git LFS is required for checkpoints and JSONL files.

```powershell
git lfs install
git clone https://github.com/anonymousLALM/LALM.git
cd LALM
git lfs pull
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -e . --no-deps
```

On Linux/macOS, activate the environment with `source .venv/bin/activate`. The five checkpoints occupy about 1 GB; saved prediction files occupy about 552 MB. Benchmark inputs and model weights are downloaded separately:

```powershell
python scripts/download_data.py --dataset longmemeval
python scripts/download_data.py --dataset locomo
```

## Verify and analyze saved results

These commands require no new model inference:

```powershell
python experiments/verify_publication.py
python -m pytest tests/unit -q
python experiments/summarize_results.py
python experiments/aggregate_five_seeds.py
python experiments/export_missing_metrics.py
python experiments/summarize_results.py --output results/followup_study
python experiments/paired_significance.py
python experiments/paired_followup.py
python experiments/report_prefix_newest.py
```

The verifier checks the SHA256 result inventory, all five checkpoints, 147 completed manuscript job receipts (plus 36 supplementary receipts) and significance-table coverage. If an artifact is an LFS pointer, run `git lfs pull`. Original experiment fingerprints are preserved; `release_artifact_sha256` records hashes after metadata anonymization. Intermediate checkpoints, deterministic stream exports, duplicate error-only files and interrupted runs are excluded from the release.

## Reproduce evaluations

```powershell
python experiments/reproduce.py --plan
python experiments/reproduce.py --output results/reproduction
```

The plan covers 190 saved manuscript evaluation jobs (and 36 supplementary agent-task jobs). To replay a subset, set `--suite` to `historical`, `evaluation`, `newest-wins`, `cue-free-completion`, `prefix-controls`, or `agent-tasks` (supplementary).

Outputs go to a separate directory. Completed replay jobs are hash-verified and skipped on resume; an interrupted job restarts individually. Use one runner per output directory. Changes to code, configuration, checkpoints or released dataset inputs require a fresh output directory. Hardware/library differences may change floating-point values or generated answers.

To retrain using a checkpoint's recorded training configuration:

```powershell
python experiments/reproduce.py --train-seed 7 --output results/reproduction
```

Repeat for 13, 23, 37 and 41. Evaluate a newly trained checkpoint directly:

```powershell
python scripts/run_synthetic.py --config configs/synthetic.yaml --checkpoint "<new-run>/checkpoints/best.pt"
python scripts/run_real_benchmark.py --config configs/longmemeval.yaml --checkpoint "<new-run>/checkpoints/best.pt" --start-index 50
python scripts/run_real_benchmark.py --config configs/locomo.yaml --checkpoint "<new-run>/checkpoints/best.pt"
```

## Protocol

- **Training seeds:** 7, 13, 23, 37, 41. **Synthetic evaluation seeds:** 11, 13, 17.
- **Synthetic horizons:** 100, 500, 1,000 and 5,000 turns; 100/75/50/50 questions per stream respectively.
- **Reader:** `Qwen/Qwen2.5-3B-Instruct`, greedy decoding. **Encoder:** `sentence-transformers/all-MiniLM-L6-v2`. Both remain frozen.
- **LongMemEval:** indices 50-499, 450 questions; token F1 and exact match are local diagnostics, not the upstream LLM-judged score.
- **LoCoMo:** 1,986 questions across ten conversations; category-aware QA score plus diagnostic token F1 and exact match. Released textual image captions are used.
- **Mean +/- sample SD:** synthetic streams are averaged within each training checkpoint before aggregation across checkpoints. Shared baselines have no training-seed SD.
- **Cue-free streams:** correction utterances omit the specified cue words; labels and truth traces remain unchanged.
- **Newest-wins:** at full capacity, cosine similarity >= 0.82 replaces the closest record without requiring a correction cue. This is an evaluation-only variant; the original cue-gated rule remains the default.
- **Supplementary studies:** exploratory simulated tool tasks are archived in `supplementary/agent_tasks/` with dedicated schemas and prompts.
- **Logical user-memory payload:** 1,318,912 bytes (`8 * 256 * 4 + 512 * (384 * 4 + 1,024)`), distinct from GPU VRAM. Recorded hardware files identify the original RTX 5080 runs.

Paired inference uses 10,000 bootstrap resamples and two-sided paired sign-randomization tests. LoCoMo resamples whole conversations. Aggregate inference averages checkpoint scores within each question and is conditional on these fitted checkpoints. **Holm correction covers aggregate comparisons only**; per-seed adjusted p-values are blank. CSV scores are fractions; multiply by 100 for percentages or percentage-point differences.

## Anonymity audit

```powershell
python scripts/anonymize_repo.py
```

The audit checks source, metadata and checkpoint metadata separately from original benchmark records. Public benchmark questions can contain place names or ordinary words matching audit terms; their questions, references and predictions are preserved unchanged. Environment files include relevant dependency versions only, without personal editable-install URLs or workstation paths.
