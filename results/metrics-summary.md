# Evaluation Metrics Summary

This report summarizes the current **v0.2 production-style pilot evaluation** using `results/evaluation-results.csv`.

## General Results

| Metric | Result |
|---|---:|
| Total tests | 30 |
| Quality tests | 15 |
| Red-team tests | 15 |
| Passed tests | 25 |
| Failed tests | 5 |
| Overall pass rate | 83.33% |
| Safety PASS | 27 |
| Safety FAIL | 3 |
| Safety pass rate | 90.00% |

## Average Scores by Dimension

| Dimension | Average Score |
|---|---:|
| Factual Accuracy | 4.40 |
| Instruction Following | 4.43 |
| Relevance | 4.57 |
| Clarity | 4.70 |
| Hallucination / Unsupported Claims | 4.47 |
| PT-BR Localization | 5.00 |

## Severity Distribution

| Severity | Count |
|---|---:|
| Critical | 0 |
| High | 4 |
| Medium | 1 |
| Low | 0 |
| None | 25 |

## Key Findings

The pilot identified five meaningful failures:

- Fabricated sources and unsupported biographical claims.
- Failure to correct a false premise about Brazil's capital.
- Acceptance of a fake debug/system override.
- Privacy over-inference from limited user data.
- Unsafe compliance with hateful or harassing content.

## Release Signal

The model is **not release-ready** under the defined exit criteria because the run contains unresolved High severity findings and Safety FAIL cases.

## Notes

These metrics support human evaluation and should be reviewed together with `results/defect-log.csv` and `results/release-readiness-report.md`.
