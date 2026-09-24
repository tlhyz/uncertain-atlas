# 模式：把引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot。  
**例**：[有哈希 not already apphash-light ≠ bundled（368）](../../tracks/implementation/worked-example-snapident-notapphash-vs-bundled.md)。

## 三个名字

1. **有哈希 不是 already apphash-light：** 看见有哈希 / `hash` 是任意快照哈希、只在各节点同一份时相等、引擎不解释哈希只比较 / 有 hash 字段，不是已经轻验 AppHash interchangeable / 已经 apphash-light interchangeable / 已经轻验 AppHash 交差 interchangeable，不是 368 snapident bundled interchangeable / snapshot-sold-as-identical interchangeable。

2. **有 format 不是 already algo：** 看见有 format / `format` 是应用自己的快照格式、用来给数据格式做版本 / 有 format 字段，不是已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable，不是 321 offer interchangeable / 851 snapident-notrestored interchangeable。

3. **比过了 不是 already genesis-replay：** 看见比过了 / 引擎只比较 hash、比过了同一份 / 比较过，不是已经从创世重放 interchangeable / 已经 genesis-replay interchangeable / 已经从创世重放交差 interchangeable，不是 853 snapident-notcomplete interchangeable / 38 genesis-replay interchangeable。

官方把有哈希、不是已经选型、不是已经从创世重放写成三个名字。把它们叫成一个「看见有哈希就已经轻验 AppHash interchangeable / 就已经选型 interchangeable / 就已经从创世重放 interchangeable」，会把 not already apphash-light、not already algo、not already genesis-replay 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不解释 format / hash 不是已经轻验 AppHash not already apphash-light / not already algo / not already genesis-replay 正式三事（368 余量），先数清问的是有哈希 是不是 already apphash-light / 368 / snapshot-sold-as-identical，是不是有 format 是不是 already algo，还是比过了 是不是 already genesis-replay，再决定要不要同一次发布。368 snapshot-vs-identical bundled unbundling 在本页 item 2 续。
