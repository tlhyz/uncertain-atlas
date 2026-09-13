# Q-crypto-2 — Is 0.40 ATR step on a parameter plateau?

**Status:** COMPLETE (2026-09-13T12:10Z)  
**Window:** C1 2024-09-01 → 2024-11-30, BTC-only grid step sweep (P2-05)  
**Sweep:** steps [0.30, 0.40, 0.50, 0.60], range fixed ±5 ATR, lev 1.5

---

## Question

Is **0.40 ATR** grid spacing near a stable optimum (plateau), or a sharp peak?

Prior claim W-02 in `docs/CURRENT_CONCLUSIONS.md` — **LOW confidence**, not verified by executed sweep.

---

## Results (P2-05 COMPLETE)

| Step | Return | Calmar | Rank (Calmar) |
|------|--------|--------|---------------|
| 0.30 | -87.39% | -16.61 | 2 |
| **0.40 (default)** | **-87.35%** | **-17.18** | **4 (worst)** |
| 0.50 | -87.55% | -15.33 | **1** |
| 0.60 | -87.35% | -17.17 | 3 |

Source: `outputs/experiments/crypto_btc_grid_atr_step/crypto_results.json`

---

## Plateau verdict

**FAIL — no actionable plateau.**

1. Return spread **0.20pp** — flat band in catastrophic ~-87% zone (inert plateau).
2. **0.40 is worst by Calmar** — W-02 **not supported**; do not promote default spacing as optimum.
3. 0.50 nominally best Calmar but -87.55% return — not deployable.
4. Consistent with P2-06 range FAIL and leverage scans.

---

## Evidence chain

- Review: `outputs/review_logs/2026-09-13_P2-05_btc_grid_atr_FAIL.md`
- Artifacts: `outputs/experiments/crypto_btc_grid_atr_step/CRYPTO_REPORT.md`
