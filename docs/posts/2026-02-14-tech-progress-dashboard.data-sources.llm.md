---
draft: true
---

# Tech Progress Dashboard — Data Source Landscape (Research Log)

_Last updated: 2026-02-14_

## 0) Implementation status update (2026-02-14)

- Canonical dashboard source is now `posts/2026-02-14-tech-progress-dashboard.llm.qmd`.
- Canonical data seed is `posts/data/tech-progress-dashboard.llm/seed-series.llm.csv`.
- Generated outputs are:
  - `posts/data/tech-progress-dashboard.llm/normalized-series.llm.csv`
  - `posts/data/tech-progress-dashboard.llm/tpd-data.llm.js`
  - `posts/data/tech-progress-dashboard.llm/ingest-log.llm.md`
- New optimization-focused series added for this pass:
  - Matrix multiplication exponent timeline (algorithmic speed proxy)
  - Hutter Prize compression history (enwik8 and enwik9)
  - Wi-Fi peak spectral-efficiency proxy from IEEE 802.11 generation specs
- New AI/ML trend-index series added for this pass:
  - Training compute index, training cost index, training power index, hardware efficiency index (derived from Epoch growth-rate statements)

## 1) Scope definition (v1)

### Goal
Build a maintainable, high-trust dataset of **technology progress time series** for use in `posts/2026-02-14-tech-progress-dashboard.llm.qmd`.

### Time scope
- Include data points from **1950 onward**.
- Prefer series with annual observations; allow coarser frequencies only when they represent key frontier milestones.

### Metric scope
Include series that track one of the following:
1. **Cost decline** (e.g., inflation-adjusted $/unit performance)
2. **Performance improvement** (e.g., speed, efficiency, accuracy, yield)
3. **Scale and diffusion** (e.g., deployment, adoption, capacity)
4. **Input intensity** (e.g., compute used in training, R&D effort)

### Domain scope
- Compute hardware and semiconductors
- AI/ML model capability and compute
- Energy generation and storage
- Communications and networking
- Biotech/health technology
- Manufacturing and industrial productivity
- Agriculture (selected benchmark technologies)
- Transportation systems

### Out-of-scope (for now)
- Pre-1950 historical reconstructions
- Single-paper one-off benchmark results with no replicable update path
- Data locked behind expensive subscriptions unless a consistent legal extraction path exists

---

## 2) Quality bar and scoring rubric

Each source is scored on 5 dimensions (1–5):

- **Coverage**: length and completeness (1950+ preferred)
- **Methodological quality**: transparent definitions, data provenance, revision policy
- **Accessibility**: open download/API, machine-readability, legal reuse clarity
- **Updateability**: likely to keep updating for future dashboard refreshes
- **Operational fit**: ease of integrating into normalized long-format pipeline

### Tiers
- **Tier A (include now)**: total score >= 22/25, no red flags
- **Tier B (include selectively)**: 17–21, with caveats documented
- **Tier C (monitor / not yet include)**: <= 16 or major access/provenance issues

---

## 3) Candidate source longlist (deep scan)

## Compute hardware, semiconductors, AI compute

