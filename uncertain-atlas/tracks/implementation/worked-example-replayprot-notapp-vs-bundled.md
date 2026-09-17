# 例：看见过了 CheckTx is not already app-guard interchangeable / not already app-predicate interchangeable / not already settled interchangeable

**层次**：实现 / 过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量）/ not 966 replayprot-notapp interchangeable / not 313 mempool-indexer-vs-replay bundled interchangeable」，不是重放 bundled（313），也不是提案收了已经从池里删掉（301），也不是 CheckTx 最终不再振荡（328）。不要另写怎样实现重放保护或怎样做索引器。

## 官方三件事

1. **看见过了 CheckTx / 看见索引器滤过 这份滤过 is not already 已经有应用自己写的、带强保证的重放保护 interchangeable，也不是已经重放 bundled（313） interchangeable / 966 replayprot-notapp interchangeable / 965 replayprot-notguar interchangeable / 313 replayprot item 1 内存池去重 interchangeable，也不是已经过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事 bundled（313 item 2 余量） interchangeable / 313 replayprot item 2 interchangeable。**  
   官方写：因此要由应用自己实现一套应用特有的重放保护，而且必须带强保证，写进 CheckTx 的逻辑。看见过了 CheckTx，不是已经有这套保护 interchangeable——本页从 313 item 2 侧钉 not already app-guard 单句。313 replayprot vs replay bundled unbundling 在本页 item 2 续。

2. **看见索引器滤过 / 看见过了 CheckTx / 这份滤过 is not already 已经是应用谓词 interchangeable，也不是已经重放 bundled（313） interchangeable / 966 replayprot-notapp interchangeable / 313 replayprot item 3 通常不受欢迎 interchangeable / 967 replayprot-notidem interchangeable，也不是已经提案收了已经从池里删掉 interchangeable / 301 pool-delete interchangeable。**  
   官方把索引器滤过和已经是应用谓词分开。看见索引器滤过，不是已经是应用谓词 interchangeable。本页钉 not already app-predicate 单句。

3. **看见引擎会挡 / 看见过了 CheckTx / 这份滤过 is not already 已经交差 interchangeable，也不是已经重放 bundled（313） interchangeable / 966 replayprot-notapp interchangeable / 965 replayprot-notguar interchangeable，也不是已经 CheckTx 最终不再振荡 interchangeable / 328 checktx-oscillate interchangeable。**  
   官方把引擎会挡和已经把保证交给了应用分开。看见引擎会挡，不是已经交差 interchangeable。313 replayprot vs replay bundled unbundling 在本页 item 2 续。

怎样实现重放保护、怎样做索引器、nonce 公式是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **过了 CheckTx not already app-guard ≠ 已经有应用级保护 interchangeable：** 官方把引擎索引器和必须写进 CheckTx 的应用谓词分开。
- **看见索引器滤过 not already app-predicate ≠ 已经是应用谓词 interchangeable：** 官方把索引器滤过和已经是应用谓词分开。
- **看见引擎会挡 not already settled ≠ 已经交差 interchangeable：** 官方把引擎会挡和已经把保证交给应用分开；313 replayprot vs replay bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 过了 CheckTx | 不是已经有应用级保护 | 不是提案收了已经从池里删掉（301） |
| 看见索引器滤过 | 不是已经是应用谓词 | 不是 CheckTx 最终不再振荡（328） |
| 看见引擎会挡 | 不是已经交差 | 不是通常不受欢迎就已经没有幂等例外（967） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx not already app-guard / not already app-predicate / not already settled 正式三事（313 余量），必须分开是不是已经有应用级保护、是不是已经是应用谓词、是不是已经交差。可以跳过「看见池子挡过就已经保证不重放」。不要另写怎样实现重放保护或怎样做索引器。313 replayprot vs replay bundled unbundling 在本页 item 2 续；续 [`worked-example-replayprot-notidem-vs-bundled.md`](worked-example-replayprot-notidem-vs-bundled.md)（不变量 967 item 3）。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式。
- 重放 bundled。那是不变量 313。
- 提案收了已经从池里删掉。那是不变量 301。
- CheckTx 最终不再振荡。那是不变量 328。
