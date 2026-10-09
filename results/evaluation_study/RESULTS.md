# evaluation experiment results

Scores are fractions. Evaluation streams are averaged within training seeds before mean/sample SD. Shared controls are not independent training replicates. Partial suites are marked by their counts.

| Group | Dataset | Method | Horizon | Rows | Mean | SD |
|---|---|---|---:|---:|---:|---:|
| cue-free | synthetic | bounded_rag | 1000 | 1 | 0.2400 |  |
| cue-free | synthetic | bounded_rag | 5000 | 1 | 0.0000 |  |
| extra-seeds | synthetic | lalm_random_prefix | 1000 | 2 | 0.6367 | 0.004714045207910347 |
| extra-seeds | synthetic | lalm_random_prefix | 5000 | 2 | 0.6467 | 0.0 |
| extra-seeds | synthetic | pure_liquid | 100 | 2 | 0.1000 | 0.07071067811865475 |
| extra-seeds | synthetic | pure_liquid | 500 | 2 | 0.0956 | 0.07228202652129152 |
| extra-seeds | synthetic | pure_liquid | 1000 | 2 | 0.0900 | 0.07071067811865477 |
| extra-seeds | synthetic | pure_liquid | 5000 | 2 | 0.0900 | 0.07071067811865477 |
| extra-seeds | synthetic | lalm_permuted_prefix | 1000 | 2 | 0.6567 | 0.004714045207910347 |
| extra-seeds | synthetic | lalm_permuted_prefix | 5000 | 2 | 0.6767 | 0.004714045207910347 |
| extra-seeds | synthetic | lalm | 100 | 2 | 0.6883 | 0.040069384267237676 |
| extra-seeds | synthetic | lalm | 500 | 2 | 0.6289 | 0.021998877636914875 |
| extra-seeds | synthetic | lalm | 1000 | 2 | 0.6767 | 0.061282587702834124 |
| extra-seeds | synthetic | lalm | 5000 | 2 | 0.7000 | 0.0848528137423857 |
| cue-free | synthetic | lexical_only | 1000 | 1 | 0.5400 |  |
| cue-free | synthetic | lexical_only | 5000 | 1 | 0.4733 |  |
| ordering | synthetic | rag_timestamp | 100 | 1 | 0.6633 |  |
| ordering | synthetic | rag_timestamp | 500 | 1 | 0.6889 |  |
| ordering | synthetic | rag_timestamp | 1000 | 1 | 0.6533 |  |
| ordering | synthetic | rag_timestamp | 5000 | 1 | 0.6200 |  |
| extra-seeds | locomo | pure_liquid |  | 2 | 0.0639 | 0.015399617760630736 |
| extra-seeds | longmemeval | lalm |  | 2 | 0.2276 | 0.027111918651404124 |
| ordering | locomo | rag_timestamp |  | 1 | 0.3233 |  |
| extra-seeds | longmemeval | pure_liquid |  | 2 | 0.0924 | 0.019793748815897048 |
| cue-free | synthetic | rag | 1000 | 1 | 0.5067 |  |
| cue-free | synthetic | rag | 5000 | 1 | 0.5067 |  |
| extra-seeds | locomo | lalm |  | 2 | 0.2598 | 0.08658975851086036 |
| extra-seeds | synthetic | lalm_zero_prefix | 1000 | 2 | 0.7000 | 0.0 |
| extra-seeds | synthetic | lalm_zero_prefix | 5000 | 2 | 0.6733 | 0.0 |
| ordering | longmemeval | rag_timestamp |  | 1 | 0.1930 |  |
| cue-free | synthetic | lalm | 1000 | 3 | 0.5578 | 0.026943012562182518 |
| cue-free | synthetic | lalm | 5000 | 3 | 0.4756 | 0.04822785425380159 |
