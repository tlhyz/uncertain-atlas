# 模式：点名 stategossip-notspec 杠

**层次**：实现 / 落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notspec-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notspec-vs-bundled.md)。

- **落盘或查询接口 不是已经进了规范：** 看见能读本地 State，不是这份接口已经是规范对象 interchangeable / 985 stategossip-notspec interchangeable。
- **看见落盘了 不是已经能在网上对上：** 看见落盘了，不是已经能在网上对上 interchangeable。
- **看见查询回了字段 不是已经交差：** 看见查询回了字段，不是这些字段已经进了块 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看落盘或查询接口 正式三事（300 余量），先数清问的是是不是已经进了规范、是不是已经能在网上对上、还是看见查询回了字段是不是已经交差，再决定要不要同一次发布。300 state vs gossip bundled unbundling 在本页 item 3 完成。
