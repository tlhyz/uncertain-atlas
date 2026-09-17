# 反模式：把 LoadSnapshotChunk not already complete / not already all snapshots / not already restored 正式三事（375 余量） 卖成 已经齐 / 已经有了全部快照 / 已经装完

**层次**：实现 / LoadSnapshotChunk。  
**分类**：建议（产品）。  
**对应例**：[worked-example-loadchunk-notcomplete-vs-bundled.md](../../tracks/implementation/worked-example-loadchunk-notcomplete-vs-bundled.md)。

官方把从邻居拉快照块 / 三列认块 / 16 MB 上限三条核心句写成三件独立的实现事。把它们卖成已经齐 / 已经有了全部快照 / 已经装完，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LoadSnapshotChunk 正式三事（375 余量），必须分开 not already complete、not already all snapshots、not already restored 三件事，不要和 375 / 322 / 501 / 660 / 397 / 740 / 801 / 802 糊成一句。

## 和相邻反模式

- [loadsnapusage-notchunks-sold-as-bundled](loadsnapusage-notchunks-sold-as-bundled.md) 是 Usage retrieve 就已经在拉（501/660），不是本页从邻居拉块边界。
- [applychunk-notload-sold-as-bundled](applychunk-notload-sold-as-bundled.md) 是 Apply 请求 chunk 就已经在拉（397/740），不是本页从邻居拉块边界。
