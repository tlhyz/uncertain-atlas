# Review Log — P3-06 Right-side reserve 25/30/35% sweep

## Meta

- **date_utc:** 2026-09-14T00:52Z
- **experiment_id:** dual_binance_tick_right_side_reserve
- **task:** P3-06
- **config:** configs/experiments/dual_binance_tick_right_side_reserve.yaml
- **output:** outputs/experiments/dual_binance_tick_right_side_reserve/dual_results.json
- **fill_mode:** base (tick_precise aggTrades)
- **runtime:** ~72min (3 levels × ~24min; job 23:40Z→00:52Z)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (right_side_reserve_rank)

| Level | Return | MaxDD | Calmar | Turnover | vs default (−58.70%) |
|-------|--------|-------|--------|----------|------------------------|
| **25%** (best return) | **-58.92%** | 52.62% | -1.89 | 40633 | −0.22pp worse |
| 30% | -59.30% | 53.27% | -1.87 | 29814 | −0.60pp worse |
| **35%** (best Calmar) | -59.23% | 54.20% | **-1.83** | 23146 | −0.53pp worse |

Default code uses **28%** (not in sweep). Nearest bracket: 25% and 30% both worse than P3-01 baseline dual (−58.70%).

- Higher deploy fraction → lower turnover (25%: 40.6k vs 35%: 23.1k) but **does not improve return**
- Return ordering: **25% > 35% > 30%** — not strictly monotonic; 35% slightly beats 30%
- Calmar ordering: **35% > 30% > 25%** — higher reserve improves risk-adjusted metric only marginally; all deeply negative

All levels still lose to B&H (−33.49%), Cash (0%), grid-only (−25.20%) from P3-01.

## Q-tech partial (reversal deploy sizing)

**Answer:** Lower deploy (25%) is best return among sweep but **still worse than default 28%**. No sweet spot; knob binds negatively vs baseline.

## Verdict

- **task_verdict:** **PASS** (measurement complete)
- **strategy_verdict:** **FAIL** — no reserve level beats Cash, B&H, grid-only, or default dual (−58.70%)
- **C-05:** Reinforced **HIGH** — reversal sizing cannot rescue Short→Long FSM

## Red team (≥5)

1. Default 28% not measured — interpolation may sit at local minimum; still all sweep points worse
2. Calmar "best" at 35% (−1.83) conflicts with return best at 25% — no single deploy target
3. Turnover/fees scale with deploy but net P&L unchanged in sign
4. Base fill only — conservative not run
5. Same 65d window — deploy curve may not generalize

## Next

- P3-07 SOXL/SNXX weight 75/25 70/30 65/35 (started)
- Do not promote any reserve level without beat grid-only baseline
