# Evaluation Metrics Summary

This report was generated from `results/evaluation-results.csv`.

## General Results

- Total tests: **20**
- Quality tests: **10**
- Red-team tests: **10**
- Passed tests: **20** (100%)
- Failed tests: **0** (0%)
- Safety PASS: **20** (100%)
- Safety FAIL: **0** (0%)

## Average Scores by Dimension

| Dimension | Average Score |
|---|---:|
| Factual Accuracy | 5.00 |
| Instruction Following | 4.95 |
| Relevance | 5.00 |
| Clarity | 4.95 |
| Hallucination | 5.00 |
| PT-BR Localization | 5.00 |

## Severity Distribution

| Severity | Count |
|---|---:|
| None | 18 |
| Low | 2 |
| Medium | 0 |
| High | 0 |
| Critical | 0 |

## Initial Findings

The first evaluation pass did not identify major failures. Most responses met the expected behavior defined in the test cases, including instruction-following, factual accuracy, localization and safety behavior.

Two low-severity issues were documented where the response was usable but could be slightly more concise or better formatted.

## Notes

These metrics are intended to support human evaluation, not replace it. The evaluator notes and qualitative findings should still be reviewed to understand why each test passed or failed.
