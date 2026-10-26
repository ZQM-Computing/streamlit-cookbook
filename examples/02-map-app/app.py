# 02-map-app (streamlit) — design-only, gate 1 target.
# Fleet invocation (Node-1):
#   C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
# Synthetic data ONLY (a made-up grid, not a real place).
# Serves on localhost:8501; stop the process after verifying (no persistent service).
import pandas as pd
import streamlit as st

st.title("Map app: filters and layers")

POINTS = pd.DataFrame(
    [
        {"name": "P1", "group": "Alpha", "lat": 10.010, "lon": 20.010, "value": 5},
        {"name": "P2", "group": "Alpha", "lat": 10.020, "lon": 20.030, "value": 15},
        {"name": "P3", "group": "Alpha", "lat": 10.030, "lon": 20.010, "value": 25},
        {"name": "P4", "group": "Alpha", "lat": 10.040, "lon": 20.040, "value": 35},
        {"name": "P5", "group": "Beta", "lat": 10.050, "lon": 20.020, "value": 45},
        {"name": "P6", "group": "Beta", "lat": 10.060, "lon": 20.030, "value": 55},
        {"name": "P7", "group": "Beta", "lat": 10.070, "lon": 20.010, "value": 65},
        {"name": "P8", "group": "Beta", "lat": 10.080, "lon": 20.040, "value": 75},
    ]
)

groups = st.multiselect("Groups", ["Alpha", "Beta"], default=["Alpha", "Beta"])
min_value = st.slider("Minimum value", 0, 75, 0)
show_map = st.checkbox("Show map", value=True)

visible = POINTS[POINTS["group"].isin(groups) & (POINTS["value"] >= min_value)]

st.metric("Points shown", len(visible))
if show_map:
    st.map(visible, latitude="lat", longitude="lon")
st.dataframe(visible)
