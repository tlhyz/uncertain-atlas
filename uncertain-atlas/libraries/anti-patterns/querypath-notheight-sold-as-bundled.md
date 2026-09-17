# 反模式：把 data not already Query height / not already fresh / not already settled 正式三事（377 余量） 卖成 已经是 Query 高度 / 已经新鲜 / 已经交差

**层次**：实现 / Query 路径。  
**分类**：建议（产品）。  
**对应例**：[worked-example-querypath-notheight-vs-bundled.md](../../tracks/implementation/worked-example-querypath-notheight-vs-bundled.md)。

官方把 data 按 URI 查询分量解释 / path /store 必须按键查 / 建议允许按类型查三条核心句写成三件独立的实现事。把它们卖成已经是 Query 高度 / 已经新鲜 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 data 正式三事（377 余量），必须分开 not already Query height、not already fresh、not already settled 三件事，不要和 377 / 371 / 380 / 789 / 383 / 781 / 798 / 799 糊成一句。

## 和相邻反模式

- [queryindex-notheight-sold-as-bundled](queryindex-notheight-sold-as-bundled.md) 是 Query 回包 key 就已经是 Query 高度（380/789），不是本页 data 边界。
- [queryprove-notreqh-sold-as-bundled](queryprove-notreqh-sold-as-bundled.md) 是 Query 证明 height 就已经是请求高度（383/781），不是本页 data 边界。
