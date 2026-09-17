# Uncertain Atlas 工具

| 工具 | 用途 | 状态 |
|---|---|---|
| [`adversarial_runner.py`](adversarial_runner.py) | 解析 / 校验 `libraries/adversarial-corpus/` | v0 可用 |
| [`review_audit.py`](review_audit.py) | 复审清单 → `REVIEW_REPORT.md` | v0 可用 |
| [`atlas_index.py`](atlas_index.py) | 本地 Markdown 目录 JSON | v0 可用 |

```bash
cd uncertain-atlas
python tools/adversarial_runner.py stats
python tools/adversarial_runner.py validate
python tools/adversarial_runner.py list --limit 20
python tools/review_audit.py
python tools/atlas_index.py --stats
```

Phase 3 余项：invariant↔corpus 链接校验（P3-2）。
