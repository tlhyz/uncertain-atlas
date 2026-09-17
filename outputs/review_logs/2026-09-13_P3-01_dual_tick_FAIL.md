# Review Log — P3-01 dual Binance tick re-run

## Meta

- **date_utc:** 2026-09-13T19:20Z
- **experiment_id:** dual_binance_tick_65d (P3-01 re-run)
- **task:** P3-01
- **config:** configs/experiments/dual_binance_tick_65d.yaml
- **output:** outputs/dual_engine_perp_binance_ticks_65d/DUAL_REPORT.md
- **fill_mode:** base (tick_precise aggTrades tech legs)
- **runtime:** ~208min (~3h28m; benchmarks ~169min CPU + seed_windows ~39min)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h
- **precision:** TICK (DATA_QUALITY PASS, 41.3M aggTrade rows)

## Results (Base fill, tick-precise)

| Benchmark | Return | MaxDD | Calmar |
|-----------|--------|-------|--------|
| B1 Cash | 0.00% | 0.00% | 0.00 |
| B2 Buy&Hold | **-33.49%** | 52.63% | -1.71 |
| B3 Long grid only | **-25.20%** | 21.08% | -3.83 |
| B4 Directional long | **-25.19%** | 21.77% | -3.71 |
| B5–B10 Short→Long / dual | **-58.70%** | 52.76% | -1.88 |

Executive: dual **-58.70%** vs hold **-33.49%** → **FAIL**.

## vs P1-11 (identical)

| Metric | P1-11 (05:17Z) | P3-01 (19:19Z) |
|--------|----------------|----------------|
| Dual return | -58.70% | **-58.70%** |
| B&H return | -33.49% | **-33.49%** |
| Grid-only | -25.20% | **-25.20%** |

**Reproducible FAIL** — P3 Tech FSM gate confirmed on current branch.

## Verdict

- **task_verdict:** **PASS** (measurement complete, artifacts written)
- **strategy_verdict:** **FAIL** — Short→Long dual loses to B&H, Cash, and long-only baselines
- **C-05:** Reinforced **HIGH** — do not deploy initial Short FSM
- **Q-tech-1 partial:** B1 Cash (0%) > B4 directional (-25%) > B5 Short→Long (-58%) on overlap

## Red team (≥5)

1. Identical to P1-11 — no new information, confirms reproducibility not new edge  
2. B3/B4 ~-25% still negative — grid-only not a live candidate either on this window  
3. Crypto book in B10 shows no diversification benefit (Q11 Δreturn 0)  
4. FAIL_F1/F2 seed windows STRUCTURAL_SEED_ONLY — direct-up / inventory trap untested on ticks  
5. Base fill only — conservative not run

## Next

- P3-02 Short init 10/15/20% sweep  
- Remove Short from baseline until sweep shows beat Cash→Long (expect FAIL)
