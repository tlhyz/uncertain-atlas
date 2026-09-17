# Q-crypto-3 — Optimal ±ATR grid range (3 / 5 / 7)

**Status:** COMPLETE (2026-09-13T11:00Z)  
**Window:** C1 2024-09-01 → 2024-11-30, BTC-only range sweep (P2-06)  
**Sweep:** ranges [3.0, 5.0, 7.0], step fixed 0.40 ATR, lev 1.5

---

## Question

Which **±ATR range** (3, 5, or 7) is optimal for crypto grid on BTC C1 tick backtest?

Default `CryptoParams.grid_atr_range = 5.0`.

---

## Results (P2-06 COMPLETE)

| Range | Return | Calmar | Liq | Final equity |
|-------|--------|--------|-----|--------------|
| **±3 ATR** | **-86.90%** | **-21.57** | 0 | 1310 USDT |
| ±5 ATR (default) | -87.35% | -17.18 | 0 | 1265 USDT |
| ±7 ATR | -87.39% | -16.60 | 0 | 1261 USDT |

Source: `outputs/experiments/crypto_btc_grid_atr_range/crypto_results.json`

---

## Verdict

**FAIL — no actionable optimal range.**

1. All ranges catastrophic (~-87%); returns within **0.5pp** — inert plateau in failure band.
2. Calmar nominally favors **±3 ATR** over default ±5, but not deployable.
3. **Do not change default r5.0** on this evidence — no edge found at any range.
4. Consistent with leverage scan failure mode (C-06).

---

## Evidence chain

- Review: `outputs/review_logs/2026-09-13_P2-06_btc_grid_range_FAIL.md`
- Artifacts: `outputs/experiments/crypto_btc_grid_atr_range/CRYPTO_REPORT.md`
