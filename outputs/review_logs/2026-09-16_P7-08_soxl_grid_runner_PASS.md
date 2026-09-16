# Review Log — P7-08 user-editable tick grid runner

## Meta

- **date_utc:** 2026-09-16T00:20Z
- **task:** P7-08
- **entry:** `soxl-lab/scripts/run_grid.py` · `soxl-lab/params/run.yaml`

## What it does

Edit YAML or pass CLI flags (`--leverage --n-grids --range-usdt --mode --hedge --capital --start --end`). Loads Binance UM 1h bars + **cache_only aggTrades**. Writes `results/runs/<name>/{spec,summary,daily}`.

Hedge modes: `flatten_survivor` (user hedge) or `independent` (P7-05 leftover-short behavior).

## Checks

- 10 unit tests (config overlay + existing user-grid)
- Bar smoke 2026-07-16→18: wrote output, no crash
- Tick smoke 2026-07-16: real cache

## Verdict

- **task_verdict:** **DONE**
- **live:** n/a (tooling)
