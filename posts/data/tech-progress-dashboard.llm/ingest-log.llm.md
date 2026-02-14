# Tech Progress Dashboard ingestion log

- Source post: `posts/2026-02-14-tech-progress-dashboard.llm.qmd`
- Seed rows parsed from embedded JS: **84**
- Series replaced with fresh OWID downloads: **transistors_per_chip, us_corn_yield, solar_pv_module_price, hdd_cost_per_gb**
- Final normalized rows: **260**

## Notes
- This pipeline keeps seed data for sources that are not yet script-downloaded (e.g., BNEF, Green500, NHGRI page-based data).
- All rows are normalized to a single long-format CSV for local dashboard ingestion.
