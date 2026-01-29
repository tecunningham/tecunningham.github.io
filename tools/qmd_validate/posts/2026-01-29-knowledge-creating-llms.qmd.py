from __future__ import annotations

import re

from tools.qmd_validate.checks import bib
from tools.qmd_validate.core import TestResult, ValidationContext
from tools.qmd_validate.util import read_text


def _extract_top_level_section(qmd_text: str, header_re: re.Pattern[str]) -> str | None:
    lines = qmd_text.splitlines(keepends=True)
    start_idx: int | None = None
    for i, line in enumerate(lines):
        if header_re.match(line):
            start_idx = i
            break
    if start_idx is None:
        return None

    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if re.match(r"^#\s+", lines[i]):
            end_idx = i
            break

    return "".join(lines[start_idx:end_idx])


def _lit_review_reference_count() -> callable:
    header_re = re.compile(r"^#\s+Literature Review: Economic Models\s*$")

    def _check(ctx: ValidationContext) -> TestResult:
        section = _extract_top_level_section(ctx.qmd_text, header_re)
        if section is None:
            return TestResult(name="literature review section present", ok=False, detail="(missing header)")

        citekeys = bib.extract_citekeys(section)
        n = len(citekeys)
        ok = 5 <= n <= 15
        detail = f"({n} citekeys)" + ("" if ok else " (expected 5-15)")
        return TestResult(
            name="literature review has 5-15 references",
            ok=ok,
            detail=detail,
            meta={"citekeys": sorted(citekeys)},
        )

    return _check


def _lit_review_quotes_match_bib() -> callable:
    header_re = re.compile(r"^#\s+Literature Review: Economic Models\s*$")

    def _check(ctx: ValidationContext) -> TestResult:
        section = _extract_top_level_section(ctx.qmd_text, header_re)
        if section is None:
            return TestResult(name="literature review quotes match posts/ai.bib", ok=False, detail="(missing header)")

        citekeys = bib.extract_citekeys(section)
        if not citekeys:
            return TestResult(name="literature review quotes match posts/ai.bib", ok=False, detail="(no citekeys found)")

        ai_bib_tests = bib._load_ai_bib_tests_module(ctx.bib_tests_path)
        bib_text = read_text(ctx.bib_path)
        entries, parse_errors = ai_bib_tests.parse_entries(bib_text.splitlines())
        if parse_errors:
            return TestResult(
                name="literature review quotes match posts/ai.bib",
                ok=False,
                detail=f"(ai.bib parse errors: {parse_errors[:3]}{' ...' if len(parse_errors) > 3 else ''})",
            )

        by_key = {entry.key: entry for entry in entries}
        missing_quotes: list[str] = []
        mismatched_quotes: list[str] = []
        for key in sorted(citekeys):
            entry = by_key.get(key)
            if entry is None:
                continue
            quote = (entry.fields.get("quote") or "").strip()
            if not quote:
                missing_quotes.append(key)
                continue
            if quote not in section:
                mismatched_quotes.append(key)

        ok = not missing_quotes and not mismatched_quotes
        detail_parts: list[str] = []
        if missing_quotes:
            detail_parts.append(f"missing quote: {missing_quotes[:6]}{' ...' if len(missing_quotes) > 6 else ''}")
        if mismatched_quotes:
            detail_parts.append(f"quote not found in QMD: {mismatched_quotes[:6]}{' ...' if len(mismatched_quotes) > 6 else ''}")
        detail = f"({len(citekeys)} citekeys)" + (f" ({'; '.join(detail_parts)})" if detail_parts else "")

        return TestResult(
            name="literature review quotes match posts/ai.bib",
            ok=ok,
            detail=detail,
            meta={"missing_quotes": missing_quotes, "mismatched_quotes": mismatched_quotes, "citekeys": sorted(citekeys)},
        )

    return _check


def post_checks():
    return [
        _lit_review_reference_count(),
        _lit_review_quotes_match_bib(),
        bib.citekeys_resolve(),
    ]

