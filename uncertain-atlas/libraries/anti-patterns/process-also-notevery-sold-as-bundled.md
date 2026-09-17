# 反模式：把 失败时可能对上更早一次或根本不调 not already this Prepare / not already every round calls / not already settled 正式三事（351 余量） 卖成 已经是这一次 Prepare / 已经每轮都会叫 / 已经交差

**层次**：实现 / Process 也会在提议者那边叫。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-also-notevery-vs-bundled.md](../../tracks/implementation/worked-example-process-also-notevery-vs-bundled.md)。

官方把 Process 也会在提议者那边叫 / 通常紧跟 Prepare、列表对得上 / 失败时可能对上更早一次或根本不调 三条核心句写成三件独立的实现事。把它们卖成已经是这一次 Prepare / 已经每轮都会叫 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看失败时可能对上更早一次或根本不调 正式三事（351 余量），必须分开 not already this Prepare、not already every round calls、not already settled 三件事，不要和 351 / 311 / 33 / 860 / 861 糊成一句。

## 和相邻反模式

- [process-also-notsame-sold-as-bundled](process-also-notsame-sold-as-bundled.md) 是通常对得上单句边界（861 item 2），不是本页失败路径边界。
- 候选已经是 ExecuteTxState 是不变量 311，不是本页失败路径边界。
