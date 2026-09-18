# 例：看见旧交易又被送来 / 池子挡过一次 / 索引器在 is not already already no-duplicate guarantee interchangeable / already strong guarantee interchangeable / already never again interchangeable

**层次**：实现 / 索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量）/ not 698 indexer-notguarantee interchangeable / not 313 mempool-indexer bundled interchangeable」，不是 Replay Protection bundled（313），也不是过了 CheckTx 不是已经有应用级保护（699 item 2 余量）或通常不受欢迎不是已经没有幂等例外（700 item 3 余量）。不要另写怎样实现重放保护或怎样做索引器。

## 官方三件事

规范把 Requirements 里旧交易有可能再被送给应用、内存池有一套机制用来挡住已经处理过的重复交易、这套机制**只是尽力**（目前靠索引器）、**不提供任何不重复保证** 和「已经是池子挡过就已经保证不重复 interchangeable / 已经是索引器在就已经有强保证 interchangeable / 已经是没报重复就已经不会再来 interchangeable / 已经是 Replay Protection bundled interchangeable」分开写成三件独立的实现事，不是「看见旧交易又被送来 就已经保证不重复 interchangeable / 就已经有强保证 interchangeable / 就已经不会再来 interchangeable」一件事：

1. **看见旧交易又被送来 / 看见池子挡过一次 / 看见内存池有去重机制 is not already 已经保证不会重复 interchangeable / 已经 no-duplicate guarantee interchangeable / 已经保证不重放 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 698 indexer-notguarantee interchangeable / 313 mempool-indexer item 1 interchangeable，也不是已经索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事 bundled（313 item 1 余量） interchangeable / 313 mempool-indexer item 1 interchangeable，也不是已经过了 CheckTx 不是已经有应用级保护（699） interchangeable / 700 indexer-notnoidempotent interchangeable / 301 proposed-removed interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：旧交易有可能再被送给应用；内存池有一套机制挡住已经处理过的重复交易，但**不提供任何不重复保证**。看见池子挡过一次，不是已经保证 interchangeable——313 钉 bundled 三事，本页从 item 1 侧钉 not already no-duplicate guarantee 单句。看见旧交易又被送来，不是已经 Replay Protection bundled（313） interchangeable——313 钉 bundled，本页钉 item 1 第一件事。看见内存池有去重机制，不是已经过了 CheckTx 不是已经有应用级保护（699） interchangeable——699 另钉 item 2，本页钉 item 1 第一件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 1 启动。

2. **看见索引器在 / 看见目前靠索引器 / 看见 best-effort indexer is not already 已经有强保证 interchangeable / 已经 strong guarantee interchangeable / 已经索引器强保证 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 698 indexer-notguarantee interchangeable / 313 mempool-indexer item 2 应用级保护 interchangeable / 313 mempool-indexer item 3 幂等例外 interchangeable，也不是已经索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事 bundled（313 item 1 余量） interchangeable / 313 mempool-indexer item 1 interchangeable，也不是已经保证不会重复（本页第一件事） interchangeable。**  
   官方把这套机制**只是尽力**（目前靠索引器）和已经有强保证路径分开——索引器在，不等于已经有强保证。看见索引器在，不是已经有强保证 interchangeable——本页钉 not already strong guarantee 单句。看见目前靠索引器，不是已经过了 CheckTx 不是已经有应用级保护（699） interchangeable——699 另钉 item 2，本页钉 item 1 第二件事。看见 best-effort indexer，不是已经通常不受欢迎不是已经没有幂等例外（700） interchangeable——700 另钉 item 3，本页钉 item 1 第二件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 1 启动。

3. **看见没报重复 / 看见这次没挡成重复 / 看见没有 duplicate 报错 is not already 已经不会再来 interchangeable / 已经 never again interchangeable / 已经不会再送 interchangeable / 313 mempool-indexer bundled interchangeable / 33 four gates interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 698 indexer-notguarantee interchangeable / 313 mempool-indexer item 2 / 313 mempool-indexer item 3，也不是已经索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事 bundled（313 item 1 余量） interchangeable / 313 mempool-indexer item 1 interchangeable，也不是已经保证不会重复（本页第一件事） interchangeable / 已经有强保证（本页第二件事） interchangeable。**  
   官方把尽力挡重复和已经不会再来路径分开——这次没报重复，不等于旧交易不会再被送来。看见没报重复，不是已经不会再来 interchangeable——本页钉 not already never again 单句。看见这次没挡成重复，不是已经保证不会重复（本页第一件事） interchangeable——三件事分开钉。看见没有 duplicate 报错，不是已经四门已经结算（33） interchangeable——33 另钉。313 mempool-indexer vs replay bundled unbundling 在本页 item 1 完成。

怎样实现重放保护、怎样做索引器、nonce 公式是规范里的取值或做法，本页不抄。Replay Protection bundled（313）、过了 CheckTx 不是已经有应用级保护（313 item 2 余量 / 699）、通常不受欢迎不是已经没有幂等例外（313 item 3 余量 / 700）、CheckTxState vs ExecuteTxState（312）、提案收了已经从池里删掉（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **池子挡过一次 not already no-duplicate guarantee ≠ 313 / 312 interchangeable：** 官方把尽力挡重复单句和已经保证不重复路径分开。
- **索引器在 not already strong guarantee ≠ 已经有强保证 interchangeable：** 官方把 best-effort indexer 单句和已经有强保证路径分开。
- **没报重复 not already never again ≠ 已经不会再来 interchangeable：** 官方把这次没报重复单句和已经不会再送来路径分开；313 mempool-indexer vs replay bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 池子挡过一次 | 不是 already no-duplicate guarantee | 不是应用级保护 alone（699） |
| 索引器在 | 不是 already strong guarantee | 不是幂等例外 alone（700） |
| 没报重复 | 不是 already never again | 不是 CheckTxState alone（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量），必须分开池子挡过一次 是不是 already no-duplicate guarantee interchangeable / 313 mempool-indexer bundled interchangeable / indexer-sold-as-replay interchangeable、索引器在 是不是 already strong guarantee interchangeable、没报重复 是不是 already never again interchangeable。可以跳过「看见池子挡过就已经保证不重放 interchangeable / 就已经有强保证 interchangeable / 就已经不会再来 interchangeable」。不要另写怎样做索引器。313 mempool-indexer vs replay bundled unbundling 在本页 item 1 完成；续 [`worked-example-indexer-notappprotect-vs-bundled.md`](worked-example-indexer-notappprotect-vs-bundled.md)（不变量 699 item 2）。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式。
- Replay Protection bundled。那是不变量 313。
- 过了 CheckTx 不是已经有应用级保护。那是不变量 313 item 2 余量 / 699。
- 通常不受欢迎不是已经没有幂等例外。那是不变量 313 item 3 余量 / 700。
- CheckTxState vs ExecuteTxState。那是不变量 312。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
