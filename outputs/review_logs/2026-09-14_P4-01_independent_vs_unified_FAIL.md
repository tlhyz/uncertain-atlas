# Review Log — P4-01 Independent vs unified 10k portfolio

## Meta

- **date_utc:** 2026-09-14T05:38Z
- **experiment_id:** dual_binance_tick_independent_vs_unified
- **task:** P4-01
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/dual_binance_tick_independent_vs_unified/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~48min (2 portfolios; job 04:50Z→05:38Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **capital:** TECH 6500 + CRYPTO 2500 + RESERVE 1000 = 10000 USDT

## Results (independent_vs_unified)

| Book mode | Return | MaxDD | Calmar | crypto_max_dd |
|-----------|--------|-------|--------|---------------|
| **Independent** | **-58.70%** | 52.76% | -1.88 | **0.0%** |
| **Unified** | **-58.70%** | 52.76% | -1.88 | **0.0%** |
| **Δ (ind − uni)** | **0.00pp** | **0.00pp** | — | — |

Independent and unified are **bit-identical** on this window — same return, DD, turnover, fees.

**Regime stats:** `tech_down_crypto_up` bars=0, `tech_up_crypto_down` bars=0 — no opposite-regime bars detected on overlap; crypto book appears inert (crypto_max_dd=0).

## Cross-venue comparison

| Venue | Δreturn | ΔDD | Verdict |
|-------|---------|-----|---------|
| Gate overlap | +2.3% | −2.06pp | weak benefit (bar mode) |
| Binance 7d tick | 0 | 0 | no benefit |
| **Binance 65d tick** | **0** | **0** | **no benefit** |

Gate weak benefit **not replicated** on Binance 65d tick-precise run.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — independent crypto book provides no diversification benefit on 65d overlap; W-01 remains LOW
- **Q11/Q14:** Reinforced FAIL — no return or DD improvement from independent books

## Red team (≥5)

1. Crypto book inert (max_dd=0) — may not be trading; independent≡unified trivially
2. Gate +2.3% used bar mode — fill/execution difference vs tick
3. No opposite-regime bars on overlap — P4-02…F regime tasks may still find structure on longer history
4. P2-14 C1 showed unified less bad by 13pp — different window/engine
5. Independent crypto FSM may need non-zero crypto activity to test hypothesis fairly

## Next

- P4-02 regime A (Tech↓ Crypto↑) — may need longer window or forced crypto activity
- Investigate why crypto_max_dd=0 on 65d dual runs (crypto book sizing or FSM gate)
- Do not promote independent books on Binance tick evidence
