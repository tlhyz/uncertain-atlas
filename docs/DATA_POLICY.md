# Data Policy

## Non-negotiable rules

1. **No synthetic tick data.** If aggTrades/trades do not exist → they do not exist.
2. **No Yahoo daily bars as tick substitutes** for execution claims.
3. **No fabricated order book** from OHLC alone.
4. **No NAV synthesis** for Gate 3L ETF path beyond documented theoretical benchmarks.
5. **Funding:** use venue real series; missing → mark missing, not average-invented.
6. **Seed windows** without target instrument history → **`STRUCTURAL_SEED_ONLY`** — shape search only, not execution PnL claims.

## Storage

| Path | Git | Contents |
|------|-----|----------|
| `data/raw/` | **ignored** | Downloaded ZIP/CSV/Parquet |
| `data/manifests/` | **tracked** | Checksum, coverage, source metadata |
| `cache/` | **ignored** | Local incremental cache |
| `outputs/` | **tracked** | Reports, JSON summaries, small CSV |

## Reproducibility

```bash
python scripts/download_binance.py --detect-start --symbols BTC ETH SOL SOXL SNXX
python scripts/build_manifest.py
```

Anyone cloning the repo must be able to rebuild datasets from official sources.

## Precision labels (required in reports)

| Label | Meaning |
|-------|---------|
| **TICK BACKTEST** | Real aggTrades/trades, maker-first engine, bar fallback forbidden |
| **BAR BACKTEST** | OHLC + volume participation model — state clearly |
| **STRUCTURAL SEED** | Price shape only — **no execution claims** |

## Tech (SOXL/SNXX)

- Binance Vision: SOXLUSDT **2026-05-15+** (probed 2026-09-15; 2026-05-14 and all 2025 dates 404). SNXXUSDT ~2026-07+ (verify via `detect_earliest_available`).
- Gate perp history may be shorter → mark **`INSUFFICIENT_GATE_HISTORY`** when needed.

## Crypto

- Binance = primary long-history research venue.
- Auto-detect symbol listing date — never backfill pre-listing bars.
