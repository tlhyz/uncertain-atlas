# 反模式：把 头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量） 写成已经 已经有了 State / 已经流言过对象 / 已经交差

**层次**：实现 / 头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notroot-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notroot-vs-bundled.md)。

把 头上的根 not already have-State / not already gossiped-object / not already settled 正式三事（300 余量） 写成已经 已经有了 State / 已经流言过对象 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上的根 正式三事（300 余量），必须分开 not already have-State、not already gossiped-object、not already settled 三件事，不要和 300 / 38 / 298 / 983 / 985 糊成一句。

也不是：

- [stategossip-notblock-sold-as-bundled](stategossip-notblock-sold-as-bundled.md) 是本地对象仍未进块单句边界（983 item 1），不是本页头上有根仍未有 State 边界。
- 快照已经从创世重放是不变量 38，不是本页根对上了仍未流言过对象边界。
