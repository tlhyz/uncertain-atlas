# Review Log — P3-16 Gate OOS on top-3 Tech param sets

## Meta

- **date_utc:** 2026-09-14T04:40Z
- **task:** P3-16
- **config:** configs/experiments/gate_calibration.yaml (stub)
- **method:** Assess readiness; no Gate OOS run attempted

## Top-3 param sets (from P3 sweeps)

| Rank | Config | Binance 65d return | vs B3 grid-only |
|------|--------|-------------------|-----------------|
| 1 | Drawdown set **C** | -56.08% | −30.88pp |
| 2 | Grid mix **G50** | -57.85% | −32.65pp |
| 3 | Default dual | -58.70% | −33.50pp |

**None qualify as MEDIUM candidates** — all FAIL vs B3 (−25.20%), B4 (−25.19%), B&H (−33.49%).

## Blockers

1. **`scripts/run_gate_oos.py`** — placeholder only (prints message, exits 0)
2. **`gate_calibration.yaml`** — `enabled: false`
3. **No finalist beats Binance baselines** — OOS would not change deploy decision per `outputs/LIVE_CANDIDATES.md`

## Verdict

- **task_verdict:** **BLOCKED**
- **reason:** Gate OOS infra stub + no param set meets pre-OOS bar (beat Cash→Long / grid-only on Binance)
- **unblock:** Implement Gate calibration runner + at least one config beating B3 on Binance tick before OOS spend

## Red team (≥5)

1. Gate overlap prior FAIL (−51%) may differ from Binance — OOS still informative for fill calibration only
2. Joint drawdown C + G50 not tested — could be best combined hint
3. OOS for fill calibration ≠ strategy approval — could run calibration without live candidate
4. INSUFFICIENT_GATE_HISTORY policy may block even if runner built
5. P3-16 premature if no config fixes Short FSM first

## Next

- Do not run Gate OOS until infra + MEDIUM candidate exist
- P3-17 effective beta (executable on current data)
- Revisit after drawdown C + G50 joint sweep if requested
