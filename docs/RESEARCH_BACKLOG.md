# Research Backlog (小目标清单)

Status: `pending` | `in_progress` | `done` | `blocked` | `failed` | `cancelled`

**Rule:** Pick the **lowest-number open task** in the current phase unless blocked. Mark `done` only with review log path.

---

## P0 — Repository SSOT

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P0-01 | Merge refactor PR #8 to main | blocked | awaiting human merge |
| P0-02 | pytest green on main after merge | **blocked** | awaiting P0-01; branch 168 passed 2026-09-14 — outputs/review_logs/2026-09-14_P0-02_premerge_pytest_BLOCKED.md |
| P0-03 | README links all docs | done | refactor delivery |
| P0-04 | Review-log policy in `.cursor/rules` | done | review-optimize-log.mdc |
| P0-05 | Phase 1 audit deliverables | done | REPO_AUDIT, GAP_ANALYSIS, ROADMAP, TASKS, LEDGER, PHASE1_SELF_AUDIT |
| P0-06 | Phase 1.5 infra gates (DATA_QUALITY, accounting, leak tests) | **done** | TASK-0008/0009/0010; TASK-0011 via manifest rebuild |

---

## P1 — Data pipeline (Binance + manifests)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P1-01 | Download BTC/ETH/SOL aggTrades (auto start date) | **done** | BTC/ETH/SOL 91d manifests; Sep-04 SOL + Sep-01 BTC gaps filled 2026-09-13 — outputs/review_logs/2026-09-13_P1-01_crypto_aggTrades_download_PASS.md |
| P1-02 | Download SOXLUSDT aggTrades (detect earliest) | done | local 59d 2026-07-15→09-11; Vision listing **2026-05-15** |
| P1-12 | Download remaining Vision SOXL 2026-05-15→07-14 | **done** | 61 prefix days + 6 gap; local **120d** 2026-05-15→09-11 0 gaps — outputs/review_logs/2026-09-16_P1-12_soxl_listing_prefix_PASS.md |
| P1-13 | Validate listing-length SOXL 1h (2866) vs cached ticks | **done** | **2866/2866** hours; p99 close err 1.8e-4 — outputs/review_logs/2026-09-16_P1-13_listing_tick_coverage_PASS.md |
| P1-14 | Manifest SOXL aggTrades 2026-05-15→09-11 (120d sha256) | **done** | 120d / 62,409,315 rows / 0 gaps — outputs/review_logs/2026-09-16_P1-14_soxl_listing_manifest_PASS.md |
| P1-15 | Audit cache vs committed tick manifests | **done** | SOXL 120d + SOXS 61d on_disk; BTC/ETH/SOL/SNXX **evicted** — outputs/review_logs/2026-09-16_P1-15_cache_vs_manifests.md |
| P1-16 | Re-download evicted SNXX/BTC/ETH/SOL ticks | **blocked** | manifests remain; not needed for SOXL lab; do not auto-pull multi-GB |
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
| P3-04 | Drawdown set A/B/C comparison | **done** | FAIL C best -56.08%; A worst -67.88% — outputs/review_logs/2026-09-13_P3-04_drawdown_sets_FAIL.md |
| P3-05 | Reversal R1–R5 no-lookahead tests | **done** | PASS — outputs/review_logs/2026-09-13_P3-05_reversal_no_leak_PASS.md |
| P3-06 | Right-side reserve 25/30/35% | **done** | FAIL 25% best −58.92%; all worse vs default −58.70% — outputs/review_logs/2026-09-14_P3-06_right_side_reserve_FAIL.md |
| P3-07 | SOXL/SNXX weight 75/25 70/30 65/35 | **done** | FAIL default 70/30 best −58.70%; 75/25 worst −58.89% — outputs/review_logs/2026-09-14_P3-07_soxl_snxx_weights_FAIL.md |
| P3-08 | Grid→Trend stage mix sweep | **done** | FAIL G50 best −57.85% (+0.85pp); G100 worst −71.41% — outputs/review_logs/2026-09-14_P3-08_grid_mix_FAIL.md |
| P3-09 | FAIL_F1 direct-up window | **blocked** | Vision SOXL starts **2026-05-15**; 2025-09→10 **404** — not downloadable — outputs/review_logs/2026-09-15_P3-09_vision_listing_BLOCKED.md |
| P3-10 | FAIL_F2 no-recovery window | **blocked** | 2024-09→11 **404**; predates UM listing 2026-05-15 — same log |
| P3-11 | Similar-window search top-20 real windows | **blocked** | 120d listing 2866 bars / 9 slides; top-20 needs 4632 — outputs/review_logs/2026-09-16_P3-11_listing_retry_BLOCKED.md |
| P3-12 | Answer Q-tech-1 Short→Long vs Cash→Long | **done** | COMPLETE FAIL dual -58.70% vs B4 -25.19%; remove Short — outputs/experiments/Q_TECH_1_short_vs_cash_long.md |
| P3-13 | Answer Q-tech-2 initial short % | **done** | FAIL via P3-02; 20% best return, no sweet spot — outputs/review_logs/2026-09-13_P3-02_short_init_FAIL.md |
| P3-14 | Answer Q-tech-8 bottom grid value-add | **done** | COMPLETE FAIL B3 -25.20% beats dual -58.70%; grid does not salvage — outputs/experiments/Q_TECH_8_bottom_grid_value_add.md |
| P3-15 | Answer Q-tech-9 grid in trend phase | **done** | CONDITIONAL FAIL G50 -57.85% sweet spot; FAIL vs B3 -25.20% — outputs/experiments/Q_TECH_9_grid_in_trend_phase.md |
| P3-16 | Gate OOS on top-3 Tech param sets | **blocked** | Gate OOS stub; no MEDIUM candidate — outputs/review_logs/2026-09-14_P3-16_gate_oos_BLOCKED.md |
| P3-17 | Effective beta rolling for SOXL/SNXX | **done** | PASS SOXL→SNXX β~0.45; SNXX→SOXL β~1.2 — outputs/review_logs/2026-09-14_P3-17_effective_beta_PASS.md |

