# Review Log — P4-09 Soft/Hard DD Pause Rules

## Meta

- **date_utc:** 2026-09-14T08:05Z
- **task:** P4-09
- **method:** Account DD from peak → soft halve targets / hard zero new risk
- **config:** configs/risk.yaml soft [-10,-12,-15]% hard [-18,-20,-25]%
- **output:** outputs/experiments/dual_binance_tick_dd_pause_7d/dual_results.json

## Implementation

`DualParams`:
- `dd_soft_threshold` / `dd_hard_threshold` (account-level, from peak `total_equity`)
- `dd_soft_risk_scale=0.5` (halve all leg targets)
- `dd_hard_risk_scale=0.0` (pause new risk — zero targets)

Hard takes precedence over soft when both set.

## Results — 7d dual-book

| Scenario | Return | Min account DD | Soft triggers | Hard triggers |
|----------|--------|----------------|---------------|---------------|
| **baseline** (no pause) | **−75.32%** | −88.75% | 0 | 0 |
| soft −10% only | −82.35% | −88.75% | **144** | 0 |
| soft −12% / hard −20% | −88.75% | −88.75% | 0 | **144** |
| soft −15% / hard −25% | −88.75% | −88.75% | 0 | **144** |

Min DD −88.75% on all paths — deep crash occurs regardless; pause rules change **path** not trough.

## Question

Do soft/hard DD pause rules improve survivability vs baseline FSM?

## Findings

1. **Soft −10% only:** FAIL — return **7pp worse** than baseline (−82.35% vs −75.32%) despite 144 soft triggers; late de-risking locks in losses without preventing trough.
2. **Hard rules:** FAIL — return −88.75% (≈ flat at ~1125 USDT residual); zeroing targets after −20% DD does not recover; effectively **cash-out at bottom**.
3. **Activation:** PASS — rules fire as designed (144 bars ≈ post-warmup stressed period on 7d).
4. **vs FSM:** Tech FSM already has tiered drawdown + `pause_long_grid`; account-level pause **duplicates** without benefit on this window.

## Verdict

- **task_verdict:** **DONE**
- **strategy_verdict:** **FAIL** — soft/hard pause rules worsen or match worst outcomes on 7d; do not deploy
- **policy:** Keep DD tiers in FSM; account pause rules need **earlier** trigger or partial close logic, not target zeroing

## Red team (≥5)

1. 7d window — min DD −88.75% dominates all scenarios
2. Hard scale=0 does not exit positions — stale inventory remains
3. Pause on total_equity mixes tech/crypto — may pause crypto unnecessarily
4. 144 triggers ≈ sustained breach — rule is always-on after first hit
5. 65d dual-book (−56%) may behave differently — run pending

## Next

- P4 phase complete after P4-09 — summarize in CURRENT_CONCLUSIONS
- Do not add account DD pause to live candidate
- Optional: 65d `dual_binance_tick_dd_pause_65d.yaml` confirmation run
