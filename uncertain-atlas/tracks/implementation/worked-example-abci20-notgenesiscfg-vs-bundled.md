# 例：看见引擎按当前高度决定存什么要什么 / 看见成功运转看当前高度 / 看见创世写了启用高度 is not already already genesiscfg interchangeable / already app-decides interchangeable / already settled interchangeable

**层次**：实现 / 引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量）/ not 793 abci20-notgenesiscfg interchangeable / not 346 abci20upgrade bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是必须协调升级不是已经只改 VoteExtensionsEnableHeight（791 item 1 余量）或 h_e 必须高于当前不是已经能写成当前高度（792 item 2 余量）。不要另写怎样做协调升级。

## 官方三件事

规范把 Requirements 里 CometBFT 按当前高度决定存哪些数据、运转要哪些数据 和「已经是创世写了就已经按创世配好了 interchangeable / 已经是应用配了参数就已经是应用自己决定存什么 interchangeable / 已经是当前高度在就已经交差 interchangeable / 已经是 abci20upgrade bundled interchangeable」分开写成三件独立的实现事，不是「看见引擎按当前高度决定存什么要什么就已经按创世配好了 interchangeable / 就已经是应用自己决定存什么 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见引擎按当前高度决定存什么、要什么 / 看见成功运转看当前高度 / 看见创世写了启用高度 is not already 已经按创世配好了 interchangeable / 已经 genesiscfg interchangeable / 已经按创世存交差 interchangeable / 346 abci20upgrade bundled interchangeable / 343 pbtsheight interchangeable / abci20upgrade-sold-as-height interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 793 abci20-notgenesiscfg interchangeable / 346 abci20 item 3 interchangeable，也不是已经引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事 bundled（346 item 3 余量） interchangeable / 346 abci20 item 3 interchangeable，也不是已经必须协调升级不是已经只改字段（791） interchangeable / 792 abci20-notwritecurrent interchangeable / 330 veheight interchangeable，也不是已经写成 0 就已经启用 PBTS（343） interchangeable。**  
   官方写：因此 CometBFT **按当前高度** 决定存哪些数据、运转要哪些数据。看见创世写了启用高度，不是已经按创世那一高在存。看见引擎按当前高度决定存什么要什么，不是已经 genesiscfg interchangeable——346 钉 bundled 三事，本页从 item 3 侧钉 not already genesiscfg 单句。看见成功运转看当前高度，不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable——346 钉 bundled，本页钉 item 3 第一件事。看见创世写了启用高度，不是已经写成 0 就已经启用 PBTS（343） interchangeable——343 另钉。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

2. **看见应用配了参数 / 看见应用填了启用高度 / 看见参数表里有 VoteExtensionsEnableHeight is not already 已经是应用自己决定存什么 interchangeable / 已经 app-decides interchangeable / 已经应用决定交差 interchangeable / 346 abci20upgrade bundled interchangeable / 791 abci20-notonlyveheight interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 793 abci20-notgenesiscfg interchangeable / 346 abci20 item 1 协调升级 interchangeable / 346 abci20 item 2 h_e interchangeable，也不是已经引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事 bundled（346 item 3 余量） interchangeable / 346 abci20 item 3 interchangeable，也不是已经按创世配好了（本页第一件事） interchangeable。**  
   官方写：看见应用配了参数，不是应用已经决定引擎存什么。看见应用填了启用高度，不是已经 app-decides interchangeable——本页钉 not already app-decides 单句。看见参数表里有 `VoteExtensionsEnableHeight`，不是已经按创世配好了（本页第一件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

3. **看见当前高度在 / 看见可以按当前高度运转 / 看见将来的 *h<sub>e</sub>* 还没到 is not already 已经按将来的 *h<sub>e</sub>* 在要扩展 interchangeable / 已经 settled interchangeable / 已经按将来要扩展交差 interchangeable / 346 abci20upgrade bundled interchangeable / 792 abci20-notwritecurrent interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 793 abci20-notgenesiscfg interchangeable / 346 abci20 item 1 / 346 abci20 item 2，也不是已经引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事 bundled（346 item 3 余量） interchangeable / 346 abci20 item 3 interchangeable，也不是已经按创世配好了（本页第一件事） interchangeable / 已经是应用自己决定存什么（本页第二件事） interchangeable。**  
   官方写：看见当前高度在，不是已经按将来的 *h<sub>e</sub>* 在要扩展。看见可以按当前高度运转，不是已经 settled interchangeable——本页钉 not already settled 单句。看见将来的 *h<sub>e</sub>* 还没到，不是已经是应用自己决定存什么（本页第二件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。ABCI 2.0 协调升级 bundled（346）、必须协调升级不是已经只改 VoteExtensionsEnableHeight（346 item 1 余量 / 791）、h_e 必须高于当前不是已经能写成当前高度（346 item 2 余量 / 792）、到了 H 就已经 Prepare 带了扩展（330）、写成 0 就已经启用 PBTS（343）、治理改 enable-height 会 panic（58）是另外那套，本页不抄。

## 官方为什么这样拆

- **引擎按当前高度决定存什么要什么 not already genesiscfg ≠ 346 / 343 interchangeable：** 官方把按当前高度存/要和已经按创世配好了分开。
- **应用配了参数 not already app-decides ≠ 已经是应用自己决定存什么 interchangeable：** 官方把应用配了参数和已经是应用自己决定引擎存什么分开。
- **当前高度在 not already settled ≠ 已经按将来的 h_e 在要扩展 interchangeable：** 官方把按当前高度运转和已经按将来的 *h<sub>e</sub>* 在要扩展分开；346 abci20 vs height bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 引擎按当前高度决定存什么要什么 | 不是 already genesiscfg | 不是写成 0 就已经启用 PBTS alone（343） |
| 应用配了参数 | 不是 already app-decides | 不是必须协调升级就已经只改字段 alone（791） |
| 当前高度在 | 不是 already settled | 不是 h_e 必须高于当前 alone（792） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么不是已经按创世配好了 not already genesiscfg / not already app-decides / not already settled 正式三事（346 余量），必须分开引擎按当前高度决定存什么要什么 是不是 already genesiscfg interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable、应用配了参数 是不是 already app-decides interchangeable、当前高度在 是不是 already settled interchangeable。可以跳过「看见创世写了就已经按创世在存 interchangeable / 就已经是应用自己决定存什么 interchangeable / 就已经按将来的 h_e 在要扩展 interchangeable」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 3 完成（791 + 792 + 793）。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- 必须协调升级不是已经只改 VoteExtensionsEnableHeight。那是不变量 346 item 1 余量 / 791。
- h_e 必须高于当前不是已经能写成当前高度。那是不变量 346 item 2 余量 / 792。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 写成 0 就已经启用 PBTS。那是不变量 343。
- 治理改 enable-height 会 panic。那是不变量 58。
