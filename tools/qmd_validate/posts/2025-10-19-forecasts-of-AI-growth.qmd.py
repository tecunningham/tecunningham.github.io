from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tools.qmd_validate.checks import bib
from tools.qmd_validate.core import TestResult, ValidationContext


def _symbol_to_ok(symbol: str) -> tuple[bool | None, str]:
    symbol = (symbol or "").strip()
    if symbol == "✅":
        return True, ""
    if symbol == "❌":
        return False, ""
    if symbol == "⚠️":
        return True, "(warning)"
    if symbol == "⏳":
        return None, "(skipped)"
    return None, f"(unknown status {symbol!r})"


def _run_forecasts_test(ctx: ValidationContext) -> TestResult:
    script = ctx.repo_root / "tools/forecasts_test.py"
    if not script.exists():
        return TestResult(name="forecasts_test.py runs", ok=False, detail=f"(missing: {script})")

    proc = subprocess.run(
        [sys.executable, str(script), "--qmd", str(ctx.qmd_path), "--bib", str(ctx.bib_path), "--json"],
        capture_output=True,
        text=True,
        cwd=str(ctx.repo_root),
    )
    if proc.returncode != 0:
        snippet = (proc.stderr or proc.stdout or "").strip()[:400]
        return TestResult(name="forecasts_test.py runs", ok=False, detail=f"(exit {proc.returncode}: {snippet})")
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return TestResult(name="forecasts_test.py runs", ok=False, detail=f"(bad JSON: {exc})")

    status = payload.get("status", {})
    overall = status.get("overall", "")
    ok = "Fail" not in str(overall)
    return TestResult(
        name="forecasts checklist overall",
        ok=ok,
        detail=f"({overall})" if overall else "",
        meta={"status": status, "counts": payload.get("counts", {})},
    )


def _forecasts_subchecks(ctx: ValidationContext) -> list[TestResult]:
    script = ctx.repo_root / "tools/forecasts_test.py"
    proc = subprocess.run(
        [sys.executable, str(script), "--qmd", str(ctx.qmd_path), "--bib", str(ctx.bib_path), "--json"],
        capture_output=True,
        text=True,
        cwd=str(ctx.repo_root),
    )
    if proc.returncode != 0:
        return []
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return []

    status = payload.get("status", {})
    counts = payload.get("counts", {})

    hard_fail_keys = {"citations", "tables", "quotes_match", "growth_match"}
    items: list[TestResult] = []
    for key, label in [
        ("citations", "Cited sources exist in posts/ai.bib"),
        ("tables", "Table rows have required fields"),
        ("quotes_match", "QMD quotes match posts/ai.bib"),
        ("growth_match", "QMD growth values match posts/ai.bib"),
        ("abstracts", "Abstracts present for all cited sources"),
        ("quotes_verified", "Bib quotes appear in local source fulltext"),
    ]:
        ok, suffix = _symbol_to_ok(status.get(key, ""))
        # Align with forecasts_test: only a subset of checks are treated as
        # hard failures; others should surface as warnings.
        if key not in hard_fail_keys and ok is False:
            ok = True
            suffix = "(warning)"
        detail = suffix
        if key in counts:
            passed, total = counts[key]
            detail = f"({passed}/{total}){(' ' + suffix) if suffix else ''}".strip()
        items.append(TestResult(name=label, ok=ok, category="programmatic", detail=detail))
    return items


def post_checks():
    # Keep using the existing forecasts-specific script for now, but wrap its
    # outputs into the shared reporting format.
    def _subchecks(ctx: ValidationContext) -> TestResult:
        items = _forecasts_subchecks(ctx)
        ok = all(i.ok is not False for i in items) and bool(items)
        return TestResult(name="forecasts checks (subtests)", ok=ok, meta={"subtests": [i.__dict__ for i in items]})

    return [
        _run_forecasts_test,
        _subchecks,
        bib.ai_bib_conventions(),
        bib.citekeys_resolve(),
    ]
