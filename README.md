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

A **Streamlit cookbook** — Python data apps for geospatial exploration. Queued in wave-11 (per-node adds). Patterns are planned from the design, not yet from fleet runs. It is intended for Python developers who turn analyses into shareable web apps. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** Streamlit patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Python developers who turn analyses into shareable web apps.

## Prerequisites

- Streamlit in the fleet Python environment
- Python 3.11+
- GeoPandas or DuckDB for the data passes

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-first-app` | A first app: widgets, maps, and tables |
| 02 | `02-map-app` | Interactive maps with filters and layers |
| 03 | `03-data-app` | Querying DuckDB or Postgres from an app |
| 04 | `04-deploy-notes` | Running an app as a service |

## Repository layout

```text
streamlit-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
- [duckdb-spatial-cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) — Analytical geospatial SQL with DuckDB Spatial
- [folium-cookbook](https://github.com/ZQM-Computing/folium-cookbook) — Interactive Leaflet maps from Python
