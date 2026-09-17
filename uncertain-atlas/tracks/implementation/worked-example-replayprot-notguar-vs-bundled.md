# 例：看见内存池会挡重复 is not already guaranteed interchangeable / not already strong interchangeable / not already settled interchangeable

**层次**：实现 / 内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量）/ not 965 replayprot-notguar interchangeable / not 313 mempool-indexer-vs-replay bundled interchangeable」，不是重放 bundled（313），也不是 CheckTxState 已经是 ExecuteTxState（312），也不是 CheckTx 弱过滤已经是 Process（339）。不要另写怎样实现重放保护或怎样做索引器。

## 官方三件事

1. **看见旧交易又被送来 / 看见内存池有去重机制 这份机制 is not already 已经保证不会重复 interchangeable，也不是已经重放 bundled（313） interchangeable / 965 replayprot-notguar interchangeable / 966 replayprot-notapp interchangeable / 313 replayprot item 2 过了 CheckTx interchangeable，也不是已经内存池去重 not already guaranteed / not already strong / not already settled 正式三事 bundled（313 item 1 余量） interchangeable / 313 replayprot item 1 interchangeable。**  
   官方写：旧交易有可能再被送给应用。内存池有一套机制，用来挡住已经处理过的重复交易。官方还写：这套机制只是尽力（目前靠索引器），不提供任何不重复保证。看见池子挡过一次，不是已经保证 interchangeable——本页从 313 item 1 侧钉 not already guaranteed 单句。313 replayprot vs replay bundled unbundling 在本页 item 1 启动。

2. **看见索引器在 / 看见池子挡过 / 这份机制 is not already 已经有强保证 interchangeable，也不是已经重放 bundled（313） interchangeable / 965 replayprot-notguar interchangeable / 313 replayprot item 3 通常不受欢迎 interchangeable / 967 replayprot-notidem interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把索引器在和已经有强保证分开——313 bundled 第一件事常与 312 混成「看见池子挡过就已经保证或不已经是工作状态 interchangeable」，本页钉 not already strong 单句。

3. **看见没报重复 / 看见池子挡过 / 这份机制 is not already 已经交差 interchangeable，也不是已经重放 bundled（313） interchangeable / 965 replayprot-notguar interchangeable / 966 replayprot-notapp interchangeable，也不是已经 CheckTx 弱过滤已经是 Process interchangeable / 339 checktx-weak interchangeable。**  
   官方把没报重复和已经不会再来分开。看见没报重复，不是已经交差 interchangeable。313 replayprot vs replay bundled unbundling 在本页 item 1 启动。

怎样实现重放保护、怎样做索引器、nonce 公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **内存池去重 not already guaranteed ≠ 已经保证不重复 interchangeable：** 官方把尽力挡重复和任何保证分开。
- **看见索引器在 not already strong ≠ 已经有强保证 interchangeable：** 官方把索引器在和已经有强保证分开。
- **看见没报重复 not already settled ≠ 已经交差 interchangeable：** 官方把没报重复和已经不会再来分开；313 replayprot vs replay bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 内存池去重 | 不是已经保证不重复 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见索引器在 | 不是已经有强保证 | 不是 CheckTx 弱过滤已经是 Process（339） |
| 看见没报重复 | 不是已经交差 | 不是过了 CheckTx 就已经有应用级保护（966） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看内存池去重 not already guaranteed / not already strong / not already settled 正式三事（313 余量），必须分开是不是已经保证、是不是已经有强保证、是不是已经交差。可以跳过「看见池子挡过就已经保证不重放」。不要另写怎样实现重放保护或怎样做索引器。313 replayprot vs replay bundled unbundling 在本页 item 1 启动；续 [`worked-example-replayprot-notapp-vs-bundled.md`](worked-example-replayprot-notapp-vs-bundled.md)（不变量 966 item 2）。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式。
- 重放 bundled。那是不变量 313。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- CheckTx 弱过滤已经是 Process。那是不变量 339。
