# 04 — Deploy notes

How to run a Streamlit app as a smoke-run service on a Windows node:
headless, localhost-bound, default port 8501, started and stopped by
the launcher script — and what a persistent deployment would still
need. No persistent service is installed by this pattern.

## Run (smoke only)

```powershell
.\serve.ps1
```

The script starts the `01-first-app` app headless on
localhost:8501, polls until it answers HTTP 200 (up to ~60 s), prints
`SMOKE-200=True`, then stops the process. Verify the port is free
afterwards before any other smoke run.

## What the flags mean

- `--server.headless true` — no browser auto-open (required for
  unattended runs).
- `--server.address localhost` — private binding. The app is reachable
  only from the node itself, per the series rule that infra patterns
  default to private bindings.
- `--server.port 8501` — Streamlit's default. Change it if another
  smoke run holds 8501; never run two smoke servers on one port.

## What a persistent deployment still needs (not done here)

- A service wrapper (e.g. NSSM, the fleet's usual Windows service
  tool) with restart-on-failure and a named service account — a
  separate decision, not installed by this pattern.
- A reverse proxy in front of localhost:8501 for any non-localhost
  access, with authentication decided by Alex (no default-credential
  service is ever left open).
- Log rotation for the Streamlit server log, which otherwise grows
  unboundedly.

## Failure behavior

- `SMOKE-200=False` — the app did not answer in ~60 s. Check the
  Streamlit log lines the script prints: a port conflict shows as an
  address-in-use error; an app error shows as a traceback on startup.
- The process lingers after the script — kill it by PID (the script
  prints the PID on start in the process list) and re-check the port
  before re-running.

## Versions and evidence

- Tool: Streamlit 1.66.1 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Port 8501 is Streamlit's default; no Streamlit
  service was started on the fleet.
- Evidence level: design-only (gate 1 target). The launcher is a
  Windows PowerShell script and cannot be executed on the drafting
  VM; running it on Node-1 and observing `SMOKE-200=True` plus a
  free port afterwards is **to confirm at validation**.
