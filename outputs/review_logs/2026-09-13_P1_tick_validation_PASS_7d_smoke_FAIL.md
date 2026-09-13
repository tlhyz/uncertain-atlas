# Review Log — P1 tick validation + 7d smoke backtest

## Meta

- **date_utc:** 2026-09-13T00:15Z
- **experiment_id:** dual_binance_tick_7d
- **git_commit:** (see commit after this log)
- **author:** cursor-agent
- **config_paths:** configs/experiments/dual_binance_tick_7d.yaml
- **data_manifest:** data/manifests/binance_SOXLUSDT_aggTrades_2026-07-09_2026-09-11.json
- **fill_modes_verdict:** base (tick_precise aggTrades tech legs)

## Data coverage

- **venue / symbols:** Binance SOXLUSDT, SNXXUSDT, BTC/ETH/SOL klines
- **start → end:** 2026-09-05 → 2026-09-11 (168 bars); full tick cache 2026-07-09 → 2026-09-11
- **precision:** TICK (every bar validated for SOXL 1560/1560, SNXX 1546/1546 on full cache)
- **known gaps:** 2026-09-12 Vision aggTrades empty; ETH/SOL cache rows=0 (corrupt legacy — re-download needed)

## Results (7d window, tick-precise)

| Metric | Dual B10 | B2 Buy&Hold |
|--------|----------|-------------|
| Total return | **-77.82%** | **+1.03%** |
| Max DD | 11.47% | 9.90% |
| Liquidations | 0 | 0 |

## Verdict

- **verdict:** FAIL
- **evidence_class:** STRONG (real aggTrades, Base fill, short window)
- **one_line_summary:** Short→Long dual still FAIL vs buy-and-hold on Binance tick-precise 7d window.

## vs prior run

- **prior_log:** outputs/dual_engine_perp/ (Gate bar overlap, dual -51% vs B&H -30%)
- **delta:** Now tick-precise on Binance; dual worse (-78%) on different 7d slice — Short→Long hypothesis still falsified
- **what_changed:** data=Binance aggTrades, execution=tick_precise, window=7d Sep 2026

## Optimization — next actions

1. Run full 65d Binance tick backtest (P1-11 new)
2. Re-download ETH/SOL aggTrades (fix corrupt cache)
3. Compare Cash→Long vs Short→Long on same tick window (Q-tech-1)
4. Do not deploy initial Short until FAIL overturned on OOS

## Do NOT retry (dead ends)

- Initial Short→Long as default without right-side confirmation

## Doc updates required?

- [x] backlog P1-02..08 marked done
- [ ] CURRENT_CONCLUSIONS after full 65d run
