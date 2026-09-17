# 反模式：把 必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量） 卖成 已经只改 VoteExtensionsEnableHeight / 已经是单节点能切 / 已经交差

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notfield-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notfield-vs-bundled.md)。

官方把必须协调升级 / h_e 必须高于当前 / 引擎按当前高度决定存什么要什么 三条核心句写成三件独立的实现事。把它们卖成已经只改 VoteExtensionsEnableHeight / 已经是单节点能切 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级 正式三事（346 余量），必须分开 not already only VoteExtensionsEnableHeight、not already single-node、not already settled 三件事，不要和 346 / 330 / 58 / 876 / 877 糊成一句。

## 和相邻反模式

- [req3-notany-sold-as-bundled](req3-notany-sold-as-bundled.md) 是 Req 3 必须 Accept（347/872），不是本页协调升级边界。
- 到了 H 就已经 Prepare 带了扩展是不变量 330，不是本页协调升级边界。
