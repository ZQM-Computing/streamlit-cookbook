# 03 — Data app

An app that queries a database: a slider feeds a parameterized query,
and the app shows the row count, the mean value, and the matching
rows. The runnable core uses a local SQLite fixture built at runtime
with the standard library — no new dependency. The DuckDB and
Postgres connection swaps are documented below as design, not
asserted (see the validation note).

## Run

```powershell
C:\geo-tools\wave11-venv\Scripts\streamlit.exe run app.py --server.headless true --server.port 8501 --server.address localhost
```

Use the fleet wave11 Streamlit by full path. Never Node-1's bare
`python` (the hermes venv). The app serves on localhost:8501; stop the
process after verifying. The `readings.db` file is written at runtime
in the app directory — it is not committed.

## Expected output

- Default slider 0: 6 rows, mean 34.0, sum 204 (values 14, 22, 30, 38,
  46, 54).
- Slider at 40: 2 rows (values 46, 54), mean 50.0.
- Slider at 54: 1 row (value 54), mean 54.0.
- The query is parameterized (`WHERE value >= ?`); the slider value
  never enters the SQL string directly.

## DuckDB / Postgres swap (design, to confirm at validation)

The seed intent is DuckDB or Postgres. The swap touches only the
connection; the query and the display code are unchanged:

- DuckDB: `con = duckdb.connect("readings.duckdb")`, same SQL, same
  `pd.read_sql_query` call.
- Postgres: `con = psycopg.connect("host=... dbname=... user=...")`
  with credentials from the environment, never baked into the app.

Neither `duckdb` nor `psycopg` is confirmed present in Node-1's
wave11-venv (the wave-11A package list does not include them), so
neither connection is asserted here. Confirming package presence and
the live-connection spellings is a validation item.

## Failure behavior

- `ModuleNotFoundError: streamlit` — you are not running the wave11
  venv's Streamlit; use the full path above.
- `ModuleNotFoundError: duckdb` / `psycopg` on the swap variants —
  expected until the validation item lands; the SQLite core still
  runs.
- Mean shows 0.0 with 0 rows — the slider excludes everything; lower
  it. The guard (`if len(df) else 0.0`) keeps the mean from dividing
  by zero.

## Versions and evidence

- Tool: Streamlit 1.66.1 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). SQLite via the standard library; pandas arrives in
  the same venv as a Streamlit dependency.
- Evidence level: design-only (gate 1 target). The app file parses;
  serving it and checking the counts above, and the DuckDB/Postgres
  swaps, are **to confirm at validation**.