---

## P4 — Portfolio & cross-market (STEP 7–8)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P4-01 | Independent vs unified 10k portfolio | **done** | FAIL Δreturn=0 ΔDD=0; ind≡uni -58.70%; crypto inert — outputs/review_logs/2026-09-14_P4-01_independent_vs_unified_FAIL.md |
| P4-02 | Regime A Tech↓ Crypto↑ | **done** | DONE unblock; 7d Regime A 40 bars; strategy FAIL Δ=0 — outputs/review_logs/2026-09-14_P4-02_regime_A_DONE.md |
| P4-03 | Regime B Tech↑ Crypto↓ | **done** | DONE 326 bars 21.1%; ind +2.3pp vs uni; uni crypto liq — outputs/review_logs/2026-09-14_P4-03_regime_B_DONE.md |
| P4-04 | Regime C both up | **done** | DONE 450 bars 29.1%; largest quadrant; FAIL alpha — outputs/review_logs/2026-09-14_P4-04_regime_C_DONE.md |
| P4-05 | Regime D both down | **done** | DONE 435 bars 28.1%; exact proxy match; FAIL hedging — outputs/review_logs/2026-09-14_P4-05_regime_D_DONE.md |
| P4-06 | Regime E/F mixed | **done** | DONE 25 bars 1.6% residual; 98.4% coverage PASS — outputs/review_logs/2026-09-14_P4-06_regime_EF_DONE.md |
| P4-07 | Margin/reserve 80/20 70/30 60/40 | **done** | 7d 60/40 best; **65d 80/20 best −53.03%** — outputs/review_logs/2026-09-14_P4-07_margin_reserve_CONDITIONAL_FAIL.md |
| P4-08 | Funding stress deleverage rule test | **done** | INERT 7d 0 triggers at 1-2% — outputs/review_logs/2026-09-14_P4-08_funding_stress_INERT.md |
| P4-09 | Soft/hard DD pause rules | **done** | FAIL soft−10% −82.35%; hard −88.75% — outputs/review_logs/2026-09-14_P4-09_dd_pause_FAIL.md |

---

## P5 — Robustness (STEP 9)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P5-01 | Implement block bootstrap MC (1000 paths) | **done** | PASS impl; 7d 6 daily obs INCONCLUSIVE — outputs/review_logs/2026-09-14_P5-01_bootstrap_mc_PASS.md |
| P5-02 | Parameter plateau detector on ATR step | **done** | PLATEAU_INERT on returns; 0.40 worst Calmar — outputs/review_logs/2026-09-14_P5-02_plateau_detector_PASS.md |
| P5-03 | Walk-forward split BTC 2019+ | **done** | FAIL ~−86.58% mean OOS; 3 calendar folds — outputs/review_logs/2026-09-14_P5-03_walk_forward_PARTIAL.md |
| P5-04 | OOS holdout report for finalists | **done** | 0/2 pass; BTC 2024 −86.44%; dual −75.49% — outputs/review_logs/2026-09-14_P5-04_oos_holdout_FAIL.md |
| P5-05 | DD>10/20/30% probability from MC | **done** | 65d P(DD>20)=89% P(DD>30)=71% — outputs/review_logs/2026-09-14_P5-05_dd_probs_DONE.md |
| P5-06 | Liquidation probability from MC | **done** | in-sample liq 0; MC proxy 0% — CONDITIONAL FAIL — outputs/review_logs/2026-09-14_P5-06_liq_probs_CONDITIONAL_FAIL.md |

