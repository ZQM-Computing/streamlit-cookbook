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

A Streamlit cookbook for Python data apps and geospatial exploration. It is intended for Python developers who turn analyses into shareable web applications. Examples should use synthetic or public data and must be validated against the reader's own software versions and environment before adoption.

## Repository role and maturity

**Status:** Examples Present — patterns are documented; fleet runtime validation remains pending.

This repository is part of the ZQM Computing geospatial portfolio. The series index is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

Automated checks cover only the paths and environments configured in this repository. Documentation, spot checks, and successful static checks do not establish production readiness or operational certification.

## Intended audience

Python developers building interactive data exploration apps, especially apps that present geospatial layers, filters, tables, and small local datasets.

## Prerequisites

- Python 3.12.10 and Streamlit 1.66.1 are the documented reference environment for the Node-1 wave11-venv spot check. Confirm the versions installed in your own environment before running examples.
- Use the dedicated project environment's Python/Streamlit executable; do not assume that a bare `python` command selects the intended virtual environment.
- Port 8501 must be available for the default local Streamlit server.
- The data-app example uses a local SQLite fixture. DuckDB/Postgres live connections are optional adaptations, not prerequisites for the documented examples.
- Do not run experimental examples as persistent production services.

## Examples

| # | Example | Maturity | What it demonstrates |
|---|---------|---------|----------------------|
| 01 | [First app](examples/01-first-app) | Written; runtime validation pending | Widgets, maps, and tables |
| 02 | [Map app](examples/02-map-app) | Written; runtime validation pending | Interactive maps, filters, and layers |
| 03 | [Data app](examples/03-data-app) | Written; runtime validation pending | Querying a local SQLite fixture; optional database adaptations |
| 04 | [Deployment notes](examples/04-deploy-notes) | Documentation; runtime validation pending | Headless local smoke-run considerations |

## Repository layout

```text
streamlit-cookbook/
├── examples/
│   ├── 01-first-app/
│   ├── 02-map-app/
│   ├── 03-data-app/
│   └── 04-deploy-notes/
├── README.md
├── CONTRIBUTING.md
└── LICENSE
```

## Validate locally

The examples have not yet been independently runtime-validated across the fleet. For a disposable local environment:

1. Confirm the Python and Streamlit versions.
2. Review the selected example's README and inspect its data paths and dependencies.
3. Start the app with the environment's Streamlit executable, for example:

   ```bash
   streamlit run app.py --server.address 127.0.0.1 --server.port 8501
   ```

   Run the command from the example directory and adjust the entry-point filename to match that example.
4. Open the local app, exercise the main controls, and check the terminal for exceptions.
5. Confirm that all inputs are synthetic/public and that no unexpected external write or remote connection occurs.

A successful startup is only a smoke test. It does not establish correctness of spatial analysis, accessibility, security, performance, or deployment behavior.

## What this does not claim

- The examples are not certified for production use.
- A spot check of one environment does not establish that all examples work on every listed version or node.
- Optional DuckDB/Postgres connections are not claimed to be configured or tested.
- Localhost smoke-running is not a production deployment guide.
- No private geospatial datasets or participant data should be added to examples.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution and validation expectations. Report security issues privately to zqmcomputing@gmail.com; do not publish exploitable details in a public issue.

## Related patterns

- [GeoPandas Cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame joins, overlays, and spatial analysis.
- [DuckDB Spatial Cookbook](https://github.com/ZQM-Computing/duckdb-spatial-cookbook) — analytical geospatial SQL with DuckDB Spatial.
- [Folium Cookbook](https://github.com/ZQM-Computing/folium-cookbook) — interactive Leaflet maps from Python.

---

Part of the [ZQM Computing geospatial cookbook portfolio](https://github.com/ZQM-Computing/geospatial-cookbooks).
