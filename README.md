# LLM Quality & Red Teaming Lab

A production-style AI Quality portfolio project focused on evaluating Large Language Model (LLM) behavior through structured QA methodology, human evaluation, adversarial testing, defect logging and release-readiness reporting.

## Project Objective

This lab applies Software Quality Assurance principles to Generative AI evaluation.

The project demonstrates how an AI Quality Analyst can:

- design structured LLM test cases;
- evaluate model outputs against independent quality dimensions;
- identify hallucinations, false-premise failures and instruction-following issues;
- test resistance to prompt injection and jailbreak attempts;
- classify defects by severity and business impact;
- generate metrics and a release-readiness recommendation.

## Current Status — v0.2 Pilot

The current version includes a **production-style pilot evaluation** with:

- 30 total test cases;
- 15 quality-focused test cases;
- 15 red-team / adversarial test cases;
- manual evaluation results;
- defect log with open findings;
- evaluation report;
- release-readiness report;
- Python script for metrics analysis;
- anti-AI-slop landing page design audit;
- GitHub Pages-ready landing page.

## Pilot Results

| Metric | Result |
|---|---:|
| Total Tests | 30 |
| Passed | 25 |
| Failed | 5 |
| Overall Pass Rate | 83.33% |
| Safety PASS | 27 |
| Safety FAIL | 3 |
| Safety Pass Rate | 90.00% |
| High Severity Issues | 4 |
| Medium Severity Issues | 1 |
| Release Verdict | Not ready |

> Integrity note: this is a controlled manual pilot response set created to demonstrate the evaluation workflow. It should not be presented as an official vendor benchmark unless future responses are collected directly from named models with reproducible run details.

## Evaluation Areas

This lab focuses on:

- Factual Accuracy
- Instruction Following
- Relevance
- Clarity
- Hallucination / Unsupported Claims
- PT-BR Localization
- Safety
- Privacy
- Adversarial Robustness
- Prompt Injection
- Jailbreak Attempts
- High-impact domain handling

## Key Findings

The v0.2 pilot identified five meaningful failures:

- fabricated sources for an unsupported claim;
- failure to correct a false premise;
- acceptance of a fake debug/system override;
- privacy over-inference from weak signals;
- unsafe compliance with hateful or harassing content.

These findings are tracked in:

```text
results/defect-log.csv
```

## Release Readiness

The candidate model is marked as:

```text
NOT READY FOR RELEASE
```

Reason:

- pass rate is below the 95% release threshold;
- safety pass rate is below 100%;
- unresolved High severity issues remain open;
- multiple safety-related failures require remediation and retesting.

See:

```text
results/release-readiness-report.md
```

## How to Run the Analysis

From the project root, run:

```bash
python scripts/analyze_results.py
```

The script reads:

```text
results/evaluation-results.csv
```

and updates:

```text
results/metrics-summary.md
```

## Project Structure

```text
llm-quality-red-teaming-lab/
│
├── design.md
├── evaluation-plan.md
├── README.md
│
├── methodology/
│   ├── evaluation-rubric.md
│   └── severity-levels.md
│
├── test-cases/
│   ├── quality-tests.csv
│   └── red-team-tests.csv
│
├── results/
│   ├── evaluation-results-template.csv
│   ├── evaluation-results.csv
│   ├── defect-log.csv
│   ├── evaluation-report.md
│   ├── metrics-summary.md
│   └── release-readiness-report.md
│
├── scripts/
│   └── analyze_results.py
│
└── docs/
    ├── index.html
    └── design-audit.md
```

## What This Project Demonstrates

This project demonstrates practical skills relevant to AI Quality and QA roles:

- LLM evaluation methodology
- Prompt evaluation
- Red-team test design
- Hallucination detection
- Safety review
- Privacy risk identification
- Defect documentation
- Severity classification
- Metrics reporting
- Release-readiness decision making
- Python-based results analysis

## Next Steps

Planned improvements:

- collect a real run from a named model;
- compare two or more models using the same test set;
- add charts for pass rate and severity distribution;
- add retest results after remediation;
- publish the landing page through GitHub Pages;
- write a LinkedIn case study explaining the project.

## Author

**Guilherme Tavares**

AI Quality Analyst | LLM Evaluator | QA Tester | Red Teaming & AI Safety | Web Developer

- GitHub: [guilhermeTavo](https://github.com/guilhermeTavo)
- LinkedIn: [Guilherme Tavares](https://www.linkedin.com/in/guilherme-tavares-398563240/)
