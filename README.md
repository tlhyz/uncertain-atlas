# gate-grid-martingale

**Single source of truth** for multi-market grid / regime-switching quantitative research on Gate & Binance.

> Research repository — not investment advice. **FAIL results are kept as FAIL.**

## Start here

| Question | Document |
|----------|----------|
| Market thesis (Tech vs Crypto books) | [`docs/THESIS.md`](docs/THESIS.md) |
| What already failed / proven | [`docs/RESEARCH_HISTORY.md`](docs/RESEARCH_HISTORY.md) |
| Data rules (no synthetic ticks) | [`docs/DATA_POLICY.md`](docs/DATA_POLICY.md) |
| Review / optimize / log rules | [`docs/REVIEW_AND_OPTIMIZATION.md`](docs/REVIEW_AND_OPTIMIZATION.md) |
| **总目标 & 小目标 backlog** | [`docs/RESEARCH_GOALS.md`](docs/RESEARCH_GOALS.md) · [`docs/RESEARCH_BACKLOG.md`](docs/RESEARCH_BACKLOG.md) |
| **定时提醒 & 工作节奏** | [`docs/WORK_CADENCE.md`](docs/WORK_CADENCE.md) |
| How to run next experiment | [`docs/EXPERIMENTS.md`](docs/EXPERIMENTS.md) |
| AI / Cursor handoff | [`docs/CURSOR_HANDOFF.md`](docs/CURSOR_HANDOFF.md) |
| Refactor status | [`REPO_REFACTOR_REPORT.md`](REPO_REFACTOR_REPORT.md) |

## Research timeline

| # | Experiment | Result | Output |
|---|------------|--------|--------|
| 001 | Gate 3L ETF grid (SL phase) | **FAIL** | [`outputs/research_sl_phase/`](outputs/research_sl_phase/) |
| 002 | ETF vs Perp A/B | PERP wins majors | [`outputs/ab_etf_vs_perp/AB_REPORT.md`](outputs/ab_etf_vs_perp/AB_REPORT.md) |
| 003 | Tech Short→Grid→Trend | **FAIL** (Gate overlap) | [`outputs/dual_engine_perp/DUAL_REPORT.md`](outputs/dual_engine_perp/DUAL_REPORT.md) |
| 004 | Crypto independent regime | **PENDING** | — |

## Architecture

```
configs/          ← capital, fees, risk, experiment YAML (no magic numbers in code)
docs/             ← thesis, policies, history, handoff
src/              ← target package (migration from qtb/)
qtb/              ← working engine (CLI, A/B, dual, optimize)
scripts/          ← download_binance, build_manifest, run_*
outputs/          ← tracked reports + JSON (not raw ticks)
data/manifests/   ← checksums & coverage metadata only
data/raw/         ← gitignored downloaded market data
```

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

# Reproduce archived results (Gate real data)
python -m qtb.cli ab -c configs/ab_etf_vs_perp.yaml
python -m qtb.cli dual -c configs/dual_engine_perp.yaml

# Download Binance official history (not committed)
python scripts/download_binance.py --detect-start --symbols BTC ETH SOL SOXL SNXX
python scripts/build_manifest.py

pytest -q
```

## Capital default (configurable)

See [`configs/portfolio.yaml`](configs/portfolio.yaml): **6500 Tech + 2500 Crypto + 1000 Reserve = 10k USDT**.

## Out of scope in this branch

**`uncertain-atlas/`** (blockchain / consensus research) lives on a **separate branch** and must **not** be modified by quant grid work. See [`docs/CURSOR_HANDOFF.md`](docs/CURSOR_HANDOFF.md).

## CLI (legacy entry — still supported)

```bash
python -m qtb.cli backtest -c configs/backtest_btc_classic_grid.yaml
python -m qtb.cli optimize -c configs/optimize.yaml
python -m qtb.cli ab -c configs/ab_etf_vs_perp.yaml
python -m qtb.cli dual -c configs/dual_engine_perp.yaml
```

## License / risk

Backtests use real public data where available. Execution models are research-grade. Past performance does not predict future results.