---

## P6 — Live candidates (STEP 10)

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P6-01 | Gate fill ratio calibration vs Binance | **done** | CONDITIONAL PASS BAR BTC 1h fill_ratio 0.986 base; vol not binding — outputs/review_logs/2026-09-14_P6-01_gate_fill_calibration_CONDITIONAL_PASS.md |
| P6-02 | Promote BTC row to MEDIUM confidence | **done** | FAIL demote MEDIUM→LOW; 5 blocking gates — outputs/review_logs/2026-09-14_P6-02_btc_promotion_FAIL.md |
| P6-03 | Promote ETH row to MEDIUM confidence | **done** | FAIL demote MEDIUM→LOW; 6 blocking gates — outputs/review_logs/2026-09-14_P6-03_eth_promotion_FAIL.md |
| P6-04 | Tech row only if beats Cash→Long OOS | **done** | FAIL holdout −75.49% vs B4 −0.38% (−75pp) — outputs/review_logs/2026-09-14_P6-04_tech_cash_long_oos_FAIL.md |
| P6-05 | Final LIVE_CANDIDATES.md review | **done** | 0 MEDIUM+ rows; SOL demoted; P6 complete — outputs/review_logs/2026-09-14_P6-05_live_candidates_review_DONE.md |

---

## P7 — SOXL/SOXS inverse-pair hedge (user 2026-09-15)

Hypothesis: same-symbol long+short grid drifts inventory; SOXL long-grid + SOXS long-grid (SOXS already shorts SOX) may cancel residual delta and keep grid harvest.

