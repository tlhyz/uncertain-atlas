# Review Log — P6-03 Promote ETH Row to MEDIUM Confidence

## Meta

- **date_utc:** 2026-09-14T10:22Z
- **task:** P6-03
- **method:** Formal promotion gate checklist (reuse P6-02 `live_promotion.py`)
- **output:** outputs/experiments/p6_promotion_gates/eth_promotion_gate.json

## Promotion gates (ETH, 1.5x lev 0.40 ATR ±5)

| Gate | Status | Blocks | Evidence |
|------|--------|:------:|----------|
| Temporal OOS holdout | **fail** | yes | P5-04: ETH not holdout-tested; P2-03 all lev ~−87.5% |
| Calendar walk-forward | **fail** | yes | P5-03 mean test −86.58% (BTC calendar proxy) |
| MC DD tail | **fail** | yes | P5-05 P(DD>20%)=89% |
| C1 tick edge | **fail** | yes | P2-03 all lev ~−87.5% (C-06) |
| Param plateau | **fail** | yes | P5-02 0.40 worst Calmar |
| Portfolio C-07 | **fail** | yes | OOS+MC gates FAIL |
| Gate fill cal | conditional | no | P6-01 BAR BTC only |
| A/B PERP>ETF | conditional | no | C-02 BAR only |

**Blocking failures: 6/6 required gates**

## Question

Can the ETH crypto grid row be promoted to (or retain) MEDIUM live confidence?

## Findings

1. **Promotion:** **FAIL** — same gate structure as BTC (P6-02).
2. **ETH-specific:** No dedicated temporal holdout run in P5-04; C1 tick sweep (P2-03) alone fails catastrophically (~−87.5% all leverage).
3. **Stale MEDIUM label** from A/B bar PERP>ETF — does not validate crypto grid FSM params.
4. **Demotion applied:** ETH row → **LOW** with evidence `C-06/C-07 FAIL; A/B bar only`.
5. **SOL still MEDIUM** — not reviewed this task (no P6-04 equivalent for SOL in backlog; P6-05 synthesis next).

## Verdict

- **task_verdict:** **done**
- **promotion_verdict:** **FAIL**
- **confidence_action:** **MEDIUM → LOW**

## Red team (≥5)

1. ETH lacks dedicated OOS holdout window — fail inferred from P2-03 + BTC proxy WF
2. ETH Sep data gap noted in manifests — tick results may understate worst case
3. Same 0.40 ATR default as BTC — plateau FAIL applies identically
4. A/B bar on Gate may differ from Binance C1 tick path
5. Demotion does not block future ETH re-test with new hypothesis

## Next

- P6-04 Tech row Cash→Long OOS check
- P6-05 final LIVE_CANDIDATES.md review (include SOL demotion recommendation)
