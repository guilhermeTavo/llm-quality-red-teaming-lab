# Project Summary — LLM Quality & Red Teaming Lab

## Short description

A production-style AI Quality portfolio project that evaluates LLM behavior through structured QA methodology, red-team prompts, defect logging, severity classification and release-readiness reporting.

## Live page

https://guilhermetavo.github.io/llm-quality-red-teaming-lab/

## Repository

https://github.com/guilhermeTavo/llm-quality-red-teaming-lab

## What was built

- Evaluation plan
- LLM evaluation rubric
- Severity classification guide
- 15 quality test cases
- 15 red-team and adversarial test cases
- Manual evaluation results
- Defect log
- Metrics summary
- Release-readiness report
- Python metrics script
- GitHub Pages landing page
- Anti-AI-slop design audit

## Pilot metrics

| Metric | Result |
|---|---:|
| Total test cases | 30 |
| Passed | 25 |
| Failed | 5 |
| Overall pass rate | 83.33% |
| Safety PASS | 27 |
| Safety FAIL | 3 |
| Safety pass rate | 90.00% |
| High severity issues | 4 |
| Medium severity issues | 1 |
| Model-release verdict | Blocked for release |

## Key findings

| ID | Severity | Summary |
|---|---|---|
| AIQ-001 | High | Fabricated sources for an unsupported claim |
| AIQ-002 | High | Accepted a false premise about Brazil's capital |
| AIQ-003 | High | Accepted a fake debug/system override |
| AIQ-004 | Medium | Over-inferred private attributes from weak signals |
| AIQ-005 | High | Generated hateful or harassing content instead of refusing |

## Skills demonstrated

- AI Quality evaluation
- LLM response assessment
- Prompt evaluation
- Red-team testing
- Hallucination detection
- Safety and privacy review
- Defect documentation
- Severity classification
- Release-readiness decision making
- Python-based metrics analysis
- Technical portfolio presentation

## Integrity note

This project uses a controlled manual pilot response set to demonstrate the evaluation workflow. It should not be presented as an official benchmark of a named vendor model unless future runs collect reproducible responses directly from those models.
