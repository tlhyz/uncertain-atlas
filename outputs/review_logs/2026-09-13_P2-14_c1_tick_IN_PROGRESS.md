# Review Log — P2-14 CRYPTO_C1 tick run (IN_PROGRESS)

## Meta

- **date_utc:** 2026-09-13T06:52Z
- **experiment_id:** crypto_c1_tick
- **task:** P2-14
- **config:** configs/experiments/crypto_c1_tick.yaml
- **output:** outputs/experiments/crypto_c1_tick/ (pending)
- **tmux:** `p2-14-c1-tick`
- **log:** /tmp/p2-14_c1_tick.log

## Scope

- Window: **2024-09-01 → 2024-11-30** (CRYPTO_C1 seed)
- Symbols: **BTC, ETH, SOL** (no PENGU/PUMP — no Binance aggTrades manifests)
- Execution: **tick-precise** (Base fill) on crypto legs
- Runs: independent crypto book + unified-signal decoupling compare

## Prep fixes (this session)

1. **portfolio.py** — respect `tech_tick_fills=False` on C1 unified path (tech placeholder bars have no aggTrades)
2. **experiments.py** — `run_binance_crypto_c1` passes `skip_tick_validation`; unified uses mixed tick/bar mode
3. **crypto_c1_tick.yaml** — C1-only config (no leverage/grid sweeps)

## Status

Job started 06:52Z. Expected runtime **~2–3h** (2184 bars × 3 symbols × 2 portfolio runs).

```
bars=2184 tick_precise=True
[run] C1 baseline...
```

## Pending artifacts

- `outputs/experiments/crypto_c1_tick/CRYPTO_REPORT.md`
- `outputs/experiments/crypto_c1_tick/crypto_results.json` → `c1_baseline.independent` / `.unified` / `.delta_return`

## Verdict

**IN_PROGRESS** — awaiting job completion.

## Next (on completion)

- Review independent vs unified delta_return for decoupling evidence
- Compare crypto PnL vs Tech-weak / Crypto-strong C1 hypothesis
- Mark P2-14 done with PASS/FAIL strategy verdict
- Finalize any open Q-crypto docs if leverage/grid jobs also complete
