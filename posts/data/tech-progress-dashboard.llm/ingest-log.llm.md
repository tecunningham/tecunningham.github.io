# Tech Progress Dashboard ingestion log

- Source post: `posts/2026-02-14-tech-progress-dashboard.llm.qmd`
- Source seed CSV: `posts/data/tech-progress-dashboard.llm/seed-series.llm.csv`
- Seed rows parsed from CSV: **283**
- Series replaced with fresh OWID downloads: **(none)**
- Derived AI/ML trend rows added: **46**
- Final normalized rows: **329**
- Final unique series: **16**
- JS bundle written: `posts/data/tech-progress-dashboard.llm/tpd-data.llm.js`

## Notes
- If OWID download fails, seed rows are retained for those series.
- Derived AI/ML trend indexes are formula-based from Epoch growth-rate statements and are not raw point extracts.
- Dashboard reads `window.TPD_DATA` from the generated JS bundle.
