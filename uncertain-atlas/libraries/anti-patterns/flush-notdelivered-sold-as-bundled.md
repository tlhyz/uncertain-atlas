# 反模式：把 Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量） 卖成 已经送到 / 已经入队 / 已经断开

**层次**：实现 / Flush。  
**分类**：建议（产品）。  
**对应例**：[worked-example-flush-notdelivered-vs-bundled.md](../../tracks/implementation/worked-example-flush-notdelivered-vs-bundled.md)。

官方把 Flush 冲队列 / 定期 Flush / 立刻 Flush 三条核心句写成三件独立的实现事。把它们卖成已经送到 / 已经入队 / 已经断开，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 冲队列 正式三事（374 余量），必须分开 not already delivered、not already queued、not already disconnected 三件事，不要和 374 / 309 / 493 / 671 / 394 / 751 / 804 / 805 糊成一句。

## 和相邻反模式

- [flushusage-notechoqueued-sold-as-bundled](flushusage-notechoqueued-sold-as-bundled.md) 是 Usage Signals flush 就已经是 Echo 测（493/671），不是本页冲队列边界。
- [extcommitround-notflush-sold-as-bundled](extcommitround-notflush-sold-as-bundled.md) 是 Echo 请求 Message 就已经是 Flush（394/751），不是本页冲队列边界。
