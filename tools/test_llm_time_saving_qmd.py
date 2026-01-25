"""Quality checks for the LLM time-saving QMD rewrite.

Programmatic tests validate structural properties and bibliography integrity.
Optional LLM-based checks validate narrative criteria and citation plausibility.
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import unittest
from functools import lru_cache
from pathlib import Path
from typing import Dict, List, Tuple
from urllib import request

QMD_PATH = Path("posts/2025-12-17-llm-time-saving-demand-theory-substitution.llm.qmd")
BIB_PATH = Path("posts/ai.bib")
BIB_TESTS_PATH = Path("tools/ai.bib.tests.py")

REQUIRED_HEADINGS = [
    "## Results-first summary",
    "## Setup: time allocation and task productivity",
    "## Estimation cheat sheet",
    "## Continuous (intensive-margin) model",
    "## Discrete (extensive-margin) model",
    "### Worked example (discrete, not continuous)",
    "## Applications",
    "## Experimental design",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_citations(text: str) -> List[str]:
    return re.findall(r"@([A-Za-z0-9:_-]+)", text)


def extract_mermaid_blocks(text: str) -> List[str]:
    """Extract Mermaid fenced code blocks from a QMD/Markdown document."""
    pattern = re.compile(r"```\{mermaid\}\s*\n(.*?)\n```", re.DOTALL)
    return [m.group(1).strip() for m in pattern.finditer(text)]


@lru_cache(maxsize=1)
def load_ai_bib_tests_module():
    if not BIB_TESTS_PATH.exists():
        raise FileNotFoundError(
            f"Missing bibliography test file: {BIB_TESTS_PATH}. "
            "Expected to subcontract ai.bib checks to this file."
        )

    spec = importlib.util.spec_from_file_location("ai_bib_tests", BIB_TESTS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module spec for {BIB_TESTS_PATH}.")

    module = importlib.util.module_from_spec(spec)
    # dataclasses (and other libs) expect the module to be present in sys.modules
    # while the module body executes.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def ai_bib_keys() -> set[str]:
    ai_bib_tests = load_ai_bib_tests_module()
    text = read_text(BIB_PATH)
    entries, parse_errors = ai_bib_tests.parse_entries(text.splitlines())
    if parse_errors:
        # If ai.bib doesn't parse, citation resolution is meaningless.
        raise AssertionError(f"ai.bib parse errors: {parse_errors}")
    return {entry.key for entry in entries}


def run_ai_bib_tests_report() -> List[object]:
    ai_bib_tests = load_ai_bib_tests_module()

    text = read_text(BIB_PATH)
    entries, parse_errors = ai_bib_tests.parse_entries(text.splitlines())
    results = ai_bib_tests.run_tests(entries)

    bibclean_result = ai_bib_tests.run_bibclean(BIB_PATH)
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

    return results


def call_llm(prompt: str) -> Dict[str, str]:
    api_key = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing LLM_API_KEY or OPENAI_API_KEY.")

    url = os.getenv("LLM_API_URL", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    payload = {
        "model": model,
        "temperature": 0,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a rigorous academic reviewer. Respond ONLY in JSON with keys: "
                    "pass (true/false), notes (string)."
                ),
            },
            {"role": "user", "content": prompt},
        ],
    }

    req = request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )

    with request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode("utf-8"))

    content = data["choices"][0]["message"]["content"]
    try:
        return json.loads(content)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"LLM response was not JSON: {content}") from exc


class TestQmdStructure(unittest.TestCase):
    def setUp(self) -> None:
        self.qmd_text = read_text(QMD_PATH)

    def test_qmd_exists(self) -> None:
        self.assertTrue(QMD_PATH.exists(), "QMD file is missing.")

    def test_required_sections_present(self) -> None:
        for heading in REQUIRED_HEADINGS:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.qmd_text)

    def test_structured_proof_collapsed(self) -> None:
        # Proofs should be collapsed by default in HTML output; in QMD that is
        # implemented via a collapsible callout.
        self.assertNotIn("Lamport", self.qmd_text)
        self.assertIn('collapse="true"', self.qmd_text)
        self.assertIn("Proof (structured)", self.qmd_text)
        self.assertIn("QED", self.qmd_text)
        self.assertRegex(self.qmd_text, r"\n1\. \*Given\*")

    def test_estimation_flowchart_present(self) -> None:
        self.assertIn("Estimation flowchart", self.qmd_text)
        self.assertIn("```{mermaid}", self.qmd_text)
        self.assertRegex(self.qmd_text, r"\nflowchart TD")

    def test_mermaid_syntax_valid(self) -> None:
        """Validate Mermaid code blocks by round-tripping through mermaid.ink.

        This catches cases where Quarto will emit a <pre class="mermaid"> block,
        but the diagram won't render client-side due to a Mermaid parse error.
        """
        if not os.getenv("MERMAID_INK_CHECK"):
            raise unittest.SkipTest("Set MERMAID_INK_CHECK=1 to validate Mermaid syntax via mermaid.ink.")

        blocks = extract_mermaid_blocks(self.qmd_text)
        self.assertGreater(len(blocks), 0, "No Mermaid blocks found to validate.")

        curl = shutil.which("curl")
        if not curl:
            raise unittest.SkipTest("curl not found; skipping Mermaid syntax validation.")

        base_url = os.getenv("MERMAID_INK_BASE_URL", "https://mermaid.ink/svg/")

        for idx, code in enumerate(blocks, start=1):
            payload = json.dumps({"code": code, "mermaid": {"theme": "default"}})
            b64 = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
            url = f"{base_url}{b64}"

            # Fast path: only fetch HTTP status code (discard SVG).
            proc = subprocess.run(
                [curl, "-sS", "--max-time", "10", "-o", "/dev/null", "-w", "%{http_code}", url],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0:
                raise unittest.SkipTest(
                    f"curl failed while validating Mermaid block {idx} (network?): {proc.stderr.strip()}"
                )
            http_code = (proc.stdout or "").strip()
            if http_code == "200":
                continue

            # On failure, fetch the error body for a readable assertion message.
            proc_body = subprocess.run(
                [curl, "-sS", "--max-time", "10", url],
                capture_output=True,
                text=True,
            )
            body = (proc_body.stdout or proc_body.stderr or "").strip()
            snippet = body[:600] + ("..." if len(body) > 600 else "")
            self.fail(f"Mermaid block {idx} failed to render (HTTP {http_code}): {snippet}")

    def test_mermaid_syntax_lint(self) -> None:
        """Offline lint for common Mermaid gotchas.

        We keep this lightweight and deterministic (no network). The goal is to
        prevent patterns that routinely cause Mermaid parse failures in Quarto.
        """
        blocks = extract_mermaid_blocks(self.qmd_text)
        self.assertGreater(len(blocks), 0, "No Mermaid blocks found to lint.")

        for idx, code in enumerate(blocks, start=1):
            # Mermaid does not accept literal backslash-newline escapes in labels.
            self.assertNotIn(
                "\\n",
                code,
                f"Mermaid block {idx} contains literal \\\\n escapes; use <br/> for line breaks.",
            )
            # Parentheses in edge labels are easy to trip Mermaid's tokenizer.
            for label in re.findall(r"\|([^|]*)\|", code):
                self.assertNotRegex(
                    label,
                    r"[()]",
                    f"Mermaid block {idx} has parentheses in an edge label: {label!r}.",
                )

    def test_applications_present(self) -> None:
        self.assertIn("## Applications", self.qmd_text)
        self.assertIn("@anthropic2025estimatingproductivitygains", self.qmd_text)
        self.assertIn("s_0=10\\%", self.qmd_text)
        self.assertIn("A=5", self.qmd_text)
        self.assertIn("@becker2025uplift", self.qmd_text)

    def test_experimental_design_present(self) -> None:
        self.assertIn("## Experimental design", self.qmd_text)
        # Light-touch guardrail: ensure key design elements are present.
        self.assertIn("Decide the estimand", self.qmd_text)
        self.assertIn("Trace a demand curve", self.qmd_text)

    def test_citations_resolve(self) -> None:
        citations = extract_citations(self.qmd_text)
        self.assertGreater(len(citations), 0, "No citations found in QMD.")
        bib_keys = ai_bib_keys()
        missing = sorted(set(citations) - bib_keys)  # type: ignore[arg-type]
        self.assertEqual(missing, [], f"Missing citations in ai.bib: {missing}")


class TestBibliography(unittest.TestCase):
    def test_ai_bib_conventions(self) -> None:
        results = run_ai_bib_tests_report()

        failures = [result for result in results if not result.ok]
        if failures:
            summary = ", ".join(result.name for result in failures)
            self.fail(f"Bibliography tests failed: {summary}")


@unittest.skipUnless(
    os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"),
    "LLM API key not set; skipping LLM-based checks.",
)
class TestLLMBasedChecks(unittest.TestCase):
    def test_llm_quality_gate(self) -> None:
        qmd_text = read_text(QMD_PATH)
        prompt = (
            "Review the following QMD content. Verify these criteria: "
            "(1) Continuous vs discrete cases are explicitly separated; "
            "(2) The worked example is discrete (unit-demand or setup-cost), not continuous; "
            "(3) There is an estimation cheat sheet with a flowchart; "
            "(4) Applications discuss both the Anthropic and METR uplift papers and include concrete back-of-envelope numbers; "
            "(5) Experimental design guidance is included; "
            "(6) Proofs are structured, collapsed by default, and include numbered steps plus a QED marker; "
            "(7) Claims with citations look plausible and not obviously mismatched. "
            "Return JSON: {\"pass\": true/false, \"notes\": "
            "\"...\"}. If any criterion is missing or dubious, set pass=false and explain.\n\n"
            f"QMD:\n{qmd_text}"
        )
        result = call_llm(prompt)
        self.assertIn("pass", result)
        self.assertTrue(result["pass"], result.get("notes", "LLM failed quality gate."))


def _symbol(ok: bool) -> str:
    return "✅" if ok else "❌"


def print_validation_report(run_llm_if_configured: bool = True) -> int:
    qmd_text = read_text(QMD_PATH)

    print("Validation Checks")

    # Required headings
    present = sum(1 for h in REQUIRED_HEADINGS if h in qmd_text)
    ok = present == len(REQUIRED_HEADINGS)
    print(f"{_symbol(ok)} Programmatic: required sections present ({present}/{len(REQUIRED_HEADINGS)})")
    overall_ok = ok

    # Proof structure (collapsed)
    ok = (
        ("Lamport" not in qmd_text)
        and ('collapse="true"' in qmd_text)
        and ("Proof (structured)" in qmd_text)
        and ("QED" in qmd_text)
        and re.search(r"\n1\. \*Given\*", qmd_text) is not None
    )
    print(f"{_symbol(ok)} Programmatic: proof structure (collapsed)")
    overall_ok = overall_ok and ok

    # Estimation flowchart
    ok = (
        ("Estimation flowchart" in qmd_text)
        and ("```{mermaid}" in qmd_text)
        and re.search(r"\nflowchart TD", qmd_text) is not None
    )
    print(f"{_symbol(ok)} Programmatic: estimation flowchart present")
    overall_ok = overall_ok and ok

    # Mermaid syntax lint (offline)
    mermaid_blocks = extract_mermaid_blocks(qmd_text)
    lint_errors: list[str] = []
    for i, code in enumerate(mermaid_blocks, start=1):
        if "\\n" in code:
            lint_errors.append(f"block {i}: contains literal \\\\n escapes")
        for label in re.findall(r"\|([^|]*)\|", code):
            if "(" in label or ")" in label:
                lint_errors.append(f"block {i}: parentheses in edge label {label!r}")
    ok = (len(mermaid_blocks) > 0) and (not lint_errors)
    print(f"{_symbol(ok)} Programmatic: Mermaid syntax lint (offline)")
    if lint_errors:
        print(f"  ❌ {lint_errors[0]}{' ...' if len(lint_errors) > 1 else ''}")
    overall_ok = overall_ok and ok

    # Mermaid render check (optional, uses network)
    if not os.getenv("MERMAID_INK_CHECK"):
        print("⏳ Programmatic: Mermaid renders via mermaid.ink (optional)")
    else:
        curl = shutil.which("curl")
        if not curl:
            print("⏳ Programmatic: Mermaid renders via mermaid.ink (optional; curl not found)")
        else:
            base_url = os.getenv("MERMAID_INK_BASE_URL", "https://mermaid.ink/svg/")
            mermaid_ok: bool | None = True
            for i, code in enumerate(mermaid_blocks, start=1):
                payload = json.dumps({"code": code, "mermaid": {"theme": "default"}})
                b64 = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
                url = f"{base_url}{b64}"
                proc = subprocess.run(
                    [curl, "-sS", "--max-time", "10", "-o", "/dev/null", "-w", "%{http_code}", url],
                    capture_output=True,
                    text=True,
                )
                if proc.returncode != 0:
                    mermaid_ok = None
                    break
                if (proc.stdout or "").strip() != "200":
                    mermaid_ok = False
                    break
            if mermaid_ok is None:
                print("⏳ Programmatic: Mermaid renders via mermaid.ink (network error)")
            else:
                print(f"{_symbol(mermaid_ok)} Programmatic: Mermaid renders via mermaid.ink")
                overall_ok = overall_ok and mermaid_ok

    # Applications
    ok = (
        ("## Applications" in qmd_text)
        and ("@anthropic2025estimatingproductivitygains" in qmd_text)
        and ("s_0=10\\%" in qmd_text)
        and ("A=5" in qmd_text)
        and ("@becker2025uplift" in qmd_text)
    )
    print(f"{_symbol(ok)} Programmatic: applications present")
    overall_ok = overall_ok and ok

    # Experimental design
    ok = ("## Experimental design" in qmd_text) and (
        ("Decide the estimand" in qmd_text) and ("Trace a demand curve" in qmd_text)
    )
    print(f"{_symbol(ok)} Programmatic: experimental design present")
    overall_ok = overall_ok and ok

    # Bibliography tests (subcontracted)
    try:
        bib_results = run_ai_bib_tests_report()
        passed = sum(1 for r in bib_results if r.ok)
        total = len(bib_results)
        bib_ok = all(r.ok for r in bib_results)
        print(f"{_symbol(bib_ok)} Programmatic: bibliography tests ({passed}/{total})")
        for r in bib_results:
            detail = getattr(r, "detail", "") or ""
            print(f"  {_symbol(bool(r.ok))} {r.name}{detail}")
        overall_ok = overall_ok and bib_ok
    except Exception as exc:
        print(f"{_symbol(False)} Programmatic: bibliography tests (error: {exc})")
        overall_ok = False

    # Citekeys resolve
    try:
        citations = extract_citations(qmd_text)
        bib_keys = ai_bib_keys()
        missing = sorted(set(citations) - bib_keys)  # type: ignore[arg-type]
        ok = (len(citations) > 0) and (missing == [])
        print(f"{_symbol(ok)} Programmatic: citekeys resolve in {BIB_PATH}")
        if missing:
            print(f"  ❌ Missing citekeys: {missing[:10]}{' ...' if len(missing) > 10 else ''}")
        overall_ok = overall_ok and ok
    except Exception as exc:
        print(f"{_symbol(False)} Programmatic: citekeys resolve in {BIB_PATH} (error: {exc})")
        overall_ok = False

    # Optional LLM gate
    has_llm_key = bool(os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"))
    if not run_llm_if_configured or not has_llm_key:
        print("⏳ LLM-assisted: quality + citation plausibility gate (optional)")
    else:
        prompt = (
            "Review the following QMD content. Verify these criteria: "
            "(1) Continuous vs discrete cases are explicitly separated; "
            "(2) The worked example is discrete (unit-demand or setup-cost), not continuous; "
            "(3) There is an estimation cheat sheet with a flowchart; "
            "(4) Applications discuss both the Anthropic and METR uplift papers and include concrete back-of-envelope numbers; "
            "(5) Experimental design guidance is included; "
            "(6) Proofs are structured, collapsed by default, and include numbered steps plus a QED marker; "
            "(7) Claims with citations look plausible and not obviously mismatched. "
            "Return JSON: {\"pass\": true/false, \"notes\": \"...\"}.\n\n"
            f"QMD:\n{qmd_text}"
        )
        try:
            result = call_llm(prompt)
            ok = bool(result.get("pass", False))
            print(f"{_symbol(ok)} LLM-assisted: quality + citation plausibility gate")
            if not ok:
                notes = (result.get("notes") or "").strip()
                if notes:
                    print(f"  ❌ Notes: {notes}")
            overall_ok = overall_ok and ok
        except Exception as exc:
            print(f"{_symbol(False)} LLM-assisted: quality + citation plausibility gate (error: {exc})")
            overall_ok = False

    return 0 if overall_ok else 1


def build_json_report(run_llm_if_configured: bool = True) -> Dict[str, object]:
    qmd_text = read_text(QMD_PATH)
    items: List[Dict[str, object]] = []
    overall_ok = True

    present = sum(1 for h in REQUIRED_HEADINGS if h in qmd_text)
    ok = present == len(REQUIRED_HEADINGS)
    items.append(
        {
            "name": "required sections present",
            "category": "programmatic",
            "ok": ok,
            "counts": {"present": present, "total": len(REQUIRED_HEADINGS)},
        }
    )
    overall_ok = overall_ok and ok

    ok = (
        ("Lamport" not in qmd_text)
        and ('collapse="true"' in qmd_text)
        and ("Proof (structured)" in qmd_text)
        and ("QED" in qmd_text)
        and re.search(r"\n1\. \*Given\*", qmd_text) is not None
    )
    items.append({"name": "proof structure (collapsed)", "category": "programmatic", "ok": ok})
    overall_ok = overall_ok and ok

    ok = ("Estimation flowchart" in qmd_text) and ("```{mermaid}" in qmd_text) and (re.search(r"\nflowchart TD", qmd_text) is not None)
    items.append({"name": "estimation flowchart present", "category": "programmatic", "ok": ok})
    overall_ok = overall_ok and ok

    mermaid_blocks = extract_mermaid_blocks(qmd_text)
    lint_errors: list[str] = []
    for i, code in enumerate(mermaid_blocks, start=1):
        if "\\n" in code:
            lint_errors.append(f"block {i}: contains literal \\\\n escapes")
        for label in re.findall(r"\|([^|]*)\|", code):
            if "(" in label or ")" in label:
                lint_errors.append(f"block {i}: parentheses in edge label {label!r}")
    ok = (len(mermaid_blocks) > 0) and (not lint_errors)
    items.append(
        {
            "name": "Mermaid syntax lint (offline)",
            "category": "programmatic",
            "ok": ok,
            "counts": {"blocks": len(mermaid_blocks), "errors": len(lint_errors)},
            "errors": lint_errors[:5],
        }
    )
    overall_ok = overall_ok and ok

    if not os.getenv("MERMAID_INK_CHECK"):
        items.append(
            {
                "name": "Mermaid renders via mermaid.ink",
                "category": "programmatic",
                "ok": None,
                "skipped": True,
                "reason": "Set MERMAID_INK_CHECK=1 to enable",
            }
        )
    else:
        curl = shutil.which("curl")
        if not curl:
            items.append(
                {
                    "name": "Mermaid renders via mermaid.ink",
                    "category": "programmatic",
                    "ok": None,
                    "skipped": True,
                    "reason": "curl not found",
                }
            )
        else:
            base_url = os.getenv("MERMAID_INK_BASE_URL", "https://mermaid.ink/svg/")
            mermaid_ok: bool | None = True
            failure_detail: dict[str, object] | None = None
            for i, code in enumerate(mermaid_blocks, start=1):
                payload = json.dumps({"code": code, "mermaid": {"theme": "default"}})
                b64 = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
                url = f"{base_url}{b64}"
                proc = subprocess.run(
                    [curl, "-sS", "--max-time", "10", "-o", "/dev/null", "-w", "%{http_code}", url],
                    capture_output=True,
                    text=True,
                )
                if proc.returncode != 0:
                    mermaid_ok = None
                    failure_detail = {"block": i, "error": (proc.stderr or "").strip()}
                    break
                http_code = (proc.stdout or "").strip()
                if http_code != "200":
                    mermaid_ok = False
                    failure_detail = {"block": i, "http_code": http_code}
                    break
            items.append(
                {
                    "name": "Mermaid renders via mermaid.ink",
                    "category": "programmatic",
                    "ok": mermaid_ok,
                    "checked_blocks": len(mermaid_blocks),
                    "base_url": base_url,
                    "failure": failure_detail,
                }
            )
            if mermaid_ok is not None:
                overall_ok = overall_ok and mermaid_ok

    ok = (
        ("## Applications" in qmd_text)
        and ("@anthropic2025estimatingproductivitygains" in qmd_text)
        and ("s_0=10\\%" in qmd_text)
        and ("A=5" in qmd_text)
        and ("@becker2025uplift" in qmd_text)
    )
    items.append({"name": "applications present", "category": "programmatic", "ok": ok})
    overall_ok = overall_ok and ok

    ok = ("## Experimental design" in qmd_text) and (
        ("Decide the estimand" in qmd_text) and ("Trace a demand curve" in qmd_text)
    )
    items.append({"name": "experimental design present", "category": "programmatic", "ok": ok})
    overall_ok = overall_ok and ok

    try:
        bib_results = run_ai_bib_tests_report()
        bib_ok = all(r.ok for r in bib_results)
        items.append(
            {
                "name": "bibliography tests",
                "category": "programmatic",
                "ok": bib_ok,
                "detail": [
                    {
                        "name": r.name,
                        "ok": bool(r.ok),
                        "detail": r.detail,
                    }
                    for r in bib_results
                ],
            }
        )
        overall_ok = overall_ok and bib_ok
    except Exception as exc:
        items.append(
            {
                "name": "bibliography tests",
                "category": "programmatic",
                "ok": False,
                "error": str(exc),
            }
        )
        overall_ok = False

    try:
        citations = extract_citations(qmd_text)
        bib_keys = ai_bib_keys()
        missing = sorted(set(citations) - bib_keys)  # type: ignore[arg-type]
        ok = (len(citations) > 0) and (missing == [])
        items.append(
            {
                "name": "citekeys resolve in ai.bib",
                "category": "programmatic",
                "ok": ok,
                "missing": missing,
            }
        )
        overall_ok = overall_ok and ok
    except Exception as exc:
        items.append(
            {
                "name": "citekeys resolve in ai.bib",
                "category": "programmatic",
                "ok": False,
                "error": str(exc),
            }
        )
        overall_ok = False

    has_llm_key = bool(os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"))
    if not run_llm_if_configured or not has_llm_key:
        items.append(
            {
                "name": "quality + citation plausibility gate",
                "category": "llm-assisted",
                "ok": None,
                "skipped": True,
            }
        )
    else:
        prompt = (
            "Review the following QMD content. Verify these criteria: "
            "(1) Continuous vs discrete cases are explicitly separated; "
            "(2) The worked example is discrete (unit-demand or setup-cost), not continuous; "
            "(3) There is an estimation cheat sheet with a flowchart; "
            "(4) Applications discuss both the Anthropic and METR uplift papers and include concrete back-of-envelope numbers; "
            "(5) Experimental design guidance is included; "
            "(6) Proofs are structured, collapsed by default, and include numbered steps plus a QED marker; "
            "(7) Claims with citations look plausible and not obviously mismatched. "
            "Return JSON: {\"pass\": true/false, \"notes\": \"...\"}.\n\n"
            f"QMD:\n{qmd_text}"
        )
        try:
            result = call_llm(prompt)
            ok = bool(result.get("pass", False))
            items.append(
                {
                    "name": "quality + citation plausibility gate",
                    "category": "llm-assisted",
                    "ok": ok,
                    "notes": result.get("notes", ""),
                }
            )
            overall_ok = overall_ok and ok
        except Exception as exc:
            items.append(
                {
                    "name": "quality + citation plausibility gate",
                    "category": "llm-assisted",
                    "ok": False,
                    "error": str(exc),
                }
            )
            overall_ok = False

    return {
        "overall_ok": overall_ok,
        "items": items,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--unittest",
        action="store_true",
        help="Run via unittest (dot-style output) instead of the checklist report.",
    )
    parser.add_argument(
        "--no-llm",
        action="store_true",
        help="Do not run the optional LLM gate (even if API key is configured).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON output instead of formatted report.",
    )
    # When running via `unittest`, we want to forward any additional CLI flags
    # (e.g. `-v`, `-k`) to unittest's own argument parser.
    args, remaining = parser.parse_known_args()

    if args.unittest:
        unittest.main(argv=[sys.argv[0], *remaining])
    else:
        if remaining:
            parser.error(f"unrecognized arguments: {' '.join(remaining)}")
        if args.json:
            report = build_json_report(run_llm_if_configured=not args.no_llm)
            print(json.dumps(report, indent=2))
            raise SystemExit(0 if report["overall_ok"] else 1)
        raise SystemExit(print_validation_report(run_llm_if_configured=not args.no_llm))
