#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import re
import importlib.util
import json
import sys
import unicodedata
from pathlib import Path

TEXT_ARCHIVE_DIR = Path(__file__).resolve().parents[1] / "references" / "text"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


BIB_TESTS_PATH = Path(__file__).resolve().parent / "ai.bib.tests.py"


def load_ai_bib_tests_module():
    if not BIB_TESTS_PATH.exists():
        raise FileNotFoundError(
            f"Missing bibliography test file: {BIB_TESTS_PATH}. "
            "Expected to reuse ai.bib parsing from this file."
        )

    spec = importlib.util.spec_from_file_location("ai_bib_tests", BIB_TESTS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module spec for {BIB_TESTS_PATH}.")

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def parse_bib_entries(text: str) -> tuple[dict[str, dict[str, str]], list[str]]:
    ai_bib_tests = load_ai_bib_tests_module()
    entries, parse_errors = ai_bib_tests.parse_entries(text.splitlines())
    entry_map = {entry.key: entry.fields for entry in entries}
    return entry_map, parse_errors


def strip_code_blocks(text: str) -> str:
    lines = text.splitlines()
    out = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            out.append(line)
    return "\n".join(out)


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = (
        text.replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2019", "'")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
    )
    text = text.replace("&#64;", "@").replace("&commat;", "@")
    text = text.replace("\\@", "@")
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("*", "").replace("_", "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        text = text[1:-1].strip()
    return text.lower()


def normalize_for_search(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.replace("&#64;", "@").replace("&commat;", "@")
    text = (
        text.replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2019", "'")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u2026", "...")
    )
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^0-9a-zA-Z]+", " ", text).strip().lower()
    return re.sub(r"\s+", " ", text)


def quote_in_fulltext(quote: str, fulltext: str) -> tuple[bool, str]:
    quote = quote.strip()
    if not quote:
        return False, "empty_quote"

    haystack = normalize_for_search(fulltext)
    if not haystack:
        return False, "empty_fulltext"

    quote_norm = (
        unicodedata.normalize("NFKD", quote)
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2026", "...")
    )
    quoted_fragments = re.findall(r"\"([^\"]+)\"", quote_norm)
    raw_segments = quoted_fragments if quoted_fragments else re.split(r"\.\.\.|…", quote_norm)
    segments = [normalize_for_search(seg) for seg in raw_segments]
    segments = [seg for seg in segments if seg]
    if not segments:
        return False, "empty_quote_after_normalization"

    idx = 0
    for seg in segments:
        found = haystack.find(seg, idx)
        if found < 0:
            return False, f"segment_not_found:{seg[:80]}"
        idx = found + len(seg)
    return True, ""


def fulltext_is_usable(fulltext: str) -> bool:
    haystack = normalize_for_search(fulltext)
    if len(haystack) < 200:
        return False
    unusable_markers = [
        "verifying you are human",
        "needs to review the security of your connection",
        "dont have permission to access",
        "errors edgesuite net",
        "bloomberg the company its products",
        "bloomberg terminal demo request",
    ]
    return not any(marker in haystack for marker in unusable_markers)


def extract_citekeys(text: str) -> set[str]:
    keys = set(re.findall(r"@([A-Za-z0-9][A-Za-z0-9:_-]*)", text))
    ignore = {"media", "font-face", "keyframes", "supports"}
    return {key for key in keys if key not in ignore and any(ch.isdigit() for ch in key)}


def iter_tables(text: str) -> list[list[str]]:
    lines = text.splitlines()
    tables: list[list[str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|"):
            table_lines: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i])
                i += 1
            tables.append(table_lines)
            continue
        i += 1
    return tables


def split_row(row: str) -> list[str]:
    row = re.sub(r"^\s*\||\|\s*$", "", row)
    return [cell.strip() for cell in row.split("|")]


def parse_table(table_lines: list[str]) -> tuple[list[str], list[list[str]]]:
    header = split_row(table_lines[0])
    rows: list[list[str]] = []
    for row in table_lines[1:]:
        if re.match(r"^\s*\|\s*[-:]", row):
            continue
        rows.append(split_row(row))
    return header, rows


def extract_table_checks(text: str) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    for table_lines in iter_tables(text):
        header, rows = parse_table(table_lines)
        header_norm = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip().lower() for h in header]
        if "author" not in header_norm or "quote" not in header_norm:
            continue
        author_idx = header_norm.index("author")
        quote_idx = header_norm.index("quote")
        growth_idx = None
        if "annual excess growth, 2025-2035" in header_norm:
            growth_idx = header_norm.index("annual excess growth, 2025-2035")
        elif "growth 2025-2035" in header_norm:
            growth_idx = header_norm.index("growth 2025-2035")
        for row in rows:
            if author_idx >= len(row):
                continue
            author_cell = row[author_idx]
            quote_cell = row[quote_idx] if quote_idx < len(row) else ""
            growth_cell = row[growth_idx] if growth_idx is not None and growth_idx < len(row) else ""
            citekeys = re.findall(r"@([A-Za-z0-9][A-Za-z0-9:_-]*)", author_cell)
            if not citekeys:
                continue
            for citekey in citekeys:
                checks.append(
                    {
                        "citekey": citekey,
                        "quote": quote_cell,
                        "growth": growth_cell,
                    }
                )
    return checks


def build_checklist(
    status: dict[str, str],
    last_checked: str,
    counts: dict[str, tuple[int, int]],
) -> str:
    def item_line(symbol: str, label: str, key: str | None = None) -> str:
        if key is None or key not in counts:
            return f"- {symbol} {label}"
        passed, total = counts[key]
        return f"- {symbol} [{passed}/{total}] {label}"

    lines = [
        "<details>",
        "<summary>Validation Checks</summary>",
        "",
        f"**Overall:** {status['overall']}",
        "",
        item_line(status["citations"], "Cited sources exist in `posts/ai.bib` (programmatic)", "citations"),
        item_line(status["tables"], "Table rows have required fields (programmatic)", "tables"),
        item_line(status["quotes_match"], "QMD quotes match `posts/ai.bib` (programmatic)", "quotes_match"),
        item_line(status["growth_match"], "QMD growth values match `posts/ai.bib` (programmatic)", "growth_match"),
        item_line(status["abstracts"], "Abstracts present for all cited sources (programmatic)", "abstracts"),
        item_line(
            status["quotes_verified"],
            "Bib quotes present in local fulltext version (programmatic)",
            "quotes_verified",
        ),
        "",
        f"Last checked: {last_checked}",
        "</details>",
    ]
    return "\n".join(lines)


def build_report(
    missing_citekeys: list[str],
    table_issues: list[int],
    quote_missing: list[str],
    quote_mismatches: list[str],
    growth_missing: list[str],
    growth_mismatches: list[str],
    missing_abstracts: list[str],
    missing_text_archives: list[str],
    quotes_not_found: list[str],
    parse_errors: list[str],
) -> str:
    lines = ["Validation report", "-----------------"]

    def add_list(label: str, items: list[str]) -> None:
        if items:
            lines.append(f"{label} ({len(items)}):")
            lines.extend([f"  - {item}" for item in sorted(items)])
        else:
            lines.append(f"{label}: none")

    def add_count(label: str, count: int) -> None:
        lines.append(f"{label}: {count}")

    add_list("BibTeX parse errors", parse_errors)
    add_list("Missing citekeys in bib", missing_citekeys)
    add_count("Table column mismatches", len(table_issues))
    add_list("Missing bib quotes", quote_missing)
    add_list("Quote mismatches", quote_mismatches)
    add_list("Missing bib growth values", growth_missing)
    add_list("Growth mismatches", growth_mismatches)
    add_list("Missing abstracts", missing_abstracts)
    add_list("Missing local text archives", missing_text_archives)
    add_list("Quotes not found in local fulltext", quotes_not_found)
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qmd", required=True)
    parser.add_argument("--bib", required=True)
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a detailed validation report after the checklist.",
    )
    parser.add_argument(
        "--report-path",
        help="Write the detailed validation report to a file path.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output (checklist + report + counts).",
    )
    args = parser.parse_args()

    qmd_path = Path(args.qmd)
    bib_path = Path(args.bib)

    qmd_text = read_text(qmd_path)
    qmd_clean = strip_code_blocks(qmd_text)
    bib_text = read_text(bib_path)

    citekeys = extract_citekeys(qmd_clean)
    bib_entries, parse_errors = parse_bib_entries(bib_text)
    bib_keys = set(bib_entries.keys())
    missing_citekeys = sorted(citekeys - bib_keys)

    table_issues = []
    total_table_rows = 0
    for table_lines in iter_tables(qmd_clean):
        header_cols = len(split_row(table_lines[0]))
        for row in table_lines[1:]:
            if re.match(r"^\s*\|\s*[-:]", row):
                continue
            total_table_rows += 1
            cols = len(split_row(row))
            if cols != header_cols:
                table_issues.append(cols)

    table_checks = extract_table_checks(qmd_clean)
    quote_mismatches = []
    quote_missing = []
    growth_mismatches = []
    growth_missing = []
    missing_text_archives: list[str] = []
    quotes_not_found: list[str] = []
    quotes_verified_pass = 0
    quotes_verified_total = 0
    for check in table_checks:
        key = check["citekey"]
        entry = bib_entries.get(key, {})
        bib_quote_raw = entry.get("quote", "")
        bib_quote = normalize_text(bib_quote_raw)
        bib_growth = normalize_text(entry.get("growth_annual_excess", ""))
        qmd_quote_raw = check["quote"]
        qmd_quote = normalize_text(check["quote"])
        qmd_growth = normalize_text(check["growth"])
        if not bib_quote and key not in quote_missing:
            quote_missing.append(key)
        elif bib_quote and bib_quote != qmd_quote:
            quote_mismatches.append(key)
        if not bib_growth and key not in growth_missing:
            growth_missing.append(key)
        elif bib_growth and bib_growth != qmd_growth:
            growth_mismatches.append(key)

        if bib_quote_raw.strip():
            text_path = TEXT_ARCHIVE_DIR / f"{key}.txt"
            if not text_path.exists():
                if key not in missing_text_archives:
                    missing_text_archives.append(key)
            else:
                try:
                    fulltext = read_text(text_path)
                except Exception:
                    if key not in missing_text_archives:
                        missing_text_archives.append(key)
                else:
                    if not fulltext_is_usable(fulltext):
                        if key not in missing_text_archives:
                            missing_text_archives.append(key)
                        continue
                    quotes_verified_total += 1
                    ok, _reason = quote_in_fulltext(bib_quote_raw, fulltext)
                    if not ok and key not in quotes_not_found:
                        quotes_not_found.append(key)
                    if ok:
                        quotes_verified_pass += 1

    missing_abstracts = []
    for key in citekeys:
        entry = bib_entries.get(key, {})
        abstract = entry.get("abstract", "").strip()
        if not abstract or abstract.lower().startswith("abstract unavailable"):
            missing_abstracts.append(key)

    status = {
        "citations": "✅" if not missing_citekeys else "❌",
        "tables": "✅" if not table_issues else "❌",
        "quotes_match": "✅" if not quote_mismatches and not quote_missing else "⚠️"
        if not quote_mismatches
        else "❌",
        "growth_match": "✅" if not growth_mismatches and not growth_missing else "⚠️"
        if not growth_mismatches
        else "❌",
        "quotes_verified": "✅"
        if not quotes_not_found and not missing_text_archives and not quote_missing
        else "❌"
        if quotes_not_found
        else "⚠️",
        "abstracts": "✅" if not missing_abstracts else "⚠️",
    }
    if parse_errors:
        status["citations"] = "❌"

    hard_fail = any(
        status[key] == "❌" for key in ("citations", "tables", "quotes_match", "growth_match")
    )
    any_warn = any(value == "⚠️" for value in status.values())
    status["overall"] = "❌ Fail" if hard_fail else "⚠️ Warning" if any_warn else "✅ Pass"

    total_citations = len(citekeys)
    counts = {
        "citations": (total_citations - len(missing_citekeys), total_citations),
        "tables": (total_table_rows - len(table_issues), total_table_rows),
        "quotes_match": (
            len(table_checks) - len(quote_missing) - len(quote_mismatches),
            len(table_checks),
        ),
        "growth_match": (
            len(table_checks) - len(growth_missing) - len(growth_mismatches),
            len(table_checks),
        ),
        "abstracts": (total_citations - len(missing_abstracts), total_citations),
    }
    if quotes_verified_total:
        counts["quotes_verified"] = (quotes_verified_pass, quotes_verified_total)

    checklist = build_checklist(status, dt.date.today().isoformat(), counts)
    report = build_report(
        missing_citekeys,
        table_issues,
        quote_missing,
        quote_mismatches,
        growth_missing,
        growth_mismatches,
        missing_abstracts,
        missing_text_archives,
        quotes_not_found,
        parse_errors,
    )
    if args.json:
        payload = {
            "status": status,
            "counts": counts,
            "checklist": checklist,
            "report": report,
        }
        print(json.dumps(payload, indent=2))
        return 0

    print(checklist)
    if args.report:
        print()
        print(report)
    if args.report_path:
        Path(args.report_path).write_text(report + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
