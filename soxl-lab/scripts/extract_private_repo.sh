#!/usr/bin/env bash
# Copy this lab to DEST and init a local git repo. Does not create GitHub remotes.
set -euo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${1:-}"
if [[ -z "$DEST" ]]; then
  echo "usage: $0 /path/to/empty/soxl-lab" >&2
  exit 2
fi
mkdir -p "$DEST"
rsync -a --exclude '.git/' --exclude 'cache/' --exclude '.audit_tmp/' "$SRC"/ "$DEST"/
cd "$DEST"
if [[ ! -d .git ]]; then
  git init -b main
  git add .
  git commit -m "SOXL personal lab (extracted)"
fi
echo "local repo ready at $DEST"
echo "create a private GitHub repo, then: git remote add origin <url> && git push -u origin main"
