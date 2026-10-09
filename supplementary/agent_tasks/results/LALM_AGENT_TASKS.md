# Memory inside simulated tool tasks

Completed jobs: 36. Shared baselines have no training-seed SD. Holm correction covers aggregate comparisons only.

| Method | Dataset | Stream | Horizon | Metric | Checkpoints | Mean +/- SD |
|---|---|---|---|---|---|---|
| bounded_rag | synthetic | cue_free | 1000 | correct_tool | shared | 92.667 % |
| bounded_rag | synthetic | cue_free | 1000 | end_to_end_ms | shared | 1241.234 |
| bounded_rag | synthetic | cue_free | 1000 | exact_arguments | shared | 30.000 % |
| bounded_rag | synthetic | cue_free | 1000 | full_success | shared | 30.000 % |
| bounded_rag | synthetic | cue_free | 1000 | read_ms | shared | 8.170 |
| bounded_rag | synthetic | cue_free | 1000 | write_ms_per_turn | shared | 0.273 |
| bounded_rag | synthetic | cue_free | 5000 | correct_tool | shared | 84.000 % |
| bounded_rag | synthetic | cue_free | 5000 | end_to_end_ms | shared | 2213.505 |
| bounded_rag | synthetic | cue_free | 5000 | exact_arguments | shared | 6.000 % |
| bounded_rag | synthetic | cue_free | 5000 | full_success | shared | 6.000 % |
| bounded_rag | synthetic | cue_free | 5000 | read_ms | shared | 8.592 |
| bounded_rag | synthetic | cue_free | 5000 | write_ms_per_turn | shared | 0.267 |
| bounded_rag | synthetic | original | 1000 | correct_tool | shared | 92.000 % |
| bounded_rag | synthetic | original | 1000 | end_to_end_ms | shared | 1233.927 |
| bounded_rag | synthetic | original | 1000 | exact_arguments | shared | 27.333 % |
| bounded_rag | synthetic | original | 1000 | full_success | shared | 27.333 % |
| bounded_rag | synthetic | original | 1000 | read_ms | shared | 8.141 |
| bounded_rag | synthetic | original | 1000 | write_ms_per_turn | shared | 0.273 |
| bounded_rag | synthetic | original | 5000 | correct_tool | shared | 88.000 % |
| bounded_rag | synthetic | original | 5000 | end_to_end_ms | shared | 2201.449 |
| bounded_rag | synthetic | original | 5000 | exact_arguments | shared | 6.000 % |
| bounded_rag | synthetic | original | 5000 | full_success | shared | 6.000 % |
| bounded_rag | synthetic | original | 5000 | read_ms | shared | 8.364 |
| bounded_rag | synthetic | original | 5000 | write_ms_per_turn | shared | 0.266 |
| lalm | synthetic | cue_free | 1000 | correct_tool | 5 | 71.067 +/- 29.252 % |
| lalm | synthetic | cue_free | 1000 | end_to_end_ms | 5 | 2408.017 +/- 285.524 |
| lalm | synthetic | cue_free | 1000 | exact_arguments | 5 | 58.400 +/- 30.039 % |
| lalm | synthetic | cue_free | 1000 | full_success | 5 | 52.000 +/- 30.416 % |
| lalm | synthetic | cue_free | 1000 | read_ms | 5 | 9.475 +/- 0.094 |
| lalm | synthetic | cue_free | 1000 | write_ms_per_turn | 5 | 1.058 +/- 0.007 |
| lalm | synthetic | cue_free | 5000 | correct_tool | 5 | 81.600 +/- 17.743 % |
| lalm | synthetic | cue_free | 5000 | end_to_end_ms | 5 | 6618.339 +/- 177.222 |
| lalm | synthetic | cue_free | 5000 | exact_arguments | 5 | 68.533 +/- 12.278 % |
| lalm | synthetic | cue_free | 5000 | full_success | 5 | 62.267 +/- 18.200 % |
| lalm | synthetic | cue_free | 5000 | read_ms | 5 | 9.424 +/- 0.094 |
| lalm | synthetic | cue_free | 5000 | write_ms_per_turn | 5 | 1.068 +/- 0.003 |
| lalm | synthetic | original | 1000 | correct_tool | 5 | 69.867 +/- 30.519 % |
| lalm | synthetic | original | 1000 | end_to_end_ms | 5 | 2378.963 +/- 280.194 |
| lalm | synthetic | original | 1000 | exact_arguments | 5 | 57.733 +/- 26.207 % |
| lalm | synthetic | original | 1000 | full_success | 5 | 52.133 +/- 27.598 % |
| lalm | synthetic | original | 1000 | read_ms | 5 | 9.355 +/- 0.104 |
| lalm | synthetic | original | 1000 | write_ms_per_turn | 5 | 1.059 +/- 0.007 |
| lalm | synthetic | original | 5000 | correct_tool | 5 | 79.600 +/- 21.672 % |
| lalm | synthetic | original | 5000 | end_to_end_ms | 5 | 6591.096 +/- 157.779 |
| lalm | synthetic | original | 5000 | exact_arguments | 5 | 66.800 +/- 14.286 % |
| lalm | synthetic | original | 5000 | full_success | 5 | 61.333 +/- 19.316 % |
| lalm | synthetic | original | 5000 | read_ms | 5 | 9.400 +/- 0.063 |
| lalm | synthetic | original | 5000 | write_ms_per_turn | 5 | 1.072 +/- 0.005 |
| lexical_only | synthetic | cue_free | 1000 | correct_tool | shared | 98.667 % |
| lexical_only | synthetic | cue_free | 1000 | end_to_end_ms | shared | 1433.635 |
| lexical_only | synthetic | cue_free | 1000 | exact_arguments | shared | 78.000 % |
| lexical_only | synthetic | cue_free | 1000 | full_success | shared | 78.000 % |
| lexical_only | synthetic | cue_free | 1000 | read_ms | shared | 7.559 |
| lexical_only | synthetic | cue_free | 1000 | write_ms_per_turn | shared | 0.302 |
| lexical_only | synthetic | cue_free | 5000 | correct_tool | shared | 97.333 % |
| lexical_only | synthetic | cue_free | 5000 | end_to_end_ms | shared | 2747.692 |
| lexical_only | synthetic | cue_free | 5000 | exact_arguments | shared | 76.667 % |
| lexical_only | synthetic | cue_free | 5000 | full_success | shared | 75.333 % |
| lexical_only | synthetic | cue_free | 5000 | read_ms | shared | 7.728 |
| lexical_only | synthetic | cue_free | 5000 | write_ms_per_turn | shared | 0.325 |
| lexical_only | synthetic | original | 1000 | correct_tool | shared | 98.667 % |
| lexical_only | synthetic | original | 1000 | end_to_end_ms | shared | 1399.715 |
| lexical_only | synthetic | original | 1000 | exact_arguments | shared | 72.000 % |
| lexical_only | synthetic | original | 1000 | full_success | shared | 72.000 % |
| lexical_only | synthetic | original | 1000 | read_ms | shared | 7.526 |
| lexical_only | synthetic | original | 1000 | write_ms_per_turn | shared | 0.299 |
| lexical_only | synthetic | original | 5000 | correct_tool | shared | 97.333 % |
| lexical_only | synthetic | original | 5000 | end_to_end_ms | shared | 2694.458 |
| lexical_only | synthetic | original | 5000 | exact_arguments | shared | 79.333 % |
| lexical_only | synthetic | original | 5000 | full_success | shared | 78.000 % |
| lexical_only | synthetic | original | 5000 | read_ms | shared | 7.447 |
| lexical_only | synthetic | original | 5000 | write_ms_per_turn | shared | 0.320 |
| rag | synthetic | cue_free | 1000 | correct_tool | shared | 96.667 % |
| rag | synthetic | cue_free | 1000 | end_to_end_ms | shared | 1413.148 |
| rag | synthetic | cue_free | 1000 | exact_arguments | shared | 78.667 % |
| rag | synthetic | cue_free | 1000 | full_success | shared | 76.000 % |
| rag | synthetic | cue_free | 1000 | read_ms | shared | 8.735 |
| rag | synthetic | cue_free | 1000 | write_ms_per_turn | shared | 0.272 |
| rag | synthetic | cue_free | 5000 | correct_tool | shared | 99.333 % |
| rag | synthetic | cue_free | 5000 | end_to_end_ms | shared | 2467.761 |
| rag | synthetic | cue_free | 5000 | exact_arguments | shared | 78.000 % |
| rag | synthetic | cue_free | 5000 | full_success | shared | 77.333 % |
| rag | synthetic | cue_free | 5000 | read_ms | shared | 11.490 |
| rag | synthetic | cue_free | 5000 | write_ms_per_turn | shared | 0.268 |
| rag | synthetic | original | 1000 | correct_tool | shared | 96.667 % |
| rag | synthetic | original | 1000 | end_to_end_ms | shared | 1385.752 |
| rag | synthetic | original | 1000 | exact_arguments | shared | 69.333 % |
| rag | synthetic | original | 1000 | full_success | shared | 66.667 % |
| rag | synthetic | original | 1000 | read_ms | shared | 8.538 |
| rag | synthetic | original | 1000 | write_ms_per_turn | shared | 0.272 |
| rag | synthetic | original | 5000 | correct_tool | shared | 99.333 % |
| rag | synthetic | original | 5000 | end_to_end_ms | shared | 2423.752 |
| rag | synthetic | original | 5000 | exact_arguments | shared | 66.000 % |
| rag | synthetic | original | 5000 | full_success | shared | 65.333 % |
| rag | synthetic | original | 5000 | read_ms | shared | 11.365 |
| rag | synthetic | original | 5000 | write_ms_per_turn | shared | 0.265 |
| rag_timestamp | synthetic | cue_free | 1000 | correct_tool | shared | 100.000 % |
| rag_timestamp | synthetic | cue_free | 1000 | end_to_end_ms | shared | 1414.316 |
| rag_timestamp | synthetic | cue_free | 1000 | exact_arguments | shared | 83.333 % |
| rag_timestamp | synthetic | cue_free | 1000 | full_success | shared | 83.333 % |
| rag_timestamp | synthetic | cue_free | 1000 | read_ms | shared | 8.813 |
| rag_timestamp | synthetic | cue_free | 1000 | write_ms_per_turn | shared | 0.278 |
| rag_timestamp | synthetic | cue_free | 5000 | correct_tool | shared | 100.000 % |
| rag_timestamp | synthetic | cue_free | 5000 | end_to_end_ms | shared | 2457.840 |
| rag_timestamp | synthetic | cue_free | 5000 | exact_arguments | shared | 80.667 % |
| rag_timestamp | synthetic | cue_free | 5000 | full_success | shared | 80.667 % |
| rag_timestamp | synthetic | cue_free | 5000 | read_ms | shared | 10.948 |
| rag_timestamp | synthetic | cue_free | 5000 | write_ms_per_turn | shared | 0.266 |
| rag_timestamp | synthetic | original | 1000 | correct_tool | shared | 100.000 % |
| rag_timestamp | synthetic | original | 1000 | end_to_end_ms | shared | 1391.605 |
| rag_timestamp | synthetic | original | 1000 | exact_arguments | shared | 79.333 % |
| rag_timestamp | synthetic | original | 1000 | full_success | shared | 79.333 % |
| rag_timestamp | synthetic | original | 1000 | read_ms | shared | 8.624 |
| rag_timestamp | synthetic | original | 1000 | write_ms_per_turn | shared | 0.276 |
| rag_timestamp | synthetic | original | 5000 | correct_tool | shared | 100.000 % |
| rag_timestamp | synthetic | original | 5000 | end_to_end_ms | shared | 2404.075 |
| rag_timestamp | synthetic | original | 5000 | exact_arguments | shared | 74.667 % |
| rag_timestamp | synthetic | original | 5000 | full_success | shared | 74.667 % |
| rag_timestamp | synthetic | original | 5000 | read_ms | shared | 10.742 |
| rag_timestamp | synthetic | original | 5000 | write_ms_per_turn | shared | 0.262 |

