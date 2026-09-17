# 反模式：把 只做基本检查再异步 Process not already can still Reject / not already can force nil / not already settled 正式三事（354 余量） 卖成 已经还能再 Reject / 已经还能强迫 nil / 已经交差

**层次**：实现 / Process 何时调用。  
**分类**：建议（产品）。  
**对应例**：[worked-example-process-when-notreject-vs-bundled.md](../../tracks/implementation/worked-example-process-when-notreject-vs-bundled.md)。

官方把 Process 调用是同步的 / 只做基本检查再异步 Process / 非验证者可以立刻回 ACCEPT 三条核心句写成三件独立的实现事。把它们卖成已经还能再 Reject / 已经还能强迫 nil / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看只做基本检查再异步 Process 正式三事（354 余量），必须分开 not already can still Reject、not already can force nil、not already settled 三件事，不要和 354 / 33 / 327 / 857 / 859 糊成一句。

## 和相邻反模式

- [process-when-notlater-sold-as-bundled](process-when-notlater-sold-as-bundled.md) 是同步单句边界（857 item 1），不是本页异步改票边界。
- 四门已经结算是不变量 33，不是本页异步改票边界。
