# Level 4 · BFT 与 CometBFT 锁

优先级：必学（「不确定」主骨架）  
先修：L0.6、L1.2、Bitcoin L3.1  
档案：[`../../protocols/cometbft/report.md`](../../protocols/cometbft/report.md)

毕业：能讲清为什么 `Propose → Prevote → Precommit → Commit` 不能收成「投票过 2/3」，以及 `V(h)` 必须唯一。

| 课 | 文件 | 覆盖 | 核心问题 |
|---|---|---|---|
| 4.1 | [L04-M01-quorum-intersection.md](L04-M01-quorum-intersection.md) | M4.1 | 2/3 从哪来 |
| 4.2 | [L04-M02-rounds-and-steps.md](L04-M02-rounds-and-steps.md) | M4.2 | 高度、轮、步；本头 LastCommit ≠ 本高已 +2/3（不变量 148） |
| 4.3 | [L04-M03-locks.md](L04-M03-locks.md) | M4.3 | 锁、解锁、超时 |
| 4.4 | [L04-M04-abci-and-wal.md](L04-M04-abci-and-wal.md) | M4.5 / M4.6 / M4.8 入口 | 应用分离、四门、崩溃不投矛盾票；本头 AppHash ≠ 本块已交差（不变量 147） |
| 4.5 | [L04-M05-validator-set.md](L04-M05-validator-set.md) | M4.4 | 集合何时算数；当选后单位见 NPoS 等权精读 |
| 4.6 | [L04-M06-hotstuff-casper-contrast.md](L04-M06-hotstuff-casper-contrast.md) | M4.7 | QC / FFG 对照，不深挖变体；BABE ≠ GRANDPA、Snow 抽样 ≠ QC 见共识精读 |
