# 反模式：把引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量）说成已经轻验 AppHash / 已经选型 / 已经从创世重放

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有哈希 not already apphash-light ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notapphash-vs-bundled.md)。

## 卖法

把有哈希 / `hash` 是任意快照哈希、只在各节点同一份时相等、引擎不解释哈希只比较 / 有 hash 字段 写成已经轻验 AppHash interchangeable / 已经 apphash-light interchangeable / 已经轻验 AppHash 交差 interchangeable / 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable；把有 format / `format` 是应用自己的快照格式、用来给数据格式做版本 / 有 format 字段 写成已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable；把比过了 / 引擎只比较 hash、比过了同一份 / 比较过 写成已经从创世重放 interchangeable / 已经 genesis-replay interchangeable / 已经从创世重放交差 interchangeable，或已经和 368 snapident bundled / snapshot-sold-as-identical interchangeable / 852 snapident-notapphash interchangeable。

## 为什么错

官方把有哈希、不是已经选型、不是已经从创世重放写成三件独立的实现事。把它们卖成 already apphash-light interchangeable / already algo interchangeable / already genesis-replay interchangeable，会把 not already apphash-light、not already algo、not already genesis-replay 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量），必须分开 not already apphash-light、not already algo、not already genesis-replay 三件事，不要和 368 / 322 / 851 / 853 糊成一句。

## 和相邻反模式

- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是 snapident bundled 全段，不是本页有哈希 item 2 单句边界。
- [snapident-notrestored-sold-as-bundled](snapident-notrestored-sold-as-bundled.md) 是快照全字段含 Metadata 对上 not already restored（368 item 1），不是本页 not already apphash-light 边界。
- [statesync-sold-as-genesis](statesync-sold-as-genesis.md) 是应用快照就已经从创世重放（38），不是本页 not already genesis-replay 单句。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐（322），不是本页 not already algo 边界。
