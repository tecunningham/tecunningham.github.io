from __future__ import annotations

import re

from tools.qmd_validate.checks import bib, common, mermaid
from tools.qmd_validate.core import TestResult, ValidationContext


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


def _proof_structure(ctx: ValidationContext) -> TestResult:
    ok = (
        ("Lamport" not in ctx.qmd_text)
        and ('collapse="true"' in ctx.qmd_text)
        and ("Proof (structured)" in ctx.qmd_text)
        and ("QED" in ctx.qmd_text)
        and (re.search(r"\n1\. \*Given\*", ctx.qmd_text) is not None)
    )
    return TestResult(name="proof structure (collapsed)", ok=ok)


def post_checks():
    return [
        common.required_substrings("required sections present", REQUIRED_HEADINGS),
        _proof_structure,
        common.required_substrings("estimation flowchart present", ["Estimation flowchart", "```{mermaid}", "flowchart TD"]),
        mermaid.mermaid_lint_offline(),
        mermaid.mermaid_render_via_ink_optional(),
        bib.ai_bib_conventions(),
        bib.citekeys_resolve(),
    ]

