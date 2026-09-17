# Review Log — P1-01 ETH/SOL download + P1-11 65d backtest restart

**Date (UTC):** 2026-09-13  
**Tasks:** P1-01 (in_progress), P1-11 (in_progress)  
**Verdict:** IN_PROGRESS — infra fixes applied; jobs restarted

---

## Context

Timer `research-continue` fired. P1 phase has two in_progress tasks. Two stale dual processes (PID 8992 full sweep since Sep 12, PID 12892 65d run 80+ min with only provenance) were consuming 100% CPU.

---

## Actions taken

### 1. run.py skip flags (focused experiments)

Added config toggles so P1-11 can skip heavy optional steps:

- `run_independent_vs_unified`
- `run_short_structures`
- `run_leverage_rank`
- `run_grid_atr_rank`
- `run_fill_modes`

Updated `configs/experiments/dual_binance_tick_65d.yaml` — benchmarks + seed_windows only.

### 2. Fixed blockers

| Issue | Fix |
|-------|-----|
| `configs/data_quality.yaml` had Python docstring — YAML parse error | Replaced with `#` comment |
| `scripts/download_binance.py` ModuleNotFoundError | Added `sys.path` bootstrap (same as download_gate.py) |

### 3. Killed stale processes

- PID 8992: `dual_engine_perp.yaml` full sweep (Sep 12)
- PID 12892: slow 65d run without skip flags

### 4. Restarted jobs (tmux)

- **P1-01:** `download_binance.py --symbols ETH SOL --start 2024-09-05 --end 2024-11-30`
  - ETH cache: 4 → 18+ day files at log time (target ~87 days)
  - SOL pending after ETH completes
- **P1-11:** `qtb.cli dual -c configs/experiments/dual_binance_tick_65d.yaml`
  - DATA_QUALITY gate PASS
  - Running benchmarks on 65d tick data

---

## Tests

```
122 passed in 33.26s
```

---

## Next steps

1. Wait for ETH/SOL download → `build_manifest.py` → mark P1-01 done
2. Wait for P1-11 backtest → review benchmarks vs B&H → write PASS/FAIL log
3. Run `build_manifest.py` after download completes

---

## Red team notes

- Do not draw conclusions from P1-11 until full report written
- Prior 7d smoke FAIL (-77.8% vs B&H +1%) preserved in ledger
- FAIL stays FAIL until new evidence chain
