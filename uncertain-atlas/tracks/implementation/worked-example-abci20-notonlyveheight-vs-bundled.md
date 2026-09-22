# 例：看见必须协调升级 / 看见切到带扩展的 CometBFT / 看见字段已经在参数表里 is not already already only-veheight interchangeable / already single-node interchangeable / already field-filled interchangeable

**层次**：实现 / 必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量）/ not 791 abci20-notonlyveheight interchangeable / not 346 abci20upgrade bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是 h_e 必须高于当前不是已经能写成当前高度（792 item 2 余量）或引擎按当前高度决定存什么要什么不是已经按创世配好了（793 item 3 余量）。不要另写怎样做协调升级。

## 官方三件事

规范把 Requirements 里切到带投票扩展的 CometBFT 版本必须协调升级 和「已经是字段在就已经只改 VoteExtensionsEnableHeight interchangeable / 已经是一个节点升了就已经单节点能切 interchangeable / 已经是能改启用高度就已经 field-filled 交差 interchangeable / 已经是 abci20upgrade bundled interchangeable」分开写成三件独立的实现事，不是「看见必须协调升级就已经只改 VoteExtensionsEnableHeight interchangeable / 就已经单节点能切 interchangeable / 就已经 field-filled 交差 interchangeable」一件事：

1. **看见必须协调升级 / 看见切到带扩展的 CometBFT / 看见字段已经在参数表里 is not already 已经只改 `VoteExtensionsEnableHeight` interchangeable / 已经 only-veheight interchangeable / 已经只改字段交差 interchangeable / 346 abci20upgrade bundled interchangeable / 330 veheight interchangeable / abci20upgrade-sold-as-height interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 791 abci20-notonlyveheight interchangeable / 346 abci20 item 1 interchangeable，也不是已经必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事 bundled（346 item 1 余量） interchangeable / 346 abci20 item 1 interchangeable，也不是已经 h_e 必须高于当前（792） interchangeable / 793 abci20-notgenesiscfg interchangeable / 330 veheight-sold-as-prepared interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展（330） interchangeable。**  
   官方写：切到带投票扩展的 CometBFT 版本，**必须协调升级**。看见字段已经在参数表里，不是已经切完。看见必须协调升级，不是已经 only-veheight interchangeable——346 钉 bundled 三事，本页从 item 1 侧钉 not already only-veheight 单句。看见切到带扩展的 CometBFT，不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable——346 钉 bundled，本页钉 item 1 第一件事。看见字段已经在参数表里，不是已经到了 H 就已经 Prepare 带了扩展（330） interchangeable——330 另钉。346 abci20 vs height bundled unbundling 在本页 item 1 启动。

2. **看见一个节点升了二进制 / 看见单节点升了版本 / 看见本机已经换了带扩展的二进制 is not already 已经是单节点能切 interchangeable / 已经 single-node interchangeable / 已经单节点切完交差 interchangeable / 346 abci20upgrade bundled interchangeable / 58 enable-height interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 791 abci20-notonlyveheight interchangeable / 346 abci20 item 2 h_e interchangeable / 346 abci20 item 3 当前高度 interchangeable，也不是已经必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事 bundled（346 item 1 余量） interchangeable / 346 abci20 item 1 interchangeable，也不是已经只改 VoteExtensionsEnableHeight（本页第一件事） interchangeable。**  
   官方写：看见一个节点升了二进制，不是全网已经能走扩展。看见单节点升了版本，不是已经 single-node interchangeable——本页钉 not already single-node 单句。看见本机已经换了带扩展的二进制，不是已经只改 VoteExtensionsEnableHeight（本页第一件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 1 启动。

3. **看见能改启用高度 / 看见字段填了 / 看见 VoteExtensionsEnableHeight 可写 is not already 已经做了这次升级 interchangeable / 已经 field-filled interchangeable / 已经 field-filled 交差 interchangeable / 346 abci20upgrade bundled interchangeable / 792 abci20-notwritecurrent interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 791 abci20-notonlyveheight interchangeable / 346 abci20 item 2 / 346 abci20 item 3，也不是已经必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事 bundled（346 item 1 余量） interchangeable / 346 abci20 item 1 interchangeable，也不是已经只改 VoteExtensionsEnableHeight（本页第一件事） interchangeable / 已经是单节点能切（本页第二件事） interchangeable。**  
   官方写：看见能改启用高度，不是已经做了这次升级。看见字段填了，不是已经 field-filled interchangeable——本页钉 not already field-filled 单句。看见 `VoteExtensionsEnableHeight` 可写，不是已经是单节点能切（本页第二件事） interchangeable——三件事分开钉。346 abci20 vs height bundled unbundling 在本页 item 1 启动。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。ABCI 2.0 协调升级 bundled（346）、h_e 必须高于当前不是已经能写成当前高度（346 item 2 余量 / 792）、引擎按当前高度决定存什么要什么不是已经按创世配好了（346 item 3 余量 / 793）、到了 H 就已经 Prepare 带了扩展（330）、治理改 enable-height 会 panic（58）是另外那套，本页不抄。

## 官方为什么这样拆

- **必须协调升级 not already only-veheight ≠ 346 / 330 interchangeable：** 官方把换二进制的协调升级和只改启用高度分开。
- **一个节点升了二进制 not already single-node ≠ 已经是单节点能切 interchangeable：** 官方把协调升级和已经是单节点能切分开。
- **能改启用高度 not already field-filled ≠ 已经做了这次升级 interchangeable：** 官方把能改启用高度和已经做了这次升级分开；346 abci20 vs height bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须协调升级 | 不是 already only-veheight | 不是到了 H 就已经 Prepare 带了扩展 alone（330） |
| 一个节点升了二进制 | 不是 already single-node | 不是治理改 enable-height 会 panic alone（58） |
| 能改启用高度 | 不是 already field-filled | 不是 h_e 必须高于当前 alone（792） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级不是已经只改 VoteExtensionsEnableHeight not already only-veheight / not already single-node / not already field-filled 正式三事（346 余量），必须分开必须协调升级 是不是 already only-veheight interchangeable / 346 abci20upgrade bundled interchangeable / abci20upgrade-sold-as-height interchangeable、一个节点升了二进制 是不是 already single-node interchangeable、能改启用高度 是不是 already field-filled interchangeable。可以跳过「看见填了启用高度就已经切到 ABCI 2.0 interchangeable / 就已经单节点能切 interchangeable / 就已经做了这次升级 interchangeable」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 1 启动；续 [`worked-example-abci20-notwritecurrent-vs-bundled.md`](worked-example-abci20-notwritecurrent-vs-bundled.md)（不变量 792 item 2）；完成见 793。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- h_e 必须高于当前不是已经能写成当前高度。那是不变量 346 item 2 余量 / 792。
- 引擎按当前高度决定存什么要什么不是已经按创世配好了。那是不变量 346 item 3 余量 / 793。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 治理改 enable-height 会 panic。那是不变量 58。
