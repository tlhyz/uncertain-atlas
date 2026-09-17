# 模式：点名 stategossip-notroot 杠

**层次**：实现 / 头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notroot-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notroot-vs-bundled.md)。

- **头上的根 不是已经有了 State：** 看见头上有根，不是已经有了本地那份 State interchangeable / 984 stategossip-notroot interchangeable。
- **看见根对上了 不是已经流言过对象：** 看见根对上了，不是 State 对象已经流言过 interchangeable。
- **看见头上有根 不是已经交差：** 看见头上有根，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上的根 正式三事（300 余量），先数清问的是是不是已经有了 State、是不是已经流言过对象、还是看见头上有根是不是已经交差，再决定要不要同一次发布。300 state vs gossip bundled unbundling 在本页 item 2 续。
