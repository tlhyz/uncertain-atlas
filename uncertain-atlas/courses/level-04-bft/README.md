# Level 4 · BFT 与 CometBFT 锁

优先级：必学（「不确定」主骨架）  
先修：L0.6、L1.2、Bitcoin L3.1（知道概率最终长什么样）  
档案：[`../../protocols/cometbft/report.md`](../../protocols/cometbft/report.md)

毕业：能讲清为什么 `Propose → Prevote → Precommit → Commit` 不能收成「投票过 2/3」。

| 课 | 文件 | 核心问题 |
|---|---|---|
| 4.1 | [L04-M01-quorum-intersection.md](L04-M01-quorum-intersection.md) | 2/3 从哪来 |
| 4.2 | [L04-M02-rounds-and-steps.md](L04-M02-rounds-and-steps.md) | 高度、轮、步 |
| 4.3 | [L04-M03-locks.md](L04-M03-locks.md) | 锁、解锁、超时 |
| 4.4 | [L04-M04-abci-and-wal.md](L04-M04-abci-and-wal.md) | 应用分离与崩溃不投矛盾票 |
