# Interview Guide — LLM Quality & Red Teaming Lab

This guide helps explain the project in interviews for AI Quality, LLM Evaluation, AI Safety and QA roles.

## 30-second explanation

I built an AI Quality portfolio project that simulates a real LLM evaluation workflow. I created a test plan, evaluation rubric, 30 test cases, red-team prompts, manual evaluation results, a defect log and a release-readiness report. The pilot run found 5 failures, including 3 safety failures, so the evaluated model was blocked for release.

## 2-minute explanation

The goal of the project was to show how QA methodology can be applied to AI-generated outputs.

Instead of judging responses vaguely, I defined independent evaluation dimensions such as factual accuracy, instruction following, relevance, clarity, hallucination risk, PT-BR localization, safety and privacy.

I then created 30 test cases split between normal quality scenarios and adversarial red-team scenarios. For each model response, I recorded the result, scored the output, classified the severity and documented defects when the behavior failed the expected standard.

The pilot run produced 25 passes and 5 failures. Because there were unresolved high-severity issues and 3 safety failures, the release-readiness recommendation was to block the candidate model from release.

## Best interview framing

Use this project to show that you understand:

- how to design structured LLM test cases;
- how to evaluate outputs beyond surface-level quality;
- how to detect hallucinations and false-premise failures;
- how to test prompt injection, jailbreak and unsafe compliance;
- how to document defects with severity and remediation;
- how to make a release recommendation based on evidence.

## STAR answer example

**Situation:** I wanted to build a portfolio project aligned with AI Quality and LLM Evaluation roles.

**Task:** I needed to demonstrate a realistic evaluation workflow, not just a simple prompt list.

**Action:** I created a structured evaluation lab with 30 test cases, a scoring rubric, red-team prompts, manual results, a defect log, a release-readiness report and a Python script for metrics.

**Result:** The pilot identified 5 failures, including 3 safety failures and 4 high-severity issues. Based on the release criteria, the candidate model was blocked for release.

## Questions I can answer from this project

### How did you evaluate the model?

I used a rubric with separate dimensions for factual accuracy, instruction following, relevance, clarity, hallucination, PT-BR localization and safety. Each response was compared against expected behavior, then classified as PASS or FAIL with severity.

### Why is the model blocked for release?

The pilot failed the release criteria. The overall pass rate was below 95%, the safety pass rate was not 100%, and high-severity findings remained open.

### What was the most important defect?

The highest-risk findings were safety and reliability failures: accepting fake system authority, fabricating sources for an unsupported claim and complying with unsafe hateful or harassing content.

### What would you improve next?

I would collect fresh responses from named models, compare multiple models using the same test suite, expand the number of cases and add retest results after remediation.

## Resume bullet

Built an LLM Quality & Red Teaming Lab simulating a production-style AI Quality workflow with 30 structured test cases, red-team prompts, evaluation rubrics, defect logging, severity classification, release-readiness reporting and Python-based metrics analysis.

## LinkedIn one-liner

I built a production-style AI Quality portfolio project that evaluates LLM behavior using structured test cases, red-team prompts, defect logging and release-readiness criteria.
