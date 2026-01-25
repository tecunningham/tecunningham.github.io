from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_repo_root(start: Path) -> Path:
    """Best-effort repo root detection for Quarto execution contexts."""
    for candidate in [start, *start.parents]:
        if (candidate / "tools").is_dir() and (candidate / "posts").is_dir():
            return candidate
    return start


def to_json(obj: Any) -> str:
    return json.dumps(obj, indent=2, sort_keys=False)