## Per-seed values

```csv
agent,dataset,style,horizon,training_seed,metric,n_questions,complete,value
bounded_rag,synthetic,cue_free,1000,shared,correct_tool,150,True,0.9266666666666666
bounded_rag,synthetic,cue_free,1000,shared,end_to_end_ms,150,True,1241.233983333368
bounded_rag,synthetic,cue_free,1000,shared,exact_arguments,150,True,0.3
bounded_rag,synthetic,cue_free,1000,shared,full_success,150,True,0.3
bounded_rag,synthetic,cue_free,1000,shared,read_ms,150,True,8.169823333179616
bounded_rag,synthetic,cue_free,1000,shared,write_ms_per_turn,150,True,0.27320412266681765
bounded_rag,synthetic,cue_free,5000,shared,correct_tool,150,True,0.84
bounded_rag,synthetic,cue_free,5000,shared,end_to_end_ms,150,True,2213.5048406665737
bounded_rag,synthetic,cue_free,5000,shared,exact_arguments,150,True,0.06
bounded_rag,synthetic,cue_free,5000,shared,full_success,150,True,0.06
bounded_rag,synthetic,cue_free,5000,shared,read_ms,150,True,8.591935333267125
bounded_rag,synthetic,cue_free,5000,shared,write_ms_per_turn,150,True,0.2673312389333296
bounded_rag,synthetic,original,1000,shared,correct_tool,150,True,0.92
bounded_rag,synthetic,original,1000,shared,end_to_end_ms,150,True,1233.9274240002487
bounded_rag,synthetic,original,1000,shared,exact_arguments,150,True,0.2733333333333333
bounded_rag,synthetic,original,1000,shared,full_success,150,True,0.2733333333333333
bounded_rag,synthetic,original,1000,shared,read_ms,150,True,8.140868000082264
bounded_rag,synthetic,original,1000,shared,write_ms_per_turn,150,True,0.2726664606666721
bounded_rag,synthetic,original,5000,shared,correct_tool,150,True,0.88
bounded_rag,synthetic,original,5000,shared,end_to_end_ms,150,True,2201.4493559999028
bounded_rag,synthetic,original,5000,shared,exact_arguments,150,True,0.06
bounded_rag,synthetic,original,5000,shared,full_success,150,True,0.06
bounded_rag,synthetic,original,5000,shared,read_ms,150,True,8.364265333184449
bounded_rag,synthetic,original,5000,shared,write_ms_per_turn,150,True,0.2659750693333117
lalm,synthetic,cue_free,1000,13,correct_tool,150,True,0.4533333333333333
lalm,synthetic,cue_free,1000,13,end_to_end_ms,150,True,2139.5520886668724
lalm,synthetic,cue_free,1000,13,exact_arguments,150,True,0.6066666666666667
lalm,synthetic,cue_free,1000,13,full_success,150,True,0.38
lalm,synthetic,cue_free,1000,13,read_ms,150,True,9.42197533334062
lalm,synthetic,cue_free,1000,13,write_ms_per_turn,150,True,1.0586472686666577
lalm,synthetic,cue_free,1000,23,correct_tool,150,True,0.98
lalm,synthetic,cue_free,1000,23,end_to_end_ms,150,True,2216.284362000006
lalm,synthetic,cue_free,1000,23,exact_arguments,150,True,0.8133333333333334
lalm,synthetic,cue_free,1000,23,full_success,150,True,0.8133333333333334
lalm,synthetic,cue_free,1000,23,read_ms,150,True,9.58952000005714
lalm,synthetic,cue_free,1000,23,write_ms_per_turn,150,True,1.0647050726665475
lalm,synthetic,cue_free,1000,37,correct_tool,150,True,0.34
lalm,synthetic,cue_free,1000,37,end_to_end_ms,150,True,2873.3057046665635
lalm,synthetic,cue_free,1000,37,exact_arguments,150,True,0.06666666666666667
lalm,synthetic,cue_free,1000,37,full_success,150,True,0.06666666666666667
lalm,synthetic,cue_free,1000,37,read_ms,150,True,9.53916200004945
lalm,synthetic,cue_free,1000,37,write_ms_per_turn,150,True,1.0626510100001179
lalm,synthetic,cue_free,1000,41,correct_tool,150,True,0.86
lalm,synthetic,cue_free,1000,41,end_to_end_ms,150,True,2424.8956206667935
lalm,synthetic,cue_free,1000,41,exact_arguments,150,True,0.6666666666666666
lalm,synthetic,cue_free,1000,41,full_success,150,True,0.5866666666666667
lalm,synthetic,cue_free,1000,41,read_ms,150,True,9.470303333024882
lalm,synthetic,cue_free,1000,41,write_ms_per_turn,150,True,1.057658644667002
lalm,synthetic,cue_free,1000,7,correct_tool,150,True,0.92
lalm,synthetic,cue_free,1000,7,end_to_end_ms,150,True,2386.048553333482
lalm,synthetic,cue_free,1000,7,exact_arguments,150,True,0.7666666666666667
lalm,synthetic,cue_free,1000,7,full_success,150,True,0.7533333333333333
lalm,synthetic,cue_free,1000,7,read_ms,150,True,9.352218666608678
lalm,synthetic,cue_free,1000,7,write_ms_per_turn,150,True,1.0464894753333405
lalm,synthetic,cue_free,5000,13,correct_tool,150,True,0.5133333333333333
lalm,synthetic,cue_free,5000,13,end_to_end_ms,150,True,6364.676591333652
lalm,synthetic,cue_free,5000,13,exact_arguments,150,True,0.56
lalm,synthetic,cue_free,5000,13,full_success,150,True,0.37333333333333335
lalm,synthetic,cue_free,5000,13,read_ms,150,True,9.364490666751712
lalm,synthetic,cue_free,5000,13,write_ms_per_turn,150,True,1.0685509302667002
lalm,synthetic,cue_free,5000,23,correct_tool,150,True,0.96
lalm,synthetic,cue_free,5000,23,end_to_end_ms,150,True,6511.708479333465
lalm,synthetic,cue_free,5000,23,exact_arguments,150,True,0.8066666666666666
lalm,synthetic,cue_free,5000,23,full_success,150,True,0.8066666666666666
lalm,synthetic,cue_free,5000,23,read_ms,150,True,9.575785333557482
lalm,synthetic,cue_free,5000,23,write_ms_per_turn,150,True,1.067895747466692
lalm,synthetic,cue_free,5000,37,correct_tool,150,True,0.88
lalm,synthetic,cue_free,5000,37,end_to_end_ms,150,True,6757.547270000359
lalm,synthetic,cue_free,5000,37,exact_arguments,150,True,0.58
lalm,synthetic,cue_free,5000,37,full_success,150,True,0.54
lalm,synthetic,cue_free,5000,37,read_ms,150,True,9.45698533357548
lalm,synthetic,cue_free,5000,37,write_ms_per_turn,150,True,1.0701535570667378
lalm,synthetic,cue_free,5000,41,correct_tool,150,True,0.8133333333333334
lalm,synthetic,cue_free,5000,41,end_to_end_ms,150,True,6784.095575333292
lalm,synthetic,cue_free,5000,41,exact_arguments,150,True,0.66
lalm,synthetic,cue_free,5000,41,full_success,150,True,0.6
lalm,synthetic,cue_free,5000,41,read_ms,150,True,9.370583333366085
lalm,synthetic,cue_free,5000,41,write_ms_per_turn,150,True,1.0707065773332822
lalm,synthetic,cue_free,5000,7,correct_tool,150,True,0.9133333333333333
lalm,synthetic,cue_free,5000,7,end_to_end_ms,150,True,6673.66515866619
lalm,synthetic,cue_free,5000,7,exact_arguments,150,True,0.82
lalm,synthetic,cue_free,5000,7,full_success,150,True,0.7933333333333333
lalm,synthetic,cue_free,5000,7,read_ms,150,True,9.353207333212291
lalm,synthetic,cue_free,5000,7,write_ms_per_turn,150,True,1.0636831805332962
lalm,synthetic,original,1000,13,correct_tool,150,True,0.38666666666666666
lalm,synthetic,original,1000,13,end_to_end_ms,150,True,2068.159773333415
lalm,synthetic,original,1000,13,exact_arguments,150,True,0.5133333333333333
lalm,synthetic,original,1000,13,full_success,150,True,0.32
lalm,synthetic,original,1000,13,read_ms,150,True,9.192460666769572
lalm,synthetic,original,1000,13,write_ms_per_turn,150,True,1.0542614179998298
lalm,synthetic,original,1000,23,correct_tool,150,True,0.9666666666666667
lalm,synthetic,original,1000,23,end_to_end_ms,150,True,2197.42766866686
lalm,synthetic,original,1000,23,exact_arguments,150,True,0.7666666666666667
lalm,synthetic,original,1000,23,full_success,150,True,0.7666666666666667
lalm,synthetic,original,1000,23,read_ms,150,True,9.417124666482172
lalm,synthetic,original,1000,23,write_ms_per_turn,150,True,1.0583821140002208
lalm,synthetic,original,1000,37,correct_tool,150,True,0.3466666666666667
lalm,synthetic,original,1000,37,end_to_end_ms,150,True,2805.456239333386
lalm,synthetic,original,1000,37,exact_arguments,150,True,0.14666666666666667
lalm,synthetic,original,1000,37,full_success,150,True,0.14666666666666667
lalm,synthetic,original,1000,37,read_ms,150,True,9.310309333231999
lalm,synthetic,original,1000,37,write_ms_per_turn,150,True,1.0538901013331876
lalm,synthetic,original,1000,41,correct_tool,150,True,0.8733333333333333
lalm,synthetic,original,1000,41,end_to_end_ms,150,True,2426.310280666779
lalm,synthetic,original,1000,41,exact_arguments,150,True,0.6933333333333334
lalm,synthetic,original,1000,41,full_success,150,True,0.62
lalm,synthetic,original,1000,41,read_ms,150,True,9.428183333414685
lalm,synthetic,original,1000,41,write_ms_per_turn,150,True,1.0564971906666567
lalm,synthetic,original,1000,7,correct_tool,150,True,0.92
lalm,synthetic,original,1000,7,end_to_end_ms,150,True,2397.462949333179
lalm,synthetic,original,1000,7,exact_arguments,150,True,0.7666666666666667
lalm,synthetic,original,1000,7,full_success,150,True,0.7533333333333333
lalm,synthetic,original,1000,7,read_ms,150,True,9.428100666652123
lalm,synthetic,original,1000,7,write_ms_per_turn,150,True,1.0719306413332137
lalm,synthetic,original,5000,13,correct_tool,150,True,0.42
lalm,synthetic,original,5000,13,end_to_end_ms,150,True,6363.229066000276
lalm,synthetic,original,5000,13,exact_arguments,150,True,0.44666666666666666
lalm,synthetic,original,5000,13,full_success,150,True,0.3
lalm,synthetic,original,5000,13,read_ms,150,True,9.450997333478881
lalm,synthetic,original,5000,13,write_ms_per_turn,150,True,1.0737100841333547
lalm,synthetic,original,5000,23,correct_tool,150,True,0.9666666666666667
lalm,synthetic,original,5000,23,end_to_end_ms,150,True,6488.875432000325
lalm,synthetic,original,5000,23,exact_arguments,150,True,0.7333333333333333
lalm,synthetic,original,5000,23,full_success,150,True,0.7333333333333333
lalm,synthetic,original,5000,23,read_ms,150,True,9.460296000324888
lalm,synthetic,original,5000,23,write_ms_per_turn,150,True,1.0744375648000133
lalm,synthetic,original,5000,37,correct_tool,150,True,0.8733333333333333
lalm,synthetic,original,5000,37,end_to_end_ms,150,True,6725.016212000021
lalm,synthetic,original,5000,37,exact_arguments,150,True,0.6266666666666667
lalm,synthetic,original,5000,37,full_success,150,True,0.5866666666666667
lalm,synthetic,original,5000,37,read_ms,150,True,9.312517333237338
lalm,synthetic,original,5000,37,write_ms_per_turn,150,True,1.0730478624000244
lalm,synthetic,original,5000,41,correct_tool,150,True,0.82
lalm,synthetic,original,5000,41,end_to_end_ms,150,True,6685.396055999881
lalm,synthetic,original,5000,41,exact_arguments,150,True,0.7066666666666667
lalm,synthetic,original,5000,41,full_success,150,True,0.6466666666666666
lalm,synthetic,original,5000,41,read_ms,150,True,9.358329999983349
lalm,synthetic,original,5000,41,write_ms_per_turn,150,True,1.0642519619999755
lalm,synthetic,original,5000,7,correct_tool,150,True,0.9
lalm,synthetic,original,5000,7,end_to_end_ms,150,True,6692.9657226666795
lalm,synthetic,original,5000,7,exact_arguments,150,True,0.8266666666666667
lalm,synthetic,original,5000,7,full_success,150,True,0.8
lalm,synthetic,original,5000,7,read_ms,150,True,9.41871866651733
lalm,synthetic,original,5000,7,write_ms_per_turn,150,True,1.0759085014666538
lexical_only,synthetic,cue_free,1000,shared,correct_tool,150,True,0.9866666666666667
lexical_only,synthetic,cue_free,1000,shared,end_to_end_ms,150,True,1433.6354726667196
lexical_only,synthetic,cue_free,1000,shared,exact_arguments,150,True,0.78
lexical_only,synthetic,cue_free,1000,shared,full_success,150,True,0.78
lexical_only,synthetic,cue_free,1000,shared,read_ms,150,True,7.558759999931984
lexical_only,synthetic,cue_free,1000,shared,write_ms_per_turn,150,True,0.3018157713334949
lexical_only,synthetic,cue_free,5000,shared,correct_tool,150,True,0.9733333333333334
lexical_only,synthetic,cue_free,5000,shared,end_to_end_ms,150,True,2747.692202666852
lexical_only,synthetic,cue_free,5000,shared,exact_arguments,150,True,0.7666666666666667
lexical_only,synthetic,cue_free,5000,shared,full_success,150,True,0.7533333333333333
lexical_only,synthetic,cue_free,5000,shared,read_ms,150,True,7.727936000180004
lexical_only,synthetic,cue_free,5000,shared,write_ms_per_turn,150,True,0.32541788440001257
lexical_only,synthetic,original,1000,shared,correct_tool,150,True,0.9866666666666667
lexical_only,synthetic,original,1000,shared,end_to_end_ms,150,True,1399.715036000113
lexical_only,synthetic,original,1000,shared,exact_arguments,150,True,0.72
lexical_only,synthetic,original,1000,shared,full_success,150,True,0.72
lexical_only,synthetic,original,1000,shared,read_ms,150,True,7.526104666952354
lexical_only,synthetic,original,1000,shared,write_ms_per_turn,150,True,0.29869976399991477
lexical_only,synthetic,original,5000,shared,correct_tool,150,True,0.9733333333333334
lexical_only,synthetic,original,5000,shared,end_to_end_ms,150,True,2694.457609333343
lexical_only,synthetic,original,5000,shared,exact_arguments,150,True,0.7933333333333333
lexical_only,synthetic,original,5000,shared,full_success,150,True,0.78
lexical_only,synthetic,original,5000,shared,read_ms,150,True,7.4466673334488105
lexical_only,synthetic,original,5000,shared,write_ms_per_turn,150,True,0.31964379293331147
rag,synthetic,cue_free,1000,shared,correct_tool,150,True,0.9666666666666667
rag,synthetic,cue_free,1000,shared,end_to_end_ms,150,True,1413.1478079997032
rag,synthetic,cue_free,1000,shared,exact_arguments,150,True,0.7866666666666666
rag,synthetic,cue_free,1000,shared,full_success,150,True,0.76
rag,synthetic,cue_free,1000,shared,read_ms,150,True,8.734992666625962
rag,synthetic,cue_free,1000,shared,write_ms_per_turn,150,True,0.27161459733322163
rag,synthetic,cue_free,5000,shared,correct_tool,150,True,0.9933333333333333
rag,synthetic,cue_free,5000,shared,end_to_end_ms,150,True,2467.760888666768
rag,synthetic,cue_free,5000,shared,exact_arguments,150,True,0.78
rag,synthetic,cue_free,5000,shared,full_success,150,True,0.7733333333333333
rag,synthetic,cue_free,5000,shared,read_ms,150,True,11.489728000039273
rag,synthetic,cue_free,5000,shared,write_ms_per_turn,150,True,0.26831299359999444
rag,synthetic,original,1000,shared,correct_tool,150,True,0.9666666666666667
rag,synthetic,original,1000,shared,end_to_end_ms,150,True,1385.7516493330331
rag,synthetic,original,1000,shared,exact_arguments,150,True,0.6933333333333334
rag,synthetic,original,1000,shared,full_success,150,True,0.6666666666666666
rag,synthetic,original,1000,shared,read_ms,150,True,8.537908666536774
rag,synthetic,original,1000,shared,write_ms_per_turn,150,True,0.27193031600003453
rag,synthetic,original,5000,shared,correct_tool,150,True,0.9933333333333333
rag,synthetic,original,5000,shared,end_to_end_ms,150,True,2423.7520979999804
rag,synthetic,original,5000,shared,exact_arguments,150,True,0.66
rag,synthetic,original,5000,shared,full_success,150,True,0.6533333333333333
rag,synthetic,original,5000,shared,read_ms,150,True,11.36500533320941
rag,synthetic,original,5000,shared,write_ms_per_turn,150,True,0.26544681986665575
rag_timestamp,synthetic,cue_free,1000,shared,correct_tool,150,True,1.0
rag_timestamp,synthetic,cue_free,1000,shared,end_to_end_ms,150,True,1414.3157060000278
rag_timestamp,synthetic,cue_free,1000,shared,exact_arguments,150,True,0.8333333333333334
rag_timestamp,synthetic,cue_free,1000,shared,full_success,150,True,0.8333333333333334
rag_timestamp,synthetic,cue_free,1000,shared,read_ms,150,True,8.813400666525316
rag_timestamp,synthetic,cue_free,1000,shared,write_ms_per_turn,150,True,0.27782181733329103
rag_timestamp,synthetic,cue_free,5000,shared,correct_tool,150,True,1.0
rag_timestamp,synthetic,cue_free,5000,shared,end_to_end_ms,150,True,2457.8399926669467
rag_timestamp,synthetic,cue_free,5000,shared,exact_arguments,150,True,0.8066666666666666
rag_timestamp,synthetic,cue_free,5000,shared,full_success,150,True,0.8066666666666666
rag_timestamp,synthetic,cue_free,5000,shared,read_ms,150,True,10.947613333482877
rag_timestamp,synthetic,cue_free,5000,shared,write_ms_per_turn,150,True,0.26581538600003113
rag_timestamp,synthetic,original,1000,shared,correct_tool,150,True,1.0
rag_timestamp,synthetic,original,1000,shared,end_to_end_ms,150,True,1391.605458000037
rag_timestamp,synthetic,original,1000,shared,exact_arguments,150,True,0.7933333333333333
rag_timestamp,synthetic,original,1000,shared,full_success,150,True,0.7933333333333333
rag_timestamp,synthetic,original,1000,shared,read_ms,150,True,8.623567999893567
rag_timestamp,synthetic,original,1000,shared,write_ms_per_turn,150,True,0.27560047333353094
rag_timestamp,synthetic,original,5000,shared,correct_tool,150,True,1.0
rag_timestamp,synthetic,original,5000,shared,end_to_end_ms,150,True,2404.075432666517
rag_timestamp,synthetic,original,5000,shared,exact_arguments,150,True,0.7466666666666667
rag_timestamp,synthetic,original,5000,shared,full_success,150,True,0.7466666666666667
rag_timestamp,synthetic,original,5000,shared,read_ms,150,True,10.741661999939728
rag_timestamp,synthetic,original,5000,shared,write_ms_per_turn,150,True,0.26236891813332475

```

