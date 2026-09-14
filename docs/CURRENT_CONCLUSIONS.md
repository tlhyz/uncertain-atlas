# Current Conclusions (Honest — 2026-09-14)

> Update after each major experiment. **Do not beautify FAIL results.**  
> Each claim: confidence + supporting + contradicting experiments.

---

## CONFIRMED / STRONG EVIDENCE

### C-01: Long-run 3L ETF grid fails on total equity
- **Confidence:** HIGH
- **Supporting:** LEDGER-001, Exp 001, `outputs/research_sl_phase/`, Gate real ETF data
- **Contradicting:** None on real data
- **Mechanism:** Grid realized profit < inventory + directional loss

### C-02: Majors prefer 1.5–2x PERP grid over 3L ETF grid
- **Confidence:** MEDIUM-HIGH (BAR BACKTEST only; not tick-precise)
- **Supporting:** LEDGER-002, `outputs/ab_etf_vs_perp/`, PR #6, Base+Conservative
- **Contradicting:** PENGU/PUMP ETF win — WEAK (meme, short sample)
- **Assets:** BTC, ETH, SOL, SOXL, SNXX, AAOI → PERP; meme exception noted

### C-03: 3x PERP not unattended-safe
- **Confidence:** HIGH
- **Supporting:** LEDGER-006, liquidations on SOL, PENGU, PUMP in A/B
- **Contradicting:** None for unattended use case

### C-04: Rebate alone is not alpha
- **Confidence:** HIGH
- **Supporting:** LEDGER-005, AB Q7–Q8 — zero-rebate does not flip majors winner
- **Contradicting:** None

### C-05: Tech Short→Long FSM fails vs simpler baselines
- **Confidence:** HIGH
- **Supporting:** LEDGER-003, Gate -51% vs B&H -30%; Binance tick 7d -78% vs B&H +1%; **65d tick -58.70% vs B&H -33.49%** (P1-11)
- **Contradicting:** None to date
- **Implication:** Do not deploy initial Short without right-side confirmation

### C-06: Crypto grid FSM on C1 tick — NO EDGE (all majors, all param sweeps)
- **Confidence:** **HIGH** (P2 phase complete 2026-09-13)
- **Supporting:** P2-02 BTC lev 1.25–2.0x all ~-87%; P2-03 ETH; P2-04 SOL; P2-05 ATR step; P2-06 ATR range ±3/5/7; P2-07 grid mix 80_20→dynamic; P2-14 C1 tick baseline -87.30%; tick-precise Base fill
- **Contradicting:** LEDGER-002 bar-mode PERP>ETF — **different engine/window/config**; does not overturn A/B bar evidence
- **Implication:** Do not deploy current crypto grid FSM on C1 parameters; investigate accounting floor (~12% equity); stop C1 param sweeps

### C-07: Dual-book fails OOS and Monte Carlo robustness gates
- **Confidence:** HIGH (P5 phase complete 2026-09-14)
- **Supporting:** P5-03 calendar WF mean test −86.58%; P5-04 holdout 0/2 pass; P5-05 P(DD>20)=89% on 65d; P5-04 dual holdout −75.5% vs B&H −33.5%
- **Contradicting:** None for live deploy
- **Implication:** No finalist survives temporal OOS or DD tail MC — do not promote to P6 without new hypothesis

## WEAK EVIDENCE

### W-01: Independent Crypto book may help vs unified Tech signal
- **Confidence:** LOW–MEDIUM (partial Binance upgrade)
- **Supporting:** Gate overlap Δreturn +2.3%; **P4-03 Binance 65d Regime B ind +2.3pp vs uni** when crypto active
- **Contradicting:** Binance 7d inert (Δreturn 0); unified coupling still FAIL (crypto wipe)
- **Status:** Helps only when crypto book active and regimes oppose — not general alpha

### W-02: 0.40 ATR grid spacing near parameter plateau
- **Confidence:** **FAIL / retract** (P5-02 on P2-05 sweep)
- **Supporting:** None actionable
- **Contradicting:** P2-05 + P5-02 — PLATEAU_INERT; 0.40 worst Calmar 4/4
- **Action:** Do not promote W-02; LEDGER-009 remains WEAK

---

## UNTESTED (Honest)

| Claim | Blocker | Priority |
|-------|---------|----------|
| Regime switching > pure grid | Full pipeline + OOS | After GRID_VALUE_ADD |
| GRID_VALUE_ADD > 0 for any asset | Isolated grid study | EXP-TECH-002 |
| Crypto leverage sweet spot 1.25–2.0 | **FAIL** all majors P2-02/03/04 | P2-10 Q-crypto-1 done |
| Binance tick-precise majors PERP vs ETF | Not re-run (bar A/B only) | Medium |
| Cross-market Tech↓ Crypto↑ capture | Real data on both books | EXP-CROSS-002 |
| Gate OOS fill calibration | Script stub; P3-16 blocked | P6-01 |
| P5 MC liquidation proxy | Daily bootstrap 0%; use DD MC | P5-06 done |

---

## LIVE Candidates

See `outputs/LIVE_CANDIDATES.md`.

**No CORE or SMALL LIVE candidates.** P5 OOS + MC gates **FAIL** (C-07). BTC/ETH/SOL MEDIUM rows remain **A/B research only**.

**Tech Short→Long:** explicitly **NOT** a live candidate until beats Cash→Long on Binance ticks + Gate OOS.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-09-14 | C-07 added; W-01/W-02 updated; P5 sync | Daily audit; P4-03/P5-02/P5-04/P5-05 review logs |
| 2026-09-13 | C-06 upgraded HIGH; P2 complete | P2-02/05/06/07 review logs |
| 2026-09-13 | C-06 added; C-05 65d tick FAIL | P1-11, P2-03, P2-04 review logs |
| 2026-09-13 | UNTESTED leverage row → PARTIAL FAIL | SOL/ETH C1 tick scans complete |
| 2026-09-13 | W-02 confidence LOW (was implicit medium) | Phase 1 red team: template Q-answers |
| 2026-09-13 | C-05 confidence HIGH | Binance 7d tick FAIL reinforces Gate FAIL |
| 2026-09-13 | Added evidence chain columns | Phase 1 audit requirement |
