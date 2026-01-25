#!/usr/bin/env python3
"""Fetch plaintext versions of bibliography sources into references/text/.

By default, uses text_url if present; otherwise uses url. Skips PDFs.
Optionally inserts text_url back into ai.bib for successful fetches.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import requests

DEFAULT_BIB = Path("posts/ai.bib")
DEFAULT_OUT_DIR = Path("references/text")
DEFAULT_QMD = Path("posts/2025-10-19-forecasts-of-AI-growth.qmd")


def load_ai_bib_tests_module(path: Path) -> object:
    spec = importlib.util.spec_from_file_location("ai_bib_tests", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module spec for {path}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def build_jina_url(url: str) -> str:
    if url.startswith("https://r.jina.ai/"):
        return url
    if "//" not in url:
        return url
    scheme, rest = url.split("//", 1)
    return f"https://r.jina.ai/{scheme}//{rest}"


def is_pdf_url(url: str) -> bool:
    lower = url.lower()
    return ".pdf" in lower


def is_unusable_fulltext(text: str) -> bool:
    lower = text.lower()
    markers = [
        "verifying you are human",
        "needs to review the security of your connection before proceeding",
        "don't have permission to access",
        "errors.edgesuite.net",
        "bloomberg the company & its products",
    ]
    return any(marker in lower for marker in markers)


def extract_markdown_content(text: str) -> str:
    marker = "Markdown Content:"
    if marker in text:
        text = text.split(marker, 1)[1]
    return text.lstrip("\n")


def sanitize_markdown(text: str) -> str:
    cleaned = []
    for line in text.splitlines():
        if re.match(r"^!\[.*\]\(.*\)", line.strip()):
            continue
        if re.match(r"^\[!\[Image", line.strip()):
            continue
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def arxiv_id_from_pdf_url(url: str) -> str | None:
    m = re.search(r"arxiv\\.org/pdf/([^?#/]+)\\.pdf", url)
    if not m:
        return None
    return m.group(1)


def pdf_to_text(pdf_bytes: bytes) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        raise RuntimeError("pdftotext not found; install poppler to enable PDF extraction.")

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "doc.pdf"
        txt_path = Path(tmpdir) / "doc.txt"
        pdf_path.write_bytes(pdf_bytes)
        proc = subprocess.run(
            [pdftotext, str(pdf_path), str(txt_path)],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError((proc.stderr or proc.stdout or "pdftotext failed").strip())
        return txt_path.read_text(encoding="utf-8", errors="replace")


def extract_citekeys_from_qmd(qmd_path: Path) -> set[str]:
    text = qmd_path.read_text(encoding="utf-8")
    return set(re.findall(r"@([A-Za-z0-9][A-Za-z0-9:_-]*)", text))


def insert_text_url(bib_text: str, citekey: str, url: str) -> str:
    lines = bib_text.splitlines()
    out = []
    in_entry = False
    current_key = None
    inserted = False
    for line in lines:
        start = re.match(r"^@\w+\{([^,]+),", line)
        if start:
            in_entry = True
            current_key = start.group(1)
            inserted = False
            out.append(line)
            continue
        if in_entry and line.strip() == "}":
            if current_key == citekey and not inserted:
                out.append(f"  text_url = {{{url}}},")
            out.append(line)
            in_entry = False
            current_key = None
            continue
        if in_entry and current_key == citekey and re.match(r"^\s*text_url\s*=", line):
            out.append(line)
            inserted = True
            continue
        if in_entry and current_key == citekey and re.match(r"^\s*url\s*=", line):
            out.append(line)
            out.append(f"  text_url = {{{url}}},")
            inserted = True
            continue
        out.append(line)
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bib", default=str(DEFAULT_BIB))
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR))
    parser.add_argument("--qmd", default=str(DEFAULT_QMD))
    parser.add_argument("--all", action="store_true", help="Fetch for all bib entries, not just citekeys in --qmd.")
    parser.add_argument("--update-bib", action="store_true", help="Insert text_url into ai.bib for successful fetches.")
    parser.add_argument("--timeout", type=int, default=20, help="Per-request timeout in seconds.")
    parser.add_argument("--max", type=int, help="Maximum number of entries to attempt.")
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="If the source is a PDF, download it and extract text via pdftotext.",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip citekeys that already have references/text/<citekey>.txt.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON summary.")
    args = parser.parse_args()

    bib_path = Path(args.bib)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    ai_bib_tests_path = Path(__file__).resolve().parent / "ai.bib.tests.py"
    ai_bib_tests = load_ai_bib_tests_module(ai_bib_tests_path)

    bib_text = bib_path.read_text(encoding="utf-8")
    entries, parse_errors = ai_bib_tests.parse_entries(bib_text.splitlines())
    if parse_errors:
        raise SystemExit(f"BibTeX parse errors: {parse_errors}")
    entry_map = {entry.key: entry.fields for entry in entries}

    if args.all:
        target_keys = set(entry_map.keys())
    else:
        target_keys = extract_citekeys_from_qmd(Path(args.qmd))

    results = []
    updated_bib = bib_text
    attempted = 0
    for key in sorted(target_keys):
        if args.max is not None and attempted >= args.max:
            break
        if args.skip_existing:
            existing_path = out_dir / f"{key}.txt"
            if existing_path.exists() and existing_path.stat().st_size > 200:
                results.append({"key": key, "status": "skipped", "reason": "already_exists"})
                continue
        attempted += 1
        fields = entry_map.get(key, {})
        source_url = fields.get("text_url") or fields.get("url")
        if not source_url:
            results.append({"key": key, "status": "skipped", "reason": "no_url"})
            continue
        if is_pdf_url(source_url) and not args.pdf:
            results.append({"key": key, "status": "skipped", "reason": "pdf"})
            continue

        if is_pdf_url(source_url):
            arxiv_id = arxiv_id_from_pdf_url(source_url)
            if arxiv_id is not None:
                ar5iv_url = f"https://ar5iv.labs.arxiv.org/html/{arxiv_id}"
                try:
                    resp = requests.get(build_jina_url(ar5iv_url), timeout=args.timeout)
                except Exception as exc:
                    results.append({"key": key, "status": "error", "reason": str(exc)})
                    continue
                if resp.status_code == 200:
                    content = sanitize_markdown(extract_markdown_content(resp.text))
                    if len(content.strip()) >= 200 and not is_unusable_fulltext(content):
                        out_path = out_dir / f"{key}.txt"
                        out_path.write_text(content.strip() + "\n", encoding="utf-8")
                        if args.update_bib and not fields.get("text_url"):
                            updated_bib = insert_text_url(updated_bib, key, ar5iv_url)
                        results.append({"key": key, "status": "ok", "bytes": len(content), "source": "ar5iv"})
                        continue
            try:
                resp = requests.get(source_url, timeout=args.timeout)
            except Exception as exc:
                results.append({"key": key, "status": "error", "reason": str(exc)})
                continue
            if resp.status_code != 200:
                results.append({"key": key, "status": "error", "reason": f"status {resp.status_code}"})
                continue
            try:
                content = pdf_to_text(resp.content)
            except Exception as exc:
                results.append({"key": key, "status": "error", "reason": f"pdf_extract_failed:{exc}"})
                continue
            content = content.strip()
            if len(content) < 200:
                results.append({"key": key, "status": "error", "reason": "content_too_short"})
                continue
            out_path = out_dir / f"{key}.txt"
            out_path.write_text(content + "\n", encoding="utf-8")
            if args.update_bib and not fields.get("text_url"):
                updated_bib = insert_text_url(updated_bib, key, source_url)
            results.append({"key": key, "status": "ok", "bytes": len(content), "source": "pdf"})
            continue

        jina_url = build_jina_url(source_url)
        try:
            resp = requests.get(jina_url, timeout=args.timeout)
        except Exception as exc:
            results.append({"key": key, "status": "error", "reason": str(exc)})
            continue
        if resp.status_code != 200:
            results.append({"key": key, "status": "error", "reason": f"status {resp.status_code}"})
            continue

        content = extract_markdown_content(resp.text)
        content = sanitize_markdown(content)
        if is_unusable_fulltext(content):
            results.append({"key": key, "status": "error", "reason": "blocked_or_placeholder"})
            continue
        if len(content.strip()) < 200:
            results.append({"key": key, "status": "error", "reason": "content_too_short"})
            continue

        out_path = out_dir / f"{key}.txt"
        out_path.write_text(content.strip() + "\n", encoding="utf-8")

        if args.update_bib and not fields.get("text_url"):
            updated_bib = insert_text_url(updated_bib, key, source_url)

        results.append({"key": key, "status": "ok", "bytes": len(content)})

    if args.update_bib and updated_bib != bib_text:
        bib_path.write_text(updated_bib, encoding="utf-8")

    if args.json:
        print(json.dumps({"results": results}, indent=2))
    else:
        for item in results:
            status = item["status"]
            line = f"{item['key']}: {status}"
            if "reason" in item:
                line += f" ({item['reason']})"
            print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
