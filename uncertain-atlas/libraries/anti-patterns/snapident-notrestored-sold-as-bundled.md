# 反模式：把快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量）说成已经装完 / 已经交差 / 已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[对上了 not already restored ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notrestored-vs-bundled.md)。

## 卖法

把对上了 / 快照全字段（含 `Metadata`）对上才算同一份 / 同一份 写成已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable；把能拉 / 同一份才能从各节点拉 chunk / 对上了就能拉 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把 `Metadata` 在 / 全字段含 Metadata / Metadata 字段在 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable，或已经和 368 snapident bundled / snapshot-sold-as-identical interchangeable / 851 snapident-notrestored interchangeable。

## 为什么错

官方把对上了、不是已经交差、不是已经齐写成三件独立的实现事。把它们卖成 already restored interchangeable / already settled interchangeable / already complete interchangeable，会把 not already restored、not already settled、not already complete 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看快照全字段含 Metadata 对上不是已经装完 not already restored / not already settled / not already complete 正式三事（368 余量），必须分开 not already restored、not already settled、not already complete 三件事，不要和 368 / 321 / 852 / 853 糊成一句。

## 和相邻反模式

- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是 snapident bundled 全段，不是本页对上了 item 1 单句边界。
- [snapshotrestore-notrestored-sold-as-bundled](snapshotrestore-notrestored-sold-as-bundled.md) 是 Offer 收下 not already restored（321 余量 / 719），不是本页 not already restored 单句边界。
- [listsnapusage-sold-as-bundled](listsnapusage-sold-as-bundled.md) 是 ListSnapshots Usage bundled，不是本页 not already complete 边界。
