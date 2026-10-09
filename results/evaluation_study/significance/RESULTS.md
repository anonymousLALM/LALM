# Paired significance results

Differences and CIs are fractions (multiply by 100 for percentage points). CIs are pointwise; Holm correction applies only to aggregate comparisons; per-seed adjusted p is blank. Aggregate inference is conditional on the fitted checkpoints, not a population claim over training seeds. LoCoMo has only ten conversation clusters.

| Dataset | Horizon | Comparison | Seed | Delta | 95% CI | Raw p | Holm p |
|---|---:|---|---|---:|---|---:|---:|
| locomo |  | lalm vs lexical_only | 7 | 0.0058 | [-0.0075, 0.0186] | 0.4386 |  |
| locomo |  | lalm vs lexical_only | 13 | 0.0121 | [-0.0048, 0.0290] | 0.2108 |  |
| locomo |  | lalm vs lexical_only | 23 | -0.0212 | [-0.0343, -0.0083] | 0.008299 |  |
| locomo |  | lalm vs lexical_only | 37 | -0.1134 | [-0.1278, -0.0972] | 0.0025 |  |
| locomo |  | lalm vs lexical_only | 41 | 0.0090 | [-0.0075, 0.0286] | 0.3797 |  |
| locomo |  | lalm vs lexical_only | mean | -0.0215 | [-0.0331, -0.0082] | 0.0247 | 0.22227777222277773 |
| longmemeval |  | lalm vs lexical_only | 7 | 0.0190 | [-0.0046, 0.0436] | 0.1291 |  |
| longmemeval |  | lalm vs lexical_only | 13 | 0.0147 | [-0.0075, 0.0374] | 0.1975 |  |
| longmemeval |  | lalm vs lexical_only | 23 | -0.0135 | [-0.0385, 0.0116] | 0.2944 |  |
| longmemeval |  | lalm vs lexical_only | 37 | 0.0612 | [0.0262, 0.0962] | 0.0005999 |  |
| longmemeval |  | lalm vs lexical_only | 41 | 0.0228 | [-0.0064, 0.0520] | 0.1288 |  |
| longmemeval |  | lalm vs lexical_only | mean | 0.0208 | [-0.0014, 0.0432] | 0.06499 | 0.4687531246875312 |
| synthetic | 100 | lalm vs lexical_only | 7 | 0.0067 | [-0.0267, 0.0400] | 0.8423 |  |
| synthetic | 100 | lalm vs lexical_only | 13 | 0.0800 | [0.0500, 0.1133] | 9.999e-05 |  |
| synthetic | 100 | lalm vs lexical_only | 23 | 0.0067 | [-0.0300, 0.0467] | 0.861 |  |
| synthetic | 100 | lalm vs lexical_only | 37 | -0.0100 | [-0.0533, 0.0333] | 0.7664 |  |
| synthetic | 100 | lalm vs lexical_only | 41 | -0.0667 | [-0.1067, -0.0267] | 0.0027 |  |
| synthetic | 100 | lalm vs lexical_only | mean | 0.0033 | [-0.0233, 0.0307] | 0.838 | 1 |
| synthetic | 1000 | lalm vs lexical_only | 7 | 0.0467 | [0.0067, 0.0933] | 0.06489 |  |
| synthetic | 1000 | lalm vs lexical_only | 13 | 0.0733 | [0.0200, 0.1267] | 0.0112 |  |
| synthetic | 1000 | lalm vs lexical_only | 23 | -0.0067 | [-0.0667, 0.0467] | 1 |  |
| synthetic | 1000 | lalm vs lexical_only | 37 | 0.0467 | [-0.0200, 0.1133] | 0.2461 |  |
| synthetic | 1000 | lalm vs lexical_only | 41 | -0.0400 | [-0.1000, 0.0200] | 0.2635 |  |
| synthetic | 1000 | lalm vs lexical_only | mean | 0.0240 | [-0.0160, 0.0653] | 0.2807 | 1 |
| synthetic | 500 | lalm vs lexical_only | 7 | 0.0267 | [-0.0044, 0.0578] | 0.1797 |  |
| synthetic | 500 | lalm vs lexical_only | 13 | 0.0756 | [0.0400, 0.1156] | 0.0003 |  |
| synthetic | 500 | lalm vs lexical_only | 23 | 0.0178 | [-0.0311, 0.0667] | 0.5967 |  |
| synthetic | 500 | lalm vs lexical_only | 37 | -0.0222 | [-0.0800, 0.0356] | 0.5525 |  |
| synthetic | 500 | lalm vs lexical_only | 41 | -0.0533 | [-0.1022, -0.0089] | 0.0435 |  |
| synthetic | 500 | lalm vs lexical_only | mean | 0.0089 | [-0.0231, 0.0427] | 0.6365 | 1 |
| synthetic | 5000 | lalm vs lexical_only | 7 | 0.0600 | [0.0200, 0.1067] | 0.012 |  |
| synthetic | 5000 | lalm vs lexical_only | 13 | 0.1067 | [0.0600, 0.1600] | 9.999e-05 |  |
| synthetic | 5000 | lalm vs lexical_only | 23 | -0.0200 | [-0.0933, 0.0533] | 0.7236 |  |
| synthetic | 5000 | lalm vs lexical_only | 37 | 0.1000 | [0.0400, 0.1600] | 0.0025 |  |
| synthetic | 5000 | lalm vs lexical_only | 41 | -0.0200 | [-0.0867, 0.0533] | 0.7012 |  |
| synthetic | 5000 | lalm vs lexical_only | mean | 0.0453 | [0.0013, 0.0920] | 0.05859 | 0.4687531246875312 |
| synthetic | 1000 | lalm vs lalm_zero_prefix | 7 | 0.0200 | [-0.0267, 0.0667] | 0.581 |  |
| synthetic | 1000 | lalm vs lalm_zero_prefix | 13 | 0.0467 | [0.0000, 0.1000] | 0.1191 |  |
| synthetic | 1000 | lalm vs lalm_zero_prefix | 23 | -0.0333 | [-0.0867, 0.0200] | 0.3374 |  |
| synthetic | 1000 | lalm vs lalm_zero_prefix | 37 | 0.0200 | [-0.0533, 0.0933] | 0.7244 |  |
| synthetic | 1000 | lalm vs lalm_zero_prefix | 41 | -0.0667 | [-0.1200, -0.0133] | 0.0201 |  |
| synthetic | 1000 | lalm vs lalm_zero_prefix | mean | -0.0027 | [-0.0413, 0.0387] | 0.9521 | 1 |
| synthetic | 5000 | lalm vs lalm_zero_prefix | 7 | 0.0333 | [-0.0267, 0.0933] | 0.3817 |  |
| synthetic | 5000 | lalm vs lalm_zero_prefix | 13 | 0.0800 | [0.0333, 0.1267] | 0.002 |  |
| synthetic | 5000 | lalm vs lalm_zero_prefix | 23 | -0.0333 | [-0.0933, 0.0267] | 0.4047 |  |
| synthetic | 5000 | lalm vs lalm_zero_prefix | 37 | 0.0867 | [0.0200, 0.1533] | 0.0166 |  |
| synthetic | 5000 | lalm vs lalm_zero_prefix | 41 | -0.0333 | [-0.1000, 0.0333] | 0.4321 |  |
| synthetic | 5000 | lalm vs lalm_zero_prefix | mean | 0.0267 | [-0.0173, 0.0733] | 0.2669 | 1 |
| synthetic | 1000 | lalm vs rag_timestamp | 7 | 0.0667 | [0.0000, 0.1333] | 0.07629 |  |
| synthetic | 1000 | lalm vs rag_timestamp | 13 | 0.0933 | [0.0267, 0.1667] | 0.0155 |  |
| synthetic | 1000 | lalm vs rag_timestamp | 23 | 0.0133 | [-0.0533, 0.0867] | 0.862 |  |
| synthetic | 1000 | lalm vs rag_timestamp | 37 | 0.0667 | [-0.0200, 0.1533] | 0.1848 |  |
| synthetic | 1000 | lalm vs rag_timestamp | 41 | -0.0200 | [-0.0933, 0.0600] | 0.7309 |  |
| synthetic | 1000 | lalm vs rag_timestamp | mean | 0.0440 | [-0.0187, 0.1080] | 0.1963 | 1 |
| synthetic | 5000 | lalm vs rag_timestamp | 7 | 0.1000 | [0.0267, 0.1733] | 0.008799 |  |
| synthetic | 5000 | lalm vs rag_timestamp | 13 | 0.1467 | [0.0867, 0.2133] | 9.999e-05 |  |
| synthetic | 5000 | lalm vs rag_timestamp | 23 | 0.0200 | [-0.0600, 0.1000] | 0.7328 |  |
| synthetic | 5000 | lalm vs rag_timestamp | 37 | 0.1400 | [0.0600, 0.2200] | 0.0005 |  |
| synthetic | 5000 | lalm vs rag_timestamp | 41 | 0.0200 | [-0.0533, 0.0933] | 0.7316 |  |
| synthetic | 5000 | lalm vs rag_timestamp | mean | 0.0853 | [0.0253, 0.1493] | 0.007599 | 0.07599240075992401 |
