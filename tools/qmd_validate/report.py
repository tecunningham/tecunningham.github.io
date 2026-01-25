from __future__ import annotations

from typing import Any, Iterable

from .core import TestResult


def overall_ok(results: Iterable[TestResult]) -> bool:
    ok = True
    for r in results:
        if r.ok is False:
            ok = False
    return ok


def render_text(results: list[TestResult], title: str = "Validation Checks") -> str:
    lines: list[str] = [title]
    for r in results:
        detail = r.detail or ""
        if detail and not detail.startswith(" "):
            detail = " " + detail
        lines.append(f"{r.symbol()} {r.category}: {r.name}{detail}")
    return "\n".join(lines)


def render_json(results: list[TestResult]) -> dict[str, Any]:
    return {
        "overall_ok": overall_ok(results),
        "items": [
            {
                "name": r.name,
                "category": r.category,
                "ok": r.ok,
                "skipped": r.skipped,
                "detail": r.detail,
                "meta": r.meta,
            }
            for r in results
        ],
    }