## Paired tests

```csv
dataset,style,horizon,metric,left,right,training_seed,n_questions,n_clusters,delta,ci_low,ci_high,p_raw,p_holm
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,7,150,150,-0.06666666666666667,-0.11333333333333333,-0.02,0.0150984901509849,
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,13,150,150,-0.5333333333333333,-0.6133333333333333,-0.4533333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,23,150,150,-0.006666666666666667,-0.03333333333333333,0.02,1.0,
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,37,150,150,-0.6466666666666666,-0.72,-0.5666666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,41,150,150,-0.12666666666666668,-0.18666666666666668,-0.07333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,lexical_only,mean,150,150,-0.27599999999999997,-0.3146666666666667,-0.23733333333333329,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,7,150,150,-0.013333333333333334,-0.08666666666666667,0.06,0.8547145285471452,
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,13,150,150,-0.17333333333333334,-0.26,-0.08666666666666667,0.0004999500049995,
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,23,150,150,0.03333333333333333,-0.04,0.10666666666666667,0.45325467453254675,
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,37,150,150,-0.7133333333333334,-0.7933333333333333,-0.6333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,41,150,150,-0.11333333333333333,-0.18,-0.04666666666666667,0.0020997900209979003,
synthetic,cue_free,1000,exact_arguments,lalm,lexical_only,mean,150,150,-0.19599999999999998,-0.25066666666666665,-0.1386666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,full_success,lalm,lexical_only,7,150,150,-0.02666666666666667,-0.1,0.04666666666666667,0.5886411358864113,
synthetic,cue_free,1000,full_success,lalm,lexical_only,13,150,150,-0.4,-0.49333333333333335,-0.30666666666666664,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,lexical_only,23,150,150,0.03333333333333333,-0.04,0.10666666666666667,0.45325467453254675,
synthetic,cue_free,1000,full_success,lalm,lexical_only,37,150,150,-0.7133333333333334,-0.7933333333333333,-0.6333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,lexical_only,41,150,150,-0.19333333333333333,-0.2733333333333333,-0.12,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,lexical_only,mean,150,150,-0.26,-0.32000000000000006,-0.19866666666666669,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,correct_tool,lalm,rag,7,150,150,-0.04666666666666667,-0.1,0.006666666666666667,0.1391860813918608,
synthetic,cue_free,1000,correct_tool,lalm,rag,13,150,150,-0.5133333333333333,-0.5933333333333334,-0.43333333333333335,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,rag,23,150,150,0.013333333333333334,-0.02,0.05333333333333334,0.7271272872712728,
synthetic,cue_free,1000,correct_tool,lalm,rag,37,150,150,-0.6266666666666667,-0.7066666666666667,-0.5466666666666666,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,rag,41,150,150,-0.10666666666666667,-0.17333333333333334,-0.04666666666666667,0.0022997700229977,
synthetic,cue_free,1000,correct_tool,lalm,rag,mean,150,150,-0.256,-0.29999999999999993,-0.21066666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,exact_arguments,lalm,rag,7,150,150,-0.02,-0.1,0.06,0.7472252774722528,
synthetic,cue_free,1000,exact_arguments,lalm,rag,13,150,150,-0.18,-0.26666666666666666,-0.09333333333333334,0.00029997000299970003,
synthetic,cue_free,1000,exact_arguments,lalm,rag,23,150,150,0.02666666666666667,-0.04666666666666667,0.1,0.5831416858314169,
synthetic,cue_free,1000,exact_arguments,lalm,rag,37,150,150,-0.72,-0.8,-0.6333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,rag,41,150,150,-0.12,-0.18666666666666668,-0.05333333333333334,0.0018998100189981002,
synthetic,cue_free,1000,exact_arguments,lalm,rag,mean,150,150,-0.20266666666666666,-0.2613333333333333,-0.14133333333333334,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,full_success,lalm,rag,7,150,150,-0.006666666666666667,-0.09333333333333334,0.08,1.0,
synthetic,cue_free,1000,full_success,lalm,rag,13,150,150,-0.38,-0.48,-0.28,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,rag,23,150,150,0.05333333333333334,-0.02,0.12666666666666668,0.22747725227477253,
synthetic,cue_free,1000,full_success,lalm,rag,37,150,150,-0.6933333333333334,-0.7733333333333333,-0.6066666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,rag,41,150,150,-0.17333333333333334,-0.26,-0.09333333333333334,0.00019998000199980003,
synthetic,cue_free,1000,full_success,lalm,rag,mean,150,150,-0.24,-0.30666666666666664,-0.17200000000000001,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,7,150,150,-0.08,-0.12666666666666668,-0.04,0.0006999300069993001,
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,13,150,150,-0.5466666666666666,-0.6266666666666667,-0.4666666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,23,150,150,-0.02,-0.04666666666666667,0.0,0.2512748725127487,
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,37,150,150,-0.66,-0.7333333333333333,-0.58,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,41,150,150,-0.14,-0.19333333333333333,-0.08666666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,rag_timestamp,mean,150,150,-0.2893333333333333,-0.3253333333333333,-0.2546666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,7,150,150,-0.06666666666666667,-0.14666666666666667,0.013333333333333334,0.14128587141285873,
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,13,150,150,-0.22666666666666666,-0.32,-0.13333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,23,150,150,-0.02,-0.09333333333333334,0.05333333333333334,0.7242275772422758,
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,37,150,150,-0.7666666666666667,-0.84,-0.6866666666666666,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,41,150,150,-0.16666666666666666,-0.23333333333333334,-0.1,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,rag_timestamp,mean,150,150,-0.24933333333333338,-0.30666666666666664,-0.18933333333333333,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,7,150,150,-0.08,-0.16,0.0,0.0765923407659234,
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,13,150,150,-0.4533333333333333,-0.5466666666666666,-0.35333333333333333,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,23,150,150,-0.02,-0.09333333333333334,0.05333333333333334,0.7242275772422758,
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,37,150,150,-0.7666666666666667,-0.84,-0.6866666666666666,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,41,150,150,-0.24666666666666667,-0.32,-0.17333333333333334,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,rag_timestamp,mean,150,150,-0.31333333333333335,-0.37466666666666665,-0.25066666666666665,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,7,150,150,-0.006666666666666667,-0.06666666666666667,0.04666666666666667,1.0,
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,13,150,150,-0.47333333333333333,-0.56,-0.38666666666666666,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,23,150,150,0.05333333333333334,0.006666666666666667,0.1,0.06059394060593941,
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,37,150,150,-0.5866666666666667,-0.6733333333333333,-0.49333333333333335,9.999000099990002e-05,
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,41,150,150,-0.06666666666666667,-0.13333333333333333,0.0,0.08849115088491151,
synthetic,cue_free,1000,correct_tool,lalm,bounded_rag,mean,150,150,-0.216,-0.26933333333333326,-0.1613333333333333,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,7,150,150,0.4666666666666667,0.37333333333333335,0.56,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,13,150,150,0.30666666666666664,0.20666666666666667,0.4,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,23,150,150,0.5133333333333333,0.41333333333333333,0.6066666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,37,150,150,-0.23333333333333334,-0.31333333333333335,-0.15333333333333332,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,41,150,150,0.36666666666666664,0.26666666666666666,0.4666666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,exact_arguments,lalm,bounded_rag,mean,150,150,0.28400000000000003,0.20400000000000001,0.36,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,1000,full_success,lalm,bounded_rag,7,150,150,0.4533333333333333,0.36,0.5466666666666666,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,bounded_rag,13,150,150,0.08,-0.013333333333333334,0.18,0.1307869213078692,
synthetic,cue_free,1000,full_success,lalm,bounded_rag,23,150,150,0.5133333333333333,0.41333333333333333,0.6066666666666667,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,bounded_rag,37,150,150,-0.23333333333333334,-0.31333333333333335,-0.15333333333333332,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,bounded_rag,41,150,150,0.2866666666666667,0.18666666666666668,0.38,9.999000099990002e-05,
synthetic,cue_free,1000,full_success,lalm,bounded_rag,mean,150,150,0.22,0.14133333333333334,0.2946666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,7,150,150,-0.06,-0.10666666666666667,-0.013333333333333334,0.023997600239976002,
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,13,150,150,-0.46,-0.54,-0.38,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,23,150,150,-0.013333333333333334,-0.04666666666666667,0.02,0.6852314768523148,
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,37,150,150,-0.09333333333333334,-0.14666666666666667,-0.04,0.0010998900109989002,
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,41,150,150,-0.16,-0.22666666666666666,-0.1,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,lexical_only,mean,150,150,-0.15733333333333335,-0.19733333333333333,-0.11733333333333335,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,7,150,150,0.05333333333333334,-0.006666666666666667,0.11333333333333333,0.1411858814118588,
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,13,150,150,-0.20666666666666667,-0.2866666666666667,-0.12666666666666668,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,23,150,150,0.04,-0.02,0.10666666666666667,0.30786921307869214,
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,37,150,150,-0.18666666666666668,-0.29333333333333333,-0.08,0.0015998400159984002,
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,41,150,150,-0.10666666666666667,-0.18666666666666668,-0.03333333333333333,0.0110988901109889,
synthetic,cue_free,5000,exact_arguments,lalm,lexical_only,mean,150,150,-0.08133333333333331,-0.13733333333333334,-0.023999999999999997,0.006799320067993201,0.04079592040795921
synthetic,cue_free,5000,full_success,lalm,lexical_only,7,150,150,0.04,-0.02666666666666667,0.11333333333333333,0.35126487351264873,
synthetic,cue_free,5000,full_success,lalm,lexical_only,13,150,150,-0.38,-0.4666666666666667,-0.29333333333333333,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,lexical_only,23,150,150,0.05333333333333334,-0.013333333333333334,0.12,0.16898310168983102,
synthetic,cue_free,5000,full_success,lalm,lexical_only,37,150,150,-0.21333333333333335,-0.32666666666666666,-0.1,0.0004999500049995,
synthetic,cue_free,5000,full_success,lalm,lexical_only,41,150,150,-0.15333333333333332,-0.24,-0.06666666666666667,0.0008999100089991,
synthetic,cue_free,5000,full_success,lalm,lexical_only,mean,150,150,-0.13066666666666665,-0.19733333333333333,-0.064,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,correct_tool,lalm,rag,7,150,150,-0.08,-0.12666666666666668,-0.03333333333333333,0.0015998400159984002,
synthetic,cue_free,5000,correct_tool,lalm,rag,13,150,150,-0.48,-0.56,-0.4,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag,23,150,150,-0.03333333333333333,-0.06666666666666667,0.0,0.12868713128687131,
synthetic,cue_free,5000,correct_tool,lalm,rag,37,150,150,-0.11333333333333333,-0.16666666666666666,-0.06,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag,41,150,150,-0.18,-0.24666666666666667,-0.12,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag,mean,150,150,-0.17733333333333334,-0.21866666666666665,-0.13733333333333334,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,exact_arguments,lalm,rag,7,150,150,0.04,-0.03333333333333333,0.11333333333333333,0.36236376362363765,
synthetic,cue_free,5000,exact_arguments,lalm,rag,13,150,150,-0.22,-0.30666666666666664,-0.13333333333333333,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,rag,23,150,150,0.02666666666666667,-0.04,0.09333333333333334,0.5607439256074392,
synthetic,cue_free,5000,exact_arguments,lalm,rag,37,150,150,-0.2,-0.30666666666666664,-0.09333333333333334,0.0005999400059994001,
synthetic,cue_free,5000,exact_arguments,lalm,rag,41,150,150,-0.12,-0.19333333333333333,-0.04666666666666667,0.0027997200279972004,
synthetic,cue_free,5000,exact_arguments,lalm,rag,mean,150,150,-0.09466666666666666,-0.15600000000000003,-0.03333333333333335,0.0033996600339966003,0.027197280271972803
synthetic,cue_free,5000,full_success,lalm,rag,7,150,150,0.02,-0.06,0.09333333333333334,0.7424257574242575,
synthetic,cue_free,5000,full_success,lalm,rag,13,150,150,-0.4,-0.49333333333333335,-0.30666666666666664,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,rag,23,150,150,0.03333333333333333,-0.03333333333333333,0.1,0.44685531446855314,
synthetic,cue_free,5000,full_success,lalm,rag,37,150,150,-0.23333333333333334,-0.3466666666666667,-0.12,0.00019998000199980003,
synthetic,cue_free,5000,full_success,lalm,rag,41,150,150,-0.17333333333333334,-0.25333333333333335,-0.09333333333333334,0.00019998000199980003,
synthetic,cue_free,5000,full_success,lalm,rag,mean,150,150,-0.15066666666666664,-0.21866666666666665,-0.08266666666666668,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,7,150,150,-0.08666666666666667,-0.13333333333333333,-0.04666666666666667,0.00029997000299970003,
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,13,150,150,-0.4866666666666667,-0.5666666666666667,-0.4066666666666667,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,23,150,150,-0.04,-0.07333333333333333,-0.013333333333333334,0.0327967203279672,
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,37,150,150,-0.12,-0.17333333333333334,-0.07333333333333333,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,41,150,150,-0.18666666666666668,-0.25333333333333335,-0.12666666666666668,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,rag_timestamp,mean,150,150,-0.184,-0.224,-0.14666666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,7,150,150,0.013333333333333334,-0.06,0.08666666666666667,0.8706129387061294,
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,13,150,150,-0.24666666666666667,-0.34,-0.16,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,23,150,150,0.0,-0.07333333333333333,0.07333333333333333,1.0,
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,37,150,150,-0.22666666666666666,-0.3333333333333333,-0.12,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,41,150,150,-0.14666666666666667,-0.22666666666666666,-0.06666666666666667,0.0004999500049995,
synthetic,cue_free,5000,exact_arguments,lalm,rag_timestamp,mean,150,150,-0.12133333333333333,-0.18666666666666668,-0.05733333333333332,0.0006999300069993001,0.006999300069993001
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,7,150,150,-0.013333333333333334,-0.09333333333333334,0.06666666666666667,0.8769123087691231,
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,13,150,150,-0.43333333333333335,-0.5266666666666666,-0.34,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,23,150,150,0.0,-0.07333333333333333,0.07333333333333333,1.0,
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,37,150,150,-0.26666666666666666,-0.37333333333333335,-0.16,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,41,150,150,-0.20666666666666667,-0.29333333333333333,-0.12,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,rag_timestamp,mean,150,150,-0.184,-0.25466666666666665,-0.11466666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,7,150,150,0.07333333333333333,0.0,0.14666666666666667,0.08999100089991001,
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,13,150,150,-0.32666666666666666,-0.4266666666666667,-0.22666666666666666,9.999000099990002e-05,
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,23,150,150,0.12,0.05333333333333334,0.18666666666666668,0.000999900009999,
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,37,150,150,0.04,-0.04,0.12,0.4196580341965803,
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,41,150,150,-0.02666666666666667,-0.11333333333333333,0.06,0.6704329567043296,
synthetic,cue_free,5000,correct_tool,lalm,bounded_rag,mean,150,150,-0.024000000000000004,-0.09599999999999999,0.050666666666666665,0.5586441355864413,1
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,7,150,150,0.76,0.6933333333333334,0.8266666666666667,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,13,150,150,0.5,0.42,0.58,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,23,150,150,0.7466666666666667,0.6733333333333333,0.8133333333333334,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,37,150,150,0.52,0.43333333333333335,0.6066666666666667,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,41,150,150,0.6,0.52,0.6733333333333333,9.999000099990002e-05,
synthetic,cue_free,5000,exact_arguments,lalm,bounded_rag,mean,150,150,0.6253333333333332,0.5706333333333333,0.676,9.999000099990002e-05,0.0047995200479952005
synthetic,cue_free,5000,full_success,lalm,bounded_rag,7,150,150,0.7333333333333333,0.66,0.8,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,bounded_rag,13,150,150,0.31333333333333335,0.24,0.38666666666666666,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,bounded_rag,23,150,150,0.7466666666666667,0.6733333333333333,0.8133333333333334,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,bounded_rag,37,150,150,0.48,0.3933333333333333,0.5666666666666667,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,bounded_rag,41,150,150,0.54,0.46,0.62,9.999000099990002e-05,
synthetic,cue_free,5000,full_success,lalm,bounded_rag,mean,150,150,0.5626666666666666,0.5066666666666667,0.6146666666666667,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,correct_tool,lalm,lexical_only,7,150,150,-0.06666666666666667,-0.11333333333333333,-0.02,0.013298670132986702,
synthetic,original,1000,correct_tool,lalm,lexical_only,13,150,150,-0.6,-0.6733333333333333,-0.52,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,lexical_only,23,150,150,-0.02,-0.05333333333333334,0.013333333333333334,0.45265473452654736,
synthetic,original,1000,correct_tool,lalm,lexical_only,37,150,150,-0.64,-0.7133333333333334,-0.5666666666666667,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,lexical_only,41,150,150,-0.11333333333333333,-0.17333333333333334,-0.06,0.00019998000199980003,
synthetic,original,1000,correct_tool,lalm,lexical_only,mean,150,150,-0.28800000000000003,-0.32533333333333336,-0.252,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,exact_arguments,lalm,lexical_only,7,150,150,0.04666666666666667,-0.02666666666666667,0.12,0.3033696630336966,
synthetic,original,1000,exact_arguments,lalm,lexical_only,13,150,150,-0.20666666666666667,-0.2866666666666667,-0.12,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,lexical_only,23,150,150,0.04666666666666667,-0.03333333333333333,0.12,0.3093690630936906,
synthetic,original,1000,exact_arguments,lalm,lexical_only,37,150,150,-0.5733333333333334,-0.6666666666666666,-0.48,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,lexical_only,41,150,150,-0.02666666666666667,-0.09333333333333334,0.04,0.5691430856914309,
synthetic,original,1000,exact_arguments,lalm,lexical_only,mean,150,150,-0.14266666666666664,-0.20133333333333334,-0.08133333333333334,0.00019998000199980003,0.0047995200479952005
synthetic,original,1000,full_success,lalm,lexical_only,7,150,150,0.03333333333333333,-0.04,0.10666666666666667,0.5074492550744926,
synthetic,original,1000,full_success,lalm,lexical_only,13,150,150,-0.4,-0.49333333333333335,-0.30666666666666664,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,lexical_only,23,150,150,0.04666666666666667,-0.03333333333333333,0.12,0.3093690630936906,
synthetic,original,1000,full_success,lalm,lexical_only,37,150,150,-0.5733333333333334,-0.6666666666666666,-0.48,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,lexical_only,41,150,150,-0.1,-0.18,-0.02,0.022397760223977603,
synthetic,original,1000,full_success,lalm,lexical_only,mean,150,150,-0.19866666666666666,-0.2626666666666667,-0.13200000000000003,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,correct_tool,lalm,rag,7,150,150,-0.04666666666666667,-0.1,0.006666666666666667,0.14538546145385461,
synthetic,original,1000,correct_tool,lalm,rag,13,150,150,-0.58,-0.6533333333333333,-0.5,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,rag,23,150,150,0.0,-0.04,0.04,1.0,
synthetic,original,1000,correct_tool,lalm,rag,37,150,150,-0.62,-0.7,-0.54,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,rag,41,150,150,-0.09333333333333334,-0.15333333333333332,-0.03333333333333333,0.006799320067993201,
synthetic,original,1000,correct_tool,lalm,rag,mean,150,150,-0.268,-0.3106666666666667,-0.2253333333333333,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,exact_arguments,lalm,rag,7,150,150,0.07333333333333333,-0.013333333333333334,0.16,0.15398460153984603,
synthetic,original,1000,exact_arguments,lalm,rag,13,150,150,-0.18,-0.2733333333333333,-0.08666666666666667,0.0006999300069993001,
synthetic,original,1000,exact_arguments,lalm,rag,23,150,150,0.07333333333333333,-0.013333333333333334,0.16,0.1508849115088491,
synthetic,original,1000,exact_arguments,lalm,rag,37,150,150,-0.5466666666666666,-0.6466666666666666,-0.44,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,rag,41,150,150,0.0,-0.08,0.08,1.0,
synthetic,original,1000,exact_arguments,lalm,rag,mean,150,150,-0.11599999999999999,-0.18933333333333333,-0.04,0.0033996600339966003,0.027197280271972803
synthetic,original,1000,full_success,lalm,rag,7,150,150,0.08666666666666667,-0.006666666666666667,0.18,0.10138986101389862,
synthetic,original,1000,full_success,lalm,rag,13,150,150,-0.3466666666666667,-0.44,-0.25333333333333335,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,rag,23,150,150,0.1,0.006666666666666667,0.19333333333333333,0.0496950304969503,
synthetic,original,1000,full_success,lalm,rag,37,150,150,-0.52,-0.6266666666666667,-0.41333333333333333,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,rag,41,150,150,-0.04666666666666667,-0.14666666666666667,0.04666666666666667,0.4106589341065893,
synthetic,original,1000,full_success,lalm,rag,mean,150,150,-0.14533333333333331,-0.22403333333333336,-0.06533333333333334,0.0006999300069993001,0.006999300069993001
synthetic,original,1000,correct_tool,lalm,rag_timestamp,7,150,150,-0.08,-0.12666666666666668,-0.04,0.0008999100089991,
synthetic,original,1000,correct_tool,lalm,rag_timestamp,13,150,150,-0.6133333333333333,-0.6866666666666666,-0.5333333333333333,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,rag_timestamp,23,150,150,-0.03333333333333333,-0.06666666666666667,-0.006666666666666667,0.06529347065293471,
synthetic,original,1000,correct_tool,lalm,rag_timestamp,37,150,150,-0.6533333333333333,-0.7266666666666667,-0.58,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,rag_timestamp,41,150,150,-0.12666666666666668,-0.18,-0.08,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,rag_timestamp,mean,150,150,-0.30133333333333334,-0.33599999999999997,-0.26933333333333326,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,7,150,150,-0.02666666666666667,-0.1,0.04666666666666667,0.6085391460853915,
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,13,150,150,-0.28,-0.37333333333333335,-0.18666666666666668,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,23,150,150,-0.02666666666666667,-0.1,0.05333333333333334,0.6107389261073892,
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,37,150,150,-0.6466666666666666,-0.7266666666666667,-0.5666666666666667,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,41,150,150,-0.1,-0.16,-0.04666666666666667,0.0018998100189981002,
synthetic,original,1000,exact_arguments,lalm,rag_timestamp,mean,150,150,-0.21600000000000003,-0.27199999999999996,-0.15866666666666668,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,full_success,lalm,rag_timestamp,7,150,150,-0.04,-0.11333333333333333,0.03333333333333333,0.39816018398160186,
synthetic,original,1000,full_success,lalm,rag_timestamp,13,150,150,-0.47333333333333333,-0.5666666666666667,-0.38,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,rag_timestamp,23,150,150,-0.02666666666666667,-0.1,0.05333333333333334,0.6107389261073892,
synthetic,original,1000,full_success,lalm,rag_timestamp,37,150,150,-0.6466666666666666,-0.7266666666666667,-0.5666666666666667,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,rag_timestamp,41,150,150,-0.17333333333333334,-0.24,-0.10666666666666667,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,rag_timestamp,mean,150,150,-0.27199999999999996,-0.3306666666666667,-0.21333333333333332,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,correct_tool,lalm,bounded_rag,7,150,150,0.0,-0.06,0.06,1.0,
synthetic,original,1000,correct_tool,lalm,bounded_rag,13,150,150,-0.5333333333333333,-0.62,-0.44,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,bounded_rag,23,150,150,0.04666666666666667,-0.006666666666666667,0.1,0.13858614138586142,
synthetic,original,1000,correct_tool,lalm,bounded_rag,37,150,150,-0.5733333333333334,-0.66,-0.4866666666666667,9.999000099990002e-05,
synthetic,original,1000,correct_tool,lalm,bounded_rag,41,150,150,-0.04666666666666667,-0.11333333333333333,0.02,0.24397560243975602,
synthetic,original,1000,correct_tool,lalm,bounded_rag,mean,150,150,-0.2213333333333333,-0.2733333333333333,-0.16533333333333336,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,exact_arguments,lalm,bounded_rag,7,150,150,0.49333333333333335,0.4,0.5866666666666667,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,bounded_rag,13,150,150,0.24,0.13333333333333333,0.34,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,bounded_rag,23,150,150,0.49333333333333335,0.3933333333333333,0.5933333333333334,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,bounded_rag,37,150,150,-0.12666666666666668,-0.21333333333333335,-0.04,0.006299370062993701,
synthetic,original,1000,exact_arguments,lalm,bounded_rag,41,150,150,0.42,0.32666666666666666,0.5133333333333333,9.999000099990002e-05,
synthetic,original,1000,exact_arguments,lalm,bounded_rag,mean,150,150,0.30400000000000005,0.22400000000000006,0.384,9.999000099990002e-05,0.0047995200479952005
synthetic,original,1000,full_success,lalm,bounded_rag,7,150,150,0.48,0.38666666666666666,0.5733333333333334,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,bounded_rag,13,150,150,0.04666666666666667,-0.06,0.15333333333333332,0.4517548245175482,
synthetic,original,1000,full_success,lalm,bounded_rag,23,150,150,0.49333333333333335,0.3933333333333333,0.5933333333333334,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,bounded_rag,37,150,150,-0.12666666666666668,-0.21333333333333335,-0.04,0.006299370062993701,
synthetic,original,1000,full_success,lalm,bounded_rag,41,150,150,0.3466666666666667,0.26,0.44,9.999000099990002e-05,
synthetic,original,1000,full_success,lalm,bounded_rag,mean,150,150,0.24800000000000003,0.1706666666666667,0.32666666666666666,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,correct_tool,lalm,lexical_only,7,150,150,-0.07333333333333333,-0.12666666666666668,-0.02666666666666667,0.008399160083991601,
synthetic,original,5000,correct_tool,lalm,lexical_only,13,150,150,-0.5533333333333333,-0.6333333333333333,-0.47333333333333333,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,lexical_only,23,150,150,-0.006666666666666667,-0.03333333333333333,0.02,1.0,
synthetic,original,5000,correct_tool,lalm,lexical_only,37,150,150,-0.1,-0.15333333333333332,-0.04666666666666667,0.00029997000299970003,
synthetic,original,5000,correct_tool,lalm,lexical_only,41,150,150,-0.15333333333333332,-0.22,-0.09333333333333334,0.00019998000199980003,
synthetic,original,5000,correct_tool,lalm,lexical_only,mean,150,150,-0.17733333333333334,-0.2173333333333333,-0.13866666666666666,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,exact_arguments,lalm,lexical_only,7,150,150,0.03333333333333333,-0.02,0.08666666666666667,0.36296370362963704,
synthetic,original,5000,exact_arguments,lalm,lexical_only,13,150,150,-0.3466666666666667,-0.43333333333333335,-0.26666666666666666,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,lexical_only,23,150,150,-0.06,-0.13333333333333333,0.013333333333333334,0.1421857814218578,
synthetic,original,5000,exact_arguments,lalm,lexical_only,37,150,150,-0.16666666666666666,-0.26666666666666666,-0.06666666666666667,0.0024997500249975004,
synthetic,original,5000,exact_arguments,lalm,lexical_only,41,150,150,-0.08666666666666667,-0.16,-0.013333333333333334,0.029997000299970003,
synthetic,original,5000,exact_arguments,lalm,lexical_only,mean,150,150,-0.12533333333333332,-0.17866666666666664,-0.06933333333333334,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,full_success,lalm,lexical_only,7,150,150,0.02,-0.04666666666666667,0.08666666666666667,0.6863313668633136,
synthetic,original,5000,full_success,lalm,lexical_only,13,150,150,-0.48,-0.5666666666666667,-0.39983333333333576,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,lexical_only,23,150,150,-0.04666666666666667,-0.12,0.02666666666666667,0.28927107289271076,
synthetic,original,5000,full_success,lalm,lexical_only,37,150,150,-0.19333333333333333,-0.29333333333333333,-0.09333333333333334,0.0005999400059994001,
synthetic,original,5000,full_success,lalm,lexical_only,41,150,150,-0.13333333333333333,-0.21333333333333335,-0.05333333333333334,0.0031996800319968005,
synthetic,original,5000,full_success,lalm,lexical_only,mean,150,150,-0.16666666666666663,-0.2266666666666667,-0.10400000000000001,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,correct_tool,lalm,rag,7,150,150,-0.09333333333333334,-0.14666666666666667,-0.04666666666666667,0.00039996000399960006,
synthetic,original,5000,correct_tool,lalm,rag,13,150,150,-0.5733333333333334,-0.6533333333333333,-0.49333333333333335,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag,23,150,150,-0.02666666666666667,-0.06,0.0,0.21847815218478153,
synthetic,original,5000,correct_tool,lalm,rag,37,150,150,-0.12,-0.18,-0.06666666666666667,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag,41,150,150,-0.17333333333333334,-0.24,-0.11333333333333333,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag,mean,150,150,-0.1973333333333333,-0.23866666666666664,-0.15866666666666665,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,exact_arguments,lalm,rag,7,150,150,0.16666666666666666,0.08,0.25333333333333335,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,rag,13,150,150,-0.21333333333333335,-0.3,-0.13333333333333333,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,rag,23,150,150,0.07333333333333333,-0.013333333333333334,0.16,0.1327867213278672,
synthetic,original,5000,exact_arguments,lalm,rag,37,150,150,-0.03333333333333333,-0.15333333333333332,0.08666666666666667,0.6559344065593441,
synthetic,original,5000,exact_arguments,lalm,rag,41,150,150,0.04666666666666667,-0.04,0.13333333333333333,0.35806419358064195,
synthetic,original,5000,exact_arguments,lalm,rag,mean,150,150,0.008000000000000007,-0.06799999999999999,0.08266666666666667,0.8609139086091391,1
synthetic,original,5000,full_success,lalm,rag,7,150,150,0.14666666666666667,0.05333333333333334,0.23333333333333334,0.0027997200279972004,
synthetic,original,5000,full_success,lalm,rag,13,150,150,-0.35333333333333333,-0.44,-0.26666666666666666,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,rag,23,150,150,0.08,-0.006666666666666667,0.16666666666666666,0.10258974102589741,
synthetic,original,5000,full_success,lalm,rag,37,150,150,-0.06666666666666667,-0.18666666666666668,0.05333333333333334,0.34526547345265474,
synthetic,original,5000,full_success,lalm,rag,41,150,150,-0.006666666666666667,-0.10666666666666667,0.08666666666666667,1.0,
synthetic,original,5000,full_success,lalm,rag,mean,150,150,-0.04,-0.12133333333333335,0.040000000000000015,0.35596440355964404,1
synthetic,original,5000,correct_tool,lalm,rag_timestamp,7,150,150,-0.1,-0.15333333333333332,-0.05333333333333334,0.00019998000199980003,
synthetic,original,5000,correct_tool,lalm,rag_timestamp,13,150,150,-0.58,-0.66,-0.5,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag_timestamp,23,150,150,-0.03333333333333333,-0.06666666666666667,-0.006666666666666667,0.0638936106389361,
synthetic,original,5000,correct_tool,lalm,rag_timestamp,37,150,150,-0.12666666666666668,-0.18,-0.07333333333333333,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag_timestamp,41,150,150,-0.18,-0.24666666666666667,-0.12,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,rag_timestamp,mean,150,150,-0.204,-0.2426666666666667,-0.16799999999999998,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,7,150,150,0.08,0.006666666666666667,0.15333333333333332,0.056394360563943605,
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,13,150,150,-0.3,-0.38666666666666666,-0.21333333333333335,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,23,150,150,-0.013333333333333334,-0.08666666666666667,0.06,0.8546145385461453,
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,37,150,150,-0.12,-0.22666666666666666,-0.013333333333333334,0.0418958104189581,
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,41,150,150,-0.04,-0.1,0.02,0.28677132286771323,
synthetic,original,5000,exact_arguments,lalm,rag_timestamp,mean,150,150,-0.07866666666666666,-0.14133333333333334,-0.017333333333333333,0.016698330166983303,0.0674932506749325
synthetic,original,5000,full_success,lalm,rag_timestamp,7,150,150,0.05333333333333334,-0.02666666666666667,0.13333333333333333,0.25847415258474155,
synthetic,original,5000,full_success,lalm,rag_timestamp,13,150,150,-0.44666666666666666,-0.54,-0.35333333333333333,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,rag_timestamp,23,150,150,-0.013333333333333334,-0.08666666666666667,0.06,0.8546145385461453,
synthetic,original,5000,full_success,lalm,rag_timestamp,37,150,150,-0.16,-0.26666666666666666,-0.04666666666666667,0.007899210078992101,
synthetic,original,5000,full_success,lalm,rag_timestamp,41,150,150,-0.1,-0.17333333333333334,-0.02666666666666667,0.011898810118988102,
synthetic,original,5000,full_success,lalm,rag_timestamp,mean,150,150,-0.13333333333333333,-0.2,-0.06666666666666667,0.00019998000199980003,0.0047995200479952005
synthetic,original,5000,correct_tool,lalm,bounded_rag,7,150,150,0.02,-0.05333333333333334,0.09333333333333334,0.7206279372062794,
synthetic,original,5000,correct_tool,lalm,bounded_rag,13,150,150,-0.46,-0.5533333333333333,-0.36666666666666664,9.999000099990002e-05,
synthetic,original,5000,correct_tool,lalm,bounded_rag,23,150,150,0.08666666666666667,0.02666666666666667,0.14666666666666667,0.006299370062993701,
synthetic,original,5000,correct_tool,lalm,bounded_rag,37,150,150,-0.006666666666666667,-0.08,0.06666666666666667,1.0,
synthetic,original,5000,correct_tool,lalm,bounded_rag,41,150,150,-0.06,-0.14666666666666667,0.02666666666666667,0.21377862213778623,
synthetic,original,5000,correct_tool,lalm,bounded_rag,mean,150,150,-0.084,-0.14799999999999996,-0.017333333333333333,0.013498650134986502,0.0674932506749325
synthetic,original,5000,exact_arguments,lalm,bounded_rag,7,150,150,0.7666666666666667,0.7,0.8333333333333334,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,bounded_rag,13,150,150,0.38666666666666666,0.30666666666666664,0.4666666666666667,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,bounded_rag,23,150,150,0.6733333333333333,0.5933333333333334,0.7466666666666667,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,bounded_rag,37,150,150,0.5666666666666667,0.48,0.6533333333333333,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,bounded_rag,41,150,150,0.6466666666666666,0.5666666666666667,0.72,9.999000099990002e-05,
synthetic,original,5000,exact_arguments,lalm,bounded_rag,mean,150,150,0.6079999999999999,0.5519999999999999,0.6613333333333332,9.999000099990002e-05,0.0047995200479952005
synthetic,original,5000,full_success,lalm,bounded_rag,7,150,150,0.74,0.6666666666666666,0.8066666666666666,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,bounded_rag,13,150,150,0.24,0.17333333333333334,0.30666666666666664,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,bounded_rag,23,150,150,0.6733333333333333,0.5933333333333334,0.7466666666666667,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,bounded_rag,37,150,150,0.5266666666666666,0.44,0.6133333333333333,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,bounded_rag,41,150,150,0.5866666666666667,0.5066666666666667,0.6666666666666666,9.999000099990002e-05,
synthetic,original,5000,full_success,lalm,bounded_rag,mean,150,150,0.5533333333333333,0.49866666666666676,0.6053666666666663,9.999000099990002e-05,0.0047995200479952005

```

