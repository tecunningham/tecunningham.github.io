# Notes for AI assistants (Quarto blog repo)

## Rendering + caching (Quarto freeze)

- This repo enables Quarto freezing by default (`_quarto.yml` and `posts/_metadata.yml` set `freeze: true`), so HTML can show stale code output even after scripts change.
- To force a post to re-execute when rendering, use one of:
  - Add `freeze: false` to that post’s YAML.
  - Render with `quarto render <post>.qmd -M freeze:false --execute --no-cache`.
  - Delete/move the relevant `_freeze/posts/<post>/` directory and re-render.

## Citation gotchas in quoted text

- Pandoc/Quarto treats `@something` as a citation key.
- When quoting Twitter handles or similar text, use `&#64;handle` to display a literal `@handle` without triggering citations.

## Forecasts-of-growth validation tooling

Files:
- `posts/2025-10-19-forecasts-of-AI-growth.qmd` (includes an embedded “Validation Checks” block)
- `tools/forecasts_test.py` (prints a Markdown checklist used by the post)
- `posts/ai.bib` (bibliography, including `quote` + `growth_annual_excess`)
- `references/text/<citekey>.txt` (local fulltext snapshots)

What `tools/forecasts_test.py` checks:
- Citekeys in the QMD exist in `posts/ai.bib`.
- Forecast table rows have consistent column counts.
- QMD table `quote` and `growth` cells match `posts/ai.bib`.
- **Bib quotes match local fulltext** in `references/text/<citekey>.txt` for forecast-table entries when the local fulltext is “usable”.
  - Some sources block scraping (Cloudflare, paywalls, etc.); those local files may contain “verifying you are human”/permission errors and are treated as missing/unusable.

## Fetching local fulltext

- `tools/fetch_bib_texts.py` can populate `references/text/` from `text_url`/`url` fields (skips PDFs).
- Some sites will still block automated fetches; in that case you may need a manual copy or a different accessible `text_url`.

### Where to find fulltext versions

- **arXiv**: prefer HTML via `https://ar5iv.labs.arxiv.org/html/<id>` (good for quote-matching); PDF is `https://arxiv.org/pdf/<id>.pdf`.
- **PDF-first sources (BIS/ECB/working papers, etc.)**: `tools/fetch_bib_texts.py --pdf` downloads PDFs and extracts text via `pdftotext` (Poppler).
- **Twitter/X**: avoid citation parsing of `@handle` in Quarto by writing it as `&#64;handle` in quoted text.
- **Paywalls/bot checks (Bloomberg/OECD/IMF/etc.)**: the “fulltext” you fetch may be a Cloudflare/Akamai placeholder (“verifying you are human”, permission errors). Treat these as unusable and find an alternative mirror/cached copy (author site, arXiv preprint, institution PDF, etc.).

## Other post-specific tests

- `posts/2025-12-17-llm-time-saving-demand-theory-substitution.llm.qmd` runs `tools/test_llm_time_saving_qmd.py`.
  - Quarto’s execution CWD can vary; that post includes logic to locate the repo root before running the tool.
