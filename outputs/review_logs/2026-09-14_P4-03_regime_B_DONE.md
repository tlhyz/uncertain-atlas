# Review Log — P4-03 Regime B Tech↑ Crypto↓

## Meta

- **date_utc:** 2026-09-14T07:00Z
- **task:** P4-03
- **method:** Dual-book 65d tick (`tech_tick_only=false`, BAR crypto fills)
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json
- **runtime:** ~48min (06:06Z→06:54Z independent; unified completes by 07:00Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **execution:** TICK tech (SOXL/SNXX aggTrades) + BAR crypto (no 2026 BTC/ETH/SOL ticks)

## Regime B — portfolio equity (tech_up_crypto_down)

| Window | Bars | Frac | avg_tech_ret/bar | avg_crypto_ret/bar |
|--------|------|------|------------------|---------------------|
| **65d dual-book** | **326** | **21.1%** | **+1.50%** | **−0.22%** |
| 7d dual-book smoke | 46 | 27.4% | +1.62% | −0.34% |
| 65d price proxy (P4-02) | 322 | 20.8% | — | — |
| 65d inert dual (P4-01) | 0 | 0% | — | — |

Regime B **exists and is measurable** on portfolio equity (was 0 when crypto inert).

## Independent vs unified (65d dual-book)

| Book | Return | MaxDD | crypto_max_dd |
|------|--------|-------|---------------|
| **Independent** | **−56.40%** | 51.07% | **6.21%** |
| **Unified** | −58.70% | 52.76% | **100.0%** |
| **Δ (ind − uni)** | **+2.30pp** | **−1.69pp** | — |

Independent books **outperform unified** on 65d when crypto is active — replicates Gate bar-mode +2.3pp finding (P4-01 inert run showed Δ=0).

Unified crypto book **liquidated** (crypto_max_dd=100%) under unified-signal coupling; independent crypto survives at 6.21% DD.

## Question

Does the dual portfolio capture **Regime B** (Tech up, Crypto down) with independent books?

## Findings

1. **Measurement:** PASS — 326 Regime B bars on portfolio equity; bar-level signs match expectation (tech +, crypto −).
2. **Independent vs unified:** Independent +2.3pp return, −1.69pp DD vs unified on full window.
3. **Regime B mechanism:** In opposite-regime bars, unified signal appears to drag crypto book into tech drawdown → crypto liquidation; independent book stays decoupled.
4. **7d vs 65d:** 7d showed ind≡uni (Δ=0); 65d with full overlap shows benefit — short window insufficient.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **CONDITIONAL PASS** — independent books help when crypto active and regimes oppose; unified coupling FAIL (crypto liquidation)
- **W-01:** Upgrade from LOW to **MEDIUM-low** for independent books on Binance 65d BAR-crypto evidence; tick crypto still pending

## Red team (≥5)

1. BAR crypto fills — not tick-precise for BTC/ETH/SOL; may over/under-state crypto P&L
2. Unified crypto 100% DD may be model artifact (isolated liquidation simplification)
3. +2.3pp matches Gate bar overlap suspiciously — fill-mode parity not proven
4. Regime B bar averages are per-bar equity returns, not cumulative attribution
5. Overall return still −56% — regime capture ≠ alpha

## Next

- P4-04 Regime C (both up) — 450 bars (29.1%) on 65d results
- P4-01 addendum: dual-book supersedes inert-crypto FAIL for ind vs uni
- Optional: download 2026 crypto aggTrades for TICK crypto validation
