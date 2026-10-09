# evaluation experiment results

Scores are fractions. Evaluation streams are averaged within training seeds before mean/sample SD. Shared controls are not independent training replicates. Partial suites are marked by their counts.

| Group | Dataset | Method | Horizon | Metric | Rows | Mean | SD |
|---|---|---|---:|---|---:|---:|---:|
| newest-wins-original | synthetic | lexical_only | 100 | correct | 1 | 0.7267 |  |
| newest-wins-original | synthetic | lexical_only | 500 | correct | 1 | 0.6711 |  |
| newest-wins-original | synthetic | lexical_only | 1000 | correct | 1 | 0.6733 |  |
| newest-wins-original | synthetic | lexical_only | 5000 | correct | 1 | 0.7000 |  |
| newest-wins-original | locomo | lexical_only |  | token_f1_diagnostic | 1 | 0.1578 |  |
| newest-wins-original | locomo | lexical_only |  | correct | 1 | 0.0579 |  |
| newest-wins-original | locomo | lexical_only |  | locomo_official_qa_score | 1 | 0.3090 |  |
| newest-wins-cue_free | synthetic | lalm | 1000 | correct | 5 | 0.5787 | 0.06007402840570034 |
| newest-wins-cue_free | synthetic | lalm | 5000 | correct | 5 | 0.6080 | 0.07665217254295896 |
| newest-wins-cue_free | synthetic | lexical_only | 1000 | correct | 1 | 0.5667 |  |
| newest-wins-cue_free | synthetic | lexical_only | 5000 | correct | 1 | 0.6067 |  |
| newest-wins-original | longmemeval | lalm |  | token_f1_diagnostic | 5 | 0.2076 | 0.025951300354151698 |
| newest-wins-original | longmemeval | lalm |  | correct | 5 | 0.1284 | 0.007601169500660927 |
| newest-wins-original | synthetic | lalm | 100 | correct | 5 | 0.7320 | 0.05377938473264847 |
| newest-wins-original | synthetic | lalm | 500 | correct | 5 | 0.6747 | 0.04882824521590141 |
| newest-wins-original | synthetic | lalm | 1000 | correct | 5 | 0.6960 | 0.06047956496022252 |
| newest-wins-original | synthetic | lalm | 5000 | correct | 5 | 0.7333 | 0.04737556801183967 |
| newest-wins-original | locomo | lalm |  | token_f1_diagnostic | 5 | 0.1801 | 0.014332431403673837 |
| newest-wins-original | locomo | lalm |  | correct | 5 | 0.0693 | 0.006927811507095746 |
| newest-wins-original | locomo | lalm |  | locomo_official_qa_score | 5 | 0.2928 | 0.050721043068481034 |
| newest-wins-original | longmemeval | lexical_only |  | token_f1_diagnostic | 1 | 0.1915 |  |
| newest-wins-original | longmemeval | lexical_only |  | correct | 1 | 0.1267 |  |
