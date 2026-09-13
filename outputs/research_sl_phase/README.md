# Research Phase: Stop-Loss / Gate 3L ETF Grid (Niulai & related)

**Verdict: FAILED** — see `docs/RESEARCH_HISTORY.md` Experiment 001.

This directory archives pointers to the SL-phase work. Primary artifacts live at repo root and under `outputs/demo_*`.

## Key reports (preserved, not moved)

| Report | Location |
|--------|----------|
| Niulai aggressive SL50 | `opt_niulai_aggressive_sl50_report.md` |
| Niulai aggressive SL70 | `opt_niulai_aggressive_sl70_report.md` |
| Niulai aggressive | `opt_niulai_aggressive_report.md` |
| Niulai base | `opt_niulai_report.md` |
| BTC SL50 | `opt_BTC_USDT_sl50_report.md` |

## Demo output

- `outputs/demo_niulai_aggressive_sl50/` — metrics, trades, config snapshot

## Core failure mode

Grid realized profit **<** inventory + directional loss → **negative total equity** on real Gate ETF paths.

## Do not

- Re-run as default strategy without new hypothesis
- Treat grid crossing count as success metric
- Assume 3L ETF avoids risk because of no classical liquidation

## Scripts (legacy)

Root `optimize_niulai_aggressive_sl50.py` etc. — superseded by `qtb optimize` for new work.
