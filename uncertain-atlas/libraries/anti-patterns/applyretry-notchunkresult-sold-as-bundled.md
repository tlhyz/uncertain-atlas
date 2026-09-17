# 反模式：把 ApplySnapshotChunk Result REJECT_SNAPSHOT not this-chunk result / not rejected senders / not Offer REJECT_FORMAT 正式三事（398 余量） 说成已经是装这块的结果 / 已经拒了人 / 已经 Offer REJECT_FORMAT

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[REJECT_SNAPSHOT ≠ bundled（398）](../../tracks/implementation/worked-example-applyretry-notchunkresult-vs-bundled.md)。

## 卖法

把 ApplySnapshotChunk Result 这句写成已经已经是装这块的结果 / 已经拒了人 / 已经 Offer REJECT_FORMAT interchangeable，或已经和 398 applyretry-vs-refetch bundled / applyretry-notchunkresult-sold-as-bundled interchangeable。

## 为什么错

官方把 ApplySnapshotChunk Result 三条核心句写成三件独立的实现事。把它们卖成已经是装这块的结果 / 已经拒了人 / 已经 Offer REJECT_FORMAT，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result REJECT_SNAPSHOT 正式三事（398 余量），必须分开 not this-chunk result、not rejected senders、not Offer REJECT_FORMAT 三件事，不要和 398 / 397 / 378 / 400 / 719 / 720 糊成一句。

## 和相邻反模式

- [applyretry 父页 bundled](../../tracks/implementation/worked-example-applyretry-vs-refetch.md) 是 ApplySnapshotChunk 结果枚举 bundled（398），不是本页 item 3 单句边界。
- [applyretry-notswitch-sold-as-bundled](applyretry-notswitch-sold-as-bundled.md) 是 RETRY_SNAPSHOT 单句边界（720 item 2），不是本页 REJECT_SNAPSHOT 边界。
