# Crypto Satellite Cap Test — PENGU/PUMP

- **execution:** BAR (Gate 1h klines — no Binance aggTrades)
- **account cap:** 5% combined (500 USDT)
- **symbols:** PENGU, PUMP

## Results

| Symbol | Budget | Return | MaxDD | Liq | Cap OK | Window |
|--------|--------|--------|-------|-----|--------|--------|
| PENGU | 250U (2.5%) | -99.3% | 99.3% | N | Y | 2025-07-23→2026-09-12 |
| PUMP | 250U (2.5%) | -98.6% | 98.7% | N | Y | 2025-07-23→2026-09-12 |

## Policy check

- Combined budget: **500 USDT** (5.0% of account)
- satellite_cap_ok: **True**

## Notes

- C1 tick-precise (2024-09→11) **blocked** — no Binance aggTrades manifests for PENGU/PUMP.
- Gate history ~10k bars; PENGU list Jul-2025+, short sample — **WEAK evidence**.
- Meme leverage capped at 1.0x per STRATEGY_CRYPTO.md.
