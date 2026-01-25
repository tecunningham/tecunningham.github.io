#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    # Allow `import tools.qmd_validate...` when executing this file directly.
    sys.path.insert(0, str(REPO_ROOT))

from tools.qmd_validate.core import ValidationContext
from tools.qmd_validate.plugin import load_plugin, plugin_path_for_qmd, run_plugin_checks
from tools.qmd_validate.report import overall_ok, render_json, render_text
from tools.qmd_validate.util import find_repo_root, read_text, to_json


def build_context(repo_root: Path, qmd_path: Path) -> ValidationContext:
    bib_path = repo_root / "posts/ai.bib"
    bib_tests_path = repo_root / "tools/ai.bib.tests.py"
    qmd_text = read_text(qmd_path)
    return ValidationContext(
        repo_root=repo_root,
        qmd_path=qmd_path,
        bib_path=bib_path,
        bib_tests_path=bib_tests_path,
        qmd_text=qmd_text,
    )


def discover_qmd_paths_from_plugins(repo_root: Path) -> list[Path]:
    plugin_dir = repo_root / "tools/qmd_validate/posts"
    if not plugin_dir.exists():
        return []
    qmds: list[Path] = []
    seen: set[Path] = set()
    for plugin in sorted(plugin_dir.glob("*.qmd.py")):
        qmd_name = plugin.name[: -len(".py")]
        qmd_path = repo_root / "posts" / qmd_name
        if qmd_path.exists() and qmd_path not in seen:
            qmds.append(qmd_path)
            seen.add(qmd_path)
    return qmds


def run_one(repo_root: Path, qmd_path: Path) -> dict:
    ctx = build_context(repo_root, qmd_path)
    plugin_path = plugin_path_for_qmd(repo_root, qmd_path)
    if not plugin_path.exists():
        raise SystemExit(f"No plugin for {qmd_path.name}. Expected: {plugin_path}")
    plugin = load_plugin(plugin_path)
    results = run_plugin_checks(ctx, plugin)
    return {"qmd": str(qmd_path), "results": results}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qmd", help="Path to a single QMD to validate.")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Validate all posts that have a plugin in tools/qmd_validate/posts/.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON output.")
    args = parser.parse_args()

    repo_root = find_repo_root(Path.cwd())

    if args.all:
        qmds = discover_qmd_paths_from_plugins(repo_root)
        payload = {"overall_ok": True, "posts": []}
        any_fail = False
        for qmd_path in qmds:
            post = run_one(repo_root, qmd_path)
            results = post["results"]
            post_json = render_json(results)
            post_json["qmd"] = post["qmd"]
            payload["posts"].append(
                {
                    "qmd": post["qmd"],
                    "overall_ok": post_json["overall_ok"],
                    "results": results,
                    "json": post_json,
                }
            )
            if not post_json["overall_ok"]:
                any_fail = True
        payload["overall_ok"] = not any_fail
        if args.json:
            print(
                to_json(
                    {
                        "overall_ok": payload["overall_ok"],
                        "posts": [p["json"] for p in payload["posts"]],
                    }
                )
            )
        else:
            for p in payload["posts"]:
                print(render_text(p["results"], title=f"Validation Checks ({p['qmd']})"))
                print()
        return 1 if any_fail else 0

    if not args.qmd:
        parser.error("Specify --qmd or --all")

    qmd_path = Path(args.qmd)
    if not qmd_path.is_absolute():
        qmd_path = repo_root / qmd_path

    post = run_one(repo_root, qmd_path)
    results = post["results"]
    if args.json:
        print(to_json(render_json(results)))
    else:
        print(render_text(results))
    return 0 if overall_ok(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
