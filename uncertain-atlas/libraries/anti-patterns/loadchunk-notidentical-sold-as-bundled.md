# 反模式：把请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量）说成已经是同一份 / 已经齐 / 已经选型

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了三列 not already identical ≠ bundled（375）](../../tracks/implementation/worked-example-loadchunk-notidentical-vs-bundled.md)。

## 卖法

把填了三列 / 请求用 height / format / chunk（从 0 起）认这块 / 填了 height·format·chunk 写成已经是同一份 interchangeable / 已经 identical interchangeable / 已经是同一份交差 interchangeable / 375 loadchunk bundled interchangeable / loadchunk-sold-as-retrieved interchangeable；把从 0 起 / 块下标从 0 起 / 从 0 起认块 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable；把有 format / 应用自己的 format / 填了 format 写成已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable，或已经和 375 loadchunk bundled / loadchunk-sold-as-retrieved interchangeable / 873 loadchunk-notidentical interchangeable。

## 为什么错

官方把填了三列、不是已经齐、不是已经选型写成三件独立的实现事。把它们卖成 already identical interchangeable / already complete interchangeable / already selected interchangeable，会把 not already identical、not already complete、not already selected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求用 height / format / chunk（从 0 起）认这块不是已经是同一份 not already identical / not already complete / not already selected 正式三事（375 余量），必须分开 not already identical、not already complete、not already selected 三件事，不要和 375 / 368 / 872 / 322 糊成一句。

## 和相邻反模式

- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 loadchunk bundled 全段，不是本页填了三列 item 2 单句边界。
- [loadchunk-notcomplete-sold-as-bundled](loadchunk-notcomplete-sold-as-bundled.md) 是在拉 not already complete（375 item 1），不是本页 not already identical 边界。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是全字段对上就已经装完（368），不是本页 not already identical 单句。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐（322），不是本页 not already complete 边界。
