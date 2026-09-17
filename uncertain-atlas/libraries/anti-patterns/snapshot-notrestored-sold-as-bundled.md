# 反模式：把 快照全字段对上 not already restored / not already complete / not already light-verified AppHash 正式三事（368 余量） 卖成 已经装完 / 已经齐 / 已经轻验 AppHash

**层次**：实现 / Snapshot 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-notrestored-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-notrestored-vs-bundled.md)。

官方把快照全字段对上 / 引擎不解释 format hash / 空快照也至少 1 块三条核心句写成三件独立的实现事。把它们卖成已经装完 / 已经齐 / 已经轻验 AppHash，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看快照全字段对上 正式三事（368 余量），必须分开 not already restored、not already complete、not already light-verified AppHash 三件事，不要和 368 / 321 / 322 / 375 / 801 / 822 / 823 糊成一句。

## 和相邻反模式

- [loadchunk-notsame-sold-as-bundled](loadchunk-notsame-sold-as-bundled.md) 是 LoadSnapshot 三列就已经是同一份（375/801），不是本页全字段对上边界。
- Offer 收下就已经装完是不变量 321，不是本页全字段对上边界。
