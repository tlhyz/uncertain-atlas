# Current Conclusions (Honest — 2026-09-13)

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

### C-06: Crypto grid FSM on C1 tick shows no leverage sweet spot (SOL/ETH)
- **Confidence:** MEDIUM (BTC scan pending P2-02 restart)
- **Supporting:** P2-03 ETH all lev ~-87.5%; P2-04 SOL all lev ~-88.0%; tick-precise Base fill
- **Contradicting:** LEDGER-002 bar-mode PERP>ETF — **different engine/window/config**; does not overturn A/B bar evidence
- **Implication:** Do not deploy current crypto grid FSM on C1 parameters; investigate accounting floor (~12% equity)

---

## WEAK EVIDENCE

### W-01: Independent Crypto book may help vs unified Tech signal
- **Confidence:** LOW
- **Supporting:** Gate overlap Δreturn +2.3%, ΔDD -2.06%
- **Contradicting:** Binance 7d tick — no benefit (Δreturn 0)
- **Status:** UNTESTED on multi-year Binance ticks

### W-02: 0.40 ATR grid spacing near parameter plateau
- **Confidence:** LOW (downgraded Phase 1 red team)
- **Supporting:** Prior demo sweeps, dual report narrative
- **Contradicting:** Dual report Q9 may be **static template** — not verified by executed sweep
- **Action:** Re-verify with plateau detector after EXP-CRYPTO-004 infra ready

---

## UNTESTED (Honest)

| Claim | Blocker | Priority |
|-------|---------|----------|
| Regime switching > pure grid | Full pipeline + OOS | After GRID_VALUE_ADD |
| GRID_VALUE_ADD > 0 for any asset | Isolated grid study | EXP-TECH-002 |
| Crypto leverage sweet spot 1.25–2.0 | **PARTIAL FAIL** SOL/ETH; BTC P2-02 restart | P2-10 when BTC done |
| Binance tick-precise majors PERP vs ETF | Not re-run (bar A/B only) | Medium |
| Cross-market Tech↓ Crypto↑ capture | Real data on both books | EXP-CROSS-002 |
| Gate OOS fill calibration | Script stub | LEVEL 9 |

---

## LIVE Candidates

See `outputs/LIVE_CANDIDATES.md`.

**No CORE or SMALL LIVE candidates.** BTC/ETH/SOL at MEDIUM confidence are **A/B research rows only** — require Gate OOS + infra gates before upgrade.

**Tech Short→Long:** explicitly **NOT** a live candidate until beats Cash→Long on Binance ticks + Gate OOS.

---

## Change Log

| Date | Change | Reason |
|------|--------|--------|
| 2026-09-13 | C-06 added; C-05 65d tick FAIL | P1-11, P2-03, P2-04 review logs |
| 2026-09-13 | UNTESTED leverage row → PARTIAL FAIL | SOL/ETH C1 tick scans complete |
| 2026-09-13 | W-02 confidence LOW (was implicit medium) | Phase 1 red team: template Q-answers |
| 2026-09-13 | C-05 confidence HIGH | Binance 7d tick FAIL reinforces Gate FAIL |
| 2026-09-13 | Added evidence chain columns | Phase 1 audit requirement |
