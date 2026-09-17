# 例：看见 h_e 必须高于当前 is not already current height interchangeable / not already height-H Prepare interchangeable / not already settled interchangeable

**层次**：实现 / h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量）/ not 876 abci20-upgrade-notcurrent interchangeable / not 346 abci20-upgrade-vs-height bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是到了 H 就已经 Prepare 带了扩展（330），也不是写成 0 就已经启用 PBTS（343）。不要另写怎样做协调升级。

## 官方三件事

1. **看见升级之后 *h<sub>u</sub>* 才能把 `VoteExtensionsEnableHeight` 写成 *h<sub>e</sub>* / 看见 *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1） 这份必须 is not already 已经能写成当前高度 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 876 abci20-upgrade-notcurrent interchangeable / 875 abci20-upgrade-notfield interchangeable / 346 abci20 item 1 协调升级 interchangeable，也不是已经 h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事 bundled（346 item 2 余量） interchangeable / 346 abci20 item 2 interchangeable。**  
   官方写：协调升级发生在高度 *h<sub>u</sub>* 之后，这个参数可以写成某个 *h<sub>e</sub>*，但必须高于当前链高度。最早的 *h<sub>e</sub>* 是 *h<sub>u</sub>*+1。看见升级过了，不是已经能写成当前这一高 interchangeable——本页从 346 item 2 侧钉 not already current height 单句。346 abci20 vs height bundled unbundling 在本页 item 2 续。

2. **看见必须比当前高 / 看见最早 *h<sub>u</sub>*+1 / 这份必须 is not already 已经是到了 H 才 Prepare 带扩展那种切换 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 876 abci20-upgrade-notcurrent interchangeable / 346 abci20 item 3 当前高度存什么 interchangeable / 877 abci20-upgrade-notgenesis interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把必须比当前高和已经是 330 那种到了 H 才 Prepare 带扩展分开——346 bundled 第二件事常与 330 混成「看见必须比当前高就已经能写成当前或已经是到了 H interchangeable」，本页钉 not already height-H Prepare 单句。

3. **看见必须比当前高 / 看见升级过了 / 这份必须 is not already 已经交差 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 876 abci20-upgrade-notcurrent interchangeable / 875 abci20-upgrade-notfield interchangeable，也不是已经写成 0 就已经启用 PBTS interchangeable / 343 pbts-zero interchangeable。**  
   官方把必须比当前高和已经交差分开。看见升级过了，不是已经交差 interchangeable。346 abci20 vs height bundled unbundling 在本页 item 2 续。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **h_e 必须高于当前 not already current height ≠ 已经能写成当前高度 interchangeable：** 官方把升级之后才能写启用高度和写成当前这一高分开。
- **看见必须比当前高 not already height-H Prepare ≠ 已经是到了 H 才 Prepare 带扩展 interchangeable：** 官方把必须比当前高和已经是 330 那种到了 H 才 Prepare 带扩展分开。
- **看见升级过了 not already settled ≠ 已经交差 interchangeable：** 官方把必须比当前高和已经交差分开；346 abci20 vs height bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| h_e 必须高于当前 | 不是已经能写成当前高度 | 不是到了 H 就已经 Prepare 带了扩展（330） |
| 看见必须比当前高 | 不是已经是到了 H 才 Prepare 带扩展 | 不是写成 0 就已经启用 PBTS（343） |
| 看见升级过了 | 不是已经交差 | 不是必须协调升级就已经只改字段（875） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h_e 必须高于当前 not already current height / not already height-H Prepare / not already settled 正式三事（346 余量），必须分开是不是已经能写成当前高度、是不是已经是到了 H 才 Prepare 带扩展、是不是已经交差。可以跳过「看见必须比当前高就已经能写成当前」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 2 续；续 [`worked-example-abci20-upgrade-notgenesis-vs-bundled.md`](worked-example-abci20-upgrade-notgenesis-vs-bundled.md)（不变量 877 item 3）。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- 必须协调升级。那是不变量 346 item 1 余量 / 875。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 写成 0 就已经启用 PBTS。那是不变量 343。
