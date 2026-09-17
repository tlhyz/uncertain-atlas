# Review Log — P4-04 Regime C Both Up

## Meta

- **date_utc:** 2026-09-14T07:10Z
- **task:** P4-04
- **method:** Regime classification on 65d dual-book results (no re-run — reuse P4-03 JSON)
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **execution:** TICK tech + BAR crypto (dual book)

## Regime C — portfolio equity (both_up)

| Window | Bars | Frac | avg_tech_ret/bar | avg_crypto_ret/bar |
|--------|------|------|------------------|---------------------|
| **65d dual-book** | **450** | **29.1%** | +∞ (artifact*) | +∞ (artifact*) |
| 7d dual-book smoke | 26 | 15.5% | +∞ (artifact*) | +∞ (artifact*) |
| 65d price proxy (P4-02) | 453 | 29.3% | — | — |
| 65d inert dual (P4-01) | 0 | 0% | — | — |

\*`avg_*_ret` = `inf` when `pct_change()` hits zero→positive equity jumps (warmup / rebalance bars). **Bar counts are valid**; use sign/magnitude from cumulative equity instead.

**Contrast — Regime D (both_down) on same run:**

| Regime | Bars | Frac | avg_tech_ret | avg_crypto_ret |
|--------|------|------|--------------|----------------|
| both_down | 435 | 28.1% | −1.73%/bar | −0.31%/bar |

Regime C is the **largest quadrant** (29.1%) — slightly above both_down (28.1%).

## Full-window context (independent vs unified)

| Book | Return | crypto_max_dd |
|------|--------|---------------|
| Independent | **−56.40%** | 6.21% |
| Unified | −58.70% | **100%** (liquidation) |

Δreturn **+2.30pp** (ind − uni) — same as P4-03.

## Question

Does the dual portfolio capture **Regime C** (Tech up, Crypto up) with independent books?

## Findings

1. **Measurement:** PASS — 450 both-up bars on portfolio equity (was 0 when crypto inert); aligns with price proxy 453 bars (29.3%).
2. **Regime balance:** Four quadrants roughly balanced (~20–29% each) — no single regime dominates pathologically.
3. **Unified crypto liquidation:** Unified book likely **misses Regime C participation** after crypto wipeout; independent retains 6.21% crypto DD and stays active through 450 both-up bars.
4. **Alpha:** FAIL — despite 29% both-up bars, total return −56.4%; correlated up moves do not salvage FSM.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **CONDITIONAL PASS** measurement; **FAIL** alpha — Regime C captured structurally but insufficient P&L
- **inf metric:** Document as known `regime_cross_stats` edge case; bar counts authoritative

## Red team (≥5)

1. `avg_ret=inf` in both_up — do not use for ranking; fix in metrics.py later
2. BAR crypto fills may mis-state both-up crypto gains vs tick
3. 450 both-up bars ≠ 450 profitable bars — equity can rise on small recoveries
4. Price proxy 453 vs portfolio 450 — 3-bar gap acceptable
5. Independent +2.3pp is full-window, not Regime-C-conditional attribution

## Next

- P4-05 Regime D both down — 435 bars already in JSON
- Fix `regime_cross_stats` inf handling for both_up quadrant
- P4-06 E/F mixed — derive from residual or cross-regime transitions
