# 03-data-app (streamlit) — design-only, gate 1 target.
# Fleet invocation (Node-1):
#   C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
# Synthetic data ONLY. Serves on localhost:8501; stop after verifying.
# The SQLite fixture is built at runtime (readings.db, NOT committed).
# DuckDB/Postgres connections are the documented swap (see README),
# NOT asserted: duckdb/psycopg presence in wave11-venv is unconfirmed.
import sqlite3
from pathlib import Path

import pandas as pd
import streamlit as st

DB = Path(__file__).with_name("readings.db")
READINGS = [
    ("R1", 14),
    ("R2", 22),
    ("R3", 30),
    ("R4", 38),
    ("R5", 46),
    ("R6", 54),
]


def ensure_db():
    if DB.exists():
        return
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE readings (station TEXT, value INTEGER)")
    con.executemany("INSERT INTO readings VALUES (?, ?)", READINGS)
    con.commit()
    con.close()


ensure_db()
st.title("Data app: query a database from an app")
min_value = st.slider("Minimum value", 0, 54, 0)
con = sqlite3.connect(DB)
df = pd.read_sql_query(
    "SELECT station, value FROM readings WHERE value >= ? ORDER BY value",
    con,
    params=(min_value,),
)
con.close()
st.metric("Rows", len(df))
st.metric("Mean value", float(df["value"].mean()) if len(df) else 0.0)
st.dataframe(df)
