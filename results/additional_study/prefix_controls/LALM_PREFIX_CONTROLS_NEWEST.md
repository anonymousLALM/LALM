# Item 1: newest-wins prefix controls

Completed new evaluation jobs: 30/30. Each job evaluates zero/random/permuted controls. Trained-prefix predictions are reused from the verified newest-wins study. Partial rows are explicitly marked; final tests require 150 matched questions and all five checkpoints.

| Stream | Horizon | Method | Seeds | Mean +/- sample SD (%) | Complete |
|---|---|---|---|---|---|
| original | 1000 | lalm | 5 | 69.60 +/- 6.05 | True |
| original | 1000 | lalm_zero_prefix | 5 | 68.00 +/- 0.00 | True |
| original | 1000 | lalm_random_prefix | 5 | 62.40 +/- 2.09 | True |
| original | 1000 | lalm_permuted_prefix | 5 | 59.87 +/- 6.10 | True |
| original | 5000 | lalm | 5 | 73.33 +/- 4.74 | True |
| original | 5000 | lalm_zero_prefix | 5 | 67.33 +/- 0.00 | True |
| original | 5000 | lalm_random_prefix | 5 | 66.00 +/- 2.00 | True |
| original | 5000 | lalm_permuted_prefix | 5 | 66.13 +/- 5.63 | True |
| cue_free | 5000 | lalm | 5 | 60.80 +/- 7.67 | True |
| cue_free | 5000 | lalm_zero_prefix | 5 | 54.00 +/- 0.00 | True |
| cue_free | 5000 | lalm_random_prefix | 5 | 58.27 +/- 1.80 | True |
| cue_free | 5000 | lalm_permuted_prefix | 5 | 59.87 +/- 2.28 | True |

## Per-seed values

| Stream | Horizon | Method | Seed | Accuracy (%) | Questions | Complete |
|---|---|---|---|---|---|---|
| original | 1000 | lalm | 7 | 73.33 | 150 | True |
| original | 1000 | lalm | 13 | 74.67 | 150 | True |
| original | 1000 | lalm | 23 | 66.00 | 150 | True |
| original | 1000 | lalm | 37 | 73.33 | 150 | True |
| original | 1000 | lalm | 41 | 60.67 | 150 | True |
| original | 1000 | lalm_zero_prefix | 7 | 68.00 | 150 | True |
| original | 1000 | lalm_zero_prefix | 13 | 68.00 | 150 | True |
| original | 1000 | lalm_zero_prefix | 23 | 68.00 | 150 | True |
| original | 1000 | lalm_zero_prefix | 37 | 68.00 | 150 | True |
| original | 1000 | lalm_zero_prefix | 41 | 68.00 | 150 | True |
| original | 1000 | lalm_random_prefix | 7 | 59.33 | 150 | True |
| original | 1000 | lalm_random_prefix | 13 | 64.67 | 150 | True |
| original | 1000 | lalm_random_prefix | 23 | 63.33 | 150 | True |
| original | 1000 | lalm_random_prefix | 37 | 61.33 | 150 | True |
| original | 1000 | lalm_random_prefix | 41 | 63.33 | 150 | True |
| original | 1000 | lalm_permuted_prefix | 7 | 56.67 | 150 | True |
| original | 1000 | lalm_permuted_prefix | 13 | 62.67 | 150 | True |
| original | 1000 | lalm_permuted_prefix | 23 | 50.67 | 150 | True |
| original | 1000 | lalm_permuted_prefix | 37 | 64.67 | 150 | True |
| original | 1000 | lalm_permuted_prefix | 41 | 64.67 | 150 | True |
| original | 5000 | lalm | 7 | 74.00 | 150 | True |
| original | 5000 | lalm | 13 | 78.00 | 150 | True |
| original | 5000 | lalm | 23 | 74.67 | 150 | True |
| original | 5000 | lalm | 37 | 74.67 | 150 | True |
| original | 5000 | lalm | 41 | 65.33 | 150 | True |
| original | 5000 | lalm_zero_prefix | 7 | 67.33 | 150 | True |
| original | 5000 | lalm_zero_prefix | 13 | 67.33 | 150 | True |
| original | 5000 | lalm_zero_prefix | 23 | 67.33 | 150 | True |
| original | 5000 | lalm_zero_prefix | 37 | 67.33 | 150 | True |
| original | 5000 | lalm_zero_prefix | 41 | 67.33 | 150 | True |
| original | 5000 | lalm_random_prefix | 7 | 62.67 | 150 | True |
| original | 5000 | lalm_random_prefix | 13 | 66.00 | 150 | True |
| original | 5000 | lalm_random_prefix | 23 | 66.67 | 150 | True |
| original | 5000 | lalm_random_prefix | 37 | 68.00 | 150 | True |
| original | 5000 | lalm_random_prefix | 41 | 66.67 | 150 | True |
| original | 5000 | lalm_permuted_prefix | 7 | 60.67 | 150 | True |
| original | 5000 | lalm_permuted_prefix | 13 | 70.00 | 150 | True |
| original | 5000 | lalm_permuted_prefix | 23 | 59.33 | 150 | True |
| original | 5000 | lalm_permuted_prefix | 37 | 70.00 | 150 | True |
| original | 5000 | lalm_permuted_prefix | 41 | 70.67 | 150 | True |
| cue_free | 5000 | lalm | 7 | 62.00 | 150 | True |
| cue_free | 5000 | lalm | 13 | 62.00 | 150 | True |
| cue_free | 5000 | lalm | 23 | 58.67 | 150 | True |
| cue_free | 5000 | lalm | 37 | 71.33 | 150 | True |
| cue_free | 5000 | lalm | 41 | 50.00 | 150 | True |
| cue_free | 5000 | lalm_zero_prefix | 7 | 54.00 | 150 | True |
| cue_free | 5000 | lalm_zero_prefix | 13 | 54.00 | 150 | True |
| cue_free | 5000 | lalm_zero_prefix | 23 | 54.00 | 150 | True |
| cue_free | 5000 | lalm_zero_prefix | 37 | 54.00 | 150 | True |
| cue_free | 5000 | lalm_zero_prefix | 41 | 54.00 | 150 | True |
| cue_free | 5000 | lalm_random_prefix | 7 | 59.33 | 150 | True |
| cue_free | 5000 | lalm_random_prefix | 13 | 55.33 | 150 | True |
| cue_free | 5000 | lalm_random_prefix | 23 | 60.00 | 150 | True |
| cue_free | 5000 | lalm_random_prefix | 37 | 58.67 | 150 | True |
| cue_free | 5000 | lalm_random_prefix | 41 | 58.00 | 150 | True |
| cue_free | 5000 | lalm_permuted_prefix | 7 | 60.67 | 150 | True |
| cue_free | 5000 | lalm_permuted_prefix | 13 | 60.00 | 150 | True |
| cue_free | 5000 | lalm_permuted_prefix | 23 | 56.00 | 150 | True |
| cue_free | 5000 | lalm_permuted_prefix | 37 | 60.67 | 150 | True |
| cue_free | 5000 | lalm_permuted_prefix | 41 | 62.00 | 150 | True |

