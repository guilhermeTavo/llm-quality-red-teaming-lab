"""
Analyze LLM evaluation results.

This script reads the CSV file generated during manual LLM evaluation and
calculates basic quality metrics such as pass rate, safety pass rate, average
scores by dimension and issue severity distribution.

Usage:
    python scripts/analyze_results.py

Optional:
    python scripts/analyze_results.py --input results/evaluation-results.csv --output results/metrics-summary.md
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path
from statistics import mean
from typing import Iterable


SCORE_COLUMNS = [
    "factual_accuracy",
    "instruction_following",
    "relevance",
    "clarity",
    "hallucination",
    "ptbr_localization",
]


def parse_score(value: str) -> float | None:
    """Convert a score field to float, ignoring blanks and N/A values."""
    value = (value or "").strip()

    if not value or value.upper() == "N/A":
        return None

    try:
        return float(value)
    except ValueError:
        return None


def percentage(part: int, total: int) -> float:
    """Return percentage safely when total may be zero."""
    if total == 0:
        return 0.0
    return round((part / total) * 100, 2)


def load_rows(input_path: Path) -> list[dict[str, str]]:
    """Load evaluation rows from CSV."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with input_path.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def average_scores(rows: Iterable[dict[str, str]]) -> dict[str, float | None]:
    """Calculate average score for each score-based evaluation dimension."""
    rows = list(rows)
    averages: dict[str, float | None] = {}

    for column in SCORE_COLUMNS:
        scores = [parse_score(row.get(column, "")) for row in rows]
        valid_scores = [score for score in scores if score is not None]
        averages[column] = round(mean(valid_scores), 2) if valid_scores else None

    return averages


def build_markdown_report(rows: list[dict[str, str]]) -> str:
    """Build a Markdown report with summary metrics."""
    total_tests = len(rows)

    overall_counter = Counter((row.get("overall_result", "").strip().upper() or "UNKNOWN") for row in rows)
    safety_counter = Counter((row.get("safety_result", "").strip().upper() or "UNKNOWN") for row in rows)
    severity_counter = Counter((row.get("severity", "").strip().title() or "Unknown") for row in rows)

    passed_tests = overall_counter.get("PASS", 0)
    failed_tests = overall_counter.get("FAIL", 0)
    safety_pass = safety_counter.get("PASS", 0)
    safety_fail = safety_counter.get("FAIL", 0)

    averages = average_scores(rows)

    lines = [
        "# Evaluation Metrics Summary",
        "",
        "This report was generated automatically from `results/evaluation-results.csv` using `scripts/analyze_results.py`.",
        "",
        "## General Results",
        "",
        f"- Total tests: **{total_tests}**",
        f"- Passed tests: **{passed_tests}** ({percentage(passed_tests, total_tests)}%)",
        f"- Failed tests: **{failed_tests}** ({percentage(failed_tests, total_tests)}%)",
        f"- Safety PASS: **{safety_pass}** ({percentage(safety_pass, total_tests)}%)",
        f"- Safety FAIL: **{safety_fail}** ({percentage(safety_fail, total_tests)}%)",
        "",
        "## Average Scores by Dimension",
        "",
        "| Dimension | Average Score |",
        "|---|---:|",
    ]

    for dimension, value in averages.items():
        display_name = dimension.replace("_", " ").title()
        display_value = "N/A" if value is None else f"{value:.2f}"
        lines.append(f"| {display_name} | {display_value} |")

    lines.extend([
        "",
        "## Severity Distribution",
        "",
        "| Severity | Count |",
        "|---|---:|",
    ])

    severity_order = ["Critical", "High", "Medium", "Low", "None", "Unknown"]
    listed = set()

    for severity in severity_order:
        if severity in severity_counter:
            lines.append(f"| {severity} | {severity_counter[severity]} |")
            listed.add(severity)

    for severity, count in sorted(severity_counter.items()):
        if severity not in listed:
            lines.append(f"| {severity} | {count} |")

    lines.extend([
        "",
        "## Notes",
        "",
        "These metrics are intended to support human evaluation, not replace it. The evaluator notes and qualitative findings should still be reviewed to understand why each test passed or failed.",
        "",
    ])

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze LLM evaluation CSV results.")
    parser.add_argument(
        "--input",
        default="results/evaluation-results.csv",
        help="Path to the evaluation results CSV file.",
    )
    parser.add_argument(
        "--output",
        default="results/metrics-summary.md",
        help="Path where the Markdown metrics report will be written.",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    rows = load_rows(input_path)
    report = build_markdown_report(rows)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")

    print(report)
    print(f"\nMetrics report written to: {output_path}")


if __name__ == "__main__":
    main()
