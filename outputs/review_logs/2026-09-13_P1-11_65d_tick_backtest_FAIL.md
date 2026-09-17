# Review Log — P1-11 Full 65d Binance tick backtest

## Meta

- **date_utc:** 2026-09-13T05:17Z
- **experiment_id:** dual_binance_tick_65d
- **task:** P1-11
- **config_paths:** configs/experiments/dual_binance_tick_65d.yaml
- **output:** outputs/dual_engine_perp_binance_ticks_65d/DUAL_REPORT.md
- **fill_modes_verdict:** base (tick_precise aggTrades tech legs)
- **runtime:** ~218 min (~3h38m)

## Data coverage

- **venue / symbols:** Binance SOXL, SNXX, BTC/ETH/SOL
- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h (SNXX-limited overlap)
- **precision:** TICK (DATA_QUALITY PASS at job start)

## Results (Base fill, tick-precise)

| Benchmark | Return | MaxDD | Calmar |
|-----------|--------|-------|--------|
| B1 Cash | 0.00% | 0.00% | 0.00 |
| B2 Buy&Hold | **-33.49%** | 52.63% | -1.71 |
| B4 Directional long | **-25.19%** | 21.77% | -3.71 |
| B10 Dual independent | **-58.70%** | 52.76% | -1.88 |

Executive summary: dual **-58.70%** vs hold **-33.49%** → **FAIL**.

## vs 7d smoke (prior)

| Metric | 7d smoke | 65d full |
|--------|----------|----------|
| Dual return | -77.82% | -58.70% |
| B&H return | +1.03% | -33.49% |
| Verdict | FAIL | **FAIL** |

Different windows (7d Sep-05→11 vs full overlap Jul→Sep) but **Short→Long hypothesis not overturned**. Full run is less extreme than 7d slice but still loses to B&H and to directional-long (-25%).

## Verdict

- **task_verdict:** **PASS** (measurement complete, reproducible artifacts)
- **hypothesis_verdict:** **FAIL** (LEDGER-003 reinforced)
- **evidence_class:** STRONG (tick-precise Binance aggTrades, Base fill, 1546 bars)
- **one_line_summary:** 65d tick backtest confirms Tech Short→Long FSM fails vs B&H and vs Cash→Long on overlap window.

## Q3/Q14 highlights

- **Q3 bottom grid:** grid-only (-25.20%) beats dual (-58.70%) — bottom grid does NOT salvage Short→Long
- **Q11/Q14 independent books:** Δreturn 0 vs unified — no diversification benefit measured

## Red team (≥5 fake-good paths)

1. SNXX overlap truncation (1546 vs 1560 bars) — may under-sample SNXX stress  
2. Crypto book idle in tech-focused benchmarks — B10 includes crypto but tech FSM dominates loss  
3. Single overlap window Jul–Sep 2026 — not multi-regime OOS  
4. Base fill only in primary verdict — conservative may be worse  
5. B&H also negative (-33%) — relative FAIL still valid but absolute regime is bearish

## Doc updates

- [x] P1-11 mark **done**
- [ ] CURRENT_CONCLUSIONS — confirm LEDGER-003 after human review
- [ ] Q-tech-1: Cash→Long vs Short→Long still open (B1 vs B4 vs B5 measured here)

## Do NOT retry

- Deploy Short→Long FSM as default without new structural evidence
