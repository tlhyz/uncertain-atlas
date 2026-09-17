# 例：看见必须协调升级 is not already only VoteExtensionsEnableHeight interchangeable / not already single-node interchangeable / not already settled interchangeable

**层次**：实现 / 必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量）/ not 875 abci20-upgrade-notfield interchangeable / not 346 abci20-upgrade-vs-height bundled interchangeable」，不是 ABCI 2.0 协调升级 bundled（346），也不是到了 H 就已经 Prepare 带了扩展（330），也不是治理改 enable-height 会 panic（58）。不要另写怎样做协调升级。

## 官方三件事

1. **看见必须协调升级 / 看见切到带扩展的 CometBFT 这份必须 is not already 已经只改 `VoteExtensionsEnableHeight` interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 875 abci20-upgrade-notfield interchangeable / 876 abci20-upgrade-notcurrent interchangeable / 346 abci20 item 2 h_e interchangeable，也不是已经必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事 bundled（346 item 1 余量） interchangeable / 346 abci20 item 1 interchangeable。**  
   官方写：切到带投票扩展的 CometBFT 版本，必须协调升级。看见字段已经在参数表里，不是已经切完 interchangeable——本页从 346 item 1 侧钉 not already only VoteExtensionsEnableHeight 单句。346 abci20 vs height bundled unbundling 在本页 item 1 启动。

2. **看见必须协调升级 / 看见一个节点升了二进制 / 这份必须 is not already 已经是单节点能切 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 875 abci20-upgrade-notfield interchangeable / 346 abci20 item 3 当前高度 interchangeable / 877 abci20-upgrade-notgenesis interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330 height-H interchangeable。**  
   官方把协调升级和已经是单节点能切分开——346 bundled 第一件事常与 330 混成「看见填了启用高度就已经只改字段或已经单节点切完 interchangeable」，本页钉 not already single-node 单句。

3. **看见必须协调升级 / 看见能改启用高度 / 这份必须 is not already 已经交差 interchangeable，也不是已经 ABCI 2.0 协调升级 bundled（346） interchangeable / 875 abci20-upgrade-notfield interchangeable / 876 abci20-upgrade-notcurrent interchangeable，也不是已经治理改 enable-height 会 panic interchangeable / 58 enable-height panic interchangeable。**  
   官方把能改启用高度和已经做了这次升级 / 已经交差分开。看见能改启用高度，不是已经做了这次升级 interchangeable。346 abci20 vs height bundled unbundling 在本页 item 1 启动。

怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值是规范里的做法，本页不抄。

## 官方为什么这样拆

- **必须协调升级 not already only VoteExtensionsEnableHeight ≠ 已经只改 VoteExtensionsEnableHeight interchangeable：** 官方把换二进制的协调升级和改启用高度分开。
- **看见一个节点升了二进制 not already single-node ≠ 已经是单节点能切 interchangeable：** 官方把协调升级和已经是单节点能切分开。
- **看见能改启用高度 not already settled ≠ 已经交差 interchangeable：** 官方把能改启用高度和已经交差分开；346 abci20 vs height bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必须协调升级 | 不是已经只改 VoteExtensionsEnableHeight | 不是到了 H 就已经 Prepare 带了扩展（330） |
| 看见一个节点升了二进制 | 不是已经是单节点能切 | 不是治理改 enable-height 会 panic（58） |
| 看见能改启用高度 | 不是已经交差 | 不是 h_e 必须高于当前（876） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须协调升级 not already only VoteExtensionsEnableHeight / not already single-node / not already settled 正式三事（346 余量），必须分开是不是已经只改 VoteExtensionsEnableHeight、是不是已经是单节点能切、是不是已经交差。可以跳过「看见填了启用高度就已经切到 ABCI 2.0」。不要另写怎样做协调升级。346 abci20 vs height bundled unbundling 在本页 item 1 启动；续 [`worked-example-abci20-upgrade-notcurrent-vs-bundled.md`](worked-example-abci20-upgrade-notcurrent-vs-bundled.md)（不变量 876 item 2）。

## 本页不抄

- 怎样做协调升级、怎样设 *h<sub>e</sub>*、默认取值。
- ABCI 2.0 协调升级 bundled。那是不变量 346。
- h_e 必须高于当前。那是不变量 346 item 2 余量 / 876。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- 治理改 enable-height 会 panic。那是不变量 58。
