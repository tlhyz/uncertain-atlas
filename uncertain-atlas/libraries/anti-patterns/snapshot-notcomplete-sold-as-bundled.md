# 反模式：把 空快照至少 1 块 not already complete / not already consensus constant / not already restored 正式三事（368 余量） 卖成 已经齐 / 已经是共识常数 / 已经装完

**层次**：实现 / Snapshot 类型。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-notcomplete-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-notcomplete-vs-bundled.md)。

官方把快照全字段对上 / 引擎不解释 format hash / 空快照也至少 1 块三条核心句写成三件独立的实现事。把它们卖成已经齐 / 已经是共识常数 / 已经装完，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空快照至少 1 块 正式三事（368 余量），必须分开 not already complete、not already consensus constant、not already restored 三件事，不要和 368 / 322 / 375 / 802 / 321 / 821 / 822 糊成一句。

## 和相邻反模式

- [snapshot-nothash-sold-as-bundled](snapshot-nothash-sold-as-bundled.md) 是不解释 format/hash 单句边界（822 item 2），不是本页至少 1 块边界。
- [loadchunk-not4mb-sold-as-bundled](loadchunk-not4mb-sold-as-bundled.md) 是 LoadSnapshot 16 MB 就已经是 4 MB 快照报文（375/802），不是本页至少 1 块边界。