| Source                                   | Example metrics                            |                      Coverage | Access                                | Quality notes                                                                          | Score | Tier |
|------------------------------------------|--------------------------------------------|------------------------------:|---------------------------------------|----------------------------------------------------------------------------------------|------:|------|
| Our World in Data (OWID) grapher         | Transistors/chip, FLOPS/$, storage price   | Varies; many start 1950–1980s | CSV + API-like URL params; open       | Strong docs, reproducible, easy extraction; often sourced from underlying institutions |    24 | A    |
| OpenAlex                                 | AI paper counts, citations by field        |   1950s+ publication metadata | Open API + snapshots                  | Massive coverage, good for diffusion proxies; requires careful field classification    |    22 | A    |
| Crossref                                 | DOI publication trends, venue metadata     |     Broad historical coverage | Open API                              | Good scale; noisier than curated bibliometric sources                                  |    19 | B    |
| arXiv bulk metadata                      | CS/AI preprint trends                      |                         1991+ | Open bulk + API                       | Clean for modern AI era, not 1950-complete                                             |    17 | B    |
| TOP500                                   | Frontier supercomputer LINPACK performance |                1993+ biannual | Public lists/download                 | Trusted frontier proxy; no 1950s coverage                                              |    18 | B    |
| MLPerf results                           | Training/inference performance curves      |                        ~2018+ | Public tables                         | High benchmark quality but short horizon                                               |    14 | C    |
| Epoch AI dataset pages                   | Frontier model training compute            |                  Mostly 2010+ | Public with mixed machine-readability | Substantive but methodology can evolve; verify each datapoint                          |    17 | B    |
| SemiAnalysis articles/data snippets      | AI hardware economics                      |                        Recent | Mostly paywalled                      | Valuable context but weak reproducible access                                          |    10 | C    |
| Semiconductor Industry Association (SIA) | Industry shipments/sales                   |                 Late 20th c.+ | Reports (mixed openness)              | Useful aggregate indicators; sometimes paywalled details                               |    15 | C    |
| FRED (selected semiconductor indexes)    | Price indexes, producer prices             |        Various; often decades | API                                   | Reliable for macro proxies, less direct technical frontier                             |    20 | B    |

## Energy generation, storage, and power systems

| Source                                     | Example metrics                                     |          Coverage | Access                                   | Quality notes                                                      | Score | Tier |
|--------------------------------------------|-----------------------------------------------------|------------------:|------------------------------------------|--------------------------------------------------------------------|------:|------|
| IEA Data Browser                           | Electricity generation tech mix, efficiency, prices |       Often 1960+ | Mixed: many series free, some restricted | High quality official source; access terms vary                    |    21 | B    |
| EIA (US Energy Information Administration) | Generation costs, fuel efficiency, capacity         | Many series 1949+ | Open API + downloads                     | Excellent long-run US series, consistent metadata                  |    24 | A    |
| Lazard LCOE reports                        | Utility-scale cost benchmarks                       |            ~2009+ | Public PDF                               | Good for modern cost snapshots; short horizon, methodology changes |    14 | C    |
| NREL ATB                                   | Forward-looking cost/performance assumptions        |      Mostly 2010+ | Public CSV                               | Great structure but not long-run historical primary source         |    15 | C    |
| BP Statistical Review / Energy Institute   | Global energy production/consumption                |            ~1965+ | Public spreadsheets                      | Long history, broadly used, transparent revisions                  |    22 | A    |
| Ember electricity datasets                 | Power-sector trends                                 |      mostly 2000+ | Open downloads                           | Strong recent coverage, not enough historical depth alone          |    16 | C    |
| BNEF battery price announcements           | Li-ion pack $/kWh                                   |            2010s+ | Mostly press releases                    | Important indicator but source data often not fully open           |    14 | C    |
| IRENA renewables cost database             | Utility-scale technology costs                      |            ~2010+ | Public reports/data                      | Good methodology, insufficient pre-2000 depth                      |    16 | C    |

## Communications and digital infrastructure

| Source                                      | Example metrics                                   |                             Coverage | Access                          | Quality notes                                            | Score | Tier |
|---------------------------------------------|---------------------------------------------------|-------------------------------------:|---------------------------------|----------------------------------------------------------|------:|------|
| ITU (International Telecommunication Union) | Broadband subscriptions, telecom diffusion        |        Several series from 1960s/70s | Public tables + API-like access | Canonical global telecom source; some usability friction |    22 | A    |
| OECD broadband portal                       | Prices, speeds, subscriptions                     |                        Mostly 1990s+ | Open tables/API                 | High trust for OECD countries; narrower geography        |    20 | B    |
| World Bank WDI                              | Internet users, secure servers, telecom variables | Many series 1960+ depending variable | Open API + bulk CSV             | Excellent operational access and metadata                |    23 | A    |
| FCC data (US)                               | Broadband deployment/performance                  |                           Modern era | Public releases                 | Good US detail but short horizon                         |    15 | C    |
| Cisco annual internet reports (archival)    | Traffic growth                                    |                               2000s+ | Public PDFs                     | Useful context but report methodology evolved            |    13 | C    |

