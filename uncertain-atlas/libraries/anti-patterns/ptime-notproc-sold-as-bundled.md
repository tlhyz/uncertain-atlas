# 反模式：把 proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量） 写成已经 已经跑过 Process / 已经知道本头哈希 / 已经交差

**层次**：实现 / proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**对应**：[`../tracks/implementation/worked-example-ptime-notproc-vs-bundled.md`](../tracks/implementation/worked-example-ptime-notproc-vs-bundled.md)。

把 proposal header-first not already processed / not already header-known / not already settled 正式三事（416 余量） 写成已经 已经跑过 Process / 已经知道本头哈希 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先验块头 正式三事（416 余量），必须分开 not already processed、not already header-known、not already settled 三件事，不要和 416 / 359 / 417 / 1094 / 1096 糊成一句。

也不是：

- [ptime-notcfg-sold-as-bundled](ptime-notcfg-sold-as-bundled.md) 是 ProposeTimeout 仍未填了 TimeoutPropose 单句边界（1094 item 1），不是本页先验块头仍未跑过 Process 边界。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process 是不变量 359，不是本页提案带上头仍未知道本头哈希边界。
