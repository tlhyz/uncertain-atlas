# 反模式：把 Finalize 回包 events not already must be deterministic / not already settled / not already same order as results 正式三事（382 余量） 说成已经必须确定 / 已经交差 / 已经是结果列表同一顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Finalize ≠ bundled（382）](../../tracks/implementation/worked-example-syncingheight-notdet-vs-bundled.md)。

## 卖法

把 Finalize 请求回包这句写成已经已经必须确定 / 已经交差 / 已经是结果列表同一顺序 interchangeable，或已经和 382 syncingheight-vs-history bundled / syncingheight-notdet-sold-as-bundled interchangeable。

## 为什么错

官方把 syncing_to_height / validator_updates 空 / Finalize events 三条核心句写成三件独立的实现事。把它们卖成已经必须确定 / 已经交差 / 已经是结果列表同一顺序，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 回包 events 正式三事（382 余量），必须分开 not already must be deterministic、not already settled、not already same order as results 三件事，不要和 382 / 342 / 782 / 783 糊成一句。

## 和相邻反模式

- [syncingheight-notnoset-sold-as-bundled](syncingheight-notnoset-sold-as-bundled.md) 是 validator_updates 空 单句边界（783 item 2），不是本页 events 边界。
- [querycode-notfresh-sold-as-bundled](querycode-notfresh-sold-as-bundled.md) 是 Query 回包 log 就已经新鲜（384/777），不是本页 Finalize events 边界。
