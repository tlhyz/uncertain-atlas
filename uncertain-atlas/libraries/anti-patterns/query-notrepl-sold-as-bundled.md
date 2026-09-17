# 反模式：把 Query 回了 not already replicated / not already consensus / not already settled 正式三事（329 余量） 卖成 已经复制到各节点 / 已经过了共识 / 已经交差

**层次**：实现 / Query。  
**分类**：建议（产品）。  
**对应例**：[worked-example-query-notrepl-vs-bundled.md](../../tracks/implementation/worked-example-query-notrepl-vs-bundled.md)。

官方把 Query 回了 / 查到了 / 实现了 Query 三条核心句写成三件独立的实现事。把它们卖成已经复制到各节点 / 已经过了共识 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 正式三事（329 余量），必须分开 not already replicated、not already consensus、not already settled 三件事，不要和 329 / 314 / 325 / 939 / 940 糊成一句。

## 和相邻反模式

- [snapshot-verify-notdos-sold-as-bundled](snapshot-verify-notdos-sold-as-bundled.md) 是封禁仍没有消掉快照 DoS 边界（332/937），不是本页 Query 回了仍不是复制边界。
- QueryState 已经是 ExecuteTxState 是不变量 314，不是本页 Query 仍是本地读边界。
