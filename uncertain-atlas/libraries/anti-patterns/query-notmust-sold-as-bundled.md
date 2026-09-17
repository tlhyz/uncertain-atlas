# 反模式：把 实现了 Query not already required for normal operation / not already peer-filter / not already settled 正式三事（329 余量） 卖成 已经是正常运转必须有 / 已经是邻居过滤 / 已经交差

**层次**：实现 / Query。  
**分类**：建议（产品）。  
**对应例**：[worked-example-query-notmust-vs-bundled.md](../../tracks/implementation/worked-example-query-notmust-vs-bundled.md)。

官方把 Query 回了 / 查到了 / 实现了 Query 三条核心句写成三件独立的实现事。把它们卖成已经是正常运转必须有 / 已经是邻居过滤 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看实现了 Query 正式三事（329 余量），必须分开 not already required for normal operation、not already peer-filter、not already settled 三件事，不要和 329 / 326 / 334 / 938 / 939 糊成一句。

## 和相邻反模式

- [query-notfresh-sold-as-bundled](query-notfresh-sold-as-bundled.md) 是查到了仍可能旧单句边界（939 item 2），不是本页实现了仍不是必须有边界。
- 发了 addr 过滤查询已经收下这个人是不变量 326，不是本页 Query 仍不是正常运转必须有边界。
