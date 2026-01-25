from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional


@dataclass(frozen=True)
class TestResult:
    name: str
    ok: Optional[bool]  # True/False, or None for skipped/unknown
    category: str = "programmatic"
    detail: str = ""
    skipped: bool = False
    meta: dict[str, Any] | None = None

    def symbol(self) -> str:
        if self.ok is True:
            return "✅"
        if self.ok is False:
            return "❌"
        return "⏳"


@dataclass(frozen=True)
class ValidationContext:
    repo_root: Path
    qmd_path: Path
    bib_path: Path
    bib_tests_path: Path
    qmd_text: str


CheckFn = Callable[[ValidationContext], TestResult]

