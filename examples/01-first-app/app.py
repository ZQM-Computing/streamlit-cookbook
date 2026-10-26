# 01-first-app (streamlit) — design-only, gate 1 target.
# Fleet invocation (Node-1):
#   C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
# Synthetic data ONLY (a made-up grid, not a real place).
# Serves on localhost:8501; stop the process after verifying (no persistent service).
import pandas as pd
import streamlit as st

st.title("First app: widgets, maps, tables")
st.markdown("Synthetic stations on a made-up grid (lat 10.0x, lon 20.0x) — not a real place.")

STATIONS = pd.DataFrame(
    [
        {"name": "Alpha", "lat": 10.010, "lon": 20.010, "value": 10},
        {"name": "Bravo", "lat": 10.020, "lon": 20.030, "value": 20},
        {"name": "Charlie", "lat": 10.030, "lon": 20.010, "value": 30},
        {"name": "Delta", "lat": 10.040, "lon": 20.040, "value": 40},
        {"name": "Echo", "lat": 10.050, "lon": 20.020, "value": 50},
    ]
)

min_value = st.slider("Minimum value", 0, 50, 0)
visible = STATIONS[STATIONS["value"] >= min_value]

st.metric("Stations shown", len(visible))
st.map(visible, latitude="lat", longitude="lon")
st.dataframe(visible)
