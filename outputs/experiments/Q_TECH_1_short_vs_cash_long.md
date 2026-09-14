# Q-tech-1 — Short→Long vs Cash→Long

**Status:** **COMPLETE FAIL** (2026-09-14T04:10Z)  
**Window:** Binance SOXL/SNXX 65d tick overlap 2026-07-09 → 2026-09-11 (1546 bars @ 1h)  
**Fill:** Base tick-precise (aggTrades tech legs)  
**Primary evidence:** P3-01 benchmarks + P3-02…P3-08 FSM knob sweeps

---

## Question

Does the **Short→Grid→Trend (Short→Long) FSM** beat **Cash→Long** (hold cash, enter long when signal confirms — proxied by directional-long-only baseline)?

---

## Answer

**NO.** Short→Long dual **FAILS decisively** vs Cash→Long on Binance 65d tick overlap.

| Strategy | Return | MaxDD | Calmar | vs dual |
|----------|--------|-------|--------|---------|
| **B1 Cash (Cash→Long upper bound)** | **0.00%** | 0.00% | 0.00 | +58.70pp |
| **B4 Directional long (Cash→Long proxy)** | **-25.19%** | 21.77% | -3.71 | **+33.51pp** |
| B3 Long grid only | -25.20% | 21.08% | -3.83 | +33.50pp |
| B2 Buy & Hold | -33.49% | 52.63% | -1.71 | +25.21pp |
| **B5–B10 Short→Long / dual (default)** | **-58.70%** | 52.76% | -1.88 | — |

**Implication (per `docs/RESEARCH_GOALS.md`):** **Remove initial Short from baseline.** Tactical Short is not net-positive on measured windows.

---

## P3 FSM knob sweeps (can any rescue Short→Long vs Cash→Long?)

Best result per sweep vs **B4 directional long (-25.19%)**:

| Sweep | Task | Best config | Return | vs B4 | vs default dual |
|-------|------|-------------|--------|-------|-----------------|
| Short init | P3-02 | 20% | -58.70% | −33.51pp | match |
| Short structure | P3-03 | all variants | -58.70% | −33.51pp | inert |
| Drawdown set | P3-04 | **C (wider)** | **-56.08%** | −30.89pp | +2.62pp |
| Right-side reserve | P3-06 | 25% | -58.92% | −33.73pp | −0.22pp |
| SOXL/SNXX weight | P3-07 | 70/30 default | -58.70% | −33.51pp | match |
| Grid→Trend mix | P3-08 | **G50** | **-57.85%** | −32.66pp | +0.85pp |

**No knob beats B4 Cash→Long proxy.** Best combined hints (drawdown C + G50) not yet joint-swept; even optimistic bound ~−56% still **−31pp** behind directional long.

---

## Cross-venue replication

| Venue | Window | Short→Long / dual | Cash→Long proxy | Verdict |
|-------|--------|-------------------|-----------------|---------|
| Gate overlap | 2026-07-14 → 09-12 | -51.05% | B4 ~-17% (Gate) | FAIL |
| Binance 7d tick | 2026-09-05 → 09-11 | -77.82% | B4 -25.19% | FAIL |
| **Binance 65d tick** | **2026-07-09 → 09-11** | **-58.70%** | **B4 -25.19%** | **FAIL** |

Direction consistent across venues and windows. C-05 confidence **HIGH**.

---

## Mechanism (why Short→Long loses)

1. Initial Short accumulates losses in sustained bounce / direct-up paths (FAIL_F1 untested on Binance — data blocked).
2. Drawdown-tier reductions and bottom grid **do not recover** Short losses before reversal phase (P3-03 structure knob inert).
3. Pure grid phase (G100) is catastrophic (-71.41%) — grid-heavy short-side inventory destroys equity.
4. Best modest improvements (drawdown C, G50) tune **magnitude of loss**, not sign vs simpler long-only entry.

---

## Red team

1. Cash (0%) is not deployable — B4 directional long is the fair Cash→Long proxy; still FAIL by 33pp.
2. B3/B4 ~-25% also negative — long-only not a live candidate either on this window.
3. FAIL_F1/F2 windows STRUCTURAL_SEED_ONLY — worst-case short paths not tick-tested on Binance.
4. Joint sweep (drawdown C + G50) not run — unlikely to close 31pp gap.
5. Gate OOS on any finalist not run (P3-16 pending).

---

## Recommendation

- **Baseline:** Cash→Long / directional-long-only; **drop initial Short** until new hypothesis + OOS beat.
- **Do not promote:** drawdown set C or G50 without beat B3 grid-only (-25.20%) first.
- **Next research:** P3-14 Q-tech-8 (bottom grid value-add), P3-16 Gate OOS on top-3 param sets (if any MEDIUM candidate emerges — none today).

---

## Evidence chain

- P3-01: `outputs/review_logs/2026-09-13_P3-01_dual_tick_FAIL.md`
- P3-02…P3-08 review logs under `outputs/review_logs/2026-09-14_P3-*`
- LEDGER-003: `docs/RESEARCH_LEDGER.md`
- C-05: `docs/CURRENT_CONCLUSIONS.md`
