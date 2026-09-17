# 反模式：把 引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量） 卖成 已经按创世配好了 / 已经是应用自己决定存什么 / 已经交差

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：建议（产品）。  
**对应例**：[worked-example-abci20-upgrade-notgenesis-vs-bundled.md](../../tracks/implementation/worked-example-abci20-upgrade-notgenesis-vs-bundled.md)。

官方把必须协调升级 / h_e 必须高于当前 / 引擎按当前高度决定存什么要什么 三条核心句写成三件独立的实现事。把它们卖成已经按创世配好了 / 已经是应用自己决定存什么 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么 正式三事（346 余量），必须分开 not already genesis configured、not already app decides、not already settled 三件事，不要和 346 / 343 / 330 / 875 / 876 糊成一句。

## 和相邻反模式

- [abci20-upgrade-notcurrent-sold-as-bundled](abci20-upgrade-notcurrent-sold-as-bundled.md) 是 h_e 必须高于当前单句边界（876 item 2），不是本页按当前高度存/要边界。
- 写成 0 就已经启用 PBTS 是不变量 343，不是本页按当前高度存/要边界。
