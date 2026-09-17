# 优化路线图入口

读 [`../ROADMAP.md`](../ROADMAP.md) 获取：

1. **极大目标** — 可验证的全球架构图谱 + 不确定设计参考库  
2. **架构评估** — 已完善 vs 需调整  
3. **Phase 0–3 小目标** — 带 ID，可勾选  
4. **canonical 分支说明**

---

## 当前 canonical 分支（建议）

```
cursor/uncertain-atlas-optimization-5ee2
```

来源：合并 `cursor/cometbft-echousage-notdone-676-2f0b`（KB 最全）+ 本优化迭代（677–988 Query/CheckTx/Commit/InitChain/Finalize/ProposalStatus/Prepare/Apply/Offer Result 拆句）。  
`main` 仍只有 `qtb/` 交易框架；协议知识不在 `main`。

---

## 快速导航

| 想做什么 | 去哪 |
|---|---|
| 理解五条轨 | [`../ARCHITECTURE.md`](../ARCHITECTURE.md) |
| 通读学习 | [`04-study-path.md`](04-study-path.md) |
| 查资产进度 | [`03-knowledge-assets.md`](03-knowledge-assets.md) |
| 做不确定选型 | [`../libraries/decision-matrix/`](../libraries/decision-matrix/README.md) |
| 跑对抗语料 | [`../tools/adversarial_runner.py`](../tools/adversarial_runner.py) |
| 审核历史 | [`../AUDIT_LOG.md`](../AUDIT_LOG.md) |
