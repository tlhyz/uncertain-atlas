# P1-15 — cache vs committed tick manifests

Verdict: **PASS** (inventory). Disk no longer holds Book A/B major ticks.

## Method

`python3 scripts/audit_tick_cache_vs_manifests.py` compares every
`data/manifests/binance_*_aggTrades_*.json` `files[].path` / `bytes` to `cache/`.
No download. No sha256 (size-only). JSON:
`outputs/experiments/cache_vs_manifests/p1_15_audit.json`.

## On disk (2026-09-16T02:40Z)

| Symbol | Manifest window | Claimed days | Present | Status |
|--------|-----------------|--------------|---------|--------|
| SOXLUSDT | 2026-05-15→09-11 | 120 | 120 | on_disk |
| SOXLUSDT | 2026-07-09→09-11 | 65 | 65 | on_disk |
| SOXLUSDT | 2026-07-15→09-11 | 59 | 59 | on_disk |
| SOXSUSDT | 2026-07-16→09-14 | 61 | 61 | on_disk |

`cache/` tick symbols: **SOXLUSDT 120d**, **SOXSUSDT 61d**. ~3.5 GB. Bytes match claimed.

## Evicted (manifest remains, files gone)

| Symbol | Claimed | Present |
|--------|---------|---------|
| BTCUSDT | 91 | 0 |
| ETHUSDT | 91 | 0 |
| SOLUSDT | 91 | 0 |
| SNXXUSDT | 65 | 0 |

These were downloaded in P1-01/P1-03. Manifests + sha256 still in git. CSVs are
rebuildable from Binance Vision. **Do not auto-redownload** unless a new Book A/B
tick experiment is opened (P1-16 blocked).

## Implications

- SOXL user grid / soxl-lab: local ticks complete. No action.
- Re-running P1-11 / P2 / P3 tick jobs on this machine: **blocked** until SNXX or
  majors are restored.
- Quality-gate tests that expect 2026-07-09 SOXL files: still on disk.

## Red team

1. Bytes match ≠ sha256. A truncated-then-padded file would pass. Unlikely.
2. Empty 0-byte files counted missing (script requires size > 0).
3. Meta `.json` siblings ignored — only `files[]` CSVs.
4. soxl-lab copies of manifests were not double-counted (script reads `data/manifests/` only).
5. Eviction date unknown; do not treat as a new data gap at the venue.

## Do not

`git add cache/`. Retry P3-11. Start a multi-GB BTC/ETH/SOL pull in a 10-minute slot.
