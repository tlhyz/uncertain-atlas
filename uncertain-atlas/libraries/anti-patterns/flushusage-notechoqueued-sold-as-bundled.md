# 反模式：把 Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量）说成已经 Echo 测 implementation / 已经 HasChannel 入队 / 已经 Echo Message 是 Flush

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Flush Usage Signals messages queued should be flushed to server not Echo test ≠ bundled（493）](../../tracks/implementation/worked-example-flushusage-notechoqueued-vs-bundled.md)。

## 卖法

把 Signals that messages queued on the client should be flushed to the server 写成已经 Echo a string to test an ABCI client/server implementation interchangeable / 492 echousage-vs-flush interchangeable / 已经 Echo 用来测 client/server implementation interchangeable / 已经 Echo 测实现 interchangeable；把 queued on client should be flushed / 客户端排队的消息要冲到服务端 写成已经 HasChannel 就已经入队 interchangeable / 309 haschannel queued interchangeable / 已经 P2P 通道入队 interchangeable / 已经送到 interchangeable；把 should be flushed to server 写成已经 Echo 请求 Message 就已经是 Flush interchangeable / 394 echo-message-is-flush interchangeable / 已经 Echo Message 是 Flush interchangeable / 492 echousage item 2 Request Message interchangeable，或已经和 493 flushusage-vs-echo bundled / flushusage-sold-as-echo interchangeable / 671 flushusage-notechoqueued interchangeable。

## 为什么错

官方把 Flush Usage Signals messages queued 单句、Echo Usage 测实现（492）、HasChannel 入队（309）、Echo 请求 Message 是 Flush（394）写成三件独立的实现事。把它们卖成 Echo 测 implementation interchangeable / HasChannel 入队 interchangeable / Echo Message 是 Flush interchangeable，会把 not Echo test、not HasChannel queued、not Echo request Message is Flush 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量），必须分开 not Echo test、not HasChannel queued、not Echo request Message is Flush 三件事，不要和 493 / 492 / 309 / 394 / 374 / 307 / 672 / 673 糊成一句。

## 和相邻反模式

- [flushusage-sold-as-echo](flushusage-sold-as-echo.md) 是 Flush Usage 正式三事 bundled 全段，不是本页 item 1 Signals messages queued 单句边界。
- [echousage-sold-as-flush](echousage-sold-as-flush.md) 是 Echo 测实现就等于 Flush，不是本页 Methods Flush Usage 冲队列单句边界。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush bundled 就等于已经送到，不是本页 Signals messages queued vs HasChannel 边界。
