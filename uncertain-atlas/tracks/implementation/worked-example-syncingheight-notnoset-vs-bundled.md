# 例：看见 validator_updates 空则引擎保持当前集合 is not already no set interchangeable / not already changed set interchangeable / not already InitChain empty list interchangeable

**层次**：实现 / validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事（382 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事（382 余量）/ not 783 syncingheight-notnoset interchangeable / not 382 syncingheight-vs-history bundled interchangeable」，不是 Finalize 请求回包 bundled（382），也不是 InitChain 空名单就已经没有集合（318），也不是 InitChain 请求 validators 就已经没有集合（388/765）。不要另写怎样写 Finalize 请求回包。

## 官方三件事

1. **看见 `validator_updates` 空则引擎保持当前集合 / 看见空着 / Finalize 这份空更新 is not already 已经没有集合 interchangeable / 318 emptyset interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 783 syncingheight-notnoset interchangeable / 782 syncingheight-nothistory interchangeable / 382 syncingheight item 1 syncing_to_height interchangeable，也不是已经 validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事 bundled（382 item 2 余量） interchangeable / 382 syncingheight item 2 interchangeable。**  
   官方写：`validator_updates` 或 `consensus_param_updates` 可以空。空着时，CometBFT 保持当前值。看见空着，不是已经没有集合 interchangeable——本页从 382 item 2 侧钉 not already no set 单句。382 syncingheight vs history bundled unbundling 在本页 item 2 续。

2. **看见空着 / 看见没回人 / Finalize 这份空更新 is not already 已经改了集合 interchangeable / 318 emptyset interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 783 syncingheight-notnoset interchangeable / 382 syncingheight item 3 events interchangeable / 784 syncingheight-notdet interchangeable。**  
   官方把没回人和已经改了集合分开——382 bundled 第二件事常与 318 混成「看见空着就已经没有集合或已经改了集合 interchangeable」，本页钉 not already changed set 单句。

3. **看见空着 / 看见能空 / Finalize 这份空更新 is not already 已经是 InitChain 那种空名单 interchangeable / 318 emptyset interchangeable，也不是已经 Finalize 请求回包 bundled（382） interchangeable / 783 syncingheight-notnoset interchangeable / 782 syncingheight-nothistory interchangeable，也不是已经 InitChain 请求 validators 就已经没有集合 interchangeable / 388 initparams / 765 initparams-notnoset interchangeable。**  
   官方把能空和已经是 InitChain 那种空名单分开。看见能空，不是已经是 InitChain 那种空名单 interchangeable。382 syncingheight vs history bundled unbundling 在本页 item 2 续。

怎样写 Finalize 请求、怎样空着更新、怎样编事件是规范里的做法，本页不抄。

## 官方为什么这样拆

- **validator_updates 空 not already no set ≠ 318 interchangeable：** 官方把 Finalize 空更新和已经没有集合分开。
- **validator_updates 空 not already changed set ≠ 318 interchangeable：** 官方把没回人和已经改了集合分开。
- **validator_updates 空 not already InitChain empty list ≠ 318 interchangeable：** 官方把能空和 InitChain 空名单分开；382 syncingheight vs history bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| validator_updates 空则引擎保持当前集合 | 不是已经没有集合（318） | 不是 syncing_to_height（782/382 item 1） |
| 看见空着 | 不是已经改了集合 | 不是 Finalize 请求回包 bundled（382） |
| 看见能空 | 不是已经是 InitChain 那种空名单（318） | 不是 InitChain 请求 validators（388/765） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 空 not already no set / not already changed set / not already InitChain empty list 正式三事（382 余量），必须分开空着是不是已经没有集合 interchangeable / 318、是不是已经改了集合、是不是已经是 InitChain 那种空名单。可以跳过「看见空着就已经没有集合」。不要另写怎样写 Finalize 请求回包。382 syncingheight vs history bundled unbundling 在本页 item 2 续；完成 [`worked-example-syncingheight-notdet-vs-bundled.md`](worked-example-syncingheight-notdet-vs-bundled.md)（不变量 784 item 3）。

## 本页不抄

- 怎样写 Finalize 请求、怎样空着更新、怎样编事件。
- Finalize 请求回包 bundled。那是不变量 382。
- syncing_to_height。那是不变量 382 item 1 余量 / 782。
- Finalize 回包 events。那是不变量 382 item 3 余量 / 784。
- InitChain 空名单就已经没有集合。那是不变量 318。
- InitChain 请求 validators 就已经没有集合。那是不变量 388 / 765。
