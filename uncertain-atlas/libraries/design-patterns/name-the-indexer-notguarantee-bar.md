# 模式：把索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**例**：[池子挡过一次 not already no-duplicate guarantee ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notguarantee-vs-bundled.md)。

## 三个名字

1. **池子挡过一次 不是 already no-duplicate guarantee：** 看见旧交易又被送来 / 内存池有去重机制，不是已经保证不会重复 interchangeable / 已经保证不重放 interchangeable，不是 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable。

2. **索引器在 不是 already strong guarantee：** 看见目前靠索引器 / best-effort indexer，不是已经有强保证 interchangeable / 已经索引器强保证 interchangeable，不是 313 mempool-indexer item 2 interchangeable / 699 indexer-notappprotect interchangeable。

3. **没报重复 不是 already never again：** 看见这次没挡成重复 / 没有 duplicate 报错，不是已经不会再来 interchangeable / 已经不会再送 interchangeable，不是 313 mempool-indexer item 3 interchangeable / 700 indexer-notnoidempotent interchangeable。

官方把池子挡过一次单句、already no-duplicate guarantee、already strong guarantee、already never again 写成三个名字。把它们叫成一个「看见池子挡过就已经保证不重放 interchangeable / 就已经有强保证 interchangeable / 就已经不会再来 interchangeable」，会把 not already no-duplicate guarantee、not already strong guarantee、not already never again 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量），先数清问的是池子挡过一次 是不是 already no-duplicate guarantee / 313 / indexer-sold-as-replay，是不是索引器在 是不是 already strong guarantee，还是没报重复 是不是 already never again，再决定要不要同一次发布。313 mempool-indexer vs replay bundled unbundling 在本页 item 1 完成。
