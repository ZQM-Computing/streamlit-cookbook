# 02 — Map app

An interactive map app: a multiselect for point groups, a slider for
a minimum value, a checkbox toggling the map, and a filtered table —
over eight synthetic points on a made-up grid (lat 10.01–10.08, lon
20.01–20.04), not a real place.

## Run

```powershell
C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
```

Use the fleet wave11 Streamlit by full path. Never Node-1's bare
`python` (the hermes venv). The app serves on localhost:8501; stop the
process after verifying. No persistent service is installed by this
pattern (see `04-deploy-notes`).

## Expected output

- Default controls (both groups, slider 0, map on): 8 points shown,
  8 table rows, 8 map markers.
- Groups set to Alpha only: 4 points (P1–P4).
- Slider at 50 with both groups: 3 points (values 55, 65, 75).
- Groups Alpha only with slider at 20: 2 points (values 25, 35).
- All eight values are 5, 15, 25, 35, 45, 55, 65, 75 (sum 320,
  mean 40.0).

## Failure behavior

- `ModuleNotFoundError: streamlit` — you are not running the wave11
  venv's Streamlit; use the full path above.
- Map shows no markers after filtering — check the metric: 0 points
  means the filter combination excludes everything (e.g. group Beta
  with slider 75 excludes all but P8 at 75; slider above 75 excludes
  all). Lower the slider before suspecting the map.
- Port 8501 already in use — another smoke run is still alive; stop
  it first, then re-run.

## Versions and evidence

- Tool: Streamlit 1.66.1 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Map tiles come from the default CDN; no tile server
  is claimed.
- Evidence level: design-only (gate 1 target). The app file parses
  and its widget/map/table calls use the Streamlit API; serving it
  against the fleet venv and checking the counts above is **to
  confirm at validation**.
