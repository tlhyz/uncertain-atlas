# Q-crypto-1 — Leverage sweet spot (1.25–2.0x)

**Status:** PARTIAL (2026-09-13T07:00Z)  
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

### ETH — PARTIAL (P2-03, 2.0x running)

| Lev | Return | Calmar | Status |
|-----|--------|--------|--------|
| 1.25 | **-87.86%** | -5.86 | done |
| 1.5 | **-87.74%** | -5.79 | done |
| 1.75 | **-87.61%** | -5.74 | done |
| 2.0 | pending | pending | running ~129min total |

**Interim:** Same catastrophic band as SOL at all completed levels. No sweet spot.

### BTC — PENDING (P2-02)

Scan running ~257 min; no `CRYPTO_REPORT.md` yet.

---

## Interim conclusion (partial)

On C1 tick-precise with current crypto grid FSM:

1. **No evidence of a viable 1.25–2.0x sweet spot** for SOL; ETH trending same at 1.25x.
2. Identical ~-88% returns across SOL leverage levels suggest **strategy/accounting floor**, not leverage sensitivity — requires red-team (see P2-04 review).
3. Does **not** overturn LEDGER-002 (bar-mode PERP vs ETF A/B) — different engine, window, and config.

---

## Remaining work

- [ ] P2-02 BTC leverage scan complete
- [ ] P2-03 ETH 2.0x complete (1.25–1.75 done)
- [ ] Conservative fill cross-check on best/worst row
- [ ] Mark P2-10 **done** when all three assets reported

---

## Evidence chain

- SOL: `outputs/experiments/crypto_sol_leverage_scan/crypto_results.json`
- ETH interim: `/tmp/p2-03_eth_leverage.log`
- Reviews: `outputs/review_logs/2026-09-13_P2-04_sol_leverage_FAIL.md`
