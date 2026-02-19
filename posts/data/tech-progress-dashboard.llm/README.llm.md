---
draft:true
---

# Tech Progress Dashboard local data cache

This folder contains locally cached and normalized data used by:
- `posts/2026-02-14-tech-progress-dashboard.llm.qmd`

## Files
- `seed-series.llm.csv`: canonical seed panel (manual + curated rows).
- `normalized-series.llm.csv`: canonical long-format panel used for chart ingestion.
- `tpd-data.llm.js`: generated browser-ready `window.TPD_DATA` bundle loaded by the dashboard page.
- `ingest-log.llm.md`: last ingestion summary (counts and replacement coverage).
- `raw/`: raw downloaded source extracts (currently OWID grapher CSVs).

## Refresh
Run:

```bash
python tools/ingest_tech_progress_dashboard.py
```

The script reads `seed-series.llm.csv`, refreshes downloadable sources when available, adds derived series, and writes:
- `normalized-series.llm.csv`
- `tpd-data.llm.js`
- `ingest-log.llm.md`
