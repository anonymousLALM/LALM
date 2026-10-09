# Follow-up paired significance

Differences/CI are fractions. Holm applies only to aggregate comparisons; per-seed adjusted p is blank. Aggregates are conditional on fitted checkpoints. LongMemEval uses diagnostic token F1; LoCoMo uses QA score.

| Dataset | Horizon | Comparison | Seed | Checkpoints | Complete | Difference | 95% CI | Raw p | Holm p |
|---|---|---|---|---|---|---|---|---|---|
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | 7 | 7 | True | 0.08000 | [0.01333, 0.14667] | 0.037896 |  |
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | 13 | 13 | True | 0.09333 | [0.02667, 0.16667] | 0.015598 |  |
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | 23 | 23 | True | 0.00667 | [-0.06667, 0.08000] | 1 |  |
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | 37 | 37 | True | 0.08000 | [-0.00667, 0.16000] | 0.087891 |  |
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | 41 | 41 | True | -0.04667 | [-0.12667, 0.03333] | 0.33327 |  |
| synthetic | 1000 | lalm_newest_standard vs rag_timestamp | mean | 7,13,23,37,41 | True | 0.04267 | [-0.02133, 0.10800] | 0.21758 | 1 |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | 7 | 7 | True | 0.12000 | [0.04667, 0.19333] | 0.0016998 |  |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | 13 | 13 | True | 0.16000 | [0.10000, 0.22000] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | 23 | 23 | True | 0.12667 | [0.06000, 0.19333] | 0.00029997 |  |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | 37 | 37 | True | 0.12667 | [0.04667, 0.20667] | 0.0022998 |  |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | 41 | 41 | True | 0.03333 | [-0.04667, 0.11333] | 0.50815 |  |
| synthetic | 5000 | lalm_newest_standard vs rag_timestamp | mean | 7,13,23,37,41 | True | 0.11333 | [0.05197, 0.17733] | 0.00019998 | 0.0023997600239976003 |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.01333 | [-0.02000, 0.04667] | 0.56694 |  |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.08333 | [0.05000, 0.11667] | 9.999e-05 |  |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | 0.00667 | [-0.03000, 0.04667] | 0.86811 |  |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | -0.01000 | [-0.05667, 0.03333] | 0.77572 |  |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | -0.06667 | [-0.10667, -0.02667] | 0.0030997 |  |
| synthetic | 100 | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | 0.00533 | [-0.02267, 0.03400] | 0.74723 | 1 |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.01778 | [-0.01333, 0.04889] | 0.42646 |  |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.07111 | [0.03556, 0.11111] | 0.00069993 |  |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | 0.01333 | [-0.03556, 0.06222] | 0.72753 |  |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | -0.02667 | [-0.08444, 0.03111] | 0.46145 |  |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | -0.05778 | [-0.10667, -0.01333] | 0.024998 |  |
| synthetic | 500 | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | 0.00356 | [-0.02756, 0.03733] | 0.87201 | 1 |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.06000 | [0.02000, 0.10667] | 0.010899 |  |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.07333 | [0.02667, 0.12000] | 0.0029997 |  |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | -0.01333 | [-0.07333, 0.04667] | 0.83162 |  |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | 0.06000 | [-0.00667, 0.12667] | 0.10089 |  |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | -0.06667 | [-0.12667, -0.01333] | 0.043196 |  |
| synthetic | 1000 | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | 0.02267 | [-0.01600, 0.06270] | 0.28777 | 1 |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.04000 | [0.01333, 0.07333] | 0.031297 |  |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.08000 | [0.04000, 0.12667] | 0.00029997 |  |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | 0.04667 | [0.00000, 0.10000] | 0.12169 |  |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | 0.04667 | [-0.01333, 0.10667] | 0.19148 |  |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | -0.04667 | [-0.11333, 0.02000] | 0.24598 |  |
| synthetic | 5000 | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | 0.03333 | [-0.00400, 0.07333] | 0.10599 | 0.8479152084791521 |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.01267 | [-0.01248, 0.03783] | 0.32387 |  |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.01480 | [-0.00827, 0.03785] | 0.19888 |  |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | -0.01717 | [-0.04334, 0.00909] | 0.19728 |  |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | 0.05574 | [0.02002, 0.09162] | 0.0021998 |  |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | 0.01470 | [-0.01460, 0.04425] | 0.32947 |  |
| longmemeval |  | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | 0.01615 | [-0.00683, 0.03872] | 0.16378 | 1 |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | 7 | 7 | True | 0.00740 | [-0.00552, 0.02121] | 0.37086 |  |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | 13 | 13 | True | 0.01564 | [-0.00117, 0.03022] | 0.10089 |  |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | 23 | 23 | True | -0.01137 | [-0.02676, 0.00257] | 0.18208 |  |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | 37 | 37 | True | -0.10504 | [-0.11985, -0.08933] | 0.0024998 |  |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | 41 | 41 | True | 0.01217 | [-0.00514, 0.02994] | 0.20218 |  |
| locomo |  | lalm_newest_standard vs lexical_only_newest_standard | mean | 7,13,23,37,41 | True | -0.01624 | [-0.02901, -0.00399] | 0.047495 | 0.42745725427457254 |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | 7 | 7 | True | 0.10000 | [0.05333, 0.14667] | 9.999e-05 |  |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | 13 | 13 | True | 0.10000 | [0.05333, 0.15333] | 9.999e-05 |  |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | 23 | 23 | True | 0.02667 | [-0.02667, 0.08000] | 0.45075 |  |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | 37 | 37 | True | 0.14000 | [0.08000, 0.20000] | 9.999e-05 |  |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | 41 | 41 | True | -0.00667 | [-0.06000, 0.04667] | 1 |  |
| synthetic | 1000 | lalm_newest_cuefree vs rag_original_cuefree | mean | 7,13,23,37,41 | True | 0.07200 | [0.03333, 0.11333] | 0.00039996 | 0.004399560043995601 |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | 7 | 7 | True | 0.11333 | [0.06000, 0.16667] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | 13 | 13 | True | 0.11333 | [0.06667, 0.16667] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | 23 | 23 | True | 0.08000 | [0.02667, 0.13333] | 0.0076992 |  |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | 37 | 37 | True | 0.20667 | [0.14000, 0.28000] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | 41 | 41 | True | -0.00667 | [-0.08000, 0.06667] | 1 |  |
| synthetic | 5000 | lalm_newest_cuefree vs rag_original_cuefree | mean | 7,13,23,37,41 | True | 0.10133 | [0.05067, 0.15600] | 9.999e-05 | 0.0013998600139986002 |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | 7 | 7 | True | 0.01333 | [-0.02000, 0.04667] | 0.69553 |  |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | 13 | 13 | True | 0.00000 | [-0.03333, 0.03333] | 1 |  |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | 23 | 23 | True | -0.00667 | [-0.04000, 0.02667] | 1 |  |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | 37 | 37 | True | 0.01333 | [-0.02667, 0.05333] | 0.75572 |  |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | 41 | 41 | True | -0.02667 | [-0.06667, 0.00667] | 0.29097 |  |
| synthetic | 1000 | lalm_newest_standard vs lalm_original_standard | mean | 7,13,23,37,41 | True | -0.00133 | [-0.01467, 0.01333] | 1 | 1 |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | 7 | 7 | True | 0.02000 | [-0.02000, 0.06667] | 0.54525 |  |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | 13 | 13 | True | 0.01333 | [0.00000, 0.03333] | 0.50375 |  |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | 23 | 23 | True | 0.10667 | [0.05333, 0.16000] | 0.00039996 |  |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | 37 | 37 | True | -0.01333 | [-0.06000, 0.03333] | 0.77692 |  |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | 41 | 41 | True | 0.01333 | [-0.04000, 0.06667] | 0.80672 |  |
| synthetic | 5000 | lalm_newest_standard vs lalm_original_standard | mean | 7,13,23,37,41 | True | 0.02800 | [0.00933, 0.04800] | 0.0069993 | 0.06999300069993 |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | 7 | 7 | True | 0.03333 | [-0.00667, 0.07333] | 0.17998 |  |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | 13 | 13 | True | 0.03333 | [-0.00667, 0.08000] | 0.23048 |  |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | 23 | 23 | True | 0.00667 | [-0.04000, 0.05333] | 1 |  |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | 37 | 37 | True | 0.02000 | [-0.02000, 0.06667] | 0.55884 |  |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | 41 | 41 | True | 0.02000 | [-0.02000, 0.06667] | 0.54945 |  |
| synthetic | 1000 | lalm_newest_cuefree vs lalm_original_cuefree | mean | 7,13,23,37,41 | True | 0.02267 | [-0.00933, 0.05867] | 0.23728 | 1 |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | 7 | 7 | True | 0.11333 | [0.06000, 0.17333] | 0.00029997 |  |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | 13 | 13 | True | 0.12000 | [0.07333, 0.17333] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | 23 | 23 | True | 0.16667 | [0.10667, 0.23333] | 9.999e-05 |  |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | 37 | 37 | True | 0.12000 | [0.04667, 0.19333] | 0.0030997 |  |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | 41 | 41 | True | 0.12000 | [0.04667, 0.19333] | 0.0022998 |  |
| synthetic | 5000 | lalm_newest_cuefree vs lalm_original_cuefree | mean | 7,13,23,37,41 | True | 0.12800 | [0.07600, 0.18267] | 9.999e-05 | 0.0013998600139986002 |
