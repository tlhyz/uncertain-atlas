# Uncertain Atlas 工具

| 工具 | 用途 | 状态 |
|---|---|---|
| [`adversarial_runner.py`](adversarial_runner.py) | 解析 / 校验 `libraries/adversarial-corpus/` | v0 可用 |
| [`review_audit.py`](review_audit.py) | 复审清单 → `REVIEW_REPORT.md` | v0 可用 |
| [`atlas_index.py`](atlas_index.py) | 本地 Markdown 目录 JSON | v0 可用 |
| [`invariant_corpus_links.py`](invariant_corpus_links.py) | 不变量 ↔ 语料双向链接（gate inv≥650） | v0 可用 |

```bash
cd uncertain-atlas
python tools/adversarial_runner.py stats
python tools/adversarial_runner.py validate
python tools/adversarial_runner.py list --limit 20
python tools/review_audit.py
python tools/atlas_index.py --stats
python tools/invariant_corpus_links.py
```

Phase 3 余项：P3-3 merge 285 snapshot 分支。
