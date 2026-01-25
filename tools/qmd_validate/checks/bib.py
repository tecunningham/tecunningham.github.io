from __future__ import annotations

import importlib.util
import re
import sys
from functools import lru_cache
from pathlib import Path

from ..core import TestResult, ValidationContext
from ..util import read_text


def extract_citekeys(text: str) -> set[str]:
    keys = set(re.findall(r"@([A-Za-z0-9][A-Za-z0-9:_-]*)", text))
    # Pandoc/Quarto documents often contain CSS fragments that look like @citekeys.
    # Keep a small ignore list (mirrors the older per-post scripts).
    ignore = {"media", "font-face", "keyframes", "supports"}
    return {k for k in keys if k not in ignore}


@lru_cache(maxsize=8)
def _load_ai_bib_tests_module(path: Path):
    spec = importlib.util.spec_from_file_location("ai_bib_tests", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module spec for {path}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ai_bib_keys(bib_path: Path, bib_tests_path: Path) -> set[str]:
    ai_bib_tests = _load_ai_bib_tests_module(bib_tests_path)
    text = read_text(bib_path)
    entries, parse_errors = ai_bib_tests.parse_entries(text.splitlines())
    if parse_errors:
        raise AssertionError(f"ai.bib parse errors: {parse_errors}")
    return {entry.key for entry in entries}


def citekeys_resolve() -> callable:
    def _check(ctx: ValidationContext) -> TestResult:
        citekeys = extract_citekeys(ctx.qmd_text)
        if not citekeys:
            return TestResult(name=f"citekeys resolve in {ctx.bib_path}", ok=False, detail="(no citekeys found)")
        try:
            keys = ai_bib_keys(ctx.bib_path, ctx.bib_tests_path)
        except Exception as exc:
            return TestResult(name=f"citekeys resolve in {ctx.bib_path}", ok=False, detail=f"(error: {exc})")
        missing = sorted(citekeys - keys)
        ok = not missing
        detail = ""
        if missing:
            detail = f"(missing: {missing[:10]}{' ...' if len(missing) > 10 else ''})"
        return TestResult(
            name=f"citekeys resolve in {ctx.bib_path}",
            ok=ok,
            detail=detail,
            meta={"missing": missing, "citekeys": len(citekeys)},
        )

    return _check


def ai_bib_conventions() -> callable:
    def _check(ctx: ValidationContext) -> TestResult:
        try:
            ai_bib_tests = _load_ai_bib_tests_module(ctx.bib_tests_path)
        except Exception as exc:
            return TestResult(name="bibliography tests", ok=False, detail=f"(error loading ai.bib tests: {exc})")

        try:
            text = read_text(ctx.bib_path)
            entries, parse_errors = ai_bib_tests.parse_entries(text.splitlines())
            results = ai_bib_tests.run_tests(entries)
            bibclean_result = ai_bib_tests.run_bibclean(ctx.bib_path)
            if bibclean_result is not None:
                results.append(bibclean_result)
            if parse_errors:
                results.insert(
                    0,
                    ai_bib_tests.TestResult(
                        name="BibTeX parse errors",
                        ok=False,
                        detail=f" ({ai_bib_tests.summarize_keys(parse_errors)})",
                    ),
                )

            ok = all(bool(getattr(r, "ok", False)) for r in results)
            passed = sum(1 for r in results if getattr(r, "ok", False))
            total = len(results)
            detail = f"({passed}/{total})"
            return TestResult(
                name="bibliography tests",
                ok=ok,
                detail=detail,
                meta={
                    "results": [
                        {"name": getattr(r, "name", ""), "ok": bool(getattr(r, "ok", False)), "detail": getattr(r, "detail", "")}
                        for r in results
                    ]
                },
            )
        except Exception as exc:
            return TestResult(name="bibliography tests", ok=False, detail=f"(error: {exc})")

    return _check
