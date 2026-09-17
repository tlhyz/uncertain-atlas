# Review Log — P4-05 Regime D Both Down

## Meta

- **date_utc:** 2026-09-14T07:20Z
- **task:** P4-05
- **method:** Regime classification on 65d dual-book results (reuse P4-03 JSON)
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **execution:** TICK tech + BAR crypto (dual book)

## Regime D — portfolio equity (both_down)

| Window | Bars | Frac | avg_tech_ret/bar | avg_crypto_ret/bar |
|--------|------|------|------------------|---------------------|
| **65d dual-book** | **435** | **28.1%** | **−1.73%** | **−0.31%** |
| 7d dual-book smoke | 32 | 19.1% | −1.41% | −0.32% |
| 65d price proxy (P4-02) | **435** | **28.1%** | — | — |
| 65d inert dual (P4-01) | 0 | 0% | — | — |

Regime D bar count **exactly matches** price proxy (435 bars) — strongest alignment of any quadrant.

## Quadrant summary (65d dual-book)

| Regime | Bars | Frac |
|--------|------|------|
| C both_up | 450 | 29.1% |
| **D both_down** | **435** | **28.1%** |
| B tech↑ crypto↓ | 326 | 21.1% |
| A tech↓ crypto↑ | 310 | 20.1% |
| **Total classified** | **1521** | **98.4%** |

(~25 bars unclassified: flat tech or flat crypto returns.)

## Full-window context (independent vs unified)

| Book | Return | crypto_max_dd |
|------|--------|---------------|
| Independent | **−56.40%** | 6.21% |
| Unified | −58.70% | **100%** (liquidation) |

Δreturn **+2.30pp** (ind − uni).

## Question

Does the dual portfolio capture **Regime D** (Tech down, Crypto down) with independent books?

## Findings

1. **Measurement:** PASS — 435 both-down bars; avg returns finite and negative on both books (−1.73% tech, −0.31% crypto per bar).
2. **Damage concentration:** ~28% of bars are correlated drawdowns on both books — explains large total loss (−56%) despite opposite-regime diversification potential.
3. **Independent vs unified:** In both-down bars both books bleed; unified coupling adds crypto liquidation risk on top (100% crypto DD vs 6.21% independent).
4. **Hedging hypothesis FAIL:** Independent books do **not** hedge Regime D — both lose together; only decoupling prevents unified crypto wipeout.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **FAIL** — Regime D is measurable but amplifies losses; no cross-book protection in correlated down moves
- **Risk note:** 28% both-down + 21% opposite-regime ≈ 49% stressed bars; FSM not survivable

## Red team (≥5)

1. BAR crypto may understate both-down crypto losses vs tick fills
2. Per-bar averages ≠ cumulative Regime D P&L attribution
3. 435 price-proxy match may reflect SOXL/BTC correlation, not independent book mechanics
4. Independent +2.3pp is full-window, not Regime-D-conditional
5. Short-heavy tech FSM loses hardest in both-down — structural, not parametric

## Next

- P4-06 Regime E/F mixed — transition bars or residual unclassified
- P4-07 margin/reserve sweep
- Consider Regime D kill-switch rule (P4-09 precursor)