## Paired tests

Differences and CIs below are percentage points. Raw p uses paired sign randomization; 95% CI uses paired bootstrap. Holm covers aggregate comparisons only. Aggregate results condition on the five fitted checkpoints.

| Stream | Horizon | Control | Seed | Difference | 95% CI | Raw p | Holm p |
|---|---|---|---|---|---|---|---|
| original | 1000 | lalm_zero_prefix | 7 | 5.33 | [0.67, 10.00] | 0.054495 |  |
| original | 1000 | lalm_zero_prefix | 13 | 6.67 | [2.00, 12.00] | 0.018898 |  |
| original | 1000 | lalm_zero_prefix | 23 | -2.00 | [-7.33, 3.33] | 0.62034 |  |
| original | 1000 | lalm_zero_prefix | 37 | 5.33 | [-2.00, 12.67] | 0.19498 |  |
| original | 1000 | lalm_zero_prefix | 41 | -7.33 | [-14.00, -1.33] | 0.043696 |  |
| original | 1000 | lalm_zero_prefix | mean | 1.60 | [-2.67, 6.13] | 0.50555 | 1 |
| original | 1000 | lalm_random_prefix | 7 | 14.00 | [8.67, 20.00] | 9.999e-05 |  |
| original | 1000 | lalm_random_prefix | 13 | 10.00 | [5.33, 15.33] | 9.999e-05 |  |
| original | 1000 | lalm_random_prefix | 23 | 2.67 | [-4.00, 9.33] | 0.56564 |  |
| original | 1000 | lalm_random_prefix | 37 | 12.00 | [5.33, 18.67] | 0.00029997 |  |
| original | 1000 | lalm_random_prefix | 41 | -2.67 | [-8.67, 3.33] | 0.52465 |  |
| original | 1000 | lalm_random_prefix | mean | 7.20 | [3.47, 11.20] | 0.00019998 | 0.0015998400159984002 |
| original | 1000 | lalm_permuted_prefix | 7 | 16.67 | [10.67, 22.67] | 9.999e-05 |  |
| original | 1000 | lalm_permuted_prefix | 13 | 12.00 | [6.67, 17.33] | 9.999e-05 |  |
| original | 1000 | lalm_permuted_prefix | 23 | 15.33 | [8.00, 23.33] | 0.00059994 |  |
| original | 1000 | lalm_permuted_prefix | 37 | 8.67 | [2.00, 15.33] | 0.012299 |  |
| original | 1000 | lalm_permuted_prefix | 41 | -4.00 | [-10.00, 1.33] | 0.26517 |  |
| original | 1000 | lalm_permuted_prefix | mean | 9.73 | [5.87, 13.87] | 9.999e-05 | 0.0008999100089991002 |
| original | 5000 | lalm_zero_prefix | 7 | 6.67 | [2.00, 12.00] | 0.020998 |  |
| original | 5000 | lalm_zero_prefix | 13 | 10.67 | [6.00, 16.00] | 0.00029997 |  |
| original | 5000 | lalm_zero_prefix | 23 | 7.33 | [2.00, 12.67] | 0.014399 |  |
| original | 5000 | lalm_zero_prefix | 37 | 7.33 | [0.00, 14.67] | 0.074793 |  |
| original | 5000 | lalm_zero_prefix | 41 | -2.00 | [-8.67, 4.67] | 0.70003 |  |
| original | 5000 | lalm_zero_prefix | mean | 6.00 | [1.33, 10.93] | 0.018298 | 0.0731926807319268 |
| original | 5000 | lalm_random_prefix | 7 | 11.33 | [6.00, 16.67] | 9.999e-05 |  |
| original | 5000 | lalm_random_prefix | 13 | 12.00 | [7.33, 17.33] | 9.999e-05 |  |
| original | 5000 | lalm_random_prefix | 23 | 8.00 | [2.00, 14.00] | 0.013199 |  |
| original | 5000 | lalm_random_prefix | 37 | 6.67 | [1.33, 12.67] | 0.044396 |  |
| original | 5000 | lalm_random_prefix | 41 | -1.33 | [-8.67, 6.00] | 0.86051 |  |
| original | 5000 | lalm_random_prefix | mean | 7.33 | [3.60, 11.47] | 0.00029997 | 0.0017998200179982003 |
| original | 5000 | lalm_permuted_prefix | 7 | 13.33 | [8.00, 19.33] | 9.999e-05 |  |
| original | 5000 | lalm_permuted_prefix | 13 | 8.00 | [4.00, 12.67] | 0.00039996 |  |
| original | 5000 | lalm_permuted_prefix | 23 | 15.33 | [8.67, 22.00] | 9.999e-05 |  |
| original | 5000 | lalm_permuted_prefix | 37 | 4.67 | [-1.33, 10.67] | 0.19158 |  |
| original | 5000 | lalm_permuted_prefix | 41 | -5.33 | [-12.00, 1.33] | 0.16928 |  |
| original | 5000 | lalm_permuted_prefix | mean | 7.20 | [3.60, 11.07] | 0.00019998 | 0.0015998400159984002 |
| cue_free | 5000 | lalm_zero_prefix | 7 | 8.00 | [4.00, 12.67] | 0.00069993 |  |
| cue_free | 5000 | lalm_zero_prefix | 13 | 8.00 | [3.33, 12.67] | 0.0017998 |  |
| cue_free | 5000 | lalm_zero_prefix | 23 | 4.67 | [0.00, 10.00] | 0.11729 |  |
| cue_free | 5000 | lalm_zero_prefix | 37 | 17.33 | [11.33, 24.00] | 9.999e-05 |  |
| cue_free | 5000 | lalm_zero_prefix | 41 | -4.00 | [-10.67, 2.67] | 0.30187 |  |
| cue_free | 5000 | lalm_zero_prefix | mean | 6.80 | [2.53, 11.33] | 0.0034997 | 0.0174982501749825 |
| cue_free | 5000 | lalm_random_prefix | 7 | 2.67 | [-0.67, 6.67] | 0.28487 |  |
| cue_free | 5000 | lalm_random_prefix | 13 | 6.67 | [2.67, 11.33] | 0.0065993 |  |
| cue_free | 5000 | lalm_random_prefix | 23 | -1.33 | [-6.00, 2.67] | 0.77172 |  |
| cue_free | 5000 | lalm_random_prefix | 37 | 12.67 | [6.67, 18.67] | 0.00029997 |  |
| cue_free | 5000 | lalm_random_prefix | 41 | -8.00 | [-14.67, -1.33] | 0.025197 |  |
| cue_free | 5000 | lalm_random_prefix | mean | 2.53 | [-0.67, 5.73] | 0.14609 | 0.43825617438256176 |
| cue_free | 5000 | lalm_permuted_prefix | 7 | 1.33 | [-2.00, 5.33] | 0.72303 |  |
| cue_free | 5000 | lalm_permuted_prefix | 13 | 2.00 | [-0.67, 5.33] | 0.37566 |  |
| cue_free | 5000 | lalm_permuted_prefix | 23 | 2.67 | [-2.00, 7.33] | 0.41356 |  |
| cue_free | 5000 | lalm_permuted_prefix | 37 | 10.67 | [4.67, 16.67] | 0.00089991 |  |
| cue_free | 5000 | lalm_permuted_prefix | 41 | -12.00 | [-17.33, -7.33] | 9.999e-05 |  |
| cue_free | 5000 | lalm_permuted_prefix | mean | 0.93 | [-1.73, 3.47] | 0.54785 | 1 |
