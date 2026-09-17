# Uncertain Atlas 工具

| 工具 | 用途 | 状态 |
|---|---|---|
| [`adversarial_runner.py`](adversarial_runner.py) | 解析 / 校验 `libraries/adversarial-corpus/` | v0 可用 |

```bash
cd uncertain-atlas
python tools/adversarial_runner.py stats
python tools/adversarial_runner.py validate
python tools/adversarial_runner.py list --limit 20
```

Phase 3 计划：`atlas_index.py`（Markdown 目录 JSON）、invariant↔corpus 链接校验。
