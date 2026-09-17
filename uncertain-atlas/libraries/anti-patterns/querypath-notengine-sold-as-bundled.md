# 反模式：把 path /store not already engine using / not already filter / not already settled 正式三事（377 余量） 卖成 已经是引擎在用 / 已经是过滤 / 已经交差

**层次**：实现 / Query 路径。  
**分类**：建议（产品）。  
**对应例**：[worked-example-querypath-notengine-vs-bundled.md](../../tracks/implementation/worked-example-querypath-notengine-vs-bundled.md)。

官方把 data 按 URI 查询分量解释 / path /store 必须按键查 / 建议允许按类型查三条核心句写成三件独立的实现事。把它们卖成已经是引擎在用 / 已经是过滤 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 path /store 正式三事（377 余量），必须分开 not already engine using、not already filter、not already settled 三件事，不要和 377 / 326 / 380 / 788 / 384 / 778 / 797 / 799 糊成一句。

## 和相邻反模式

- [querypath-notheight-sold-as-bundled](querypath-notheight-sold-as-bundled.md) 是 data 单句边界（797 item 1），不是本页 path /store 边界。
- [queryindex-notstore-sold-as-bundled](queryindex-notstore-sold-as-bundled.md) 是 Query 回包 index 就已经是按键查（380/788），不是本页 path /store 边界。
