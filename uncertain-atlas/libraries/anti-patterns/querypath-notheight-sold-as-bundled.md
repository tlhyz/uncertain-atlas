# 反模式：把 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量）说成已经是 Query 高度 / 已经新鲜 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[填了 data not already height ≠ bundled（377）](../../tracks/implementation/worked-example-querypath-notheight-vs-bundled.md)。

## 卖法

把填了 data / data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 / 填了 data 字段 写成已经是 Query 高度 interchangeable / 已经 height interchangeable / 已经是 Query 高度交差 interchangeable / 377 querypath bundled interchangeable / querypath-sold-as-store interchangeable；把能代替 path / data 可以代替 path / 代替 path 写成已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable；把有字节 / data 有字节 / 填了字节 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 377 querypath bundled / querypath-sold-as-store interchangeable / 878 querypath-notheight interchangeable。

## 为什么错

官方把填了 data、不是已经新鲜、不是已经交差写成三件独立的实现事。把它们卖成 already height interchangeable / already fresh interchangeable / already settled interchangeable，会把 not already height、not already fresh、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 余量），必须分开 not already height、not already fresh、not already settled 三件事，不要和 377 / 371 / 326 / 329 糊成一句。

## 和相邻反模式

- [querypath-sold-as-store](querypath-sold-as-store.md) 是 querypath bundled 全段，不是本页填了 data item 1 单句边界。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState（371），不是本页 not already height 单句。
- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是有 /store 路径就已经是引擎在用（326），不是本页 not already fresh 边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是实现了 Query 就已经是正常运转必须有（329），不是本页 not already settled 边界。
