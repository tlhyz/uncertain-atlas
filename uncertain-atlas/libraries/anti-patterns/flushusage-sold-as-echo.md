# 反模式：把 Flush Usage 正式三事卖成 Echo 测实现 interchangeable / 已经送到 / 已经能往下走

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Signals messages queued should be flushed to server ≠ Echo 测 implementation](../../tracks/implementation/worked-example-flushusage-vs-echo.md)。

## 卖法

- 「看见 Signals that messages queued on the client should be flushed to the server / Flush 要把客户端排队的消息冲到服务端 就已经 Echo a string to test an ABCI client/server implementation / Echo 用来测实现 interchangeable / 已经 HasChannel 入队 interchangeable / 已经送到。」
- 「看见 Called periodically to ensure async requests are actually sent / 定期 Flush 是为了让异步请求真发出去 就已经 Echo 用来测实现 interchangeable / 已经一条连接就是四门 / 已经交差。」
- 「看见 Called immediately for sync request; returns when Flush response comes back / 立刻 Flush 是为了做成同步请求、回包回来才算这次同步 就已经 Echo 回包 Message 是入参那串 interchangeable / 已经 Commit 里等广播就能往下走 / 已经 Commit。」

## 为什么错

官方把 Flush Usage 三句写成三件独立的实现事。把它们卖成 Echo 测 implementation interchangeable / 已经送到 / 已经能往下走，会把冲队列、定期异步、同步回包三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage 正式三事，必须分开 Signals messages queued should be flushed to server、Called periodically to ensure async requests are actually sent、Called immediately for sync request returns when Flush response comes back 三个名字，不要把它们卖成 Echo 测 implementation interchangeable / 已经送到 / 已经能往下走。

## 和相邻反模式

- [echousage-sold-as-flush](echousage-sold-as-flush.md) 是 Echo 测实现就等于 Flush，不是本页 Flush Usage 专用三事。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush bundled 就等于已经送到，不是本页 Methods Flush Usage 正式三事与 Echo 的边界。
