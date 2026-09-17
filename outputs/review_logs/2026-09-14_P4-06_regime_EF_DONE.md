# Review Log — P4-06 Regime E/F Mixed

## Meta

- **date_utc:** 2026-09-14T07:30Z
- **task:** P4-06
- **method:** Residual analysis on 65d dual-book quadrant classifier + SOXL/BTC price proxy decomposition
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json

## Definitions

Quadrant classifier (`regime_cross_stats`) assigns A/B/C/D when both book returns are strictly positive or negative. **Regime E/F mixed** = bars where at least one book return is **flat (0%)** — not in any quadrant.

| Label | Condition |
|-------|-----------|
| **E** | Tech flat, crypto moves (`tr==0`, `cr≠0`) |
| **F** | Crypto flat, tech moves (`cr==0`, `tr≠0`) |
| **G** | Both flat (`tr==0`, `cr==0`) |

## Portfolio equity (65d dual-book independent)

| Bucket | Bars | Frac |
|--------|------|------|
| A + B + C + D (classified) | 1521 | **98.4%** |
| **E/F mixed (residual)** | **25** | **1.6%** |

Breakdown: classifier does not export E/F separately; residual = `1546 − (310+326+450+435)`.

**Interpretation:** Grid rebalance / hold bars on tech or crypto book produce zero equity change while the other book moves — inflates mixed count vs raw price series.

## Price proxy (SOXL vs BTC closes, same 1546 bars)

| Bucket | Bars | Frac |
|--------|------|------|
| Quadrants A/B/C/D | 1534 | 99.2% |
| **E** tech flat | 11 | 0.7% |
| **F** crypto flat | 0 | 0.0% |
| **G** both flat | 1 | 0.06% |
| **Mixed total** | **12** | **0.8%** |

Portfolio mixed (25) > price mixed (12) — **+13 bars** from FSM/grid mechanics, not market structure.

## Full-window context

| Book | Return | crypto_max_dd |
|------|--------|---------------|
| Independent | −56.40% | 6.21% |
| Unified | −58.70% | 100% |

Δreturn **+2.30pp** — unchanged from P4-03…05.

## Question

Are **mixed / unclassified** bars material for portfolio regime analysis?

## Findings

1. **Coverage:** PASS — 98.4% of bars fall cleanly into A/B/C/D on portfolio equity.
2. **E/F materiality:** FAIL as alpha source — 1.6% mixed bars cannot explain −56% total return.
3. **E vs F:** Price proxy shows E-dominant (tech flat while crypto moves); F≈0 on 1h bars — crypto book updates every bar under BAR fills; tech grid produces more zero-return bars.
4. **Classifier gap:** `regime_cross_stats` should add explicit `mixed` / E / F buckets (backlog metrics fix).

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **PASS** (classifier sufficient) — mixed bars negligible; no separate E/F strategy warranted
- **infra:** Add `mixed` regime to `metrics.py` in maintenance pass

## Red team (≥5)

1. E/F split on portfolio inferred from residual, not direct measurement
2. Price proxy ≠ portfolio equity for mixed decomposition
3. 25 bars too small for statistical tests
4. `pct_change` zero vs epsilon — float noise may misclassify
5. 1h bar granularity hides intra-bar mixed moves

## Next

- P4-07 margin/reserve 80/20 70/30 60/40 sweep
- metrics.py: export `mixed`, `tech_flat`, `crypto_flat` buckets
- P4 quadrant series complete (A–D + E/F) — ready for margin tests
