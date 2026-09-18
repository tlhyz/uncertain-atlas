# 反模式：把过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量）说成已经有应用级保护 / 已经是应用谓词 / 已经交给应用

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[过了 CheckTx not already app-level protection ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notappprotect-vs-bundled.md)。

## 卖法

把过了 CheckTx / 没报错进了池 / CheckTx 绿了 写成已经有应用自己写的、带强保证的重放保护 interchangeable / 已经 app-level protection interchangeable / 已经应用级强保证 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable；把索引器滤过 / 引擎索引器挡过 / best-effort indexer filtered 写成已经是应用谓词 interchangeable / 已经 app predicate interchangeable；把引擎会挡 / 内存池会挡重复 写成已经把保证交给了应用 interchangeable / 已经 handed to app interchangeable，或已经和 313 mempool-indexer bundled / indexer-sold-as-replay interchangeable / 699 indexer-notappprotect interchangeable。

## 为什么错

官方把过了 CheckTx 单句、already app-level protection、already app predicate、already handed to app 写成三件独立的实现事。把它们卖成 already app-level protection interchangeable / already app predicate interchangeable / already handed to app interchangeable，会把 not already app-level protection、not already app predicate、not already handed to app 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量），必须分开 not already app-level protection、not already app predicate、not already handed to app 三件事，不要和 313 / 312 / 698 / 700 / 301 / 33 糊成一句。

## 和相邻反模式

- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是 Replay Protection bundled 全段，不是本页过了 CheckTx item 2 单句边界。
- [indexer-notguarantee-sold-as-bundled](indexer-notguarantee-sold-as-bundled.md) 是池子挡过一次 item 1，不是本页应用级保护边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState（312），不是本页应用谓词边界。
