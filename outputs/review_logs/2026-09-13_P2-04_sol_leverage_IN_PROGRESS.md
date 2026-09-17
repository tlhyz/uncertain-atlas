# Review Log — P2-04 SOL leverage scan started + long-run checkpoint

**Date (UTC):** 2026-09-13T04:50Z  
**Task:** P2-04 (started); P1-11 + P2-02 checkpoint  
**Verdict:** P2-04 IN_PROGRESS; P1-11/P2-02 CHECKPOINT

---

## P2-04 started (lowest pending after P0-02 blocked)

| Item | Value |
|------|-------|
| Config | `configs/experiments/crypto_sol_leverage_scan.yaml` |
| tmux | `p2-04-sol-leverage` |
| Window | C1 2024-09-01 → 2024-11-30, 2184 bars |
| SOL Sep-04 | verified full-day aggTrades (920k rows, ts_ms format) |

Leverage 1.25x running at start.

---

## P1-11 / P2-02 checkpoint

| Job | Wall elapsed | CPU | Output |
|-----|--------------|-----|--------|
| P1-11 | ~188 min (~3h08m) | 99.5% | DUAL_REPORT pending |
| P2-02 | ~127 min (~2h07m) | 99.9% | CRYPTO_REPORT pending |

P2-02 exceeded prior ~116min estimate — likely ~30min/level on 2184 tick bars.

---

## Parallel jobs (8 cores)

| tmux | Task |
|------|------|
| p1-11-backtest | P1-11 |
| p2-02-btc-leverage | P2-02 |
| p2-03-eth-leverage | P2-03 (restarted after ETH Sep-04 fix) |
| p2-04-sol-leverage | P2-04 |
