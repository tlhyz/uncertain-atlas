# 模式：把 Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[Flush Usage Signals messages queued should be flushed to server not Echo test ≠ bundled（493）](../../tracks/implementation/worked-example-flushusage-notechoqueued-vs-bundled.md)。

## 三个名字

1. **Signals messages queued should be flushed to server 不是 Echo test implementation：** 看见 Methods Flush Usage 冲客户端排队，不是已经 Echo a string to test an ABCI client/server implementation interchangeable，不是 492 echousage-vs-flush interchangeable / 493 flushusage-vs-echo bundled interchangeable / 671 flushusage-notechoqueued interchangeable。

2. **queued on client should be flushed 不是 HasChannel 入队：** 看见客户端排队的消息要冲到服务端，不是已经 HasChannel 就已经入队 interchangeable，不是 309 haschannel queued interchangeable / 307 abci-conn-vs-gates interchangeable / 374 flush bundled interchangeable。

3. **should be flushed to server 不是 Echo 请求 Message 是 Flush：** 看见 Signals messages queued should be flushed to server，不是已经 Echo 请求 Message 就已经是 Flush interchangeable，不是 394 echo-message-is-flush interchangeable / 492 echousage item 2 Request Message interchangeable / 399 commit-empty-echo bundled interchangeable。

官方把 Flush Usage Signals messages queued 单句、Echo Usage 测实现（492）、HasChannel 入队（309）、Echo 请求 Message 是 Flush（394）写成三个名字。把它们叫成一个「看见 Signals messages queued should be flushed 就已经 Echo 测 implementation interchangeable / 就已经 HasChannel 入队 interchangeable / 就已经 Echo Message 是 Flush interchangeable」，会把 not Echo test、not HasChannel queued、not Echo request Message is Flush 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量），先数清问的是 Signals messages queued 是不是 Echo test / 492 / 493 bundled，是不是 queued on client 是不是 HasChannel queued / 309 / 307，还是 should be flushed to server 是不是 Echo request Message is Flush / 394 / 374，再决定要不要同一次发布。493 flushusage vs echo bundled unbundling 在本页 item 1 完成。
