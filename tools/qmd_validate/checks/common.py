from __future__ import annotations

import re

from ..core import TestResult, ValidationContext


def required_substrings(name: str, needles: list[str], category: str = "programmatic"):
    def _check(ctx: ValidationContext) -> TestResult:
        missing = [n for n in needles if n not in ctx.qmd_text]
        ok = not missing
        detail = ""
        if missing:
            detail = f"(missing: {missing[:5]}{' ...' if len(missing) > 5 else ''})"
        return TestResult(name=name, ok=ok, category=category, detail=detail, meta={"missing": missing})

    return _check


def required_headings(headings: list[str]):
    return required_substrings(
        name=f"required sections present ({len(headings)}/{len(headings)})",
        needles=headings,
        category="programmatic",
    )


def regex_present(name: str, pattern: str, category: str = "programmatic"):
    rx = re.compile(pattern, re.MULTILINE)

    def _check(ctx: ValidationContext) -> TestResult:
        ok = rx.search(ctx.qmd_text) is not None
        return TestResult(name=name, ok=ok, category=category, detail=f"(pattern: {pattern})" if not ok else "")

    return _check

