# Q-crypto-1 — Leverage sweet spot (1.25–2.0x)

**Status:** **COMPLETE FAIL** (2026-09-13T15:40Z)  
**Window:** C1 2024-09-01 → 2024-11-30, tick-precise, crypto FSM+grid, tech disabled  
**Fill:** Base (primary verdict)

---

## Question

Does a leverage sweet spot exist in **1.25 / 1.5 / 1.75 / 2.0x** for BTC, ETH, SOL on Binance aggTrades?

---

## Answer

**NO.** All three majors show catastrophic ~-87 to -88% returns across the full 1.25–2.0x band on C1 tick-precise crypto grid FSM. Calmar rankings vary slightly but no level is deployable.

---

## Results by asset

### BTC — COMPLETE (P2-02)

| Lev | Return | Calmar | Final (USDT) | Liq |
|-----|--------|--------|--------------|-----|
| 1.25 | -87.47% | -16.89 | 1253 | 0 |
| 1.5 | -87.35% | -17.18 | 1265 | 0 |
| 1.75 | -87.32% | **-14.67** | 1268 | 0 |
| 2.0 | **-87.06%** | -16.65 | 1294 | 0 |

**Verdict:** **NO sweet spot.** Return spread 0.41pp; all ~-87%. Calmar favors 1.75x; return favors 2.0x — neither actionable.

### ETH — COMPLETE (P2-03)

| Lev | Return | Calmar | Liq |
|-----|--------|--------|-----|
| 1.25 | -87.86% | -5.86 | 0 |
| 1.5 | -87.74% | -5.79 | 0 |
| 1.75 | -87.61% | -5.74 | 0 |
| 2.0 | -87.50% | -5.69 | 0 |

**Verdict:** **NO sweet spot.** Final equity 1214–1250 USDT.

### SOL — COMPLETE (P2-04)

| Lev | Return | Calmar | Liq |
|-----|--------|--------|-----|
| 1.25–2.0 | -88.01% | -2.49 to -2.52 | 0 |

**Verdict:** **NO sweet spot.** Identical ~-88% at all levels (~1199 USDT final).

---

## Conclusion

1. **No viable 1.25–2.0x sweet spot** for BTC, ETH, or SOL on C1 tick crypto grid FSM.
2. Does **not** overturn LEDGER-002 (bar-mode PERP vs ETF A/B) — different engine, window, and config.
3. Conservative fill cross-check remains open but unlikely to rescue ~-87% band.

---

## Evidence chain

- BTC: `outputs/experiments/crypto_btc_leverage_scan/crypto_results.json`
- ETH: `outputs/experiments/crypto_eth_leverage_scan/crypto_results.json`
- SOL: `outputs/experiments/crypto_sol_leverage_scan/crypto_results.json`
- Reviews: `outputs/review_logs/2026-09-13_P2-02_btc_leverage_FAIL.md`, `P2-03`, `P2-04`