## Manufacturing, macro productivity, technology diffusion proxies

| Source                                  | Example metrics                                      |            Coverage | Access           | Quality notes                                                     | Score | Tier |
|-----------------------------------------|------------------------------------------------------|--------------------:|------------------|-------------------------------------------------------------------|------:|------|
| Penn World Table (PWT)                  | TFP, capital deepening                               |               1950+ | Open downloads   | Standard in growth accounting; model-based estimates need caveats |    22 | A    |
| EU KLEMS / World KLEMS                  | Sector productivity and ICT capital                  |         Often 1970+ | Open downloads   | Great granularity, weaker pre-1970 coverage                       |    20 | B    |
| Conference Board Total Economy Database | Productivity levels and growth                       |        Mid-20th c.+ | Public downloads | High-quality macro benchmark                                      |    21 | B    |
| UNIDO INDSTAT (where accessible)        | Industrial output and intensity                      |              Varies | Mixed access     | Valuable, but access constraints in some components               |    15 | C    |
| FRED macro series                       | Price deflators, productivity, industrial production | Many start pre-1950 | Open API         | Strong operational backbone for normalization/deflation           |    23 | A    |

## Agriculture and food technology

| Source                                | Example metrics                   |          Coverage | Access          | Quality notes                                                               | Score | Tier |
|---------------------------------------|-----------------------------------|------------------:|-----------------|-----------------------------------------------------------------------------|------:|------|
| FAOSTAT                               | Crop yields, inputs, production   |             1961+ | Open API + bulk | Global, consistent, machine-readable                                        |    23 | A    |
| USDA Quick Stats                      | US yields, adoption, productivity | Many series 1950+ | Open API        | Excellent US depth and metadata                                             |    24 | A    |
| Our World in Data agriculture grapher | Harmonized yield/diet/land series |            Varies | Open CSV        | Great dashboard-ready integration; verify underlying source transformations |    22 | A    |
| ASTI (agricultural R&D indicators)    | R&D spending and personnel        |      Mostly 1980+ | Public tables   | Important input proxy, but limited long-run depth                           |    17 | B    |

## Biotech and health technology

| Source                                    | Example metrics           |                        Coverage | Access        | Quality notes                                                 | Score | Tier |
|-------------------------------------------|---------------------------|--------------------------------:|---------------|---------------------------------------------------------------|------:|------|
| NIH RePORTER / historical NIH funding     | Biomedical R&D inputs     |         Mid-20th c.+ aggregates | API + files   | Good funding signals; variable granularity over time          |    20 | B    |
| FDA (Drugs@FDA, device approvals)         | Approval counts/timelines | Modern electronic era primarily | Public DB     | Robust for modern period; weak earlier machine-readable data  |    16 | C    |
| CDC/NCHS (selected tech-related outcomes) | Mortality/outcome proxies |                 Long historical | Open datasets | Useful as outcomes, less direct as technical frontier measure |    18 | B    |
| GenBank growth statistics (NCBI)          | Sequence database scale   |                          1980s+ | Public        | Useful diffusion proxy; not direct performance/cost           |    17 | B    |

## Patents, innovation intensity, cross-domain

| Source                              | Example metrics                           |                                                   Coverage | Access                               | Quality notes                                         | Score | Tier |
|-------------------------------------|-------------------------------------------|-----------------------------------------------------------:|--------------------------------------|-------------------------------------------------------|------:|------|
| USPTO PatentsView                   | Patent counts, citations, classifications | 1976+ structured modern data; historical text back further | API + bulk                           | High-quality US patent backbone                       |    21 | B    |
| EPO PATSTAT (via access agreements) | Global patent panel data                  |                                            Long historical | Restricted/licensed                  | Very strong data quality but access barriers          |    15 | C    |
| WIPO IP statistics                  | Patent applications by country/field      |                                               Multi-decade | Public downloads                     | Strong international comparability at aggregate level |    21 | B    |
| OECD STAN / ANBERD / MSTI           | R&D, industry innovation stats            |                                                Often 1970+ | Mixed (some open, some subscription) | High quality but access friction                      |    18 | B    |

