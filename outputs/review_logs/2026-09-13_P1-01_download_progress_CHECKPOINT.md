# Review Log — P1-01 ETH/SOL download progress checkpoint

**Date (UTC):** 2026-09-13T01:45Z  
**Task:** P1-01 (in_progress)  
**Verdict:** CHECKPOINT — download active; partial manifest rebuilt

---

## Progress

| Symbol | Cache days | Manifest rows | Target |
|--------|-----------|---------------|--------|
| BTC | 91 | 130.5M | C1 window complete |
| ETH | 57+ (downloading) | 39.6M (39 days) | 2024-09-05→2024-11-30 (~87d) |
| SOL | 3 (queued) | 2.1M | same window after ETH |

- Download tmux: `eth-sol-download` — ~1 day/sec throughput
- Partial `build_manifest.py` run — ETH manifest extended to 2024-10-09
- Stale manifest `binance_ETHUSDT_aggTrades_2024-09-01_2024-09-04.json` removed

## P1-11 status

- Backtest tmux: `p1-11-backtest` — 100% CPU, running benchmarks (10 B1–B10) on 65d tick data
- No report yet — expected; tick-precise benchmarks are compute-heavy

## Next

1. ETH download completes → SOL download → full manifest rebuild → mark P1-01 done
2. P1-11 report → PASS/FAIL review vs prior 7d smoke FAIL
