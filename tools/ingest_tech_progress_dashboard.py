#!/usr/bin/env python3
"""Ingest and normalize data for the tech progress dashboard post.

Pipeline:
- Read canonical seed rows from CSV.
- Optionally refresh selected OWID-backed series when network is available.
- Add derived AI/ML trend-index series from Epoch-reported growth rates.
- Write normalized CSV plus JS bundle consumed directly by the dashboard page.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
POST_PATH = ROOT / "posts/2026-02-14-tech-progress-dashboard.llm.qmd"
OUT_DIR = ROOT / "posts/data/tech-progress-dashboard.llm"
RAW_DIR = OUT_DIR / "raw"
SEED_CSV = OUT_DIR / "seed-series.llm.csv"
NORMALIZED_CSV = OUT_DIR / "normalized-series.llm.csv"
JS_BUNDLE = OUT_DIR / "tpd-data.llm.js"
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

# Source: https://epoch.ai/gradient-updates/how-has-ai-progress-changed-over-time
# Values are growth factors described in the article and encoded as yearly indexes.
DERIVED_SERIES = [
    {
        "id": "ai_training_compute_index_epoch",
        "name": "AI training compute index (Epoch trend)",
        "domain": "ai-ml",
        "metric_type": "training-scale",
        "frontier_class": "frontier",
        "direction": "higher_better",
        "unit": "index (2010=1)",
        "start_year": 2010,
        "end_year": 2025,
        "base_value": 1.0,
        "annual_factor": 4.4,
        "source_name": "Epoch AI",
        "source_url": "https://epoch.ai/gradient-updates/how-has-ai-progress-changed-over-time",
        "provenance_note": "Derived index from reported ~4.4x annual growth in notable AI training compute since 2010.",
    },
    {
        "id": "ai_training_cost_index_epoch",
        "name": "AI training cost index (Epoch trend)",
        "domain": "ai-ml",
        "metric_type": "training-scale",
        "frontier_class": "frontier",
        "direction": "higher_better",
        "unit": "index (2018=1)",
        "start_year": 2018,
        "end_year": 2025,
        "base_value": 1.0,
        "annual_factor": 2.4,
        "source_name": "Epoch AI",
        "source_url": "https://epoch.ai/gradient-updates/how-has-ai-progress-changed-over-time",
        "provenance_note": "Derived index from reported ~2.4x annual growth in training expenditure since 2018.",
    },
    {
        "id": "ai_training_power_index_epoch",
        "name": "AI training power requirement index (Epoch trend)",
        "domain": "ai-ml",
        "metric_type": "training-scale",
        "frontier_class": "frontier",
        "direction": "higher_better",
        "unit": "index (2015=1)",
        "start_year": 2015,
        "end_year": 2025,
        "base_value": 1.0,
        "annual_factor": 2.0,
        "source_name": "Epoch AI",
        "source_url": "https://epoch.ai/gradient-updates/how-has-ai-progress-changed-over-time",
        "provenance_note": "Derived index from reported annual doubling of power requirements for notable AI model training.",
    },
    {
        "id": "ai_hardware_efficiency_index_epoch",
        "name": "AI hardware efficiency index (Epoch trend)",
        "domain": "ai-ml",
        "metric_type": "optimization-efficiency",
        "frontier_class": "frontier",
        "direction": "higher_better",
        "unit": "index (2014=1)",
        "start_year": 2014,
        "end_year": 2024,
        "base_value": 1.0,
        "annual_factor": math.pow(12.0, 1.0 / 10.0),
        "source_name": "Epoch AI",
        "source_url": "https://epoch.ai/gradient-updates/how-has-ai-progress-changed-over-time",
        "provenance_note": "Derived index from reported ~12x improvement in AI hardware efficiency across the prior decade.",
    },
]


def _clean_text(value: str) -> str:
    return (value or "").strip()


def _parse_year(raw: str) -> int | None:
    try:
        y = int(float(raw))
        return y if y >= 1950 else None
    except Exception:
        return None


def _parse_value(raw: str) -> float | None:
    try:
        v = float(raw)
        return v if math.isfinite(v) and v > 0 else None
    except Exception:
        return None


def read_seed_rows_from_csv() -> list[dict]:
    if not SEED_CSV.exists():
        raise FileNotFoundError(f"Missing seed CSV: {SEED_CSV}")

    rows: list[dict] = []
    with SEED_CSV.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row or not _clean_text(row.get("id", "")):
                continue

            year = _parse_year(row.get("year", ""))
            value = _parse_value(row.get("value", ""))
            if year is None or value is None:
                continue

            norm = {
                "id": _clean_text(row.get("id", "")),
                "name": _clean_text(row.get("name", "")),
                "domain": _clean_text(row.get("domain", "")),
                "metric_type": _clean_text(row.get("metric_type", "")),
                "frontier_class": _clean_text(row.get("frontier_class", "")) or "frontier",
                "direction": _clean_text(row.get("direction", "")) or "higher_better",
                "unit": _clean_text(row.get("unit", "")),
                "year": str(year),
                "value": str(value),
                "source_name": _clean_text(row.get("source_name", "")),
                "source_url": _clean_text(row.get("source_url", "")),
                "provenance_note": _clean_text(row.get("provenance_note", "")),
            }

            if norm["direction"] not in {"higher_better", "lower_better"}:
                continue
            rows.append(norm)

    return rows


def fetch_csv(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def normalize_owid_rows(series_id: str, metadata: dict) -> tuple[list[dict], str]:
    cfg = OWID_CONFIG[series_id]
    url = f"https://ourworldindata.org/grapher/{cfg['slug']}.csv"
    raw_text = fetch_csv(url)

    rows: list[dict] = []
    parsed = csv.DictReader(raw_text.splitlines())
    for row in parsed:
        if row.get("Entity") != cfg["entity"]:
            continue
        year = _parse_year(row.get("Year", ""))
        value = _parse_value(row.get(cfg["value_col"], ""))
        if year is None or value is None:
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
                "year": str(year),
                "value": str(value),
                "source_name": cfg["source_name"],
                "source_url": cfg["source_url"],
                "provenance_note": (
                    f"Auto-ingested from OWID grapher slug '{cfg['slug']}' "
                    f"filtered to Entity={cfg['entity']}."
                ),
            }
        )

    rows.sort(key=lambda r: int(r["year"]))
    return rows, raw_text


def generate_derived_series_rows() -> list[dict]:
    rows: list[dict] = []
    for spec in DERIVED_SERIES:
        for year in range(spec["start_year"], spec["end_year"] + 1):
            value = spec["base_value"] * (spec["annual_factor"] ** (year - spec["start_year"]))
            rows.append(
                {
                    "id": spec["id"],
                    "name": spec["name"],
                    "domain": spec["domain"],
                    "metric_type": spec["metric_type"],
                    "frontier_class": spec["frontier_class"],
                    "direction": spec["direction"],
                    "unit": spec["unit"],
                    "year": str(year),
                    "value": str(value),
                    "source_name": spec["source_name"],
                    "source_url": spec["source_url"],
                    "provenance_note": spec["provenance_note"],
                }
            )
    return rows


def dedupe_rows(rows: list[dict]) -> list[dict]:
    # Last writer wins for duplicated (id, year) keys.
    merged: dict[tuple[str, str], dict] = {}
    for row in rows:
        merged[(row["id"], row["year"])] = row
    return sorted(merged.values(), key=lambda r: (r["id"], int(r["year"])))


def write_normalized(rows: list[dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with NORMALIZED_CSV.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CANONICAL_COLUMNS, lineterminator="\n")
        w.writeheader()
        for row in rows:
            w.writerow({k: row.get(k, "") for k in CANONICAL_COLUMNS})


def write_js_bundle(rows: list[dict]) -> None:
    payload = []
    for row in rows:
        payload.append(
            {
                "id": row["id"],
                "name": row["name"],
                "domain": row["domain"],
                "metric_type": row["metric_type"],
                "frontier_class": row["frontier_class"],
                "direction": row["direction"],
                "unit": row["unit"],
                "year": int(row["year"]),
                "value": float(row["value"]),
                "source_name": row["source_name"],
                "source_url": row["source_url"],
                "provenance_note": row["provenance_note"],
            }
        )
    JS_BUNDLE.write_text(
        "window.TPD_DATA = " + json.dumps(payload, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )


def main() -> None:
    seed_rows = read_seed_rows_from_csv()
    seed_meta: dict[str, dict] = {}
    for row in seed_rows:
        seed_meta.setdefault(row["id"], row)

    RAW_DIR.mkdir(parents=True, exist_ok=True)

    replaced_ids: list[str] = []
    replacement_rows: list[dict] = []
    for series_id in OWID_CONFIG:
        if series_id not in seed_meta:
            continue
        try:
            rows, raw_text = normalize_owid_rows(series_id, seed_meta[series_id])
            if rows:
                replaced_ids.append(series_id)
                replacement_rows.extend(rows)
                (RAW_DIR / f"owid-{OWID_CONFIG[series_id]['slug']}.csv").write_text(
                    raw_text,
                    encoding="utf-8",
                )
        except Exception:
            # Fall back to seed rows if download fails.
            pass

    derived_rows = generate_derived_series_rows()

    replaced_set = set(replaced_ids)
    kept_seed_rows = [r for r in seed_rows if r["id"] not in replaced_set]
    final_rows = dedupe_rows(kept_seed_rows + replacement_rows + derived_rows)

    write_normalized(final_rows)
    write_js_bundle(final_rows)

    unique_series = len({r["id"] for r in final_rows})
    log_lines = [
        "# Tech Progress Dashboard ingestion log",
        "",
        f"- Source post: `{POST_PATH.relative_to(ROOT)}`",
        f"- Source seed CSV: `{SEED_CSV.relative_to(ROOT)}`",
        f"- Seed rows parsed from CSV: **{len(seed_rows)}**",
        f"- Series replaced with fresh OWID downloads: **{', '.join(replaced_ids) if replaced_ids else '(none)'}**",
        f"- Derived AI/ML trend rows added: **{len(derived_rows)}**",
        f"- Final normalized rows: **{len(final_rows)}**",
        f"- Final unique series: **{unique_series}**",
        f"- JS bundle written: `{JS_BUNDLE.relative_to(ROOT)}`",
        "",
        "## Notes",
        "- If OWID download fails, seed rows are retained for those series.",
        "- Derived AI/ML trend indexes are formula-based from Epoch growth-rate statements and are not raw point extracts.",
        "- Dashboard reads `window.TPD_DATA` from the generated JS bundle.",
    ]
    INGEST_LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
