# Review Log — P5-05 DD>10/20/30% Probability from MC

## Meta

- **date_utc:** 2026-09-14T09:15Z
- **task:** P5-05
- **method:** Block bootstrap MC 1000 paths on 65d dual-book independent equity; DD thresholds 10/20/30%
- **config:** configs/experiments/dual_binance_tick_independent_vs_unified.yaml
- **output:** outputs/experiments/p5_dd_probs_65d/dd_probabilities.json

## Implementation

- **`scripts/run_p5_dd_probs.py`:** dual portfolio → `block_bootstrap_mc` → `dd_probabilities` table + markdown
- **`tests/test_p5_dd_probs.py`:** extraction smoke (162 full suite green)

## In-sample (65d, 1546 bars, 64 daily obs)

| Metric | Value |
|--------|-------|
| Return | −55.41% |
| Final equity | 4,459 USDT |
| Liq count | 0 |
| Execution | TICK tech + BAR crypto |

## DD probabilities — 65d (1000 paths)

| Block | P(DD>10%) | P(DD>20%) | P(DD>30%) | P(loss) | Median max DD |
|-------|----------:|----------:|----------:|--------:|--------------:|
| 1d | **100.0%** | 94.9% | 73.5% | 8.0% | 37.7% |
| 3d | **99.6%** | **89.0%** | **70.6%** | 14.7% | 39.0% |
| 5d | 99.4% | 88.6% | 72.6% | 20.8% | 43.2% |

Reference block **3d** per P5-01 convention.

## 7d smoke (6 daily obs — not decision-grade)

| Block | P(DD>20%) | P(DD>30%) |
|-------|----------:|----------:|
| 3d | 0.7% | 0.0% |

Tiny sample understates tail risk vs 65d.

## Question

What is the bootstrap probability of account DD exceeding 10/20/30% on the 65d dual-book reference?

## Findings

1. **Measurement:** PASS — all three thresholds exported; 64 daily obs on 65d window.
2. **P(DD>10%):** **~100%** on all block sizes — resampled paths almost always breach 10% DD.
3. **P(DD>20/30%):** **89% / 71%** (3d) — severe tail risk under block bootstrap.
4. **vs in-sample:** Realized return −55% with max_dd ~51% (P4); bootstrap median max DD ~39% but **frequency** of breaches is high due to daily return composition.
5. **Survivability:** FAIL — MC indicates strategy is not robust to path reordering at standard DD gates.

## Verdict

- **task_verdict:** **DONE**
- **implementation_verdict:** **PASS**
- **strategy_verdict:** **FAIL** — P(DD>20%)≈89%; not deployable under 20% risk budget

## Red team (≥5)

1. Bootstrap on daily returns ignores intraday DD sequencing from tick engine
2. p50_final >> in-sample final on some blocks — return distribution skew vs DD frequency
3. Independent book only — unified path has crypto liq 100% DD
4. Block size sensitivity moderate (1d vs 3d within ~10pp on DD>20%)
5. No conservative fill replay

## Next

- P5-06 liquidation probability from MC (needs liq flag in path sim or in-sample only)
- Document DD thresholds in risk.yaml vs MC for gate decisions
