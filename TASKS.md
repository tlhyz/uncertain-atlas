# TASKS — gate-grid-martingale

> Autonomous task system. Each task has a file in `tasks/`.  
> On completion: create `tasks/TASK_RESULT/TASK-XXXX.md`. On failure: mark FAILED + `NEXT QUESTION`.  
> Updated: 2026-09-13

---

## Status Legend

| Status | Meaning |
|--------|---------|
| `done` | Completed with TASK_RESULT |
| `in_progress` | Active work |
| `pending` | Ready to start |
| `blocked` | Waiting on dependency |
| `failed` | Attempted, hypothesis rejected — do not delete |

---

## Phase 1 — Audit & Governance (LEVEL 0)

| ID | Title | Status | Result |
|----|-------|--------|--------|
| [TASK-0001](tasks/TASK-0001.md) | Full repository audit | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0001.md) |
| [TASK-0002](tasks/TASK-0002.md) | Create RESEARCH_LEDGER from history | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0002.md) |
| [TASK-0003](tasks/TASK-0003.md) | Create ROADMAP LEVEL 0–12 | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0003.md) |
| [TASK-0004](tasks/TASK-0004.md) | Create experiment registry | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0004.md) |
| [TASK-0005](tasks/TASK-0005.md) | GAP_ANALYSIS + REPO_AUDIT | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0005.md) |
| [TASK-0006](tasks/TASK-0006.md) | Update CURRENT_CONCLUSIONS + CURSOR_HANDOFF | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0006.md) |
| [TASK-0007](tasks/TASK-0007.md) | Phase 1 independent self-audit (red team) | **done** | [PHASE1_SELF_AUDIT.md](PHASE1_SELF_AUDIT.md) |

---

## Phase 1.5 — Infrastructure Blockers (LEVEL 1–2 gates)

| ID | Title | Status | Depends |
|----|-------|--------|---------|
| [TASK-0008](tasks/TASK-0008.md) | DATA_QUALITY_REPORT pre-experiment gate | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0008.md) |
| [TASK-0009](tasks/TASK-0009.md) | ACCOUNTING_INVARIANTS + property tests | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0009.md) |
| [TASK-0010](tasks/TASK-0010.md) | test_no_future_leak.py | **done** | [TASK_RESULT](tasks/TASK_RESULT/TASK-0010.md) |
| [TASK-0011](tasks/TASK-0011.md) | Fix build_manifest rows + re-download ETH/SOL | **done** | merged into TASK-0008 manifest rebuild |
| [TASK-0012](tasks/TASK-0012.md) | Fix dual report Q-answers from actual sweeps | **pending** | TASK-0005 |
| [TASK-0013](tasks/TASK-0013.md) | Complete 65d Binance tick run + review log | **in_progress** | P1-11 (pre-Phase-1) |
| [TASK-0014](tasks/TASK-0014.md) | Merge PR #8 to main | **blocked** | human |

---

## Data Layer (DATA-001 → DATA-018)

| ID | Title | Status |
|----|-------|--------|
| DATA-001 | Binance historical trades downloader | partial → see `qtb/data/binance_futures.py` |
| DATA-002 | Binance aggTrades | **done** (Tech); ETH/SOL corrupt |
| DATA-003 | Binance funding | partial |
| DATA-004 | Binance klines | **done** |
| DATA-005 | Gate trades | **pending** |
| DATA-006 | Gate funding | **done** |
| DATA-007 | Contract metadata | partial |
| DATA-008 | Symbol lifecycle | **pending** |
| DATA-009 | Tick size history | **pending** |
| DATA-010 | Missing data detector | **pending** → TASK-0008 |
| DATA-011 | Duplicate detector | **pending** |
| DATA-012 | Outlier detector | **pending** |
| DATA-013 | Clock normalization | partial |
| DATA-014 | Checksum system | partial → TASK-0011 |
| DATA-015 | Data manifest | partial |
| DATA-016 | Dataset versioning | **pending** |
| DATA-017 | Cross-venue price validation | **pending** |
| DATA-018 | Data completeness score | **pending** |

---

## Execution Layer (EXEC-001 → EXEC-015)

| ID | Title | Status |
|----|-------|--------|
| EXEC-001 | Limit order state machine | partial |
| EXEC-002 | Partial fill | **done** |
| EXEC-003 | Multi-grid jump protection | partial |
| EXEC-004 | Maker/taker classification | partial |
| EXEC-005 | Volume cap | **done** |
| EXEC-006 | Queue pessimism | partial |
| EXEC-007 | Funding settlement | **done** |
| EXEC-008 | Isolated margin | **done** |
| EXEC-009 | Cross margin | **pending** |
| EXEC-010 | Liquidation | **done** |
| EXEC-011 | Reserve margin | partial |
| EXEC-012 | Fee | **done** |
| EXEC-013 | Rebate | **done** |
| EXEC-014 | Realized/unrealized accounting | partial → TASK-0009 |
| EXEC-015 | Daily equity reconciliation | **pending** |

---

## Phase 2 — First Research Questions (blocked until 1.5 complete)

| ID | Title | Status | Priority |
|----|-------|--------|----------|
| EXP-TECH-001 | Cash→Long vs Short→Long | **blocked** | #1 |
| EXP-TECH-002 | Grid→Trend value-add (GRID_VALUE_ADD) | **blocked** | #2 |
| EXP-CRYPTO-001 | BTC leverage 1.25–2.0 sweet spot | **blocked** | #3 |
| EXP-CRYPTO-004 | ATR 0.3–0.6 plateau | **blocked** | #4 |
| EXP-CROSS-001 | Independent vs unified FSM | **blocked** | #5 |

See `NEXT_EXPERIMENTS.md` for information-gain ordering.

---

## TOP 10 Next Tasks (Post Phase 1)

1. **TASK-0008** — DATA_QUALITY_REPORT gate (blocks all credible experiments)
2. **TASK-0009** — Accounting invariants + property tests
3. **TASK-0010** — test_no_future_leak.py
4. **TASK-0011** — Fix ETH/SOL aggTrades + manifest row counts
5. **TASK-0012** — Fix dual report static Q-answers
6. **TASK-0013** — Complete 65d tick run + honest review log
7. **TASK-0014** — Merge PR #8 (human)
8. **DATA-010–012** — Missing/duplicate/outlier detectors
9. **EXP-TECH-001** — Cash→Long vs Short→Long (first real question)
10. **EXP-TECH-002** — GRID_VALUE_ADD isolated grid study

---

## Reviewer Checklist (All Tasks)

- [ ] Evidence cites git commit + data manifest
- [ ] FAIL results not deleted or renamed
- [ ] Base + Conservative fills for conclusions
- [ ] Review log written under `outputs/review_logs/`
- [ ] Ledger updated in `docs/RESEARCH_LEDGER.md`
- [ ] Red team pass or BLOCKED documented
