# 反模式：把 落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量） 写成已经 已经进了规范 / 已经能在网上对上 / 已经交差

**层次**：实现 / 落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [State](https://github.com/cometbft/cometbft/blob/main/spec/core/state.md) Data Structures / local State object。  
**对应**：[`../tracks/implementation/worked-example-stategossip-notspec-vs-bundled.md`](../tracks/implementation/worked-example-stategossip-notspec-vs-bundled.md)。

把 落盘或查询接口 not already in-spec / not already network-aligned / not already settled 正式三事（300 余量） 写成已经 已经进了规范 / 已经能在网上对上 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看落盘或查询接口 正式三事（300 余量），必须分开 not already in-spec、not already network-aligned、not already settled 三件事，不要和 300 / 56 / 148 / 983 / 984 糊成一句。

也不是：

- [stategossip-notroot-sold-as-bundled](stategossip-notroot-sold-as-bundled.md) 是头上有根仍未有 State 单句边界（984 item 2），不是本页接口仍未进规范边界。
- 提议者选择已经对齐是不变量 56，不是本页落盘了仍不能在网上对上边界。