## Prediction/config files

```csv
job,config,predictions,training_seed,evaluation_seed
0050f35561cd,results\additional_study\agent_tasks\jobs\0050f35561cd\config.yaml,results\additional_study\agent_tasks\jobs\0050f35561cd\runs\20261008T152849Z\20261008T152851Z_agent_tasks\predictions.jsonl,7,13
01b9e6f2a071,results\additional_study\agent_tasks\jobs\01b9e6f2a071\config.yaml,results\additional_study\agent_tasks\jobs\01b9e6f2a071\runs\20261008T135044Z\20261008T135045Z_agent_tasks\predictions.jsonl,23,17
029020365465,results\additional_study\agent_tasks\jobs\029020365465\config.yaml,results\additional_study\agent_tasks\jobs\029020365465\runs\20261008T160251Z\20261008T160252Z_agent_tasks\predictions.jsonl,7,13
02f9adedb913,results\additional_study\agent_tasks\jobs\02f9adedb913\config.yaml,results\additional_study\agent_tasks\jobs\02f9adedb913\runs\20261008T172011Z\20261008T172013Z_agent_tasks\predictions.jsonl,37,17
11327eb9777b,results\additional_study\agent_tasks\jobs\11327eb9777b\config.yaml,results\additional_study\agent_tasks\jobs\11327eb9777b\runs\20261008T164816Z\20261008T164817Z_agent_tasks\predictions.jsonl,23,13
1f735e8d74d8,results\additional_study\agent_tasks\jobs\1f735e8d74d8\config.yaml,results\additional_study\agent_tasks\jobs\1f735e8d74d8\runs\20261008T125030Z\20261008T125032Z_agent_tasks\predictions.jsonl,7,11
393138839f84,results\additional_study\agent_tasks\jobs\393138839f84\config.yaml,results\additional_study\agent_tasks\jobs\393138839f84\runs\20261008T151541Z\20261008T151542Z_agent_tasks\predictions.jsonl,7,11
3b8e5b905e29,results\additional_study\agent_tasks\jobs\3b8e5b905e29\config.yaml,results\additional_study\agent_tasks\jobs\3b8e5b905e29\runs\20261008T170327Z\20261008T170329Z_agent_tasks\predictions.jsonl,37,11
4e481a661660,results\additional_study\agent_tasks\jobs\4e481a661660\config.yaml,results\additional_study\agent_tasks\jobs\4e481a661660\runs\20261008T131357Z\20261008T131358Z_agent_tasks\predictions.jsonl,13,11
5e3d610f1dba,results\additional_study\agent_tasks\jobs\5e3d610f1dba\config.yaml,results\additional_study\agent_tasks\jobs\5e3d610f1dba\runs\20261008T122450Z\20261008T122452Z_agent_tasks\predictions.jsonl,7,13
6049fb88941b,results\additional_study\agent_tasks\jobs\6049fb88941b\config.yaml,results\additional_study\agent_tasks\jobs\6049fb88941b\runs\20261008T172831Z\20261008T172832Z_agent_tasks\predictions.jsonl,41,11
60a132831401,results\additional_study\agent_tasks\jobs\60a132831401\config.yaml,results\additional_study\agent_tasks\jobs\60a132831401\runs\20261008T125818Z\20261008T125820Z_agent_tasks\predictions.jsonl,7,13
66a9fbf2a904,results\additional_study\agent_tasks\jobs\66a9fbf2a904\config.yaml,results\additional_study\agent_tasks\jobs\66a9fbf2a904\runs\20261008T161042Z\20261008T161044Z_agent_tasks\predictions.jsonl,7,17
7472d608c607,results\additional_study\agent_tasks\jobs\7472d608c607\config.yaml,results\additional_study\agent_tasks\jobs\7472d608c607\runs\20261008T150746Z\20261008T150747Z_agent_tasks\predictions.jsonl,41,17
75c3b05a0c9c,results\additional_study\agent_tasks\jobs\75c3b05a0c9c\config.yaml,results\additional_study\agent_tasks\jobs\75c3b05a0c9c\runs\20261008T133545Z\20261008T133546Z_agent_tasks\predictions.jsonl,23,11
76a79d16a9bc,results\additional_study\agent_tasks\jobs\76a79d16a9bc\config.yaml,results\additional_study\agent_tasks\jobs\76a79d16a9bc\runs\20261008T132825Z\20261008T132826Z_agent_tasks\predictions.jsonl,13,17
8c11dabe52fe,results\additional_study\agent_tasks\jobs\8c11dabe52fe\config.yaml,results\additional_study\agent_tasks\jobs\8c11dabe52fe\runs\20261008T154155Z\20261008T154157Z_agent_tasks\predictions.jsonl,7,17
93c49740cbfd,results\additional_study\agent_tasks\jobs\93c49740cbfd\config.yaml,results\additional_study\agent_tasks\jobs\93c49740cbfd\runs\20261008T174429Z\20261008T174431Z_agent_tasks\predictions.jsonl,41,17
9f26304e1965,results\additional_study\agent_tasks\jobs\9f26304e1965\config.yaml,results\additional_study\agent_tasks\jobs\9f26304e1965\runs\20261008T155500Z\20261008T155502Z_agent_tasks\predictions.jsonl,7,11
aac108d1010e,results\additional_study\agent_tasks\jobs\aac108d1010e\config.yaml,results\additional_study\agent_tasks\jobs\aac108d1010e\runs\20261008T123745Z\20261008T123747Z_agent_tasks\predictions.jsonl,7,17
ab03e1a22567,results\additional_study\agent_tasks\jobs\ab03e1a22567\config.yaml,results\additional_study\agent_tasks\jobs\ab03e1a22567\runs\20261008T145956Z\20261008T145958Z_agent_tasks\predictions.jsonl,41,13
abac327f1021,results\additional_study\agent_tasks\jobs\abac327f1021\config.yaml,results\additional_study\agent_tasks\jobs\abac327f1021\runs\20261008T161832Z\20261008T161833Z_agent_tasks\predictions.jsonl,13,11
b231c9c87925,results\additional_study\agent_tasks\jobs\b231c9c87925\config.yaml,results\additional_study\agent_tasks\jobs\b231c9c87925\runs\20261008T144359Z\20261008T144401Z_agent_tasks\predictions.jsonl,37,17
bae04ce23358,results\additional_study\agent_tasks\jobs\bae04ce23358\config.yaml,results\additional_study\agent_tasks\jobs\bae04ce23358\runs\20261008T162553Z\20261008T162554Z_agent_tasks\predictions.jsonl,13,13
be988411aaac,results\additional_study\agent_tasks\jobs\be988411aaac\config.yaml,results\additional_study\agent_tasks\jobs\be988411aaac\runs\20261008T165549Z\20261008T165551Z_agent_tasks\predictions.jsonl,23,17
c2c349f0dddf,results\additional_study\agent_tasks\jobs\c2c349f0dddf\config.yaml,results\additional_study\agent_tasks\jobs\c2c349f0dddf\runs\20261008T121159Z\20261008T121200Z_agent_tasks\predictions.jsonl,7,11
cc60c1b8d156,results\additional_study\agent_tasks\jobs\cc60c1b8d156\config.yaml,results\additional_study\agent_tasks\jobs\cc60c1b8d156\runs\20261008T163317Z\20261008T163318Z_agent_tasks\predictions.jsonl,13,17
ce5edf8f6da4,results\additional_study\agent_tasks\jobs\ce5edf8f6da4\config.yaml,results\additional_study\agent_tasks\jobs\ce5edf8f6da4\runs\20261008T171153Z\20261008T171155Z_agent_tasks\predictions.jsonl,37,13
d18f8163889b,results\additional_study\agent_tasks\jobs\d18f8163889b\config.yaml,results\additional_study\agent_tasks\jobs\d18f8163889b\runs\20261008T164041Z\20261008T164043Z_agent_tasks\predictions.jsonl,23,11
e6117b920b77,results\additional_study\agent_tasks\jobs\e6117b920b77\config.yaml,results\additional_study\agent_tasks\jobs\e6117b920b77\runs\20261008T132109Z\20261008T132110Z_agent_tasks\predictions.jsonl,13,13
e65ef7bbe315,results\additional_study\agent_tasks\jobs\e65ef7bbe315\config.yaml,results\additional_study\agent_tasks\jobs\e65ef7bbe315\runs\20261008T173629Z\20261008T173631Z_agent_tasks\predictions.jsonl,41,13
e7beb4b74ca2,results\additional_study\agent_tasks\jobs\e7beb4b74ca2\config.yaml,results\additional_study\agent_tasks\jobs\e7beb4b74ca2\runs\20261008T145206Z\20261008T145208Z_agent_tasks\predictions.jsonl,41,11
eb3fba979717,results\additional_study\agent_tasks\jobs\eb3fba979717\config.yaml,results\additional_study\agent_tasks\jobs\eb3fba979717\runs\20261008T130606Z\20261008T130608Z_agent_tasks\predictions.jsonl,7,17
ecad66a9183a,results\additional_study\agent_tasks\jobs\ecad66a9183a\config.yaml,results\additional_study\agent_tasks\jobs\ecad66a9183a\runs\20261008T140627Z\20261008T140628Z_agent_tasks\predictions.jsonl,37,13
f7bd1deed95c,results\additional_study\agent_tasks\jobs\f7bd1deed95c\config.yaml,results\additional_study\agent_tasks\jobs\f7bd1deed95c\runs\20261008T135813Z\20261008T135814Z_agent_tasks\predictions.jsonl,37,11
ff43ced77b74,results\additional_study\agent_tasks\jobs\ff43ced77b74\config.yaml,results\additional_study\agent_tasks\jobs\ff43ced77b74\runs\20261008T134309Z\20261008T134311Z_agent_tasks\predictions.jsonl,23,13

```
