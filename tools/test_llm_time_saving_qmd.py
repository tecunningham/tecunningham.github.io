"""Quality checks for the LLM time-saving QMD rewrite.

Programmatic tests validate structural properties and bibliography integrity.
Optional LLM-based checks validate narrative criteria and citation plausibility.
"""

from __future__ import annotations

import json
import os
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple
from urllib import request

QMD_PATH = Path("posts/2025-12-17-llm-time-saving-demand-theory-substitution.llm.qmd")
BIB_PATH = Path("posts/ai.bib")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_citations(text: str) -> List[str]:
    return re.findall(r"@([A-Za-z0-9:_-]+)", text)


def parse_bib_entries(text: str) -> List[Tuple[str, str]]:
    entries: List[Tuple[str, str]] = []
    current_key = None
    current_lines: List[str] = []
    brace_balance = 0

    for line in text.splitlines():
        if line.strip().startswith("@"):
            if current_key is not None and current_lines:
                entries.append((current_key, "\n".join(current_lines)))
            match = re.match(r"@\w+\{([^,]+),", line.strip())
            current_key = match.group(1) if match else None
            current_lines = [line]
            brace_balance = line.count("{") - line.count("}")
            if brace_balance == 0 and current_key is not None:
                entries.append((current_key, "\n".join(current_lines)))
                current_key = None
                current_lines = []
            continue

        if current_key is not None:
            current_lines.append(line)
            brace_balance += line.count("{") - line.count("}")
            if brace_balance == 0:
                entries.append((current_key, "\n".join(current_lines)))
                current_key = None
                current_lines = []

    if current_key is not None and current_lines:
        entries.append((current_key, "\n".join(current_lines)))

    return entries


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
        self.bib_text = read_text(BIB_PATH)

    def test_qmd_exists(self) -> None:
        self.assertTrue(QMD_PATH.exists(), "QMD file is missing.")

    def test_required_sections_present(self) -> None:
        for heading in [
            "## Results-first summary",
            "## Continuous (intensive-margin) model",
            "## Discrete (extensive-margin) model",
            "### Worked example (discrete, not continuous)",
            "## Practical examples",
        ]:
            with self.subTest(heading=heading):
                self.assertIn(heading, self.qmd_text)

    def test_lamport_style_proof(self) -> None:
        self.assertIn("Proof (Lamport style).", self.qmd_text)
        self.assertIn("QED", self.qmd_text)
        self.assertRegex(self.qmd_text, r"\n1\. \*Given\*")

    def test_diagrams_present(self) -> None:
        self.assertIn("```{mermaid}", self.qmd_text)
        self.assertIn("```{tikz}", self.qmd_text)

    def test_practical_examples_present(self) -> None:
        self.assertIn("Practical examples", self.qmd_text)
        self.assertRegex(self.qmd_text, r"- \*\*Query-level time savings:\*\*")

    def test_bibliography_entries_parse(self) -> None:
        entries = parse_bib_entries(self.bib_text)
        self.assertGreater(len(entries), 0, "No bibliography entries found.")
        for key, entry in entries:
            with self.subTest(key=key):
                balance = entry.count("{") - entry.count("}")
                self.assertEqual(balance, 0, f"Unbalanced braces in {key}.")

    def test_citations_resolve(self) -> None:
        citations = extract_citations(self.qmd_text)
        self.assertGreater(len(citations), 0, "No citations found in QMD.")
        bib_keys = {key for key, _ in parse_bib_entries(self.bib_text)}
        missing = sorted(set(citations) - bib_keys)
        self.assertEqual(missing, [], f"Missing citations in ai.bib: {missing}")


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
            "(2) Cadillac tasks are discussed in the discrete context; "
            "(3) The worked example is discrete (unit-demand or setup-cost), not continuous; "
            "(4) Proofs are structured in Lamport style with numbered steps; "
            "(5) Diagrams are present and likely legible; "
            "(6) Practical examples are included; "
            "(7) Claims with citations look plausible and not obviously mismatched. "
            "Return JSON: {\"pass\": true/false, \"notes\": "
            "\"...\"}. If any criterion is missing or dubious, set pass=false and explain.\n\n"
            f"QMD:\n{qmd_text}"
        )
        result = call_llm(prompt)
        self.assertIn("pass", result)
        self.assertTrue(result["pass"], result.get("notes", "LLM failed quality gate."))


if __name__ == "__main__":
    unittest.main()
