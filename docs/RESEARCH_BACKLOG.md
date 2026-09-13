# Research Backlog (小目标清单)

Status: `pending` | `in_progress` | `done` | `blocked` | `failed` | `cancelled`

**Rule:** Pick the **lowest-number open task** in the current phase unless blocked. Mark `done` only with review log path.

---

## P0 — Repository SSOT

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P0-01 | Merge refactor PR #8 to main | blocked | awaiting human merge |
| P0-02 | pytest green on main after merge | pending | |
| P0-03 | README links all docs | done | refactor delivery |
| P0-04 | Review-log policy in `.cursor/rules` | done | review-optimize-log.mdc |
| P0-05 | Phase 1 audit deliverables | done | REPO_AUDIT, GAP_ANALYSIS, ROADMAP, TASKS, LEDGER, PHASE1_SELF_AUDIT |
| P0-06 | Phase 1.5 infra gates (DATA_QUALITY, accounting, leak tests) | **done** | TASK-0008/0009/0010; TASK-0011 via manifest rebuild |

---

## P1 — Data pipeline (Binance + manifests)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P1-01 | Download BTC/ETH/SOL aggTrades (auto start date) | **done** | BTC 91d 130.5M; ETH 91d 128.8M; SOL 90d 44.2M (Sep-04 gap) — outputs/review_logs/2026-09-13_P1-01_crypto_aggTrades_download_PASS.md |
| P1-02 | Download SOXLUSDT aggTrades (detect earliest) | done | 65 days 2026-07-09→09-11 |
| P1-03 | Download SNXXUSDT aggTrades (detect earliest) | done | 65 days |
| P1-04 | Run `build_manifest.py` + sha256 all files | done | data/manifests/*.json |
| P1-05 | Validate every SOXL bar has aggTrades | done | 1560/1560 |
| P1-06 | Validate every SNXX bar has aggTrades | done | 1546/1546 |
| P1-07 | Cross-check tick OHLCV vs kline (SOXL) | done | lazy validation passed |
| P1-08 | Cross-check tick OHLCV vs kline (SNXX) | done | lazy validation passed |
| P1-09 | Document data gaps in manifest notes | done | Sep-12 empty; ETH/SOL noted |
| P1-10 | Gate download script smoke test BTC_USDT | done | 720 bars 1h; scripts/download_gate.py path fix |
| P2-02 | BTC leverage scan 1.25/1.5/1.75/2.0 | in_progress | leverage scan running; skip_tick_validation; BTC Sep-01 gap fixed |
| P1-11 | Full 65d Binance tick backtest SOXL/SNXX | in_progress | 62+ min; DUAL_REPORT pending |

---

## P2 — Crypto long-history (STEP 4)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P2-01 | Enable `crypto_regime.yaml` runner | **done** | qtb/dual/crypto_run.py + qtb.cli crypto; outputs/review_logs/2026-09-13_P2-01_crypto_regime_runner_PASS.md |
| P2-02 | BTC leverage scan 1.25/1.5/1.75/2.0 | in_progress | 8+ min; tick validation 2184 bars then 4 leverage levels |
| P2-03 | ETH leverage scan | pending | klines cache ready; config crypto_eth_leverage_scan.yaml |
| P2-04 | SOL leverage scan | pending | klines cache ready; config crypto_sol_leverage_scan.yaml |
| P2-05 | Grid ATR step 0.30–0.60 sweep | pending | |
| P2-06 | Grid range ±3/5/7 ATR sweep | pending | |
| P2-07 | Grid→Trend mix 80/20→20/80 | pending | |
| P2-08 | High-vol range regime auto-label sample | pending | |
| P2-09 | Bull trend sell-the-winner check | pending | |
| P2-10 | Answer Q-crypto-1 (leverage sweet spot) | pending | |
| P2-11 | Answer Q-crypto-2 (0.40 ATR plateau?) | pending | |
| P2-12 | Answer Q-crypto-3 (±ATR range) | pending | |
| P2-13 | PENGU/PUMP satellite cap 5% test | pending | |
| P2-14 | CRYPTO_C1 window 2024-09→11 tick run | pending | |

---

## P3 — Tech FSM (STEP 5–6)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P3-01 | Re-run dual on Binance ticks (tick_precise) | pending | |
| P3-02 | Short init 10/15/20% sweep | pending | |
| P3-03 | Short structure dir vs grid vs 70/30 | pending | |
| P3-04 | Drawdown set A/B/C comparison | pending | |
| P3-05 | Reversal R1–R5 no-lookahead tests | pending | |
| P3-06 | Right-side reserve 25/30/35% | pending | |
| P3-07 | SOXL/SNXX weight 75/25 70/30 65/35 | pending | |
| P3-08 | Grid→Trend stage mix sweep | pending | |
| P3-09 | FAIL_F1 direct-up window | pending | |
| P3-10 | FAIL_F2 no-recovery window | pending | |
| P3-11 | Similar-window search top-20 real windows | pending | |
| P3-12 | Answer Q-tech-1 Short→Long vs Cash→Long | pending | Gate FAIL preserved |
| P3-13 | Answer Q-tech-2 initial short % | pending | |
| P3-14 | Answer Q-tech-8 bottom grid value-add | pending | |
| P3-15 | Answer Q-tech-9 grid in trend phase | pending | |
| P3-16 | Gate OOS on top-3 Tech param sets | pending | |
| P3-17 | Effective beta rolling for SOXL/SNXX | pending | |

---

## P4 — Portfolio & cross-market (STEP 7–8)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P4-01 | Independent vs unified 10k portfolio | pending | weak +2.3% one window |
| P4-02 | Regime A Tech↓ Crypto↑ | pending | |
| P4-03 | Regime B Tech↑ Crypto↓ | pending | |
| P4-04 | Regime C both up | pending | |
| P4-05 | Regime D both down | pending | |
| P4-06 | Regime E/F mixed | pending | |
| P4-07 | Margin/reserve 80/20 70/30 60/40 | pending | |
| P4-08 | Funding stress deleverage rule test | pending | |
| P4-09 | Soft/hard DD pause rules | pending | |

---

## P5 — Robustness (STEP 9)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P5-01 | Implement block bootstrap MC (1000 paths) | pending | placeholder exists |
| P5-02 | Parameter plateau detector on ATR step | pending | |
| P5-03 | Walk-forward split BTC 2019+ | pending | |
| P5-04 | OOS holdout report for finalists | pending | |
| P5-05 | DD>10/20/30% probability from MC | pending | |
| P5-06 | Liquidation probability from MC | pending | |

---

## P6 — Live candidates (STEP 10)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P6-01 | Gate fill ratio calibration vs Binance | pending | |
| P6-02 | Promote BTC row to MEDIUM confidence | pending | |
| P6-03 | Promote ETH row to MEDIUM confidence | pending | |
| P6-04 | Tech row only if beats Cash→Long OOS | pending | |
| P6-05 | Final LIVE_CANDIDATES.md review | pending | |

---

## Maintenance (recurring)

| ID | Task | Status | Cadence |
|----|------|--------|---------|
| M-01 | Run `pytest -q` | done | 122 passed 2026-09-13T01:42Z |
| M-02 | Update `CURRENT_CONCLUSIONS.md` if verdict changes | pending | after each experiment |
| M-03 | Append `review_logs/INDEX.md` | pending | after each experiment |
| M-04 | Check PR CI status | pending | after each push |
| M-05 | Refresh backlog — move done, add discovered tasks | pending | every session end |

---

## Blocked / failed (do not retry without new data)

| ID | Task | Status | Reason |
|----|------|--------|--------|
| X-01 | 3L ETF long-run grid | failed | Exp 001 — inventory loss |
| X-02 | 3x PERP unattended SOL/PENGU/PUMP | failed | liquidations |
| X-03 | Dual Short→Long on Gate overlap | failed | −51% vs B&H −30% |
| X-04 | Tech seed T1/T2 on Gate perp | blocked | STRUCTURAL_SEED_ONLY |
