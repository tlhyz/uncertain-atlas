# 模式：点名 stategossip-notblock 杠

**层次**：实现 / 本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notblock-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notblock-vs-bundled.md)。

- **本地 State 不是已经进了块：** 看见本机有一份 State，不是这份已经进了某块 interchangeable / 983 stategossip-notblock interchangeable。
- **看见能读到它 不是已经流言：** 看见能读到它，不是邻居已经收到同一份 interchangeable。
- **看见字段齐了 不是已经交差：** 看见字段齐了，不是已经有一个 State 哈希可以对 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地 State 正式三事（300 余量），先数清问的是是不是已经进了块、是不是已经流言、还是看见字段齐了是不是已经交差，再决定要不要同一次发布。300 state vs gossip bundled unbundling 在本页 item 1 启动。
