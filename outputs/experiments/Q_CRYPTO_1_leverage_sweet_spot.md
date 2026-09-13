# Q-crypto-1 — Leverage sweet spot (1.25–2.0x)

**Status:** PARTIAL (2026-09-13T10:40Z)  
**Window:** C1 2024-09-01 → 2024-11-30, tick-precise, crypto FSM+grid, tech disabled  
**Fill:** Base (primary verdict)

---

## Question

Does a leverage sweet spot exist in **1.25 / 1.5 / 1.75 / 2.0x** for BTC, ETH, SOL on Binance aggTrades?

---

## Answers by asset

### SOL — COMPLETE (P2-04)

| Lev | Return | Calmar | Liq |
|-----|--------|--------|-----|
| 1.25 | -88.01% | -2.52 | 0 |
| 1.5 | -88.01% | -2.51 | 0 |
| 1.75 | -88.01% | -2.50 | 0 |
| 2.0 | -88.01% | -2.49 | 0 |

**Verdict:** **NO sweet spot.** All levels collapse to ~12% of initial (~1199 USDT final). Calmar ranking favors higher leverage only because MaxDD differs by ~0.5% — not actionable.

### ETH — COMPLETE (P2-03)

| Lev | Return | Calmar | Liq |
|-----|--------|--------|-----|
| 1.25 | -87.86% | -5.86 | 0 |
| 1.5 | -87.74% | -5.79 | 0 |
| 1.75 | -87.61% | -5.74 | 0 |
| 2.0 | -87.50% | -5.69 | 0 |

**Verdict:** **NO sweet spot.** Final equity 1214–1250 USDT. Calmar nominally favors 2.0x but all ~-87.5% — not actionable.

### BTC — IN_PROGRESS (P2-02)

| Lev | Return | Calmar | Status |
|-----|--------|--------|--------|
| 1.25 | **-87.47%** | -16.89 | done (~109min) |
| 1.5 | — | — | running |
| 1.75 | — | — | pending |
| 2.0 | — | — | pending |

**Interim:** First level matches ETH ~-87.5% band. Restart 08:40Z after 5h57m stale run. Per-level baseline **~109min** (BTC tick grid slower than ETH ~43min).

**Early read:** No sweet spot at 1.25x — catastrophic loss consistent with SOL/ETH.

---

## Interim conclusion (partial)

On C1 tick-precise with current crypto grid FSM:

1. **No evidence of a viable 1.25–2.0x sweet spot** for SOL or ETH on C1 tick grid FSM.
2. **BTC 1.25x -87.47%** (first level) — consistent with ETH band; await full scan.
3. SOL shows near-identical ~-88% across levels (accounting floor suspected); ETH varies slightly but all catastrophic.
4. Does **not** overturn LEDGER-002 (bar-mode PERP vs ETF A/B) — different engine, window, and config.

---

## Remaining work

- [ ] P2-02 BTC leverage scan complete
- [x] P2-03 ETH complete (FAIL)
- [ ] Conservative fill cross-check on best/worst row
- [ ] Mark P2-10 **done** when BTC reported

---

## Evidence chain

- SOL: `outputs/experiments/crypto_sol_leverage_scan/crypto_results.json`
- ETH: `outputs/experiments/crypto_eth_leverage_scan/crypto_results.json`
- Reviews: `outputs/review_logs/2026-09-13_P2-04_sol_leverage_FAIL.md`, `outputs/review_logs/2026-09-13_P2-03_eth_leverage_FAIL.md`
