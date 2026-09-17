# Review Log — P4-08 Funding Stress Deleverage Rule

## Meta

- **date_utc:** 2026-09-14T07:55Z
- **task:** P4-08
- **method:** Rolling 7d net funding cost / book equity → cut targets 50% when above threshold
- **config:** configs/risk.yaml thresholds [1.0%, 1.5%, 2.0%]
- **output:** outputs/experiments/dual_binance_tick_funding_stress_7d/dual_results.json

## Implementation

Added to `DualParams`:
- `funding_stress_threshold` (None = baseline off)
- `funding_stress_deleverage=0.5` (halve targets when triggered)
- `funding_stress_window_bars=168` (7d @ 1h)

Tracks per-book rolling net funding **cost** (paid − recv) vs prior bar equity; scales tech/crypto leg targets independently.

## Results — 7d dual-book (2026-09-05→11)

| Mode | Threshold | Return | Triggers (tech/crypto) | Max roll stress tech |
|------|-----------|--------|------------------------|----------------------|
| baseline | off | −75.32% | 0 / 0 | 0.00% |
| stress | 1.0% | −75.32% | 0 / 0 | 0.00% |
| stress | 1.5% | −75.32% | 0 / 0 | 0.00% |
| stress | 2.0% | −75.32% | 0 / 0 | 0.00% |

**All four paths identical** — rule **never triggered**.

## Why inert?

- 7d dual-book `net_funding` **positive** (+96 USDT on prior 7d smoke) — books **received** more funding than paid.
- Rolling net **cost** ratio stayed 0% vs book equity → thresholds (1–2%) never breached.
- Short-heavy tech losing on price ≠ funding stress under positive funding rate regime on this window.

## Question

Does the funding stress deleverage rule improve survivability when rolling 7d funding cost exceeds 1/1.5/2% of book?

## Findings

1. **Implementation:** PASS — rule wired, unit test green, metrics exported (`stress_triggers_*`, `max_rolling_stress_*`).
2. **Activation:** FAIL on 7d — zero triggers; rule is **inert** (no counterfactual delta).
3. **Policy fit:** Thresholds reasonable per `RISK_POLICY.md` but untested on stressful funding window — need window with sustained negative net funding.
4. **65d context:** P4-03 ind run net_funding TBD; tech short may pay funding on longer window — 65d test recommended.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **INERT** on 7d — no deleverage events; cannot validate benefit
- **next data:** C1 crypto window or high-positive-funding-rate period for stress activation

## Red team (≥5)

1. 7d too short for 168-bar window warmup interaction
2. Net funding positive ≠ no risk — mark-price funding on shorts differs from net sign
3. 50% deleverage arbitrary — not from risk.yaml
4. Tech/crypto stressed independently — may miss account-level funding stress
5. BAR crypto fills on dual-book path

## Next

- P4-09 soft/hard DD pause rules
- Run `dual_binance_tick_funding_stress_65d.yaml` when compute free
- Test on synthetic high funding cost window to validate trigger logic
