# 模式：点名 wal-notfsync 杠

**层次**：实现 / 写下每条消息 not already fsynced / not already double-sign-safe / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notfsync-vs-bundled.md`](../tracks/implementation/worked-example-wal-notfsync-vs-bundled.md)。

- **写下每条消息 不是已经刷盘：** 看见写下了，不是已经刷盘 interchangeable / 980 wal-notfsync interchangeable。
- **看见别人的消息也在日志里 不是已经防了双签：** 看见别人的消息也在日志里，不是已经按本节点签名那条路刷过 interchangeable。
- **看见有预写日志 不是已经交差：** 看见有预写日志，不是已经守住不得再签矛盾票 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写下每条消息 正式三事（298 余量），先数清问的是是不是已经刷盘、是不是已经防了双签、还是看见有预写日志是不是已经交差，再决定要不要同一次发布。298 wal vs signed bundled unbundling 在本页 item 1 启动。
