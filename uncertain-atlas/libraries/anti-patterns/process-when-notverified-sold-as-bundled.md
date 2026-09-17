# 反模式：把 非验证者可以立刻回 ACCEPT not already verified this block / not already validators can skip / not already settled 正式三事（354 余量） 卖成 已经验过这块 / 已经是验证者也可以立刻交差 / 已经交差

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notverified-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notverified-vs-bundled.md)。

官方把 Process 调用是同步的 / 只做基本检查再异步 Process / 非验证者可以立刻回 ACCEPT 三条核心句写成三件独立的实现事。把它们卖成已经验过这块 / 已经是验证者也可以立刻交差 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看非验证者可以立刻回 ACCEPT 正式三事（354 余量），必须分开 not already verified this block、not already validators can skip、not already settled 三件事，不要和 354 / 351 / 33 / 857 / 858 糊成一句。

## 和相邻反模式

- [process-when-notreject-sold-as-bundled](process-when-notreject-sold-as-bundled.md) 是异步改票单句边界（858 item 2），不是本页立刻 ACCEPT 边界。
- Process 也会在提议者那边叫是不变量 351，不是本页非验证者立刻 ACCEPT 边界。
