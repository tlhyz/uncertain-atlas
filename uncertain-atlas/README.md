# Uncertain Atlas

全球区块链架构图谱 + 「不确定」设计参考库。

**这不是交易机器人。**  
本目录与 Gate 永续回测（`qtb/`、`strategies/`、`configs/`）隔离。协议知识只写在这里。

**最高准则：** [`GOAL.md`](GOAL.md)（含细致 / 精密 / 全面）  
**目录说明：** [`ARCHITECTURE.md`](ARCHITECTURE.md)  
**审核日志：** [`AUDIT_LOG.md`](AUDIT_LOG.md)

出题后置，见 [`exams/`](exams/README.md)。现在先读知识。

---

## 从这里读

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — 五条轨
2. [`index/04-study-path.md`](index/04-study-path.md) — 目的 A：按通读，不要浏览
3. [`index/00-master-roadmap.md`](index/00-master-roadmap.md) — Level 0–10
4. [`index/01-knowledge-tree.md`](index/01-knowledge-tree.md) — 依赖
5. [`index/02-research-order.md`](index/02-research-order.md) — 为何先 Bitcoin
6. 课程：[`courses/`](courses/README.md)
7. 协议：[`protocols/`](protocols/README.md)
8. 横向：生命周期、实现、轻节点、升级、经济、网络、内存池、测试、PQ 迁移 [`tracks/post-quantum/migration.md`](tracks/post-quantum/migration.md)
9. 新链接待：[`libraries/new-chain-intake.md`](libraries/new-chain-intake.md)

修改日志：[`CHANGELOG.md`](CHANGELOG.md)

---

## 目录

```text
uncertain-atlas/
  index/          地图
  courses/        课程 Level 0–10
  protocols/      一条链（或一个品类）一份 19 节
  tracks/         横向专题与对照表
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
