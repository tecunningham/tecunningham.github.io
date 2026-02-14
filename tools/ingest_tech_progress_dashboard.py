#!/usr/bin/env python3
"""Ingest and normalize data for the tech progress dashboard post.

- Reads seed data embedded in the post's `TPD_DATA` JS array.
- Downloads open-source replacements for selected series (currently OWID).
- Writes raw downloads + normalized long-format panel for local use.
"""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
POST_PATH = ROOT / "posts/2026-02-14-tech-progress-dashboard.llm.qmd"
OUT_DIR = ROOT / "posts/data/tech-progress-dashboard.llm"
RAW_DIR = OUT_DIR / "raw"
NORMALIZED_CSV = OUT_DIR / "normalized-series.llm.csv"
INGEST_LOG = OUT_DIR / "ingest-log.llm.md"

CANONICAL_COLUMNS = [
    "id",
    "name",
    "domain",
    "metric_type",
    "frontier_class",
    "direction",
    "unit",
    "year",
    "value",
    "source_name",
    "source_url",
    "provenance_note",
]

OWID_CONFIG = {
    "transistors_per_chip": {
        "slug": "transistors-per-microprocessor",
        "value_col": "Transistors per microprocessor",
        "entity": "World",
        "source_name": "Our World in Data",
        "source_url": "https://ourworldindata.org/grapher/transistors-per-microprocessor",
    },
    "us_corn_yield": {
        "slug": "maize-yields",
        "value_col": "Maize yield",
        "entity": "United States",
        "source_name": "USDA/FAO via OWID",
        "source_url": "https://ourworldindata.org/grapher/maize-yields",
    },
    "solar_pv_module_price": {
        "slug": "solar-pv-prices",
        "value_col": "Solar PV module cost",
        "entity": "World",
        "source_name": "Our World in Data",
        "source_url": "https://ourworldindata.org/grapher/solar-pv-prices",
    },
    "hdd_cost_per_gb": {
        "slug": "historical-cost-of-computer-memory-and-storage",
        "value_col": "Disk",
        "entity": "World",
        "source_name": "Our World in Data",
        "source_url": "https://ourworldindata.org/grapher/historical-cost-of-computer-memory-and-storage",
    },
}


def extract_seed_rows_from_qmd() -> list[dict]:
    text = POST_PATH.read_text(encoding="utf-8")
    start_marker = "const TPD_DATA = ["
    end_marker = "];"
    start = text.index(start_marker) + len("const TPD_DATA = ")
    end = text.index(end_marker, start)
    js_array = text[start:end + 1]

    node_script = (
        "const fs = require('fs');"
        "const data = "
        f"{js_array};"
        "process.stdout.write(JSON.stringify(data));"
    )
    out = subprocess.check_output(["node", "-e", node_script], text=True)
    rows = json.loads(out)
    return [r for r in rows if int(r.get("year", 0)) >= 1950]


def fetch_csv(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize_owid_rows(series_id: str, metadata: dict) -> tuple[list[dict], str]:
    cfg = OWID_CONFIG[series_id]
    url = f"https://ourworldindata.org/grapher/{cfg['slug']}.csv"
    raw_text = fetch_csv(url)

    rows = []
    parsed = csv.DictReader(raw_text.splitlines())
    for row in parsed:
        if row.get("Entity") != cfg["entity"]:
            continue
        year = row.get("Year")
        value = row.get(cfg["value_col"])
        if not year or not value:
            continue
        y = int(float(year))
        if y < 1950:
            continue

        rows.append(
            {
                "id": series_id,
                "name": metadata["name"],
                "domain": metadata["domain"],
                "metric_type": metadata["metric_type"],
                "frontier_class": metadata["frontier_class"],
                "direction": metadata["direction"],
                "unit": metadata["unit"],
                "year": str(y),
                "value": str(float(value)),
                "source_name": cfg["source_name"],
                "source_url": cfg["source_url"],
                "provenance_note": f"Auto-ingested from OWID grapher slug '{cfg['slug']}' filtered to Entity={cfg['entity']}.",
            }
        )

    rows.sort(key=lambda r: int(r["year"]))
    return rows, raw_text


def write_normalized(rows: list[dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with NORMALIZED_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CANONICAL_COLUMNS)
        w.writeheader()
        for row in sorted(rows, key=lambda r: (r["id"], int(r["year"]))):
            w.writerow({k: row.get(k, "") for k in CANONICAL_COLUMNS})


def main() -> None:
    seed_rows = extract_seed_rows_from_qmd()
    seed_meta = {}
    for row in seed_rows:
        seed_meta.setdefault(row["id"], row)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    replaced_ids = []
    replacement_rows = []
    for series_id in OWID_CONFIG:
        if series_id not in seed_meta:
            continue
        try:
            rows, raw_text = normalize_owid_rows(series_id, seed_meta[series_id])
            if rows:
                replaced_ids.append(series_id)
                replacement_rows.extend(rows)
                (RAW_DIR / f"owid-{OWID_CONFIG[series_id]['slug']}.csv").write_text(raw_text, encoding="utf-8")
        except Exception:
            # Fall back to seed rows if download fails.
            pass

    kept_seed_rows = [r for r in seed_rows if r["id"] not in set(replaced_ids)]
    final_rows = kept_seed_rows + replacement_rows
    write_normalized(final_rows)

    log_lines = [
        "# Tech Progress Dashboard ingestion log",
        "",
        f"- Source post: `{POST_PATH.relative_to(ROOT)}`",
        f"- Seed rows parsed from embedded JS: **{len(seed_rows)}**",
        f"- Series replaced with fresh OWID downloads: **{', '.join(replaced_ids) if replaced_ids else '(none)'}**",
        f"- Final normalized rows: **{len(final_rows)}**",
        "",
        "## Notes",
        "- This pipeline keeps seed data for sources that are not yet script-downloaded (e.g., BNEF, Green500, NHGRI page-based data).",
        "- All rows are normalized to a single long-format CSV for local dashboard ingestion.",
    ]
    INGEST_LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
