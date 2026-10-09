# Missing released-data metrics

Scores below are percentages. LALM/Pure Liquid summaries here cover seeds 37 and 41 only; they are not five-seed summaries. Timestamp RAG has no training checkpoint. Exact match is the existing diagnostic, not the LongMemEval official judge score.

| Dataset | Method | Type | Metric | Mean +/- sample SD (%) |
|---|---|---|---|---|
| locomo | pure_liquid | all | diagnostic_token_f1 | 5.81 +/- 1.54 |
| locomo | pure_liquid | all | diagnostic_exact_match | 1.89 +/- 0.18 |
| locomo | pure_liquid | all | locomo_official_qa_score | 6.39 +/- 1.54 |
| locomo | pure_liquid | category-1 | diagnostic_token_f1 | 7.74 +/- 2.26 |
| locomo | pure_liquid | category-1 | diagnostic_exact_match | 3.01 +/- 0.75 |
| locomo | pure_liquid | category-2 | diagnostic_token_f1 | 3.01 +/- 0.36 |
| locomo | pure_liquid | category-2 | diagnostic_exact_match | 1.09 +/- 0.22 |
| locomo | pure_liquid | category-3 | diagnostic_token_f1 | 16.96 +/- 1.02 |
| locomo | pure_liquid | category-3 | diagnostic_exact_match | 10.42 +/- 1.47 |
| locomo | pure_liquid | category-4 | diagnostic_token_f1 | 7.88 +/- 2.67 |
| locomo | pure_liquid | category-4 | diagnostic_exact_match | 1.72 +/- 0.25 |
| locomo | pure_liquid | category-5 | diagnostic_token_f1 | 0.28 +/- 0.08 |
| locomo | pure_liquid | category-5 | diagnostic_exact_match | 0.22 +/- 0.00 |
| longmemeval | lalm | all | diagnostic_token_f1 | 22.76 +/- 2.71 |
| longmemeval | lalm | all | diagnostic_exact_match | 13.00 +/- 0.47 |
| longmemeval | lalm | knowledge-update | diagnostic_token_f1 | 32.14 +/- 0.06 |
| longmemeval | lalm | knowledge-update | diagnostic_exact_match | 19.87 +/- 2.72 |
| longmemeval | lalm | multi-session | diagnostic_token_f1 | 12.30 +/- 0.23 |
| longmemeval | lalm | multi-session | diagnostic_exact_match | 7.14 +/- 1.59 |
| longmemeval | lalm | single-session-assistant | diagnostic_token_f1 | 41.55 +/- 3.71 |
| longmemeval | lalm | single-session-assistant | diagnostic_exact_match | 25.89 +/- 6.31 |
| longmemeval | lalm | single-session-preference | diagnostic_token_f1 | 6.48 +/- 2.94 |
| longmemeval | lalm | single-session-preference | diagnostic_exact_match | 0.00 +/- 0.00 |
| longmemeval | lalm | single-session-user | diagnostic_token_f1 | 48.98 +/- 4.66 |
| longmemeval | lalm | single-session-user | diagnostic_exact_match | 35.00 +/- 0.00 |
| longmemeval | lalm | temporal-reasoning | diagnostic_token_f1 | 19.53 +/- 9.17 |
| longmemeval | lalm | temporal-reasoning | diagnostic_exact_match | 9.02 +/- 4.25 |
| locomo | rag_timestamp | all | diagnostic_token_f1 | 18.52 |
| locomo | rag_timestamp | all | diagnostic_exact_match | 7.25 |
| locomo | rag_timestamp | all | locomo_official_qa_score | 32.33 |
| locomo | rag_timestamp | category-1 | diagnostic_token_f1 | 16.91 |
| locomo | rag_timestamp | category-1 | diagnostic_exact_match | 3.19 |
| locomo | rag_timestamp | category-2 | diagnostic_token_f1 | 21.67 |
| locomo | rag_timestamp | category-2 | diagnostic_exact_match | 0.93 |
| locomo | rag_timestamp | category-3 | diagnostic_token_f1 | 5.80 |
| locomo | rag_timestamp | category-3 | diagnostic_exact_match | 2.08 |
| locomo | rag_timestamp | category-4 | diagnostic_token_f1 | 29.02 |
| locomo | rag_timestamp | category-4 | diagnostic_exact_match | 15.34 |
| locomo | rag_timestamp | category-5 | diagnostic_token_f1 | 0.22 |
| locomo | rag_timestamp | category-5 | diagnostic_exact_match | 0.22 |
| longmemeval | pure_liquid | all | diagnostic_token_f1 | 9.24 +/- 1.98 |
| longmemeval | pure_liquid | all | diagnostic_exact_match | 4.56 +/- 0.79 |
| longmemeval | pure_liquid | knowledge-update | diagnostic_token_f1 | 7.02 +/- 2.43 |
| longmemeval | pure_liquid | knowledge-update | diagnostic_exact_match | 3.85 +/- 0.00 |
| longmemeval | pure_liquid | multi-session | diagnostic_token_f1 | 7.11 +/- 2.75 |
| longmemeval | pure_liquid | multi-session | diagnostic_exact_match | 4.14 +/- 1.59 |
| longmemeval | pure_liquid | single-session-assistant | diagnostic_token_f1 | 8.05 +/- 4.94 |
| longmemeval | pure_liquid | single-session-assistant | diagnostic_exact_match | 2.68 +/- 3.79 |
| longmemeval | pure_liquid | single-session-preference | diagnostic_token_f1 | 2.06 +/- 1.91 |
| longmemeval | pure_liquid | single-session-preference | diagnostic_exact_match | 0.00 +/- 0.00 |
| longmemeval | pure_liquid | single-session-user | diagnostic_token_f1 | 10.57 +/- 2.88 |
| longmemeval | pure_liquid | single-session-user | diagnostic_exact_match | 2.50 +/- 3.54 |
| longmemeval | pure_liquid | temporal-reasoning | diagnostic_token_f1 | 14.58 +/- 0.44 |
| longmemeval | pure_liquid | temporal-reasoning | diagnostic_exact_match | 7.52 +/- 0.00 |
| locomo | lalm | all | diagnostic_token_f1 | 18.38 +/- 1.94 |
| locomo | lalm | all | diagnostic_exact_match | 6.80 +/- 0.07 |
| locomo | lalm | all | locomo_official_qa_score | 25.98 +/- 8.66 |
| locomo | lalm | category-1 | diagnostic_token_f1 | 19.08 +/- 2.71 |
| locomo | lalm | category-1 | diagnostic_exact_match | 1.77 +/- 0.50 |
| locomo | lalm | category-2 | diagnostic_token_f1 | 18.81 +/- 0.20 |
| locomo | lalm | category-2 | diagnostic_exact_match | 1.56 +/- 0.44 |
| locomo | lalm | category-3 | diagnostic_token_f1 | 12.22 +/- 4.50 |
| locomo | lalm | category-3 | diagnostic_exact_match | 6.77 +/- 0.74 |
| locomo | lalm | category-4 | diagnostic_token_f1 | 28.32 +/- 3.24 |
| locomo | lalm | category-4 | diagnostic_exact_match | 14.03 +/- 0.67 |
| locomo | lalm | category-5 | diagnostic_token_f1 | 0.22 +/- 0.00 |
| locomo | lalm | category-5 | diagnostic_exact_match | 0.11 +/- 0.16 |
| longmemeval | rag_timestamp | all | diagnostic_token_f1 | 19.30 |
| longmemeval | rag_timestamp | all | diagnostic_exact_match | 13.33 |
| longmemeval | rag_timestamp | knowledge-update | diagnostic_token_f1 | 35.69 |
| longmemeval | rag_timestamp | knowledge-update | diagnostic_exact_match | 28.21 |
| longmemeval | rag_timestamp | multi-session | diagnostic_token_f1 | 6.40 |
| longmemeval | rag_timestamp | multi-session | diagnostic_exact_match | 4.51 |
| longmemeval | rag_timestamp | single-session-assistant | diagnostic_token_f1 | 55.23 |
| longmemeval | rag_timestamp | single-session-assistant | diagnostic_exact_match | 37.50 |
| longmemeval | rag_timestamp | single-session-preference | diagnostic_token_f1 | 4.10 |
| longmemeval | rag_timestamp | single-session-preference | diagnostic_exact_match | 0.00 |
| longmemeval | rag_timestamp | single-session-user | diagnostic_token_f1 | 26.36 |
| longmemeval | rag_timestamp | single-session-user | diagnostic_exact_match | 20.00 |
| longmemeval | rag_timestamp | temporal-reasoning | diagnostic_token_f1 | 9.84 |
| longmemeval | rag_timestamp | temporal-reasoning | diagnostic_exact_match | 5.26 |
