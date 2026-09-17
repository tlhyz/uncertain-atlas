# Review Log — P1-11 + P2-02 dual long-run checkpoint (04:30 UTC)

**Date (UTC):** 2026-09-13T04:30Z  
**Tasks:** P1-11, P2-02 (both in_progress)  
**Verdict:** CHECKPOINT — both jobs healthy; awaiting final reports

---

## P1-11 — 65d Tech tick backtest

| Metric | Value |
|--------|-------|
| PID | 29982 |
| tmux | `p1-11-backtest` |
| Elapsed | ~168 min (~2h48m) |
| CPU | 99.4% |
| RSS | ~1.45 GB |
| Config | `configs/experiments/dual_binance_tick_65d.yaml` |
| Output dir | `outputs/dual_engine_perp_binance_ticks_65d/` |
| Artifacts so far | `DATA_QUALITY_REPORT.json`, `provenance.json` only |

`DUAL_REPORT.md` is written only after all configured steps (benchmarks B1–B10 + seed_windows) finish. Tick-precise simulation over **1560 bars** × 10 benchmarks remains compute-bound; no stall detected.

**Prior evidence (unchanged):** 7d smoke dual **-77.82%** vs B&H **+1.03%** (FAIL). Full 65d required before ledger update.

---

## P2-02 — BTC leverage scan

| Metric | Value |
|--------|-------|
| PID | 44529 |
| tmux | `p2-02-btc-leverage` |
| Elapsed | ~107 min (~1h47m) |
| CPU | 99.9% |
| RSS | ~392 MB |
| Config | `configs/experiments/crypto_btc_leverage_scan.yaml` |
| Output dir | `outputs/experiments/crypto_btc_leverage_scan/` |
| Artifacts so far | `provenance.json` only |

Log shows leverage scan started on **2184 bars** (C1 window). Per-level progress prints not yet visible (process started before per-level logging landed); observed **~25–27 min/level** extrapolated → **~100–110 min total** for 4 levels, possibly finishing next cycle.

---

## Tests

`python3 -m pytest -q` → **126 passed** (04:30 UTC).

---

## Blockers / next

| Task | Action |
|------|--------|
| P0-02 | blocked — awaiting human merge of PR #8 |
| P1-11 | wait for `DUAL_REPORT.md` → PASS/FAIL review vs 7d smoke |
| P2-02 | wait for `CRYPTO_REPORT.md` + `crypto_results.json` → mark done, partial Q-crypto-1 |
| P2-03 | ETH klines + aggTrades manifests ready; queue after P2-02 completes (avoid CPU contention) |

---

## Red team (≥5 fake-good paths)

1. Tick fill optimism inflates crypto returns at higher leverage  
2. C1 window (Sep–Nov 2024) may not generalize — single regime  
3. P1-11 65d window may differ materially from 7d smoke — need full report before overturning FAIL  
4. Long runtime without intermediate checkpoints — silent OOM/restart risk (not observed; RSS stable)  
5. Missing conservative fill cross-check on P2-02 (config uses base only for ranking)
