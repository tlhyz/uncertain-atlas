# 反模式：把 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量）说成已经齐 / 已经有了全部快照 / 已经装完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[在拉 not already complete ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-notcomplete-vs-bundled.md)。

## 卖法

把在拉 / LoadSnapshotChunk 用来从邻居拉快照块 / 在拉块 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable；把问了邻居 / 从邻居拉 / 问邻居 写成已经有了全部快照 interchangeable / 已经 all interchangeable / 已经有了全部快照交差 interchangeable；把能拉 / 能拉快照块 / 能拉块 写成已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，或已经和 375 loadchunk bundled / loadchunk-sold-as-retrieved interchangeable / 872 loadchunk-notcomplete interchangeable。

## 为什么错

官方把在拉、不是已经有了全部快照、不是已经装完写成三件独立的实现事。把它们卖成 already complete interchangeable / already all interchangeable / already restored interchangeable，会把 not already complete、not already all、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 余量），必须分开 not already complete、not already all、not already restored 三件事，不要和 375 / 322 / 321 / 368 糊成一句。

## 和相邻反模式

- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 loadchunk bundled 全段，不是本页在拉 item 1 单句边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐（322），不是本页 not already complete 单句。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是全字段对上就已经装完（368），不是本页 not already all 边界。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完（321），不是本页 not already restored 单句。
