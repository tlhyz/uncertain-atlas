# Q-tech-9 — Grid in trend phase

**Status:** **CONDITIONAL FAIL** (2026-09-14T04:30Z)  
**Window:** Binance SOXL/SNXX 65d tick overlap 2026-07-09 → 2026-09-11 (1546 bars @ 1h)  
**Fill:** Base tick-precise  
**Primary evidence:** P3-08 grid-mix sweep (G100/G75/G50/G25/dynamic) + P3-01 benchmarks

---

## Question

What is the optimal **grid vs directional mix in the trend phase**, and does grid in trend **add value** vs going fully directional?

---

## Answer

**Grid in trend phase has a narrow sweet spot at ~50/50 (G50), but FAILS vs simpler baselines.**

| Mix | Grid share | Return | MaxDD | Calmar | vs default (−58.70%) |
|-----|------------|--------|-------|--------|------------------------|
| G100 | 100% grid | -71.41% | 48.27% | -2.07 | −12.71pp |
| G75 | 75% | -59.53% | 43.36% | -2.29 | −0.83pp |
| **G50** | **50%** | **-57.85%** | 50.73% | -1.96 | **+0.85pp (best return)** |
| G25 | 25% | -64.97% | 42.02% | -2.37 | −6.27pp |
| dynamic | schedule | -58.70% | 52.76% | **-1.88 (best Calmar)** | match |

**U-shaped curve:** Too much grid (G100) or too little (G25) both hurt. **G50 is optimum** within discrete sweep; default dynamic matches baseline dual exactly.

**Vs baselines (P3-01):**

| Strategy | Return | vs G50 |
|----------|--------|--------|
| B3 Long grid only | -25.20% | G50 **32.65pp worse** |
| B4 Directional long | -25.19% | G50 **32.66pp worse** |
| B2 Buy & Hold | -33.49% | G50 **24.36pp worse** |
| **G50 (best mix)** | **-57.85%** | — |

Grid in trend phase **does not rescue** the FSM — even optimal G50 remains catastrophic vs long-only or grid-only baselines.

---

## Q4 Grid→Directional conversion (related)

P3-08 **measured** what Gate bar reports only narrated:

- **Reduce grid below 50%** in trend helps vs G100/G75 on this window
- **Going below 25% grid (G25) reverses** the benefit — pure directional in trend phase is worse than G50
- Default **dynamic schedule ≡ baseline dual** (−58.70%) — no improvement vs fixed G50 on return (+0.85pp for G50)

**Recommendation:** If trend phase retained at all, **cap grid at ~50%** (not 100%, not <25%). Still not deployable without beat B3/B4 first.

---

## Interaction with other knobs

| Combined hint | Return | Notes |
|---------------|--------|-------|
| G50 alone | -57.85% | best grid-mix |
| Drawdown C alone (P3-04) | -56.08% | best drawdown set |
| Default dual | -58.70% | baseline |
| G50 + drawdown C | **not run** | speculative ~−55% bound; still >> B3 |

---

## Cross-venue note

Gate `DUAL_REPORT.md` claims dynamic mix improves vs G100 in uptrend legs — **not replicated** on Binance 65d tick where dynamic ≡ dual and G50 only +0.85pp. Treat Gate narrative as **WEAK** until same sweep on Gate ticks.

---

## Red team

1. G50 +0.85pp may be noise (single window)
2. Only 5 discrete mixes — optimum may be 40/60 or 55/45
3. Trend phase not isolated — mix applies to full FSM including Short
4. Calmar best at dynamic, return best at G50 — no single optimum
5. Joint G50 + drawdown C not measured

---

## Recommendation

- **Do not deploy** grid-in-trend tuning as alpha — FAIL vs B3/B4/B2.
- **If FSM research continues:** fixed **G50** preferred over dynamic or G100 for trend phase on this evidence.
- **P3-16:** Gate OOS on {drawdown C, G50, default} only if user requests — no MEDIUM candidate today.

---

## Evidence chain

- P3-08: `outputs/review_logs/2026-09-14_P3-08_grid_mix_FAIL.md`
- P3-01 benchmarks: `outputs/review_logs/2026-09-13_P3-01_dual_tick_FAIL.md`
- P3-14 Q-tech-8: `outputs/experiments/Q_TECH_8_bottom_grid_value_add.md`
