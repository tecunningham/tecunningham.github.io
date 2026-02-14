# Tech Progress Dashboard local data cache

This folder contains locally cached and normalized data used by:
- `posts/2026-02-14-tech-progress-dashboard.llm.qmd`

## Files
- `normalized-series.llm.csv`: canonical long-format panel used for chart ingestion.
- `ingest-log.llm.md`: last ingestion summary (counts and replacement coverage).
- `raw/`: raw downloaded source extracts (currently OWID grapher CSVs).

## Refresh
Run:

```bash
python tools/ingest_tech_progress_dashboard.py
```

The script parses seed rows from the post, refreshes downloadable sources, and writes normalized output.
