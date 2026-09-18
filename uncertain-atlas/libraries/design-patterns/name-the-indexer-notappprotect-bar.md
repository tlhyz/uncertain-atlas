# 模式：把过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**例**：[过了 CheckTx not already app-level protection ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notappprotect-vs-bundled.md)。

## 三个名字

1. **过了 CheckTx 不是 already app-level protection：** 看见没报错进了池 / CheckTx 绿了，不是已经有应用自己写的、带强保证的重放保护 interchangeable / 已经应用级强保证 interchangeable，不是 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable。

2. **索引器滤过 不是 already app predicate：** 看见引擎索引器挡过 / best-effort indexer filtered，不是已经是应用谓词 interchangeable / 已经写进 CheckTx 的应用谓词 interchangeable，不是 313 mempool-indexer item 1 interchangeable / 698 indexer-notguarantee interchangeable。

3. **引擎会挡 不是 already handed to app：** 看见内存池会挡重复 / CometBFT 挡过，不是已经把保证交给了应用 interchangeable / 已经应用接过保证 interchangeable，不是 313 mempool-indexer item 3 interchangeable / 700 indexer-notnoidempotent interchangeable。

官方把过了 CheckTx 单句、already app-level protection、already app predicate、already handed to app 写成三个名字。把它们叫成一个「看见过了就已经有应用级保护 interchangeable / 就已经是应用谓词 interchangeable / 就已经交给应用 interchangeable」，会把 not already app-level protection、not already app predicate、not already handed to app 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看过了 CheckTx 不是已经有应用级保护 not already app-level protection / not already app predicate / not already handed to app 正式三事（313 余量），先数清问的是过了 CheckTx 是不是 already app-level protection / 313 / indexer-sold-as-replay，是不是索引器滤过 是不是 already app predicate，还是引擎会挡 是不是 already handed to app，再决定要不要同一次发布。313 mempool-indexer vs replay bundled unbundling 在本页 item 2 完成。
