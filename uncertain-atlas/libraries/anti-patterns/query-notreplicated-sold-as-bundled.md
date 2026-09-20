# 反模式：把 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量）说成已经复制到各节点 / 已经过了共识 / 已经全网同一份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Query 回了 not already replicated ≠ bundled（329）](../../tracks/implementation/worked-example-query-notreplicated-vs-bundled.md)。

## 卖法

把 Query 回了 / 查有回包 / 通用查询回了 写成已经复制到各节点 interchangeable / 已经 replicated interchangeable / 已经复制交差 interchangeable / 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable；把 RPC 能查 / RPC 绿了 / 经 RPC 暴露给用户 写成已经过了共识 interchangeable / 已经 consensus-passed interchangeable；把查的是本节点本地 / 本地状态 / 本机查询 写成已经全网同一份 interchangeable / 已经 network-same interchangeable，或已经和 329 query bundled / query-sold-as-replicated interchangeable / 743 query-notreplicated interchangeable。

## 为什么错

官方把 Query 回了单句、already replicated、already consensus-passed、already network-same 写成三件独立的实现事。把它们卖成 already replicated interchangeable / already consensus-passed interchangeable / already network-same interchangeable，会把 not already replicated、not already consensus-passed、not already network-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量），必须分开 not already replicated、not already consensus-passed、not already network-same 三件事，不要和 329 / 33 / 314 / 325 / 744 / 745 糊成一句。

## 和相邻反模式

- [query-notfresh-sold-as-bundled](query-notfresh-sold-as-bundled.md) 是查到了新鲜（329 item 2），不是本页复制 item 1 单句边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query bundled 全段，不是本页复制 item 1 单句边界。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState ≠ ExecuteTxState（314），不是本页本地查询与复制边界。
- [checktxoscillate-notsameb-sold-as-bundled](checktxoscillate-notsameb-sold-as-bundled.md) 是本地不再振荡同一份 b（328 item 3），不是本页 Query 本地查询边界。