---

## 4) Shortlist for immediate integration (recommended subset)

These are highest-priority because they combine 1950+ relevance, quality, and accessible extraction:

1. **OWID Grapher series** (cross-domain normalized quick wins)
2. **EIA API** (US energy long-run, 1949+ in many series)
3. **World Bank WDI API** (cross-country diffusion and infrastructure)
4. **FAOSTAT + USDA Quick Stats** (agriculture and biological productivity anchors)
5. **FRED API** (deflators + macro-normalization backbones)
6. **PWT** (macro productivity context)
7. **BP/Energy Institute Statistical Review** (global energy long-run)
8. **ITU datasets** (communications diffusion)

Secondary additions after MVP:
- WIPO/PatentsView for innovation intensity overlays
- TOP500 for compute frontier scaling (1993+)
- Epoch AI model-compute series (careful provenance tagging)

---

## 5) Proposed ongoing pipeline (for future source additions)

## A. Repository structure

- `posts/2026-02-14-tech-progress-dashboard.data-sources.llm.md` (this human-readable research log)
- `posts/2026-02-14-tech-progress-dashboard.source-registry.llm.csv` (machine-readable source registry)
- `posts/data/tech-progress-dashboard.llm/seed-series.llm.csv` (canonical seed rows)
- `posts/data/tech-progress-dashboard.llm/normalized-series.llm.csv` (normalized long-format panel)
- `posts/data/tech-progress-dashboard.llm/tpd-data.llm.js` (browser-ready bundle loaded by dashboard)
- `posts/data/tech-progress-dashboard.llm/raw/` (fetched raw extracts)

## B. Source intake workflow

1. **Discover** candidate source and add one row to registry with status `candidate`
2. **Score** using rubric (coverage/method/access/updateability/fit)
3. **License check**: verify legal reuse and citation requirements
4. **Extraction test**: confirm scriptable fetch and parse
5. **Quality audit**:
   - Missingness profile
   - Unit consistency
   - Breaks/redefinitions over time
   - Update cadence and revision handling
6. **Decision gate**:
   - Promote to `approved` if Tier A or strong Tier B with caveats
   - Otherwise set `watchlist` or `rejected`
7. **Integrate** into dashboard canonical schema
8. **Document** provenance note and assumptions in the post

## C. Canonical schema for series integration

For each final series keep:
- `id`, `name`, `domain`, `metric_type`, `frontier_class`, `direction`, `unit`
- `year`, `value`
- `source_name`, `source_url`
- `provenance_note`
- `quality_tier`, `last_verified_at`

## D. Quality controls before publish

- Check each selected series has at least 8 observations (or explicit frontier exception)
- Verify at least one citation URL resolves
- Validate no mixed nominal/real units without explicit deflator
- Confirm directionality (`higher_better` / `lower_better`) and transformations
- Keep changelog of source revisions affecting historical points

---

## 6) Known risks and mitigation

- **Risk: methodology changes over time** (e.g., benchmark definitions)
  - Mitigation: version-tag each source and keep per-series caveats.
- **Risk: paywalled sources become inaccessible**
  - Mitigation: prefer open replicas or use source only for contextual triangulation.
- **Risk: frontier series are sparse and noisy**
  - Mitigation: require minimum-point rule + robustness checks on trend fits.
- **Risk: mixed geographic scope (US-only vs global)**
  - Mitigation: encode geography explicitly and avoid combining incompatible units.

---

## 7) Next execution step

For the next pass, prioritize:
- Replacing formula-derived Epoch trend indexes with direct machine-readable per-model extracts.
- Extending optimization coverage with additional compression and channel-efficiency benchmarks from primary structured sources.
- Adding quality metadata fields (`quality_tier`, `last_verified_at`) into the dashboard provenance table.

Priority source integrations:
- OWID
- EIA
- World Bank WDI
- FAOSTAT
- USDA Quick Stats
- FRED
