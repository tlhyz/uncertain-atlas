# Q-crypto-3 — Optimal ±ATR grid range (3 / 5 / 7)

**Status:** PARTIAL (2026-09-13T06:30Z)  
**Window:** C1 2024-09-01 → 2024-11-30, BTC-only range sweep (P2-06)  
**Sweep:** ranges [3.0, 5.0, 7.0], step fixed 0.40 ATR, lev 1.5

---

## Question

Which **±ATR range** (3, 5, or 7) is optimal for crypto grid on BTC C1 tick backtest?

Default `CryptoParams.grid_atr_range = 5.0`.

---

## Status

**P2-06 running** (~59 min at 06:30Z). No `CRYPTO_REPORT.md` yet.

---

## Pre-registration criteria

- Rank ranges by **Calmar** (Base fill primary)
- Plateau: top-2 ranges within ≤10% return of best
- Conservative fill must not invert top rank
- Report `liquidation_count` and `crypto_max_dd_pct` per range

---

## Context from leverage scans (same window/engine)

SOL/ETH leverage scans show **~-88% return** at all levels — if range sweep shows similar collapse, range tuning may be **inert** (same failure mode as leverage).

---

## Remaining work

- [ ] P2-06 complete → read `grid_rank` in `crypto_results.json`
- [ ] Mark P2-12 **done** with verdict

---

## Config

`configs/experiments/crypto_btc_grid_atr_range.yaml`
