# 模式：把 Flush Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[Signals messages queued should be flushed to server ≠ Echo 测 implementation](../../tracks/implementation/worked-example-flushusage-vs-echo.md)。

## 三个名字

1. **Signals messages queued should be flushed to server 不是 Echo 测 implementation：** 看见 Methods Flush Usage 冲客户端排队，不是 Echo 测 client/server interchangeable。
2. **Called periodically to ensure async requests are actually sent 不是 Echo 用来测实现：** 看见定期冲异步请求，不是 Echo Usage 测实现或已经是四门 interchangeable。
3. **Called immediately for sync request; returns when Flush response comes back 不是 Echo 回包 Message：** 看见 Flush 同步回包，不是 Echo 回包栏 the input string 或 Commit 锁 interchangeable。

## 为什么要分开叫

官方把 Flush Usage 三句、Echo Usage 正式三事（492）、Flush bundled（374）、HasChannel（309）、四门（307）、Commit 锁（310）写成三个名字。把它们叫成一个「看见 Flush 了就已经 Echo 测实现 interchangeable、已经送到、已经能往下走」，会把冲队列、定期异步、同步回包三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage 正式三事，先数清问的是 Signals messages queued should be flushed to server 是不是 Echo 测 implementation interchangeable / 已经送到、Called periodically to ensure async requests are actually sent 是不是 Echo 用来测实现 interchangeable / 已经是四门、Called immediately for sync request returns when Flush response comes back 是不是 Echo 回包 Message interchangeable / 已经能往下走，再决定要不要同一次发布。
