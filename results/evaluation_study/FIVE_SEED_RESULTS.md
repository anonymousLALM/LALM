# Five-training-seed results

Percentages; synthetic evaluation streams are averaged within each training seed before computing mean/sample SD across 7/13/23/37/41. Released-data scores are local diagnostics.

| Experiment | Method | Horizon | Metric | Mean +/- SD (%) |
|---|---|---:|---|---:|
| locomo | lalm |  | locomo_official_qa_score | 29.05 +/- 5.30 |
| locomo | pure_liquid |  | locomo_official_qa_score | 7.44 +/- 4.45 |
| longmemeval | lalm |  | diagnostic_token_f1 | 20.64 +/- 2.67 |
| longmemeval | pure_liquid |  | diagnostic_token_f1 | 8.69 +/- 1.20 |
| prefix_1000 | lalm | 1000 | accuracy | 69.73 +/- 4.61 |
| prefix_1000 | lalm_permuted_prefix | 1000 | accuracy | 60.80 +/- 6.72 |
| prefix_1000 | lalm_random_prefix | 1000 | accuracy | 62.80 +/- 2.38 |
| prefix_1000 | lalm_zero_prefix | 1000 | accuracy | 70.00 +/- 0.00 |
| prefix_5000 | lalm | 5000 | accuracy | 70.53 +/- 6.23 |
| prefix_5000 | lalm_permuted_prefix | 5000 | accuracy | 62.53 +/- 6.82 |
| prefix_5000 | lalm_random_prefix | 5000 | accuracy | 62.67 +/- 2.49 |
| prefix_5000 | lalm_zero_prefix | 5000 | accuracy | 67.87 +/- 0.73 |
| synthetic | lalm | 100 | accuracy | 73.00 +/- 5.24 |
| synthetic | lalm | 1000 | accuracy | 69.73 +/- 4.61 |
| synthetic | lalm | 500 | accuracy | 67.56 +/- 4.92 |
| synthetic | lalm | 5000 | accuracy | 70.53 +/- 6.23 |
| synthetic | pure_liquid | 100 | accuracy | 12.27 +/- 4.36 |
| synthetic | pure_liquid | 1000 | accuracy | 10.67 +/- 6.45 |
| synthetic | pure_liquid | 500 | accuracy | 11.64 +/- 4.44 |
| synthetic | pure_liquid | 5000 | accuracy | 10.00 +/- 7.48 |
