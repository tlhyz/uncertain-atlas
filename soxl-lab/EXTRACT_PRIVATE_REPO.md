# Extract this folder to a private GitHub repo

This environment **cannot** create the remote (`gh` is read-only). You create
an empty **private** repository, then push this tree.

## What goes in the private repo

- This folder only: params, manifests, classified results, audit logs.
- **Not** tick CSVs (1.65 GB). Keep them on the machine or in your own object store.
- **Not** SOXS / SNXX / BTC / ETH / SOL raw data.

## Commands

```bash
# from the research checkout
cd soxl-lab
git init -b main
git add .
git status   # confirm no cache/*.csv
git commit -m "SOXL personal lab: ticks classified, params locked, results audited"
git remote add origin git@github.com:<you>/soxl-lab.git
git push -u origin main
```

Or use the helper (still does not create the GitHub repo):

```bash
./scripts/extract_private_repo.sh /path/to/empty/soxl-lab
```

Point `SOXLLAB_CACHE` at the machine that still has
`cache/binance_futures_SOXLUSDT_aggTrades_*.csv` if you want pass-1 checksums
after extract.
