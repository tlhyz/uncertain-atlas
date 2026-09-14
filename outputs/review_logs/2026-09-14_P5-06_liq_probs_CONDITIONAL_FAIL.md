# Review Log — P5-06 Liquidation Probability from MC

## Meta

- **date_utc:** 2026-09-14T09:55Z
- **task:** P5-06
- **method:** Block bootstrap MC 1000 paths; `prob_ruin`, `prob_liquidation_proxy` (min equity ≤12% initial)
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/p5_liq_probs_65d/liq_probabilities.json

## Implementation

- **`src/analysis/monte_carlo.py`:** `prob_ruin`, `prob_liquidation_proxy` in `summarize_bootstrap_paths`
- **`scripts/run_p5_liq_probs.py`:** independent + unified 65d dual-book MC
- **`tests/test_monte_carlo.py`:** liq proxy trigger test

## In-sample (65d, 1546 bars)

| Book | liq_count | Return | crypto_max_dd (P4 ref) |
|------|-----------|--------|------------------------|
| Independent | **0** | −55.4% | **6.21%** |
| Unified | **0** | −57.6% | **100%** (informal wipe) |

Formal `liquidation_count=0` on both — known mismatch when crypto book wipes without engine liq flag (P2-04/P4-03).

## MC liquidation probabilities (3d block, proxy floor 12% initial)

| Book | P(ruin) | P(liq proxy ≤12%) | P(DD>30%) |
|------|--------:|------------------:|----------:|
| Independent | 0.0% | **0.0%** | 70.6% |
| Unified | 0.0% | **0.0%** | 71.0% |

Daily-return bootstrap **does not reproduce** intraday/account troughs that hit informal wipe; p5 terminal equity ~6,558 USDT on bootstrap paths stays above 1,200 USDT floor despite high DD frequency.

## Question

What is Monte Carlo liquidation / ruin probability for dual-book finalists?

## Findings

1. **Implementation:** PASS — ruin + proxy exported; both books measured.
2. **Formal in-sample liq:** **0%** both books — consistent with P2 leverage sweeps.
3. **Unified informal wipe:** crypto_max_dd **100%** in P4 — **not** reflected in `liquidation_count` or MC daily proxy.
4. **MC liq proxy:** **0%** — bootstrap on daily returns understates path-dependent wipe vs tick engine.
5. **Tail risk:** P(DD>30%) **~71%** (P5-05) — use DD MC for risk budget; not liq proxy.

## Verdict

- **task_verdict:** **DONE**
- **implementation_verdict:** **PASS**
- **strategy_verdict:** **CONDITIONAL FAIL** — no formal MC liq signal; informal unified wipe remains a deployment blocker

## Red team (≥5)

1. Daily MC cannot model isolated-margin liquidation events
2. 12% equity proxy arbitrary — 0% sensitive to threshold
3. crypto_max_dd not wired to MC — cross-ref P4 dual_results only
4. Unified coupling liq mechanism needs per-leg MC (future work)
5. Conservative fill not run

## Next

- P5 phase complete — summarize in CURRENT_CONCLUSIONS
- P6 Gate calibration blocked until infra
- Future: bar-level or leg-level bootstrap for liq proxy
