# 例：看见必须协调升级不是已经只改 VoteExtensionsEnableHeight；看见 h_e 必须高于当前不是已经能写成当前高度；看见引擎按当前高度决定存什么要什么不是已经按创世配好了

**层次**：实现 / ABCI 2.0 协调升级。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「必须协调升级不是已经只改 VoteExtensionsEnableHeight / h_e 必须高于当前不是已经能写成当前高度 / 引擎按当前高度决定存什么要什么不是已经按创世配好了」，不是到了 H 就已经 Prepare 带了扩展，也不是治理改 enable-height 会 panic。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 完成（791+792+793）；精读 [`worked-example-abci20-notonlyveheight-vs-bundled.md`](worked-example-abci20-notonlyveheight-vs-bundled.md)（不变量 791 item 1）、[`worked-example-abci20-notwritecurrent-vs-bundled.md`](worked-example-abci20-notwritecurrent-vs-bundled.md)（不变量 792 item 2）、[`worked-example-abci20-notgenesiscfg-vs-bundled.md`](worked-example-abci20-notgenesiscfg-vs-bundled.md)（不变量 793 item 3）。

## 官方三件事

规范把切到带扩展的版本写成三件独立的实现事，不是「看见填了启用高度就已经切完、已经能写成当前、已经按创世配好了存什么」一件事：

1. **看见必须协调升级 / 看见切到带扩展的 CometBFT 不是已经只改 `VoteExtensionsEnableHeight`，也不是已经是单节点能切。**  
   官方写：切到带投票扩展的 CometBFT 版本，**必须协调升级**。看见字段已经在参数表里，不是已经切完。看见一个节点升了二进制，不是全网已经能走扩展。看见能改启用高度，不是已经做了这次升级。
2. **看见升级之后 *h<sub>u</sub>* 才能把 `VoteExtensionsEnableHeight` 写成 *h<sub>e</sub>* / 看见 *h<sub>e</sub>* 必须高于当前（最早 *h<sub>u</sub>*+1） 不是已经能写成当前高度，也不是已经是到了 H 才 Prepare 带扩展那种切换。**  
   官方写：协调升级发生在高度 *h<sub>u</sub>* 之后，这个参数 **可以** 写成某个 *h<sub>e</sub>*，但 **必须** 高于当前链高度。最早的 *h<sub>e</sub>* 是 *h<sub>u</sub>*+1。看见升级过了，不是已经能写成当前这一高。看见必须比当前高，不是已经是 330 那种到了 H 才 Prepare 带扩展。
3. **看见引擎按当前高度决定存什么、要什么 / 看见成功运转看当前高度 不是已经按创世配好了，也不是已经是应用自己决定存什么。**  
   官方写：因此 CometBFT **按当前高度** 决定存哪些数据、运转要哪些数据。看见创世写了启用高度，不是已经按创世那一高在存。看见应用配了参数，不是应用已经决定引擎存什么。看见当前高度在，不是已经按将来的 *h<sub>e</sub>* 在要扩展。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。到了 H 不是已经 Prepare 带了扩展是不变量 330，本页不抄。

## 官方为什么这样拆

- **必须协调升级 ≠ 已经只改 VoteExtensionsEnableHeight：** 官方把换二进制的协调升级和改启用高度分开。
- **h_e 必须高于当前 ≠ 已经能写成当前高度：** 官方把升级之后才能写启用高度和写成当前这一高分开。
- **引擎按当前高度决定存什么要什么 ≠ 已经按创世配好了：** 官方把按当前高度存/要和创世或应用自己决定分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须协调升级 | 不是已经只改 VoteExtensionsEnableHeight | 不是到了 H 就已经 Prepare 带了扩展（330） |
| h_e 必须高于当前 | 不是已经能写成当前高度 | 不是治理改 enable-height 会让未升级节点 panic（58） |
| 引擎按当前高度决定存什么要什么 | 不是已经按创世配好了 | 不是写成 0 就已经启用 PBTS（343） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了启用高度就已经切完、已经能写成当前、已经按创世配好了存什么」，必须分开必须协调升级是不是已经只改 VoteExtensionsEnableHeight、h_e 必须高于当前是不是已经能写成当前高度、引擎按当前高度决定存什么要什么是不是已经按创世配好了。可以跳过「看见填了启用高度就已经切到 ABCI 2.0」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 完成（791+792+793）。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 治理改 enable-height 会 panic。那是不变量 58。
- 写成 0 就已经启用 PBTS。那是不变量 343。
