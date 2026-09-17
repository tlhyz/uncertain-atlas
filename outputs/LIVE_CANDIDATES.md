# Live Candidate Parameters

> **NO LIVE DEPLOYMENT.** All rows **LOW confidence — research reference only.**  
> P6 phase complete (2026-09-14): zero MEDIUM+ rows survive OOS, MC, and promotion gates.

## P6 verdict summary

| Check | Result | Log |
|-------|--------|-----|
| Gate fill calibration (BTC 1h BAR) | CONDITIONAL PASS — fill_ratio 0.986; not binding | P6-01 |
| BTC promotion gate | FAIL → demoted MEDIUM→LOW | P6-02 |
| ETH promotion gate | FAIL → demoted MEDIUM→LOW | P6-03 |
| Tech vs Cash→Long OOS | FAIL −75pp holdout | P6-04 |
| SOL promotion gate | FAIL → demoted MEDIUM→LOW | P6-05 |
| **Deployable candidates** | **0** | C-07 |

---

## Parameter table (research reference)

| Asset | State | Lev | Grid ATR | Range | G/D Mix | Margin/Res | Funding Cap | Max Alloc | Pause Rule | Confidence | Evidence |
|-------|-------|-----|----------|-------|---------|------------|-------------|-----------|------------|------------|----------|
| SOXL | T2_BOTTOM_GRID | 1.25x | 0.40 | ±5 | 80/20 | 70/30 | TBD | 6500 tech book | DD hard −20% | **LOW** | OOS FAIL vs B4 −75pp (P6-04) |
| SNXX | T3_REVERSAL | 1.25x | 0.40 | ±5 | 60/40 | 70/30 | TBD | ~30% tech | R4 confirm | **LOW** | OOS FAIL vs B4 −75pp (P6-04) |
| BTC | BULL | 1.5x | 0.40 | ±5 | 60/40 | 70/30 | 1.5%/7d | 833 crypto | funding stress | **LOW** | C-06/C-07 FAIL; A/B bar only |
| ETH | BULL | 1.5x | 0.40 | ±5 | 60/40 | 70/30 | 1.5%/7d | 833 crypto | funding stress | **LOW** | C-06/C-07 FAIL; A/B bar only |
| SOL | BULL | 1.25x | 0.40 | ±5 | 60/40 | 70/30 | 1.5%/7d | 833 crypto | no 3x | **LOW** | C-06/C-07 FAIL; P2-04 −88% |
| PENGU | satellite | 1.0x | 0.50 | ±5 | 80/20 | 80/20 | 1%/7d | ≤5% acct | meme cap | **LOW** | Short history |
| PUMP | satellite | 1.0x | 0.50 | ±5 | 80/20 | 80/20 | 1%/7d | ≤5% acct | meme cap | **LOW** | Short history |

---

## Book A — Tech

**Verdict: NOT DEPLOYABLE**

- Short→Long FSM **FAIL** vs Cash→Long in-sample (−34pp, P3-12) and OOS (−75pp, P6-04)
- No FSM knob rescues vs B4 directional long (P3-02…P3-08)
- Gate overlap prior FAIL −51% vs B&H −30% (C-05)
- **Action:** Remove initial Short from baseline; do not paper-trade Tech FSM

## Book B — Crypto

**Verdict: NOT DEPLOYABLE**

- C1 tick grid FSM **NO EDGE** all majors ~−87% (C-06 HIGH)
- OOS holdout BTC 2024 −86.44%; walk-forward mean −86.58% (P5-03/04)
- MC P(DD>20%)=89% on dual-book reference (P5-05)
- Stale A/B bar PERP>ETF (C-02) does **not** validate listed grid params
- **Action:** Stop param sweeps on current FSM; investigate accounting floor or abandon grid hypothesis

## Execution calibration

- Gate vs Binance BTC 1h BAR fill_ratio **0.986** base (P6-01) — modest drift; volume not binding at grid size tested
- Tick-path Gate calibration **not done** — BAR label required
- Raising confidence requires tick calibration + strategy edge — neither present

---

## Explicit non-candidates

| Claim | Status |
|-------|--------|
| Tech Short→Long live | **FAIL** — P6-04 OOS |
| Crypto grid FSM live | **FAIL** — C-06, P6-02/03/05 |
| Dual-book combined live | **FAIL** — C-07 |
| 3x PERP unattended | **FAIL** — C-03 |
| Rebate as alpha | **FAIL** — C-04 |

**Terminal outcome for current hypothesis set:** `NO EDGE FOUND` for live deployment.
