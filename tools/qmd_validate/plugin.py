from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional

from .core import CheckFn, TestResult, ValidationContext


@dataclass(frozen=True)
class PostPlugin:
    path: Path
    module: object

    def post_checks(self) -> list[CheckFn]:
        fn = getattr(self.module, "post_checks", None)
        if fn is None:
            return []
        return list(fn())  # type: ignore[misc]


def plugin_path_for_qmd(repo_root: Path, qmd_path: Path) -> Path:
    """Plugins are named after the QMD file, plus `.py`.

    Example:
      posts/2025-10-19-forecasts-of-AI-growth.qmd
      -> tools/qmd_validate/posts/2025-10-19-forecasts-of-AI-growth.qmd.py
    """
    return repo_root / "tools/qmd_validate/posts" / f"{qmd_path.name}.py"


def load_plugin(path: Path) -> PostPlugin:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load plugin module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return PostPlugin(path=path, module=module)


def run_plugin_checks(ctx: ValidationContext, plugin: PostPlugin) -> list[TestResult]:
    results: list[TestResult] = []
    for check in plugin.post_checks():
        try:
            results.append(check(ctx))
        except Exception as exc:
            results.append(
                TestResult(
                    name=getattr(check, "__name__", "plugin check"),
                    ok=False,
                    category="programmatic",
                    detail=f"(exception: {exc})",
                )
            )
    return results

