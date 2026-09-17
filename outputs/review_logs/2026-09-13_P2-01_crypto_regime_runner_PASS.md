# Review Log — P2-01 Enable crypto_regime.yaml runner

**Date (UTC):** 2026-09-13  
**Task:** P2-01  
**Verdict:** PASS

---

## Deliverables

| Item | Path |
|------|------|
| Runner module | `qtb/dual/crypto_run.py` |
| CLI | `python3 -m qtb.cli crypto -c configs/experiments/crypto_regime.yaml` |
| Script | `scripts/run_crypto.py` |
| Config | `configs/experiments/crypto_regime.yaml` (`enabled: true`) |

## Capabilities

- Loads Book B crypto-only dataset via `load_binance_crypto_dataset` (tech disabled)
- Leverage scan on `CryptoParams.leverage` (config: `leverage_scan`)
- Grid ATR scan on crypto params (config: `grid.atr_step_scan` / `atr_range_scan`)
- Optional C1 baseline via `run_binance_crypto_c1`
- `--smoke` flag: BTC-only, single leverage, fast validation
- Outputs: `crypto_results.json`, `CRYPTO_REPORT.md`, `provenance.json`

## Tests

```
tests/test_crypto_run.py — 4 passed
Full suite — 126 passed
```

## Not run this session

Full C1 leverage/grid sweeps (P2-02+) deferred — runner enabled, data manifests ready from P1-01.

## P1-11 note

65d Tech tick backtest still running separately (PID 29982 at implementation time).
