# 04-deploy-notes — smoke-run launcher (NOT a persistent service).
# Starts the 01-first-app app headless on localhost:8501, checks it
# answers HTTP 200, then stops it. Run on Node-1 only (Windows).
# Design-only, gate 1 target — running it on Node-1 is to confirm at validation.
$ErrorActionPreference = 'Stop'
$streamlit = 'C:\geo-tools\wave11-venv\Scripts\streamlit.exe'
$app = Join-Path $PSScriptRoot '..\01-first-app\app.py'
if (-not (Test-Path $app)) { throw "App not found: $app" }
$proc = Start-Process -FilePath $streamlit -ArgumentList @('run', $app, '--server.headless', 'true', '--server.port', '8501', '--server.address', 'localhost') -PassThru -NoNewWindow
"STARTED-PID=$($proc.Id)"
try {
    $ok = $false
    for ($i = 0; $i -lt 30; $i++) {
        Start-Sleep -Seconds 2
        try {
            $r = Invoke-WebRequest -Uri 'http://localhost:8501/' -UseBasicParsing -TimeoutSec 5
            if ($r.StatusCode -eq 200) { $ok = $true; break }
        } catch { }
    }
    "SMOKE-200=$ok"
    if (-not $ok) { throw "Streamlit did not answer on localhost:8501 within ~60 s" }
} finally {
    Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
}
"PORT-NOTE: smoke process stopped; verify 8501 is free before any other smoke run."
