# 反模式：把 三列认块 not already same snapshot / not already complete / not already selected format 正式三事（375 余量） 卖成 已经是同一份 / 已经齐 / 已经选型

**层次**：实现 / LoadSnapshotChunk。  
**分类**：建议（产品）。  
**对应例**：[worked-example-loadchunk-notsame-vs-bundled.md](../../tracks/implementation/worked-example-loadchunk-notsame-vs-bundled.md)。

官方把从邻居拉快照块 / 三列认块 / 16 MB 上限三条核心句写成三件独立的实现事。把它们卖成已经是同一份 / 已经齐 / 已经选型，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看三列认块 正式三事（375 余量），必须分开 not already same snapshot、not already complete、not already selected format 三件事，不要和 375 / 368 / 396 / 738 / 395 / 735 / 800 / 802 糊成一句。

## 和相邻反模式

- [loadchunk-notcomplete-sold-as-bundled](loadchunk-notcomplete-sold-as-bundled.md) 是从邻居拉块单句边界（800 item 1），不是本页三列认块边界。
- [listsnapempty-notidentical-sold-as-bundled](listsnapempty-notidentical-sold-as-bundled.md) 是 ListSnapshots 本地列表就已经是同一份（395/735），不是本页三列认块边界。
