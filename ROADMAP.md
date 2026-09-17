# ROADMAP — gate-grid-martingale Research System

> 13 levels from infrastructure to continuous research loop.  
> **Rule:** Do not advance until Acceptance Criteria pass + Red Team review.  
> Updated: 2026-09-13

---

## LEVEL 0 — Infrastructure

**Objectives:** Repo SSOT, docs, task system, experiment registry, review logs, CI/tests green.

**Tasks:**
- T0-1 Repository audit (`REPO_AUDIT.md`)
- T0-2 Research ledger (`docs/RESEARCH_LEDGER.md`)
- T0-3 Roadmap + task system (`ROADMAP.md`, `TASKS.md`, `tasks/`)
- T0-4 Experiment registry (`experiments/registry.yaml`)
- T0-5 Cursor governance rules (`.cursor/rules/`)
- T0-6 Review log policy operational

**Subtasks:** README handoff, backlog sync, gitignore hygiene, PR workflow.

**Dependencies:** None.

**Acceptance Criteria:**
- All Phase 1 deliverables exist and cross-linked
- 79+ tests pass
- FAIL history preserved in ledger
- Any agent can onboard in ≤5 min via README + CURSOR_HANDOFF

**Failure Criteria:**
- Missing ledger entries for known experiments
- Undocumented FAIL results
- No task IDs traceable to work items

**Outputs:** `REPO_AUDIT.md`, `GAP_ANALYSIS.md`, `PHASE1_SELF_AUDIT.md`, `docs/RESEARCH_LEDGER.md`

**Status:** ✅ **CONDITIONAL PASS** (2026-09-13) — infra gaps documented, not all fixed

---

## LEVEL 1 — Data

**Objectives:** Reliable multi-venue data pipeline with quality gates.

**Tasks:** DATA-001 → DATA-018 (see `TASKS.md`)

**Subtasks:**
- Binance Vision aggTrades/klines/funding (crypto long history)
- Gate candles/funding (execution calibration)
- Manifests + checksums + versioning
- Missing/duplicate/outlier detectors
- Cross-venue price validation
- `DATA_QUALITY_REPORT` pre-experiment gate

**Dependencies:** LEVEL 0.

**Acceptance Criteria:**
- Each DATA-* has unit test
- Pre-experiment gate blocks runs when missing rate / gaps exceed threshold
- SOXL/SNXX + BTC/ETH/SOL manifests valid (rows > 0, sha256 match)
- Precision labels enforced: TICK | BAR | STRUCTURAL SEED

**Failure Criteria:**
- Synthetic tick generation
- Experiments run on corrupt manifests
- Undeclared data gaps in reports

**Outputs:** `data/manifests/`, quality reports per run, `scripts/download_*.py`

**Status:** 🟡 **IN PROGRESS** (~35% — aggTrades for Tech done; detectors/gate missing)

---

## LEVEL 2 — Execution

**Objectives:** Unified realistic simulator: grid, directional, funding, margin, liquidation, partial fill.

**Tasks:** EXEC-001 → EXEC-015

**Subtasks:**
- Limit order state machine (bar + tick)
- Three fill modes (Optimistic/Base/Conservative)
- Maker/taker, rebate, funding settlement
- Isolated margin + liquidation
- Volume participation + queue pessimism

**Dependencies:** LEVEL 1 (valid data to test against).

**Acceptance Criteria:**
- Base + Conservative required for conclusions
- Tick path validated for Tech legs (every bar has aggTrades)
- EXEC-* unit tests green
- No multi-level phantom fills

**Failure Criteria:**
- Conclusions drawn from Optimistic only
- OHLC fill claimed as tick-precise

**Outputs:** `qtb/ab/fills.py`, `qtb/dual/tick_*`, execution test suite

**Status:** 🟡 **PARTIAL** (~60% — core fills done; cross-margin, daily recon missing)

---

## LEVEL 3 — Single Asset Research

**Objectives:** Isolated grid + leverage studies per asset without FSM mixing.

**Tasks:**
- Grid geometric vs arithmetic
- ATR spacing 0.2–0.75, range ±2–10 ATR
- GRID_VALUE_ADD metric
- Leverage scan BTC/ETH/SOL 1.0–2.0