| ID | Task | Status | Log / notes |
|----|------|--------|-------------|
| P7-01 | Download SOXSUSDT aggTrades (detect earliest) + manifest | **done** | SOXS 61d 7.7M; SOXL overlap 58d 31.2M; 1392/1392 + 1383/1383 — outputs/review_logs/2026-09-15_P7-01_soxl_soxs_ticks_PASS.md |
| P7-02 | Rolling beta / OLS hedge ratio SOXL↔SOXS vs SOXL↔SNXX | **done** | PASS corr −0.988 β −0.991; SNXX was +0.45 not inverse — outputs/review_logs/2026-09-15_P7-02_soxl_soxs_beta_PASS.md |
| P7-03 | Same-symbol L+S grid vs pair long-grid hedge backtest | **done** | BAR CONDITIONAL PASS **overturned by P7-04 TICK** — outputs/review_logs/2026-09-15_P7-03_pair_hedge_CONDITIONAL_PASS.md |
| P7-04 | Tick-precise pair grid + funding vs daily 50/50 B&H | **done** | **FAIL** default 0.40/±5 pair −6.0%/DD −20%; all sweep FAIL — outputs/review_logs/2026-09-15_P7-04_tick_pair_hedge_FAIL.md |
| P7-05 | User SOXL L+S: 5x, ±20U **and** ±20%, 200-grid moving, 5k+5k, daily PnL | **done** | **FAIL** both: ±20U −12.8%/DD −80% long liq; ±20% −18.7%/DD −77% long liq — outputs/review_logs/2026-09-15_P7-05_user_soxl_ls_grid_FAIL.md |
| P7-06 | Classify SOXL ticks/params/results; 3-pass audit; extractable private lab | **done** | `soxl-lab/`; verify --times 3 all ok; remote not creatable here — outputs/review_logs/2026-09-15_soxl_lab_3pass_PASS.md |
| P7-07 | User moving L+S **hedge**: shared band, flatten survivor on liq, ±20U and ±20% | **done** | **STOPPED** 07-28; ±20U +15.6%/DD −6.0%; ±20% +6.2%/DD −9.7%; long still liq — outputs/review_logs/2026-09-16_P7-07_user_moving_hedge_STOPPED.md |
| P7-08 | User-editable tick grid runner (YAML + CLI) | **done** | `soxl-lab/scripts/run_grid.py` + `params/run.yaml` |
| P7-09 | Harden runner 5-pass review/optimize (check/cache/remap/YAML) | **done** | 5 passes; ROOT fix; 25 tests + cache smoke — outputs/review_logs/2026-09-16_P7-09_runner_5pass.md |
| P7-10 | Write Chinese usage notes and push | **done** | `soxl-lab/使用注意事项.md` — outputs/review_logs/2026-09-16_P7-10_usage_notes.md |
| P7-11 | Extensible spec (grid_kind/fee_bps/reanchor/hedge registry) | **done** | outputs/review_logs/2026-09-16_P7-11_extensible_spec.md |
| P7-12 | 1d tick smoke: default vs geometric vs fee_bps=4 | **done** | knobs move path; 1d not a verdict — outputs/review_logs/2026-09-16_P7-12_knob_smoke.md |
| P7-13 | Plugin registry + sweep + extensions dir | **done** | outputs/review_logs/2026-09-16_P7-13_extension_hooks.md |
| P7-14 | Listing-prefix 2026-05-15→07-15 user flatten hedge (new days) | **done** | BAR +37%/+26% **not a verdict**; 3d tick +2.1% — outputs/review_logs/2026-09-16_P7-14_listing_prefix.md |
| P7-15 | Listing-prefix 62d **TICK** flatten hedge (05-15→07-15) | **done** | **STOPPED** 05-26 short liq; ±20U +39.3% then 50 zero days; 120d no restart — outputs/review_logs/2026-09-16_P7-15_listing_prefix_tick.md |
| P7-16 | Flatten hedge 2x/3x TICK full listing (does lower lev survive?) | **done** | 3x STOPPED 05-27; 2x +70.7% survived path, inventory 1.81 **not live** — outputs/review_logs/2026-09-16_P7-16_leverage_tick.md |
| P7-17 | Leverage cliff: 4x ±20U and 2x ±20% TICK 120d | **done** | 4x STOPPED 05-26; 2x±20% −20.5% survived; +70% is usdt-only — outputs/review_logs/2026-09-16_P7-17_lev_cliff.md |
| P7-18 | Cliff refine: 2.5x ±20U TICK 120d | **done** | survived +86% / inv 2.30; cliff **(2.5, 3]** — outputs/review_logs/2026-09-16_P7-18_lev25.md |
| P7-19 | 5x restart-after-liq TICK 120d (split remaining equity) | **done** | **FAIL** 3 deaths +271% leftover re-lever; inv 14× — outputs/review_logs/2026-09-16_P7-19_restart.md |
| P7-20 | Write Q_SOXL_USER_GRID (is 5x moving L+S tradeable?) | **done** | **NO** — outputs/experiments/Q_SOXL_USER_GRID.md |
| P7-21 | Extensibility: extras stay, sizer registry, --set | **done** | plugin keys no longer vanish; equal/martingale/fixed — outputs/review_logs/2026-09-16_P7-21_extensibility.md |

---

## Maintenance (recurring)

| ID | Task | Status | Cadence |
|----|------|--------|---------|
| M-01 | Run `pytest -q` | **done** | 2026-09-17T11:20Z **220 passed, 1 skipped** |
| M-02 | Update `CURRENT_CONCLUSIONS.md` if verdict changes | **done** | 0900Z daily audit; no verdict change |
| M-03 | Append `review_logs/INDEX.md` | **done** | timer 1120Z |
| M-04 | Check PR CI status | **done** | 2026-09-17T09:00Z PR #8 open MERGEABLE; no checks; unmerged |
| M-05 | Refresh backlog — move done, add discovered tasks | **done** | pending=0; P0-01 still blocked |

---

## Blocked / failed (do not retry without new data)

| ID | Task | Status | Reason |
|----|------|--------|--------|
| P0-01 | Merge refactor PR #8 to main | blocked | awaiting human merge |
| P0-02 | pytest green on main after merge | blocked | depends on P0-01; branch 177 green + 1 env-fail |
| P3-09 | FAIL_F1 2025-09→10 | blocked | Vision SOXL listing 2026-05-15; window 404 |
| P3-10 | FAIL_F2 2024-09→11 | blocked | predates listing |
| P3-11 | similar-window top-20 @ 60d | blocked | Vision 120d → 9 slides; need 193d |
| P1-16 | Re-download evicted SNXX/BTC/ETH/SOL ticks | blocked | only if a new Book A/B tick experiment opens |
| X-01 | 3L ETF long-run grid | failed | Exp 001 — inventory loss |
| X-02 | 3x PERP unattended SOL/PENGU/PUMP | failed | liquidations |
| X-03 | Dual Short→Long on Gate overlap | failed | −51% vs B&H −30% |
| X-04 | Tech seed T1/T2 on Gate perp | blocked | STRUCTURAL_SEED_ONLY |
