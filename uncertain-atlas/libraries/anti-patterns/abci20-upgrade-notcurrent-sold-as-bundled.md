# 反模式：把 h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量） 卖成 已经能写成当前高度 / 已经是到了 H 才 Prepare 带扩展 / 已经交差

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notcurrent-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notcurrent-vs-bundled.md)。

官方把必须协调升级 / h_e 必须高于当前 / 引擎按当前高度决定存什么要什么 三条核心句写成三件独立的实现事。把它们卖成已经能写成当前高度 / 已经是到了 H 才 Prepare 带扩展 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前 正式三事（346 余量），必须分开 not already current height、not already height-H Prepare、not already settled 三件事，不要和 346 / 330 / 343 / 875 / 877 糊成一句。

## 和相邻反模式

- [abci20-upgrade-notfield-sold-as-bundled](abci20-upgrade-notfield-sold-as-bundled.md) 是必须协调升级单句边界（875 item 1），不是本页 h_e 必须高于当前边界。
- 到了 H 就已经 Prepare 带了扩展是不变量 330，不是本页 h_e 必须高于当前边界。
