# 01 — First app

A first Streamlit app: a title, a slider widget, a map, and a table —
all over five synthetic stations on a made-up grid (lat 10.01–10.05,
lon 20.01–20.04), not a real place.

## Run

```powershell
C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
```

Use the fleet wave11 Streamlit by full path. Never Node-1's bare
`python` (the hermes venv). The app serves on localhost:8501; stop the
process after verifying. No persistent service is installed by this
pattern (see `04-deploy-notes`).

## Expected output

- The browser page shows the title "First app: widgets, maps, tables".
- With the slider at 0, the metric reads 5 stations and the table has
  5 rows; the map shows 5 markers.
- With the slider at 30, the metric reads 3 stations (values 30, 40,
  50) and the table has 3 rows.
- Station values are 10, 20, 30, 40, 50 (sum 150, mean 30.0).

## Failure behavior

- `ModuleNotFoundError: streamlit` — you are not running the wave11
  venv's Streamlit; use the full path above.
- Port 8501 already in use — another smoke run is still alive; stop
  it first, then re-run. Do not leave smoke servers running.
- Blank map tiles at view time — the map tiles load from a CDN and
  need network access; markers render regardless.

## Versions and evidence

- Tool: Streamlit 1.66.1 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Port 8501 is Streamlit's default; no Streamlit
  service was started on the fleet.
- Evidence level: design-only (gate 1 target). The app file parses
  and its widget/map/table calls use the Streamlit API; serving it
  against the fleet venv and checking the counts above is **to
  confirm at validation**.
