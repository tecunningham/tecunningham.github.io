from __future__ import annotations

import base64
import json
import os
import re
import shutil
import subprocess

from ..core import TestResult, ValidationContext


def extract_mermaid_blocks(text: str) -> list[str]:
    pattern = re.compile(r"```\{mermaid\}\s*\n(.*?)\n```", re.DOTALL)
    return [m.group(1).strip() for m in pattern.finditer(text)]


def mermaid_lint_offline() -> callable:
    def _check(ctx: ValidationContext) -> TestResult:
        blocks = extract_mermaid_blocks(ctx.qmd_text)
        if not blocks:
            return TestResult(name="Mermaid syntax lint (offline)", ok=False, detail="(no Mermaid blocks found)")

        lint_errors: list[str] = []
        for i, code in enumerate(blocks, start=1):
            if "\\n" in code:
                lint_errors.append(f"block {i}: contains literal \\\\n escapes")
            for label in re.findall(r"\|([^|]*)\|", code):
                if "(" in label or ")" in label:
                    lint_errors.append(f"block {i}: parentheses in edge label {label!r}")

        ok = not lint_errors
        detail = ""
        if lint_errors:
            detail = f"({lint_errors[0]}{' ...' if len(lint_errors) > 1 else ''})"
        return TestResult(
            name="Mermaid syntax lint (offline)",
            ok=ok,
            detail=detail,
            meta={"blocks": len(blocks), "errors": lint_errors[:5]},
        )

    return _check


def mermaid_render_via_ink_optional() -> callable:
    def _check(ctx: ValidationContext) -> TestResult:
        if not os.getenv("MERMAID_INK_CHECK"):
            return TestResult(
                name="Mermaid renders via mermaid.ink",
                ok=None,
                skipped=True,
                detail="(set MERMAID_INK_CHECK=1 to enable)",
            )

        blocks = extract_mermaid_blocks(ctx.qmd_text)
        if not blocks:
            return TestResult(name="Mermaid renders via mermaid.ink", ok=False, detail="(no Mermaid blocks found)")

        curl = shutil.which("curl")
        if not curl:
            return TestResult(
                name="Mermaid renders via mermaid.ink",
                ok=None,
                skipped=True,
                detail="(curl not found)",
            )

        base_url = os.getenv("MERMAID_INK_BASE_URL", "https://mermaid.ink/svg/")
        for i, code in enumerate(blocks, start=1):
            payload = json.dumps({"code": code, "mermaid": {"theme": "default"}})
            b64 = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
            url = f"{base_url}{b64}"
            proc = subprocess.run(
                [curl, "-sS", "--max-time", "10", "-o", "/dev/null", "-w", "%{http_code}", url],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0:
                return TestResult(
                    name="Mermaid renders via mermaid.ink",
                    ok=None,
                    skipped=True,
                    detail=f"(curl error on block {i}: {(proc.stderr or '').strip()})",
                )
            if (proc.stdout or "").strip() != "200":
                return TestResult(
                    name="Mermaid renders via mermaid.ink",
                    ok=False,
                    detail=f"(HTTP {(proc.stdout or '').strip()} on block {i})",
                )

        return TestResult(name="Mermaid renders via mermaid.ink", ok=True, meta={"blocks": len(blocks)})

    return _check

