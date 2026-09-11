# LLM Quality & Red Teaming Lab

A practical portfolio project focused on evaluating Large Language Model (LLM) outputs through structured quality assurance, human evaluation and adversarial testing.

## Project Objective

The goal of this project is to design and execute a systematic process for evaluating LLM responses and identifying quality issues, behavioral inconsistencies, hallucinations, instruction-following failures, safety risks and edge cases.

The project applies traditional Software Quality Assurance principles to Generative AI and LLM evaluation.

## Current Status

The first version of the lab includes:

- Structured LLM evaluation rubric
- Severity classification guide
- 10 quality-focused test cases
- 10 red-team / adversarial test cases
- Sample evaluation results
- Evaluation report
- Python script for basic metrics analysis
- Metrics summary in Markdown
- Editorial landing page in `docs/index.html`
- Design system in `design.md`
- Landing page anti-slop audit in `docs/design-audit.md`

> Note: the current evaluation results are a first manual sample run used to demonstrate the evaluation workflow. Future iterations can compare multiple models and replace sample outputs with fresh model responses.

## Evaluation Areas

This lab focuses on:

- Factual Accuracy
- Instruction Following
- Relevance
- Hallucination Detection
- Clarity
- PT-BR Localization
- Safety
- Adversarial Robustness

## Testing Approach

The evaluation process includes:

- Structured evaluation rubrics
- Manual LLM evaluation
- Functional-style AI testing
- Edge-case testing
- Adversarial prompts
- Prompt injection testing
- Safety testing
- Failure documentation
- Severity classification
- Result analysis

## Metrics Generated

The analysis script calculates:

- Total evaluated test cases
- PASS / FAIL counts
- Overall pass rate
- Safety pass rate
- Average score by evaluation dimension
- Severity distribution

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

## Landing Page

The project includes a static portfolio landing page at:

```text
docs/index.html
```

The page was redesigned using a Hallmark-inspired anti-AI-slop direction. Instead of a generic AI SaaS layout, the page uses an editorial / field-report style focused on methodology, evidence and project credibility.

The design process is documented in:

```text
design.md
docs/design-audit.md
```

## Project Structure

```text
llm-quality-red-teaming-lab/
│
├── design.md
│
├── docs/
│   ├── index.html
│   └── design-audit.md
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
│   ├── evaluation-report.md
│   └── metrics-summary.md
│
├── scripts/
│   └── analyze_results.py
│
└── README.md
```

## What This Project Demonstrates

This project demonstrates the ability to:

- Design structured test cases for LLM evaluation
- Evaluate model responses using independent quality dimensions
- Identify hallucinations, instruction-following failures and unsafe behavior
- Classify issue severity based on user impact
- Document evaluation results in a reproducible format
- Use Python to generate simple quality metrics from evaluation data
- Present technical work through a portfolio-ready project page
- Audit and improve AI-generated design patterns

## Next Steps

Planned improvements:

- Enable GitHub Pages using the `/docs` folder
- Add model comparison results
- Add more PT-BR localization and safety cases
- Add charts for pass rate and severity distribution
- Add a LinkedIn-ready project summary

## Author

**Guilherme Tavares**

AI Quality Analyst | LLM Evaluator | QA Tester | Red Teaming & AI Safety | Web Developer

- GitHub: [guilhermeTavo](https://github.com/guilhermeTavo)
- LinkedIn: [Guilherme Tavares](https://www.linkedin.com/in/guilherme-tavares-398563240/)
