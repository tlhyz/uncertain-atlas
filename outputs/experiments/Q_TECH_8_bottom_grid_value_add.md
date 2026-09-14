# Q-tech-8 — Bottom grid value-add

**Status:** **COMPLETE FAIL** (2026-09-14T04:20Z)  
**Window:** Binance SOXL/SNXX 65d tick overlap 2026-07-09 → 2026-09-11 (1546 bars @ 1h)  
**Fill:** Base tick-precise  
**Primary evidence:** P3-01 benchmarks (B3 vs B5–B10) + P3-08 grid-mix sweep

---

## Question

Does the **bottom grid phase** in the Short→Grid→Trend FSM **add net equity** vs running without it (or vs isolated long grid)?

---

## Answer

**NO.** Bottom grid embedded in the full FSM **does not add value** — isolated long grid (**B3**) massively outperforms the full Short→Grid→Trend pipeline on the same window.

| Strategy | Return | MaxDD | Interpretation |
|----------|--------|-------|----------------|
| **B3 Long grid only** | **-25.20%** | 21.08% | Grid without Short FSM |
| B4 Directional long only | -25.19% | 21.77% | No grid |
| B5 Short→Long grid (full FSM) | -58.70% | 52.76% | Short + bottom grid + trend |
| B6–B10 FSM variants | -58.70% | 52.76% | All identical on overlap |

**Gap:** Full FSM with bottom grid is **33.50pp worse** than long grid only. Bottom grid does **not salvage** Short losses (Q3 in `DUAL_REPORT.md`).

---

## P3-08 grid-mix evidence (grid in trend phase)

| Mix | Return | vs default (−58.70%) |
|-----|--------|------------------------|
| G100 (max grid) | -71.41% | −12.71pp worse |
| G75 | -59.53% | −0.83pp worse |
| **G50** | **-57.85%** | +0.85pp better |
| G25 | -64.97% | −6.27pp worse |
| dynamic (default) | -58.70% | match |

More grid (G100) is **catastrophic**; moderate grid (G50) modestly helps vs default but still **−32.65pp** behind B3 long grid only. Grid phase tuning cannot flip sign vs isolated grid baseline.

---

## Cross-venue replication

| Venue | Grid-only | Dual / Short→Long | Grid beats dual? |
|-------|-----------|---------------------|------------------|
| Gate overlap | -26.40% | -51.05% | **Yes** (+24.65pp) |
| Binance 7d tick | -25.36% | -77.82% | **Yes** (+52.46pp) |
| **Binance 65d tick** | **-25.20%** | **-58.70%** | **Yes** (+33.50pp) |

Consistent FAIL across venues: bottom grid in FSM context is net destructive vs standalone grid.

---

## GRID_VALUE_ADD (LEDGER-008) status

Formal isolated metric `GRID_VALUE_ADD = Equity(with Grid) − Equity(same exposure without Grid)` **not yet implemented** as standalone per-asset study (EXP-TECH-002 blocked).

**Proxy verdict from benchmarks:** On overlap, **grid-only equity path dominates** any FSM path that includes Short + bottom grid. Formal GRID_VALUE_ADD implementation remains future work; **directional answer is FAIL** from B3 vs B5 comparison.

---

## Mechanism

1. Short phase losses dominate before bottom grid activates (P3-12).
2. Bottom grid runs on depleted equity with adverse inventory from Short (P3-03 structure inert).
3. Grid turnover/fees on underwater book (P3-08 G100) amplifies losses.
4. B5–B10 all −58.70% identical — FSM phase variants do not differentiate; grid phase not the binding improvement lever.

---

## Red team

1. B3 is long grid from start, not apples-to-apples with bottom grid after Short — fair critique; still best available proxy on same data.
2. Isolated bottom-grid-only benchmark not run (would need custom ablation).
3. FAIL_F1/F2 not executable — grid behavior in direct-up path untested.
4. Formal GRID_VALUE_ADD metric unimplemented.
5. G50 + drawdown C joint sweep not run.

---

## Recommendation

- Do **not** claim bottom grid adds equity in Short→Long FSM on current evidence.
- If grid is retained, test **long grid only** (B3 path) separately from Short FSM — B3 still −25% (not live-ready) but 33pp better than dual.
- Implement LEDGER-008 isolated GRID_VALUE_ADD before parameter sweeps on grid spacing.

---

## Evidence chain

- P3-01: `outputs/review_logs/2026-09-13_P3-01_dual_tick_FAIL.md`
- P3-08: `outputs/review_logs/2026-09-14_P3-08_grid_mix_FAIL.md`
- P3-12 Q-tech-1: `outputs/experiments/Q_TECH_1_short_vs_cash_long.md`
- DUAL_REPORT Q3: `outputs/dual_engine_perp_binance_ticks_65d/DUAL_REPORT.md`
