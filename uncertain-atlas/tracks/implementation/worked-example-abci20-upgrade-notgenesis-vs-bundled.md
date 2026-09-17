# 例：看见引擎按当前高度决定存什么要什么 is not already genesis configured interchangeable / not already app decides interchangeable / not already settled interchangeable

**层次**：实现 / 引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量）/ not 877 abci20-upgrade-notgenesis interchangeable / not 346 abci20-upgrade-vs-height bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是写成 0 就已经启用 PBTS（343），也不是到了 H 就已经 Prepare 带了扩展（330）。不要另写怎样做协调升级。

## 官方三件事

1. **看见引擎按当前高度决定存什么、要什么 / 看见成功运转看当前高度 这份按当前 is not already 已经按创世配好了 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 877 abci20-upgrade-notgenesis interchangeable / 875 abci20-upgrade-notfield interchangeable / 346 abci20 item 1 协调升级 interchangeable，也不是已经引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事 bundled（346 item 3 余量） interchangeable / 346 abci20 item 3 interchangeable。**  
   官方写：因此 CometBFT 按当前高度决定存哪些数据、运转要哪些数据。看见创世写了启用高度，不是已经按创世那一高在存 interchangeable——本页从 346 item 3 侧钉 not already genesis configured 单句。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

2. **看见应用配了参数 / 看见当前高度在 / 这份按当前 is not already 已经是应用自己决定存什么 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 877 abci20-upgrade-notgenesis interchangeable / 346 abci20 item 2 h_e interchangeable / 876 abci20-upgrade-notcurrent interchangeable，也不是已经写成 0 就已经启用 PBTS interchangeable / 343 pbts-zero interchangeable。**  
   官方把应用配了参数和已经是应用自己决定引擎存什么分开——346 bundled 第三件事常与 343 混成「看见创世写了就已经按创世在存或已经是应用自己决定 interchangeable」，本页钉 not already app decides 单句。

3. **看见当前高度在 / 看见创世写了启用高度 / 这份按当前 is not already 已经交差 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 877 abci20-upgrade-notgenesis interchangeable / 875 abci20-upgrade-notfield interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把按当前高度存/要和已经按将来的 *h<sub>e</sub>* 在要扩展 / 已经交差分开。看见当前高度在，不是已经按将来的 *h<sub>e</sub>* 在要扩展 interchangeable。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **引擎按当前高度决定存什么要什么 not already genesis configured ≠ 已经按创世配好了 interchangeable：** 官方把按当前高度存/要和创世配好了分开。
- **看见应用配了参数 not already app decides ≠ 已经是应用自己决定存什么 interchangeable：** 官方把应用配了参数和已经是应用自己决定引擎存什么分开。
- **看见当前高度在 not already settled ≠ 已经交差 interchangeable：** 官方把按当前高度存/要和已经交差分开；346 abci20 vs height bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 引擎按当前高度决定存什么要什么 | 不是已经按创世配好了 | 不是写成 0 就已经启用 PBTS（343） |
| 看见应用配了参数 | 不是已经是应用自己决定存什么 | 不是到了 H 就已经 Prepare 带了扩展（330） |
| 看见当前高度在 | 不是已经交差 | 不是必须协调升级就已经只改字段（875） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎按当前高度决定存什么要什么 not already genesis configured / not already app decides / not already settled 正式三事（346 余量），必须分开是不是已经按创世配好了、是不是已经是应用自己决定存什么、是不是已经交差。可以跳过「看见创世写了就已经按创世在存」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- 必须协调升级。那是不变量 346 item 1 余量 / 875。
- 写成 0 就已经启用 PBTS。那是不变量 343。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
