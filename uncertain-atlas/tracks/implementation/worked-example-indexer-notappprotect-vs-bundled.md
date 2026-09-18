# 例：看见过了 CheckTx / 索引器滤过 / 引擎会挡 is not already already app-level protection interchangeable / already app predicate interchangeable / already handed to app interchangeable

**层次**：实现 / 过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量）/ not 699 indexer-notappprotect interchangeable / not 313 mempool-indexer bundled interchangeable」，不是 Replay Protection bundled（313），也不是索引器去重不是已经保证不重复（698 item 1 余量）或通常不受欢迎不是已经没有幂等例外（700 item 3 余量）。不要另写怎样实现重放保护或怎样做索引器。

## 官方三件事

规范把 Requirements 里因此要由应用自己实现一套**应用特有**的重放保护、而且必须带强保证、写进 `CheckTx` 的逻辑 和「已经是过了 CheckTx 就已经有应用级保护 interchangeable / 已经是索引器滤过就已经是应用谓词 interchangeable / 已经是引擎会挡就已经把保证交给了应用 interchangeable / 已经是 Replay Protection bundled interchangeable」分开写成三件独立的实现事，不是「看见过了 就已经有应用级保护 interchangeable / 就已经是应用谓词 interchangeable / 就已经交给应用 interchangeable」一件事：

1. **看见过了 CheckTx / 看见没报错进了池 / 看见 CheckTx 绿了 is not already 已经有应用自己写的、带强保证的重放保护 interchangeable / 已经 app-level protection interchangeable / 已经应用级强保证 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 699 indexer-notappprotect interchangeable / 313 mempool-indexer item 2 interchangeable，也不是已经过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事 bundled（313 item 2 余量） interchangeable / 313 mempool-indexer item 2 interchangeable，也不是已经索引器去重不是已经保证不重复（698） interchangeable / 700 indexer-notnoidempotent interchangeable / 301 proposed-removed interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：因此要由应用自己实现一套**应用特有**的重放保护，而且必须带强保证，写进 `CheckTx` 的逻辑。看见过了 CheckTx，不是已经有这套保护 interchangeable——313 钉 bundled 三事，本页从 item 2 侧钉 not already app-level protection 单句。看见没报错进了池，不是已经 Replay Protection bundled（313） interchangeable——313 钉 bundled，本页钉 item 2 第一件事。看见 CheckTx 绿了，不是已经索引器去重不是已经保证不重复（698） interchangeable——698 另钉 item 1，本页钉 item 2 第一件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 2 续。

2. **看见索引器滤过 / 看见引擎索引器挡过 / 看见 best-effort indexer filtered is not already 已经是应用谓词 interchangeable / 已经 app predicate interchangeable / 已经写进 CheckTx 的应用谓词 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 699 indexer-notappprotect interchangeable / 313 mempool-indexer item 1 保证不重复 interchangeable / 313 mempool-indexer item 3 幂等例外 interchangeable，也不是已经过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事 bundled（313 item 2 余量） interchangeable / 313 mempool-indexer item 2 interchangeable，也不是已经有应用级保护（本页第一件事） interchangeable。**  
   官方把引擎索引器滤过和必须写进 CheckTx 的应用谓词分开——索引器滤过，不等于已经是应用谓词。看见索引器滤过，不是已经是应用谓词 interchangeable——本页钉 not already app predicate 单句。看见引擎索引器挡过，不是已经索引器去重不是已经保证不重复（698） interchangeable——698 另钉 item 1 强保证侧，本页钉 item 2 应用谓词侧。看见 best-effort indexer filtered，不是已经通常不受欢迎不是已经没有幂等例外（700） interchangeable——700 另钉 item 3，本页钉 item 2 第二件事。313 mempool-indexer vs replay bundled unbundling 在本页 item 2 续。

3. **看见引擎会挡 / 看见内存池会挡重复 / 看见 CometBFT 挡过 is not already 已经把保证交给了应用 interchangeable / 已经 handed to app interchangeable / 已经应用接过保证 interchangeable / 313 mempool-indexer bundled interchangeable / 33 four gates interchangeable，也不是已经 Replay Protection bundled（313） interchangeable / 699 indexer-notappprotect interchangeable / 313 mempool-indexer item 1 / 313 mempool-indexer item 3，也不是已经过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事 bundled（313 item 2 余量） interchangeable / 313 mempool-indexer item 2 interchangeable，也不是已经有应用级保护（本页第一件事） interchangeable / 已经是应用谓词（本页第二件事） interchangeable。**  
   官方把引擎会挡和已经把保证交给了应用路径分开——引擎挡，不等于应用已经接过强保证。看见引擎会挡，不是已经把保证交给了应用 interchangeable——本页钉 not already handed to app 单句。看见内存池会挡重复，不是已经有应用级保护（本页第一件事） interchangeable——三件事分开钉。看见 CometBFT 挡过，不是已经四门已经结算（33） interchangeable——33 另钉。313 mempool-indexer vs replay bundled unbundling 在本页 item 2 完成。

怎样实现重放保护、怎样做索引器、nonce 公式是规范里的取值或做法，本页不抄。Replay Protection bundled（313）、索引器去重不是已经保证不重复（313 item 1 余量 / 698）、通常不受欢迎不是已经没有幂等例外（313 item 3 余量 / 700）、CheckTxState vs ExecuteTxState（312）、提案收了已经从池里删掉（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **过了 CheckTx not already app-level protection ≠ 313 / 312 interchangeable：** 官方把过了单句和已经有应用级保护路径分开。
- **索引器滤过 not already app predicate ≠ 已经是应用谓词 interchangeable：** 官方把引擎索引器滤过单句和已经写进 CheckTx 的应用谓词路径分开。
- **引擎会挡 not already handed to app ≠ 已经把保证交给了应用 interchangeable：** 官方把引擎挡单句和已经应用接过保证路径分开；313 mempool-indexer vs replay bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 过了 CheckTx | 不是 already app-level protection | 不是保证不重复 alone（698） |
| 索引器滤过 | 不是 already app predicate | 不是幂等例外 alone（700） |
| 引擎会挡 | 不是 already handed to app | 不是 CheckTxState alone（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量），必须分开过了 CheckTx 是不是 already app-level protection interchangeable / 313 mempool-indexer bundled interchangeable / indexer-sold-as-replay interchangeable、索引器滤过 是不是 already app predicate interchangeable、引擎会挡 是不是 already handed to app interchangeable。可以跳过「看见过了就已经有应用级保护 interchangeable / 就已经是应用谓词 interchangeable / 就已经交给应用 interchangeable」。不要另写怎样做索引器。313 mempool-indexer vs replay bundled unbundling 在本页 item 2 完成；续 [`worked-example-indexer-notnoidempotent-vs-bundled.md`](worked-example-indexer-notnoidempotent-vs-bundled.md)（不变量 700 item 3，待写）。

## 本页不抄

- 怎样实现重放保护、怎样做索引器、nonce 公式。
- Replay Protection bundled。那是不变量 313。
- 索引器去重不是已经保证不重复。那是不变量 313 item 1 余量 / 698。
- 通常不受欢迎不是已经没有幂等例外。那是不变量 313 item 3 余量 / 700。
- CheckTxState vs ExecuteTxState。那是不变量 312。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
