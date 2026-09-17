# Review Log — P3-11 Similar-window search top-20

## Meta

- **date_utc:** 2026-09-14T04:00Z
- **experiment_id:** dual_binance_tick_similar_windows
- **task:** P3-11
- **config:** configs/experiments/dual_binance_tick_similar_windows.yaml
- **output:** outputs/experiments/dual_binance_tick_similar_windows/dual_results.json
- **runtime:** <1min (bar-mode, no tick backtest)

## Data coverage

- **overlap:** 2026-07-09 14:00 → 2026-09-11 23:00 UTC
- **bars:** 1546 @ 1h (only Binance SOXL/SNXX history loaded)

## Results

```json
"similar_windows": []
```

Default seed **TECH_T2** (2025-02→2025-06) has **zero SOXL bars** in loaded range → `extract_template()` returns None → empty list.

Manual probe on same data:

| Seed | Windows found | Notes |
|------|---------------|-------|
| TECH_T2 | **0** | no template (STRUCTURAL_SEED_ONLY) |
| TECH_T3 | **1** | composite 0.9677; only scannable window at overlap start |
| TECH_T4 | **1** | composite 0.7536 |

**Root cause:** `search_similar_windows()` uses `horizon_bars=1440` (60d) with `step_bars=168` on **1546 bars** → at most **1** sliding window (`i0=0` only). **Top-20 impossible** on current 65d SOXL history without extending kline range or shrinking horizon.

## Verdict

- **task_verdict:** **BLOCKED**
- **reason:** Default seed unavailable; 65d overlap insufficient for top-20 similar-window scan
- **unblock:** (a) extend SOXL Binance klines before 2026-07-09, or (b) pass `similar_search_seed: TECH_T3` + reduce `horizon_bars` in runner config

## Red team (≥5)

1. TECH_T2 BTC proxy fallback not triggered with cache_only bar load
2. Single-window self-match (TECH_T3 composite 0.97) is tautological — not OOS validation
3. Similarity on 65d crash window may not generalize
4. No backtest on discovered windows yet — search-only task incomplete
5. SNXX template path untested for multi-symbol top-20

## Next

- Extend SOXL history download (P1 extension) before retry
- Wire `similar_search_seed` + `horizon_bars` config knobs in `run.py` for retry
- P3-12 Q-tech-1 answer can proceed from existing FAIL evidence