**Dependencies:** LEVEL 1 + 2 + GRID_VALUE_ADD implementation.

**Acceptance Criteria:**
- GRID_VALUE_ADD computed and logged per config
- Grid FAIL if total equity < no-grid baseline
- Results in experiment registry with full output schema

**Failure Criteria:**
- Grid gross profit cited without total equity
- Mixed with direction FSM in same run

**Outputs:** Per-asset reports in `outputs/grid_study/`

**Status:** ⬜ **NOT STARTED** (blocked by LEVEL 1 gate)

---

## LEVEL 4 — Regime Detection

**Objectives:** No-lookahead regime labels for Crypto (7 classes) and Tech context.

**Tasks:**
- Bull, Bear, High/Low Vol Range, Breakout, Capitulation, Recovery
- `test_no_future_leak.py` for all features
- Regime classifier unit tests

**Dependencies:** LEVEL 3 feature modules stable.

**Acceptance Criteria:**
- All regime features pass leak tests
- Regime labels reproducible from manifest + commit

**Failure Criteria:**
- Centered windows / future bar access detected

**Outputs:** `src/features/regime.py` (full), regime validation reports

**Status:** ⬜ **NOT STARTED**

---

## LEVEL 5 — Strategy State Machine

**Objectives:** Validate Tech Short→Grid→Trend and Crypto independent FSM.

**Tasks:** EXP-TECH-001 → EXP-TECH-008, EXP-CRYPTO-001 → EXP-CRYPTO-007

**Subtasks:**
- Short init %, exit tiers, left/right timing, Grid→Trend mix
- Prior-wrong tests (direct up, sustained down, fake reversal)
- Cash→Long vs Short→Long as **first** question

**Dependencies:** LEVEL 4 + accounting invariants.

**Acceptance Criteria:**
- EXP-TECH-001 answered with Base+Conservative on Binance ticks
- FAIL preserved if hypothesis fails
- Parameter recommendations from actual sweeps (not templates)

**Failure Criteria:**
- Short→Long deployed as default without beating Cash→Long OOS

**Outputs:** `outputs/tech_fsm/`, `outputs/crypto_regime/`

**Status:** 🟡 **EARLY FAIL recorded** — full matrix blocked

---

## LEVEL 6 — Cross Asset Portfolio

**Objectives:** Independent Tech + Crypto books; allocation sweeps.

**Tasks:** EXP-CROSS-001 → EXP-CROSS-004, portfolio 70/20/10 etc.

**Dependencies:** LEVEL 5 both books validated independently.

**Acceptance Criteria:**
- Regime classification: Tech↓ Crypto↑ etc. on real data
- Independent vs unified FSM comparison with same capital/fees/fills

**Failure Criteria:**
- Forced complexity if independent books don't improve survivability

**Outputs:** `outputs/cross_market/`

**Status:** ⬜ **NOT STARTED**

---

## LEVEL 7 — Robustness

**Objectives:** Walk-forward, OOS, Monte Carlo, parameter plateau, sensitivity.

**Tasks:**
- Block bootstrap MC 1000+ paths (1D/3D/5D)
- Train/Val/OOS splits (rolling for short Tech history)
- Fee/funding/fill sensitivity ×0.5/×1/×2
- Negative controls + placebo tests
- ROBUSTNESS_SCORE

**Dependencies:** LEVEL 5–6 finalist strategies only.

**Acceptance Criteria:**
- OOS not used for tuning
- Plateau required — single-point peaks = REJECT
- MC outputs P5/P95, liq probability

**Failure Criteria:**
- Parameter snooping on OOS
- Fragile strategies promoted

**Outputs:** `outputs/robustness/`

**Status:** ⬜ **NOT STARTED** (MC stub)

---

## LEVEL 8 — Risk

**Objectives:** Portfolio risk controller, hard limits, dynamic de-risk.

**Tasks:**
- Contract leverage, effective beta, margin buffer monitoring
- Configurable limits (≤1.5x baseline, meme ≤5%, reserve ≥10%)
- DD/funding/correlation triggers → deleverage
- `effective_beta.py` for SOXL/SNXX

