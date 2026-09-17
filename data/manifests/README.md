# Dataset manifests — checksums and coverage metadata only
# Raw files live under data/raw/ (gitignored). Regenerate via scripts/download_binance.py

This directory stores JSON manifests produced by `scripts/build_manifest.py`.

Each manifest records:
- venue, symbol, market, start, end, source
- file list, checksum (sha256), row counts
- missing periods and known limitations

Example filename: `binance_BTCUSDT_aggTrades_2020-01-01_2025-12-31.json`
