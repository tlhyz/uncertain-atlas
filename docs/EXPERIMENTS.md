# Experiment Pipeline

## STEP order (do not skip)

| Step | Task | Status |
|------|------|--------|
| 1 | Archive + docs + configs | **This delivery** |
| 2 | Binance downloader + manifests | **Skeleton ready** |
| 3 | Unified limit fill engine | **qtb + src/execution** |
| 4 | Crypto long-history grid scan | **NOT RUN** |
| 5 | Tech state machine | **Code exists; tick re-run pending** |
| 6 | Gate Tech OOS | **NOT RUN** |
| 7 | Independent books | **Partial** |
| 8 | Combined 10k portfolio | **NOT RUN** |
| 9 | Monte Carlo + plateau | **Placeholder** |
| 10 | LIVE_CANDIDATES.md | **Skeleton** |

## Config entry points

| Experiment | Config |
|------------|--------|
| Tech FSM | `configs/experiments/tech_state_machine.yaml` |
| Crypto regime | `configs/experiments/crypto_regime.yaml` |
| Cross-market | `configs/experiments/cross_market.yaml` |
| Gate OOS | `configs/experiments/gate_calibration.yaml` |
| Legacy A/B | `configs/ab_etf_vs_perp.yaml` → `qtb ab` |
| Legacy dual | `configs/dual_engine_perp.yaml` → `qtb dual` |

## Anti-overfit requirements

- Walk-forward / train-val-OOS for BTC ETH SOL
- Parameter plateau (`src/analysis/parameter_plateau.py`)
- Block bootstrap MC (`src/analysis/monte_carlo.py`) — 1000 paths, 1/3/5d blocks
- Same window cannot be both tune and validate

## Reproduce prior results

```bash
# A/B ETF vs Perp (Gate real data)
python -m qtb.cli ab -c configs/ab_etf_vs_perp.yaml

# Dual engine (Gate overlap — FAIL verdict preserved)
python -m qtb.cli dual -c configs/dual_engine_perp.yaml
```

Reports: `outputs/ab_etf_vs_perp/`, `outputs/dual_engine_perp/`.
