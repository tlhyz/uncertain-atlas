# 反模式：把 自己是提议者 not already every round calls Prepare / not already validValue is nil / not already settled 正式三事（356 余量） 卖成 已经每轮都会调 Prepare / 已经是 validValue 为 nil / 已经交差

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notevery-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notevery-vs-bundled.md)。

官方把 validValue 非 nil 不再调 Prepare / 只有提议者且 validValue 为 nil 才调 / 没调 Prepare 不是又装 raw 提案三条核心句写成三件独立的实现事。把它们卖成已经每轮都会调 Prepare / 已经是 validValue 为 nil / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看自己是提议者 正式三事（356 余量），必须分开 not already every round calls Prepare、not already validValue is nil、not already settled 三件事，不要和 356 / 338 / 351 / 851 / 853 糊成一句。

## 和相邻反模式

- [validvalue-notcall-sold-as-bundled](validvalue-notcall-sold-as-bundled.md) 是 validValue 非 nil 单句边界（851 item 1），不是本页提议者边界。
- Prepare 没有确定性要求是不变量 338，不是本页每轮都会调边界。
