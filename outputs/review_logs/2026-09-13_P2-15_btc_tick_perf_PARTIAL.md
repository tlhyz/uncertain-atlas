# Review Log — P2-15 BTC tick backtest perf investigation

## Meta

- **date_utc:** 2026-09-13T09:10Z
- **task:** P2-15
- **verdict:** **PARTIAL PASS** (root cause narrowed; full profile deferred)

---

## Trigger

P2-02 first leverage level (1.25x) ran **~6h** with 99.9% CPU and no completion log before 08:40Z restart.

---

## Data volume (manifests)

| Symbol | aggTrades rows (91d C1) |
|--------|-------------------------|
| BTC | **130,521,594** |
| ETH | 128,851,279 |
| SOL | 45,143,557 |

BTC is **not** an outlier vs ETH in row count — rules out "BTC has 3× trades" as sole explanation.

---

## I/O micro-benchmark (2024-09-01 → 09-05, 96 bars)

| Symbol | load_days | slice all bars | ms/bar slice |
|--------|-----------|----------------|--------------|
| BTC | 5.7s | 0.9s | **7.8ms** |

Script: `scripts/benchmark_crypto_tick_bar.py`

**Conclusion:** Per-bar aggTrades load+slice is **fast**. Bottleneck is **`run_dual_portfolio` tick grid loop** (grid levels × tick path × rebalance per bar), not disk I/O.

---

## Runtime reference (completed scans)

| Job | Symbol | Per level | Total 4 levels |
|-----|--------|-----------|----------------|
| P2-04 SOL | SOL | ~19 min | ~53 min |
| P2-03 ETH | ETH | ~43 min | ~172 min |
| P2-02 BTC | BTC | **>6h (1.25x killed)** | pending restart |

ETH/BTC similar data volume but ETH ~43 min/level — BTC 6h suggests **pathological bar** (high grid fill count) or **stdout buffering** masking progress, not raw row count.

---

## Recommendations

1. Add **bar-index progress log** inside `run_dual_portfolio` warm loop (every N bars)
2. Cache **day aggTrades DataFrame** in portfolio loop (already per `_load_bar_trades` call — verify no redundant reload)
3. Optional: `--max-bars` smoke flag for leverage scans during dev
4. Do **not** kill BTC job before **2h/level** on restart unless 0% CPU

---

## Next

- P2-02 restart: monitor `1.25x done` (started 08:40Z)
- Full cProfile on 24-bar BTC smoke when P2 jobs idle
