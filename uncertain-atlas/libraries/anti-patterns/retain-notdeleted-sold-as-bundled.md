# 反模式：把低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量）说成已经删完 / 已经是快照截断 / 已经没有历史

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[能删 not already deleted ≠ bundled（366）](../../tracks/implementation/worked-example-retain-notdeleted-vs-bundled.md)。

## 卖法

把能删 / 低于这个高度的块可以被删 / 回了高度可删 写成已经删完 interchangeable / 已经 deleted interchangeable / 已经删完交差 interchangeable / 366 retain bundled interchangeable / retain-sold-as-kept interchangeable；把回了高度 / 回了高度可删 / 能删 写成已经是这个节点快照截断 interchangeable / 已经 snapshot-trunc interchangeable / 已经快照截断交差 interchangeable；把能剪 / 能删就等于能剪 / 低于这个高度可剪 写成已经没有历史 interchangeable / 已经 no-history interchangeable / 已经没有历史交差 interchangeable，或已经和 366 retain bundled / retain-sold-as-kept interchangeable / 846 retain-notdeleted interchangeable。

## 为什么错

官方把能删、不是已经是快照截断、不是已经没有历史写成三件独立的实现事。把它们卖成 already deleted interchangeable / already snapshot-trunc interchangeable / already no-history interchangeable，会把 not already deleted、not already snapshot-trunc、not already no-history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看低于这个高度的块可以被删不是已经没有历史 not already deleted / not already snapshot-trunc / not already no-history 正式三事（366 余量），必须分开 not already deleted、not already snapshot-trunc、not already no-history 三件事，不要和 366 / 323 / 845 / 847 糊成一句。

## 和相邻反模式

- [retain-sold-as-kept](retain-sold-as-kept.md) 是 retain bundled 全段，不是本页能删 item 2 单句边界。
- [retain-notpruning-sold-as-bundled](retain-notpruning-sold-as-bundled.md) 是 retain_height 默认 0 not already pruning（366 item 1），不是本页 not already deleted 边界。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识就已经有完整历史（323），不是本页 not already snapshot-trunc 单句。
