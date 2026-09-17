# 反模式：把 查到了 not already fresh / not already tip / not already settled 正式三事（329 余量） 卖成 已经新鲜 / 已经是当前尖 / 已经交差

**层次**：实现 / Query。  
**分类**：建议（产品）。  
**对应例**：[worked-example-query-notfresh-vs-bundled.md](../../tracks/implementation/worked-example-query-notfresh-vs-bundled.md)。

官方把 Query 回了 / 查到了 / 实现了 Query 三条核心句写成三件独立的实现事。把它们卖成已经新鲜 / 已经是当前尖 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看查到了 正式三事（329 余量），必须分开 not already fresh、not already tip、not already settled 三件事，不要和 329 / 325 / 326 / 938 / 940 糊成一句。

## 和相邻反模式

- [query-notrepl-sold-as-bundled](query-notrepl-sold-as-bundled.md) 是 Query 回了仍不是复制单句边界（938 item 1），不是本页查到了仍可能旧边界。
- Query 回了 Proof 已经对上 AppHash 是不变量 325，不是本页查到了仍可能旧边界。
