# 反模式：把 Process 调用是同步的 not already can change verdict later / not already left critical path / not already settled 正式三事（354 余量） 卖成 已经能稍后改裁决 / 已经离开关键路径 / 已经交差

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notlater-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notlater-vs-bundled.md)。

官方把 Process 调用是同步的 / 只做基本检查再异步 Process / 非验证者可以立刻回 ACCEPT 三条核心句写成三件独立的实现事。把它们卖成已经能稍后改裁决 / 已经离开关键路径 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 调用是同步的 正式三事（354 余量），必须分开 not already can change verdict later、not already left critical path、not already settled 三件事，不要和 354 / 327 / 361 / 843 / 858 / 859 糊成一句。

## 和相邻反模式

- [extend-when-notlater-sold-as-bundled](extend-when-notlater-sold-as-bundled.md) 是 ExtendVote 同步就已经能稍后改（361/843），不是本页 Process 同步边界。
- 立刻整块执行就已经离开关键路径是不变量 327，不是本页同步边界。
