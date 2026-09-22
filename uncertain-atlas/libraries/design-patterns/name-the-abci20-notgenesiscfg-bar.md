# 模式：把引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**例**：[引擎按当前高度决定存什么要什么 not already genesiscfg ≠ bundled（346）](../../tracks/implementation/worked-example-abci20-notgenesiscfg-vs-bundled.md)。

## 三个名字

1. **引擎按当前高度决定存什么要什么 不是 already genesiscfg：** 看见引擎按当前高度决定存什么、要什么 / 成功运转看当前高度 / 创世写了启用高度，不是已经按创世配好了 interchangeable / 已经 genesiscfg interchangeable / 已经按创世存交差 interchangeable，不是 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable。

2. **应用配了参数 不是 already app-decides：** 看见应用配了参数 / 应用填了启用高度 / 参数表里有 `VoteExtensionsEnableHeight`，不是已经是应用自己决定存什么 interchangeable / 已经 app-decides interchangeable / 已经应用决定交差 interchangeable，不是 791 abci20-notonlyveheight interchangeable / 343 pbtsheight interchangeable。

3. **当前高度在 不是 already settled：** 看见当前高度在 / 可以按当前高度运转 / 将来的 *h<sub>e</sub>* 还没到，不是已经按将来的 *h<sub>e</sub>* 在要扩展 interchangeable / 已经 settled interchangeable / 已经按将来要扩展交差 interchangeable，不是 792 abci20-notwritecurrent interchangeable / 330 veheight interchangeable。

官方把按当前高度存/要、不是应用自己决定引擎存什么、不是已经按将来的 *h<sub>e</sub>* 在要扩展写成三个名字。把它们叫成一个「看见创世写了就已经按创世在存 interchangeable / 就已经是应用自己决定存什么 interchangeable / 就已经按将来的 h_e 在要扩展 interchangeable」，会把 not already genesiscfg、not already app-decides、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量），先数清问的是引擎按当前高度决定存什么要什么 是不是 already genesiscfg / 346 / abci20upgrade-sold-as-height，是不是应用配了参数 是不是 already app-decides，还是当前高度在 是不是 already settled，再决定要不要同一次发布。346 abci20 vs height bundled unbundling 在本页 item 3 完成。
