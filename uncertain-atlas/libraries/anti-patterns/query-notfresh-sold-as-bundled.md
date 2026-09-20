# 反模式：把查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量）说成已经新鲜 / 已经是当前尖 / 已经是决定块之后那份

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[查到了 not already fresh ≠ bundled（329）](../../tracks/implementation/worked-example-query-notfresh-vs-bundled.md)。

## 卖法

把查到了 / 本地有这份 / 查有结果 写成已经新鲜 interchangeable / 已经 fresh interchangeable / 已经新鲜交差 interchangeable / 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable；把跟上了尖 / 当前尖 / 尖上这份 写成已经是当前尖 interchangeable / 已经 tip interchangeable；把决定块之后那份 / 决定后状态 / 已决定状态 写成已经是决定块之后那份 interchangeable / 已经 decided-state interchangeable，或已经和 329 query bundled / query-sold-as-replicated interchangeable / 744 query-notfresh interchangeable。

## 为什么错

官方把查到了单句、already fresh、already tip、already decided-state 写成三件独立的实现事。把它们卖成 already fresh interchangeable / already tip interchangeable / already decided-state interchangeable，会把 not already fresh、not already tip、not already decided-state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看查到了不是已经新鲜 not already fresh / not already tip / not already decided-state 正式三事（329 余量），必须分开 not already fresh、not already tip、not already decided-state 三件事，不要和 329 / 33 / 314 / 325 / 743 / 745 糊成一句。

## 和相邻反模式

- [query-notrequired-sold-as-bundled](query-notrequired-sold-as-bundled.md) 是必须有（329 item 3），不是本页新鲜 item 2单句边界。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query bundled 全段，不是本页新鲜 item 2 单句边界。
- [query-notreplicated-sold-as-bundled](query-notreplicated-sold-as-bundled.md) 是复制 item 1，不是本页查到了与新鲜边界。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState ≠ ExecuteTxState（314），不是本页决定后状态边界。
