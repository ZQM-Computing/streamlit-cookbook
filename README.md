# Streamlit Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **Streamlit cookbook** — Python data apps for geospatial exploration. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). It is intended for Python developers who turn analyses into shareable web apps. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** Streamlit patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who turn analyses into shareable web apps.

## Prerequisites

- Streamlit 1.66.1 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Streamlit by full path, never bare `python` (hermes venv)
- SQLite (standard library) for the 03 data fixture; DuckDB/Postgres live connections are validation items, not asserted
- Port 8501 (Streamlit default) free for smoke runs; no persistent service is installed by these patterns

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-first-app](examples/01-first-app) | A first app: widgets, maps, and tables | Written (design-only) |
| 02 | [examples/02-map-app](examples/02-map-app) | Interactive maps with filters and layers | Written (design-only) |
| 03 | [examples/03-data-app](examples/03-data-app) | Querying a database from an app (SQLite fixture; DuckDB/Postgres swap documented) | Written (design-only) |
| 04 | [examples/04-deploy-notes](examples/04-deploy-notes) | Running an app as a smoke-run service (headless, localhost, port 8501) | Written (design-only) |

## Repository layout

```text
streamlit-cookbook/
├── examples/
│   ├── 01-first-app/
│   ├── 02-map-app/
│   ├── 03-data-app/
│   └── 04-deploy-notes/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [duckdb-spatial-cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) — Analytical geospatial SQL with DuckDB Spatial
- [folium-cookbook](https://github.com/ZQM-Computing/folium-cookbook) — Interactive Leaflet maps from Python