**Dependencies:** LEVEL 2 accounting + LEVEL 6 portfolio.

**Acceptance Criteria:**
- All limits in `configs/risk.yaml`
- Risk engine blocks orders when limits breached
- Drawdown anatomy on every major DD event

**Failure Criteria:**
- Hidden leverage increase after losses
- Martingale patterns

**Outputs:** `docs/RISK_POLICY.md` (live rules), risk test suite

**Status:** 🟡 **PARTIAL** (policy doc exists; engine not built)

---

## LEVEL 9 — Live Simulation

**Objectives:** Gate OOS fill calibration vs Binance structure.

**Tasks:**
- `run_gate_oos.py` operational
- Fill ratio Binance → Gate mapping
- Execution drift metrics

**Dependencies:** LEVEL 2 + Gate data (LEVEL 1).

**Acceptance Criteria:**
- Top-3 param sets validated on Gate OOS
- Documented fill drift distributions

**Failure Criteria:**
- Binance-only conclusions labeled as live-ready

**Outputs:** `outputs/gate_calibration/`

**Status:** ⬜ **NOT STARTED**

---

## LEVEL 10 — Paper Trading

**Objectives:** Paper engine records signal → expected fill → market evolution → PnL.

**Tasks:**
- Extend `qtb/live/` beyond DRY_RUN stub
- Continuous run for predefined period
- Compare backtest vs paper fill

**Dependencies:** LEVEL 9 calibration + LEVEL 8 risk pass.

**Acceptance Criteria:**
- 30+ day paper run logged
- Execution drift within documented bounds

**Failure Criteria:**
- Undocumented manual overrides

**Outputs:** `outputs/paper/`

**Status:** ⬜ **NOT STARTED**

---

## LEVEL 11 — Limited Live Candidate

**Objectives:** Promote strategies to LIVE_CANDIDATES with evidence grades.

**Tasks:**
- OOS PASS + Robustness PASS + Base/Conservative PASS + Risk PASS
- Grades: RESEARCH ONLY → PAPER → SMALL LIVE → CORE CANDIDATE
- No single backtest → CORE

**Dependencies:** LEVEL 7–10 all pass for candidate.

**Acceptance Criteria:**
- Each row in `outputs/LIVE_CANDIDATES.md` cites experiment IDs
- Confidence honestly LOW/MEDIUM/HIGH

**Failure Criteria:**
- CORE candidate without OOS
- Tech Short→Long as live without overturning FAIL

**Outputs:** Updated `outputs/LIVE_CANDIDATES.md`

**Status:** ⬜ **NO CANDIDATES** (correct state)

---

## LEVEL 12 — Continuous Research Loop

**Objectives:** Autonomous OBSERVE → QUESTION → EXPERIMENT → REVIEW → RED TEAM → LEDGER → NEXT.

**Tasks:**
- Auto-generate `NEXT_EXPERIMENTS.md` by information gain
- Auto-update ledger post-experiment
- Timer-driven backlog (`research-continue` 20min)
- Red team + fix loop (max 3 rounds)

**Dependencies:** All prior levels operational.

**Acceptance Criteria:**
- Loop runs without human parameter selection
- Every FAIL reduces search space in ledger
- "NO EDGE FOUND" is valid terminal state

**Failure Criteria:**
- Infinite retry on blocked hypotheses
- AI self-deception (pretty results without red team)

**Outputs:** `research_log/`, `NEXT_EXPERIMENTS.md`, updated ledger

**Status:** 🟡 **PARTIAL** (manual backlog + timers; not fully automated)

---

## Current Position

```
LEVEL 0  ████████████████████░░  ~90%  (conditional pass)
LEVEL 1  ███████░░░░░░░░░░░░░░░  ~35%
LEVEL 2  ████████████░░░░░░░░░░  ~60%
LEVEL 3+ ░░░░░░░░░░░░░░░░░░░░░░  blocked
```

**Next level to complete:** LEVEL 1 (DATA_QUALITY_REPORT + DATA-010–018 core)

**Phase 2 research entry:** After LEVEL 1 acceptance + TASK-0009/0010 + dual report fix
