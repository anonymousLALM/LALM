# Supplementary Archive: Simulated Agent Tool Tasks

This supplementary archive preserves the experimental configurations, runner scripts, analysis utilities, and complete evaluation outputs for the simulated agent tool-task study. These experiments are exploratory and are not reported in the main AAMAS 2027 manuscript.

## Directory Structure

```text
supplementary/agent_tasks/
├── configs/                  # Tool calling prompt templates and JSON schemas
│   ├── prompt.txt
│   ├── system_prompt.txt
│   └── tool_schemas.json
├── experiments/              # Study execution and reporting scripts
│   ├── report_agent_tasks.py
│   └── run_agent_study.py
├── scripts/                  # Runner script for agent tasks
│   └── run_agent_tasks.py
└── results/                  # Evaluation outputs, job receipts, and significance tests
    ├── jobs/                 # 36 completed evaluation jobs across models and horizons
    ├── artifact_index.csv    # Inventory of all job artifacts and configs
    ├── paired_tests.csv      # 288 paired significance test comparisons
    └── LALM_AGENT_TASKS.md   # Tabulated results for tool selection, arguments, and success
```

## Summary of Findings

The study evaluated tool selection accuracy, argument extraction, and end-to-end task success on synthetic horizons (1,000 and 5,000 turns) comparing LALM against Lexical-only, RAG, and Bounded-RAG baselines. Detailed per-condition breakdowns and paired comparisons are available in [`results/LALM_AGENT_TASKS.md`](results/LALM_AGENT_TASKS.md).
