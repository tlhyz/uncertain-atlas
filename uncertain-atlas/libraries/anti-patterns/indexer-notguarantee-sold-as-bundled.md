# 反模式：把索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量）说成已经保证不重复 / 已经有强保证 / 已经不会再来

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[池子挡过一次 not already no-duplicate guarantee ≠ bundled（313）](../../tracks/implementation/worked-example-indexer-notguarantee-vs-bundled.md)。

## 卖法

把旧交易又被送来 / 池子挡过一次 / 内存池有去重机制 写成已经保证不会重复 interchangeable / 已经 no-duplicate guarantee interchangeable / 已经保证不重放 interchangeable / 313 mempool-indexer bundled interchangeable / 312 checktxstate bundled interchangeable / indexer-sold-as-replay interchangeable；把索引器在 / 目前靠索引器 / best-effort indexer 写成已经有强保证 interchangeable / 已经 strong guarantee interchangeable；把没报重复 / 这次没挡成重复 写成已经不会再来 interchangeable / 已经 never again interchangeable，或已经和 313 mempool-indexer bundled / indexer-sold-as-replay interchangeable / 698 indexer-notguarantee interchangeable。

## 为什么错

官方把池子挡过一次单句、already no-duplicate guarantee、already strong guarantee、already never again 写成三件独立的实现事。把它们卖成 already no-duplicate guarantee interchangeable / already strong guarantee interchangeable / already never again interchangeable，会把 not already no-duplicate guarantee、not already strong guarantee、not already never again 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看索引器去重不是已经保证不重复 not already no-duplicate guarantee / not already strong guarantee / not already never again 正式三事（313 余量），必须分开 not already no-duplicate guarantee、not already strong guarantee、not already never again 三件事，不要和 313 / 312 / 699 / 700 / 301 / 33 糊成一句。

## 和相邻反模式

- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是 Replay Protection bundled 全段，不是本页池子挡过一次 item 1 单句边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState vs ExecuteTxState（312），不是本页索引器保证边界。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了 ≠ 已经从池里删掉（301），不是本页没报重复边界。
