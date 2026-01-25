"""Shared validation framework for Quarto posts.

This package provides:
- A small, stable result model (`TestResult`)
- Reusable checks (citations, ai.bib conventions, Mermaid lint, etc.)
- Report rendering (text / JSON)
- Per-post plugin loading (plugins live in `tools/qmd_validate/posts/` and are
  named after the source QMD file, with an added `.py` suffix).
"""

