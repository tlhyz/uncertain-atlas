# NEXT_EXPERIMENTS.md

> Auto-generated after Phase 1 audit. Sorted by **Expected Information Gain** — not expected profit.  
> Updated: 2026-09-13

**Phase 2 entry blocked until:** TASK-0008, TASK-0009, TASK-0010 complete (see GAP_ANALYSIS §9).

---

## Priority Queue

| Rank | ID | Question | Why First | Blocker |
|------|-----|----------|-----------|---------|
| 1 | INFRA-001 | Can we trust the data? | Without quality gate, all results void | TASK-0008 |
| 2 | INFRA-002 | Does accounting conserve equity? | Silent bugs invalidate PnL | TASK-0009 |
| 3 | INFRA-003 | Do signals leak future data? | FSM conclusions untrustworthy | TASK-0010 |
| 4 | EXP-TECH-001 | Cash→Long vs Short→Long? | **Highest strategy structure question** — FAIL on Gate+7d tick but needs 65d + Cash baseline | TASK-0013, infra |
| 5 | EXP-TECH-002 | Does grid add total equity (GRID_VALUE_ADD)? | Grid may profit but lose on inventory | INFRA + isolated grid runner |
| 6 | EXP-CRYPTO-001 | BTC leverage 1.25–2.0 sweet spot? | Majors PERP STRONG but leverage unset | ETH/SOL data fix |
| 7 | EXP-CRYPTO-004 | ATR 0.3–0.6 plateau exists? | Only after structure questions answered | Plateau detector |
| 8 | EXP-CROSS-001 | Independent vs unified FSM? | Portfolio structure — WEAK evidence only | Both books validated |
| 9 | EXP-TECH-008 | SOXL effective beta vs contract leverage? | Risk sizing for Tech book | effective_beta.py |
| 10 | EXP-CROSS-002 | Tech↓ Crypto↑ decoupling real? | C1 seed STRUCTURAL only | Binance multi-year data |

---

## Explicitly Deprioritized (Do Not Run Yet)

| ID | Reason |
|----|--------|
| Fine ATR 0.42 vs 0.44 | Parameter tuning before structure answered — forbidden |
| 3L ETF grid re-test | LEDGER-001 FAILED — dead end without new hypothesis |
| 3x PERP unattended | LEDGER-006 FAILED — stress only |
| Martingale variants | Policy forbidden |
| Mass dual parameter sweep | C-02 static Q-answers — fix report first |

---

## After Each Experiment

1. Write review log → `outputs/review_logs/`
2. Update `docs/RESEARCH_LEDGER.md`
3. Update `experiments/registry.yaml`
4. Red team pass or BLOCKED
5. Regenerate this file

---

## Valid Terminal Outcomes

- **NO EDGE FOUND** on Short→Long → simplify to Cash→Long or directional only
- **NO EDGE FOUND** on grid → focus on regime switching without grid
- **NO EDGE FOUND** on cross-market independence → single-book or fixed allocation

All are legitimate. Do not force complexity.
