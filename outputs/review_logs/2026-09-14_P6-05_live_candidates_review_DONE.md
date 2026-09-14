# Review Log — P6-05 Final LIVE_CANDIDATES.md Review

## Meta

- **date_utc:** 2026-09-14T10:42Z
- **task:** P6-05
- **method:** Synthesize P6-01…P6-04 + SOL promotion gate; rewrite `outputs/LIVE_CANDIDATES.md`
- **outputs:** outputs/LIVE_CANDIDATES.md, outputs/experiments/p6_promotion_gates/sol_promotion_gate.json

## P6 phase rollup

| ID | Verdict | Key action |
|----|---------|------------|
| P6-01 | CONDITIONAL PASS | Gate/BTC BAR fill_ratio 0.986 |
| P6-02 | FAIL | BTC MEDIUM→LOW |
| P6-03 | FAIL | ETH MEDIUM→LOW |
| P6-04 | FAIL | Tech OOS −75pp vs B4 |
| P6-05 | **DONE** | SOL MEDIUM→LOW; final table audit |

## SOL promotion gate (1.25x lev 0.40 ATR ±5)

| Gate | Status | Evidence |
|------|--------|----------|
| C1 tick edge | **fail** | P2-04 all lev −88.01%; crypto_max_dd=100% |
| OOS / WF / MC DD / plateau / C-07 | **fail** | Same portfolio gates as BTC/ETH |
| 3x liq history | **fail** | C-03 HIGH — SOL 3x PERP liquidations in A/B |

**Blocking failures: 6/6** — demote **MEDIUM → LOW**

## Final confidence audit

| Row | Before P6 | After P6-05 | Highest evidence |
|-----|-----------|-------------|------------------|
| SOXL | LOW | **LOW** | P6-04 OOS FAIL |
| SNXX | LOW | **LOW** | P6-04 OOS FAIL |
| BTC | MEDIUM | **LOW** | P6-02 |
| ETH | MEDIUM | **LOW** | P6-03 |
| SOL | MEDIUM | **LOW** | P6-05 |
| PENGU/PUMP | LOW | **LOW** | unchanged |

**MEDIUM+ rows: 0 / 7**

## Question

After P6 live-candidate phase, are any rows honestly deployable?

## Findings

1. **Zero deployable candidates** — all rows LOW; terminal `NO EDGE FOUND` for current hypothesis.
2. **LIVE_CANDIDATES.md rewritten** with P6 summary, book verdicts, execution footnote, non-candidate table.
3. **P6 phase complete** — all P6-01…P6-05 done; only P0-02 pending (blocked on PR merge).
4. **C-07 stands** — no contradiction with final table.
5. **Gate fill cal (P6-01)** documented but does not upgrade any row.

## Verdict

- **task_verdict:** **done**
- **live_candidates_verdict:** **NO DEPLOYMENT** — honest LOW across board
- **P6_phase:** **COMPLETE**

## Red team (≥5)

1. SOL demotion uses BTC WF proxy — no dedicated SOL holdout run
2. PENGU/PUMP never got promotion gate — remain LOW by default
3. B4 holdout −0.38% on Tech OOS — neither Tech nor B4 is positive alpha
4. C-02 A/B bar evidence still valid for PERP vs ETF structure — not retracted, just not live grid
5. Re-opening live path requires new hypothesis + fresh OOS — not parameter tweak

## Next

- P0-02 pytest on main after PR #8 merge (human gate)
- Optional: paper engine (ROADMAP L10) only after new edge hypothesis
