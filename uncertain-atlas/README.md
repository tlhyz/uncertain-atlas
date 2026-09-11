# Uncertain Atlas

全球区块链架构图谱 + 「不确定」设计参考库。

**这不是交易机器人。**  
本目录与 Gate 永续回测（`qtb/`、`strategies/`、`configs/`）隔离。协议知识只写在这里。

**最高准则：** [`GOAL.md`](GOAL.md)  
**目录说明：** [`ARCHITECTURE.md`](ARCHITECTURE.md)  
**审核日志：** [`AUDIT_LOG.md`](AUDIT_LOG.md)

出题后置，见 [`exams/`](exams/README.md)。现在先读知识。

---

## 从这里读

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — 五条轨怎么分开
2. [`index/00-master-roadmap.md`](index/00-master-roadmap.md) — Level 0–10 怎么走
3. [`index/01-knowledge-tree.md`](index/01-knowledge-tree.md) — 依赖
4. [`index/02-research-order.md`](index/02-research-order.md) — 为什么先 Bitcoin 再 BFT
5. [`courses/level-00-machine/`](courses/level-00-machine/README.md) — 机器直觉
6. [`courses/level-01-crypto/`](courses/level-01-crypto/README.md) — 工程密码学
7. [`courses/level-02-state/`](courses/level-02-state/README.md) — 状态模型
8. [`protocols/bitcoin/`](protocols/bitcoin/README.md)
9. [`protocols/cometbft/`](protocols/cometbft/README.md)
10. [`protocols/ethereum/`](protocols/ethereum/README.md)

修改日志：[`CHANGELOG.md`](CHANGELOG.md) · 审核：[`AUDIT_LOG.md`](AUDIT_LOG.md)

---

## 目录

```text
uncertain-atlas/
  index/          地图
  courses/        课程 Level 0, 1, 2, …
  protocols/      一条链一份 19 节档案
  tracks/         横向专题（共识 / 状态 / PQ / 失败博物馆）
  libraries/      模式、反模式、决策矩阵
  exams/          统一题库（后置）
```

---

## 优先级

| 标记 | 含义 |
|---|---|
| 必学 | 不学会，后面会变成背词 |
| 重要 | 「不确定」大概率会碰到 |
| 进阶 | 设计时要懂，实现第一版可后置 |
| 研究级 | 论文 / 形式化 / 后量子深水区 |
