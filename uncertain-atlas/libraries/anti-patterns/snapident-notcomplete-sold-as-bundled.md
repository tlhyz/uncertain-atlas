# 反模式：把空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量）说成已经齐 / 已经是共识常数 / 已经装完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写成 1 not already complete ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notcomplete-vs-bundled.md)。

## 卖法

把写成 1 / `chunks` 至少是 1、哪怕是空快照 / 有块数 写成已经齐 interchangeable / 已经 complete interchangeable / 已经齐交差 interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable；把有上限 / 网上一份快照报文最多 4 MB / 有 4 MB 上限 写成已经是共识常数 interchangeable / 已经 consensus-const interchangeable / 已经是共识常数交差 interchangeable；把能发 / 能发这份快照报文 / 报文能上网上 写成已经装完 interchangeable / 已经 restored interchangeable / 已经装完交差 interchangeable，或已经和 368 snapident bundled / snapshot-sold-as-identical interchangeable / 853 snapident-notcomplete interchangeable。

## 为什么错

官方把写成 1、不是已经是共识常数、不是已经装完写成三件独立的实现事。把它们卖成 already complete interchangeable / already consensus-const interchangeable / already restored interchangeable，会把 not already complete、not already consensus-const、not already restored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空快照也至少 1 块不是已经齐 not already complete / not already consensus-const / not already restored 正式三事（368 余量），必须分开 not already complete、not already consensus-const、not already restored 三件事，不要和 368 / 322 / 851 / 852 糊成一句。

## 和相邻反模式

- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是 snapident bundled 全段，不是本页写成 1 item 3 单句边界。
- [snapident-notrestored-sold-as-bundled](snapident-notrestored-sold-as-bundled.md) 是快照全字段含 Metadata 对上 not already restored（368 item 1），不是本页 not already complete 边界。
- [snapident-notapphash-sold-as-bundled](snapident-notapphash-sold-as-bundled.md) 是引擎不解释 format / hash not already apphash-light（368 item 2），不是本页 not already consensus-const 边界。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐（322），不是本页 not already restored 单句。
