# 反模式：把引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量）说成已经按创世配好了 / 已经是应用自己决定存什么 / 已经按将来的 h_e 在要扩展

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[引擎按当前高度决定存什么要什么 not already genesiscfg ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notgenesiscfg-vs-bundled.md)。

## 卖法

把引擎按当前高度决定存什么、要什么 / 成功运转看当前高度 / 创世写了启用高度 写成已经按创世配好了 interchangeable / 已经 genesiscfg interchangeable / 已经按创世存交差 interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable；把应用配了参数 / 应用填了启用高度 写成已经是应用自己决定存什么 interchangeable / 已经 app-decides interchangeable / 已经应用决定交差 interchangeable；把当前高度在 / 可以按当前高度运转 写成已经按将来的 *h<sub>e</sub>* 在要扩展 interchangeable / 已经 settled interchangeable / 已经按将来要扩展交差 interchangeable，或已经和 346 abci20upgrade bundled / abci20upgrade-sold-as-height interchangeable / 793 abci20-notgenesiscfg interchangeable。

## 为什么错

官方把按当前高度存/要、不是应用自己决定引擎存什么、不是已经按将来的 *h<sub>e</sub>* 在要扩展写成三件独立的实现事。把它们卖成 already genesiscfg interchangeable / already app-decides interchangeable / already settled interchangeable，会把 not already genesiscfg、not already app-decides、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量），必须分开 not already genesiscfg、not already app-decides、not already settled 三件事，不要和 346 / 343 / 330 / 791 / 792 糊成一句。

## 和相邻反模式

- [abci20upgrade-sold-as-height](abci20upgrade-sold-as-height.md) 是 ABCI 2.0 协调升级 bundled 全段，不是本页引擎按当前高度 item 3 单句边界。
- [abci20-notwritecurrent-sold-as-bundled](abci20-notwritecurrent-sold-as-bundled.md) 是 h_e 必须高于当前 not already writecurrent（346 item 2），不是本页 not already genesiscfg 边界。
- [pbtsheight-sold-as-enabled](pbtsheight-sold-as-enabled.md) 是写成 0 不是已经启用 PBTS（343），不是本页创世写了 ≠ 按创世在存 边界。
