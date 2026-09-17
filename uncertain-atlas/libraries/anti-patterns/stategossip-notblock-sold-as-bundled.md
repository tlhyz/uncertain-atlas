# 反模式：把 本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量） 写成已经 已经进了块 / 已经流言 / 已经交差

**层次**：实现 / 本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notblock-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notblock-vs-bundled.md)。

把 本地 State not already in-block / not already gossiped / not already settled 正式三事（300 余量） 写成已经 已经进了块 / 已经流言 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看本地 State 正式三事（300 余量），必须分开 not already in-block、not already gossiped、not already settled 三件事，不要和 300 / 147 / 298 / 984 / 985 糊成一句。

也不是：

- [wal-notheight-sold-as-bundled](wal-notheight-sold-as-bundled.md) 是 LastSignBytes 对上仍未换高度边界（298/982），不是本页本地对象仍未进块边界。
- 本头 AppHash 已经交差是不变量 147，不是本页能读到它仍未流言边界。
