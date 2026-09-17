# 反模式：把 引擎不解释 format/hash not already light-verified AppHash / not already genesis replay / not already selected 正式三事（368 余量） 卖成 已经轻验 AppHash / 已经从创世重放 / 已经选型

**层次**：实现 / Snapshot 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-nothash-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-nothash-vs-bundled.md)。

官方把快照全字段对上 / 引擎不解释 format hash / 空快照也至少 1 块三条核心句写成三件独立的实现事。把它们卖成已经轻验 AppHash / 已经从创世重放 / 已经选型，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看引擎不解释 format/hash 正式三事（368 余量），必须分开 not already light-verified AppHash、not already genesis replay、not already selected 三件事，不要和 368 / 325 / 38 / 321 / 821 / 823 糊成一句。

## 和相邻反模式

- [snapshot-notrestored-sold-as-bundled](snapshot-notrestored-sold-as-bundled.md) 是全字段对上单句边界（821 item 1），不是本页不解释 format/hash 边界。
- 应用快照就已经从创世重放是不变量 38，不是本页不解释 format/hash 边界。
