# 例：看见 CheckTx may come from an external user or another node is not already mempool dedup interchangeable / not already app replay protection interchangeable / not already CheckTx guard bundled interchangeable

**层次**：实现 / CheckTx Usage may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事（488 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事（488 余量）/ not 685 chktxsource-notreplay interchangeable / not 488 chktxsource-vs-recheck bundled interchangeable」，不是 CheckTx Usage tx source 正式三事 bundled（488），也不是 Replay Protection（313）或 CheckTx 守卫余量（405）。不要另写怎样挑邻居、怎样做索引器。

## 官方三件事

规范把 CheckTx Usage 里 The transaction may come from an external user or another node 和「已经内存池去重那种保证不重放（313） interchangeable / 已经过了 CheckTx 就有应用级重放保护（313） interchangeable / 已经 CheckTx 守卫余量（405） bundled 第二句 interchangeable」分开写成三件独立的实现事，不是「看见送来了 就已经 mempool dedup interchangeable / 就已经 app replay protection interchangeable / 就已经 CheckTx guard bundled interchangeable」一件事：

1. **看见 The transaction may come from an external user or another node / 看见送来了 / source is not already 已经内存池去重那种保证不重放（313） interchangeable / 313 replay interchangeable / 已经索引器滤过就保证不重放 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 685 chktxsource-notreplay interchangeable / 683 chktxsource-notrecheck interchangeable / 488 chktxsource item 1 external user interchangeable，也不是已经 may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事 bundled（488 item 3 余量） interchangeable / 488 chktxsource item 3 interchangeable。**  
   官方把 may come from external user or another node 和 mempool replay protection 分开写。App requirements Replay Protection 写：旧交易有可能再被送给应用；内存池去重只是尽力、不提供强保证。看见送来了，不是已经内存池去重就保证不重放 interchangeable。488 chktxsource vs recheck bundled unbundling 在本页 item 3 完成。

2. **看见 may come from an external user or another node / 能来自用户或邻居 / 看见送来了 is not already 已经过了 CheckTx 就有应用级重放保护（313） interchangeable / 313 app replay interchangeable / 已经应用自己写了谓词 interchangeable / 已经 CheckTx 过了就永远有效（301） interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 685 chktxsource-notreplay interchangeable / 488 chktxsource item 2 another node interchangeable / 684 chktxsource-notremoved interchangeable。**  
   官方把 Usage tx source 单句和应用级重放保护路径分开——488 bundled 第三件事常与 313 混成「看见送来了 就已经有应用级保护 interchangeable」，本页钉 not app replay protection 单句。看见能来自用户或邻居，不是已经过了 CheckTx 就有应用级保护 interchangeable——313 钉应用必须自己实现，本页钉 Usage 来源语义。

3. **看见 may come from an external user or another node / 看见 Usage 这句 / 看见送来了 is not already 已经 CheckTx 守卫余量（405） bundled 第二句 interchangeable / 405 checktxguard interchangeable / 已经 Guardian 就已经交差 interchangeable / 已经每条节点先跑 CheckTx 才进本地池 interchangeable，也不是已经 CheckTx Usage tx source 正式三事 bundled（488） interchangeable / 685 chktxsource-notreplay interchangeable / 683 chktxsource-notrecheck interchangeable。**  
   官方把 Usage tx source 单句和 CheckTx 守卫余量 bundled 路径分开——488 bundled 第三件事常与 405 混成「看见 Usage 这句 就已经守卫 bundled interchangeable」，本页钉 not CheckTx guard bundled 单句。看见送来了，不是已经 Guardian 就已经交差 interchangeable——405 钉守卫余量，本页钉 Usage item 3。488 chktxsource vs recheck bundled unbundling 在本页 item 3 完成。

怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage tx source 正式三事 bundled（488）、may come from an external user（488 item 1 余量 / 683）、may come from another node（488 item 2 余量 / 684）、Replay Protection（313）、CheckTx 守卫余量（405）是另外那套，本页不抄。

## 官方为什么这样拆

- **source not mempool dedup ≠ 313 去重就保证不重放 interchangeable：** 官方把 Methods Usage 来源和内存池去重强保证路径分开。
- **source not app replay protection ≠ 313 应用级保护 interchangeable：** 官方把 Usage 来源单句和过了 CheckTx 就有应用级保护路径分开。
- **source not CheckTx guard bundled ≠ 405 checktxguard interchangeable：** 官方把 Usage 来源单句和守卫余量 bundled 路径分开；488 chktxsource vs recheck bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| external user or another node | 不是内存池去重就保证不重放（313） | 不是 external user 单句（683/488 item 1） |
| 看见送来了 | 不是已经有应用级重放保护（313） | 不是 another node 单句（684/488 item 2） |
| Usage 这句 | 不是 CheckTx 守卫余量 bundled（405） | 不是 CheckTx Usage Code≠0（489） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage may come from external user or another node not mempool dedup / not app replay protection / not CheckTx guard bundled 正式三事（488 余量），必须分开送来了 是不是内存池去重就保证不重放 interchangeable / 313、是不是已经有应用级保护 interchangeable / 313、是不是守卫 bundled interchangeable / 405。可以跳过「看见送来了就已经保证不重放」。不要另写怎样写重放谓词。488 chktxsource vs recheck bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做索引器、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage tx source 正式三事 bundled。那是不变量 488。
- may come from an external user。那是不变量 488 item 1 余量 / 683。
- may come from another node。那是不变量 488 item 2 余量 / 684。
- 内存池去重 / 应用级重放保护。那是不变量 313。
- CheckTx 是内存池守卫。那是不变量 405。
