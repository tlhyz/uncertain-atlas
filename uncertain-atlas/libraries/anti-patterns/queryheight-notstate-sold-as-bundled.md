# 反模式：把 Query 高度 not already QueryState / not already replicated / not already settled 正式三事（371 余量） 卖成 已经是 QueryState / 已经复制 / 已经交差

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notstate-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notstate-vs-bundled.md)。

官方把 Query 能查当前或过去高度 / height 默认 0 / 这个 height 含 Merkle 根三条核心句写成三件独立的实现事。把它们卖成已经是 QueryState / 已经复制 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 高度 正式三事（371 余量），必须分开 not already QueryState、not already replicated、not already settled 三件事，不要和 371 / 329 / 377 / 797 / 380 / 789 / 813 / 814 糊成一句。

## 和相邻反模式

- [querypath-notheight-sold-as-bundled](querypath-notheight-sold-as-bundled.md) 是 data 就已经是 Query 高度（377/797），不是本页能查边界。
- [queryindex-notheight-sold-as-bundled](queryindex-notheight-sold-as-bundled.md) 是 Query 回包 key 就已经是 Query 高度（380/789），不是本页能查边界。
