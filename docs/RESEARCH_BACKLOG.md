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
| P1-01 | Download BTC/ETH/SOL aggTrades (auto start date) | **done** | BTC/ETH/SOL 91d manifests; Sep-04 SOL + Sep-01 BTC gaps filled 2026-09-13 — outputs/review_logs/2026-09-13_P1-01_crypto_aggTrades_download_PASS.md |
| P1-02 | Download SOXLUSDT aggTrades (detect earliest) | done | 65 days 2026-07-09→09-11 |
| P1-03 | Download SNXXUSDT aggTrades (detect earliest) | done | 65 days |
| P1-04 | Run `build_manifest.py` + sha256 all files | done | data/manifests/*.json |
| P1-05 | Validate every SOXL bar has aggTrades | done | 1560/1560 |
| P1-06 | Validate every SNXX bar has aggTrades | done | 1546/1546 |
| P1-07 | Cross-check tick OHLCV vs kline (SOXL) | done | lazy validation passed |
| P1-08 | Cross-check tick OHLCV vs kline (SNXX) | done | lazy validation passed |
| P1-09 | Document data gaps in manifest notes | done | Sep-12 empty; ETH/SOL noted |
| P1-10 | Gate download script smoke test BTC_USDT | done | 720 bars 1h; scripts/download_gate.py path fix |
| P1-11 | Full 65d Binance tick backtest SOXL/SNXX | **done** | FAIL dual -58.70% vs B&H -33.49%; 1546 bars tick — outputs/review_logs/2026-09-13_P1-11_65d_tick_backtest_FAIL.md |

---

## P2 — Crypto long-history (STEP 4)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P2-01 | Enable `crypto_regime.yaml` runner | **done** | qtb/dual/crypto_run.py + qtb.cli crypto; outputs/review_logs/2026-09-13_P2-01_crypto_regime_runner_PASS.md |
| P2-02 | BTC leverage scan 1.25/1.5/1.75/2.0 | **done** | FAIL all lev ~-87%; no sweet spot — outputs/review_logs/2026-09-13_P2-02_btc_leverage_FAIL.md |
| P2-03 | ETH leverage scan | **done** | FAIL all lev ~-87.5%; no sweet spot — outputs/review_logs/2026-09-13_P2-03_eth_leverage_FAIL.md |
| P2-04 | SOL leverage scan | **done** | FAIL all lev -88.01%; crypto_max_dd=100% — outputs/review_logs/2026-09-13_P2-04_sol_leverage_FAIL.md |
| P2-05 | Grid ATR step 0.30–0.60 sweep | **done** | FAIL all ~-87%; 0.40 worst Calmar; W-02 not supported — outputs/review_logs/2026-09-13_P2-05_btc_grid_atr_FAIL.md |
| P2-06 | Grid range ±3/5/7 ATR sweep | **done** | FAIL all ~-87%; ±3 Calmar best but inert — outputs/review_logs/2026-09-13_P2-06_btc_grid_range_FAIL.md |
| P2-07 | Grid→Trend mix 80/20→20/80 | **done** | FAIL all ~-87 to -89%; dynamic≡80_20 — outputs/review_logs/2026-09-13_P2-07_btc_grid_mix_FAIL.md |
| P2-08 | High-vol range regime auto-label sample | **done** | C1 mostly RANGE_LOW_VOL; SOL 3 HV bars — outputs/review_logs/2026-09-13_P2-08_regime_label_sample_PASS.md |
| P2-09 | Bull trend sell-the-winner check | **done** | CONDITIONAL PASS structural; C1 0 BULL bars — outputs/review_logs/2026-09-13_P2-09_bull_sell_winner_CONDITIONAL_PASS.md |
| P2-10 | Answer Q-crypto-1 (leverage sweet spot) | **done** | COMPLETE FAIL all majors ~-87%; no sweet spot — outputs/experiments/Q_CRYPTO_1_leverage_sweet_spot.md |
| P2-11 | Answer Q-crypto-2 (0.40 ATR plateau?) | **done** | FAIL no actionable plateau; 0.40 worst Calmar — outputs/experiments/Q_CRYPTO_2_atr_step_plateau.md |
| P2-12 | Answer Q-crypto-3 (±ATR range) | **done** | FAIL no actionable range; ±3 Calmar best — outputs/experiments/Q_CRYPTO_3_atr_range.md |
| P2-13 | PENGU/PUMP satellite cap 5% test | **done** | CONDITIONAL PASS cap OK; BAR -99%/-99%; C1 tick blocked — outputs/review_logs/2026-09-13_P2-13_satellite_cap_CONDITIONAL_PASS.md |
| P2-14 | CRYPTO_C1 window 2024-09→11 tick run | **done** | FAIL ind -87.30%; uni -74.30%; delta -13pp — outputs/review_logs/2026-09-13_P2-14_c1_tick_FAIL.md |
| P2-15 | BTC tick backtest perf investigation | **done** | PARTIAL — I/O fast; bottleneck portfolio tick grid — outputs/review_logs/2026-09-13_P2-15_btc_tick_perf_PARTIAL.md |

---

## P3 — Tech FSM (STEP 5–6)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P3-01 | Re-run dual on Binance ticks (tick_precise) | **done** | FAIL reproduces P1-11 dual -58.70% — outputs/review_logs/2026-09-13_P3-01_dual_tick_FAIL.md |
| P3-02 | Short init 10/15/20% sweep | **done** | FAIL 20% best return -58.70%; 10% worst -59.24%; Q-tech-2 partial — outputs/review_logs/2026-09-13_P3-02_short_init_FAIL.md |
| P3-03 | Short structure dir vs grid vs 70/30 | **done** | FAIL all -58.70% inert; structure knob dead — outputs/review_logs/2026-09-13_P3-03_short_structures_FAIL.md |
| P3-04 | Drawdown set A/B/C comparison | **in_progress** | 1/3 set A ~20min — outputs/review_logs/2026-09-13_P3-04_drawdown_sets_IN_PROGRESS.md |
| P3-05 | Reversal R1–R5 no-lookahead tests | **done** | PASS — outputs/review_logs/2026-09-13_P3-05_reversal_no_leak_PASS.md |
| P3-06 | Right-side reserve 25/30/35% | pending | config ready; queue after P3-04 |
| P3-07 | SOXL/SNXX weight 75/25 70/30 65/35 | pending | config ready; queue after P3-06 |
| P3-08 | Grid→Trend stage mix sweep | pending | config dual_binance_tick_grid_mix.yaml ready; queue after P3-07 |
| P3-09 | FAIL_F1 direct-up window | pending | blocked: needs SOXL 2025-09→10 aggTrades (STRUCTURAL_SEED_ONLY on 65d overlap) |
| P3-10 | FAIL_F2 no-recovery window | pending | blocked: needs SOXL 2024-09→11 aggTrades (STRUCTURAL_SEED_ONLY on 65d overlap) |
| P3-11 | Similar-window search top-20 real windows | pending | |
| P3-12 | Answer Q-tech-1 Short→Long vs Cash→Long | pending | Gate FAIL preserved |
| P3-13 | Answer Q-tech-2 initial short % | **done** | FAIL via P3-02; 20% best return, no sweet spot — outputs/review_logs/2026-09-13_P3-02_short_init_FAIL.md |
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
| M-01 | Run `pytest -q` | done | 139 passed 2026-09-13T21:30Z |
| M-02 | Update `CURRENT_CONCLUSIONS.md` if verdict changes | done | C-05 65d + C-06 crypto grid FAIL |
| M-03 | Append `review_logs/INDEX.md` | done | daily audit 0900Z |
| M-04 | Check PR CI status | done | PR #8 no checks reported |
| M-05 | Refresh backlog — move done, add discovered tasks | done | P2-15 added; elapsed refresh |

---

## Blocked / failed (do not retry without new data)

| ID | Task | Status | Reason |
|----|------|--------|--------|
| X-01 | 3L ETF long-run grid | failed | Exp 001 — inventory loss |
| X-02 | 3x PERP unattended SOL/PENGU/PUMP | failed | liquidations |
| X-03 | Dual Short→Long on Gate overlap | failed | −51% vs B&H −30% |
| X-04 | Tech seed T1/T2 on Gate perp | blocked | STRUCTURAL_SEED_ONLY |
