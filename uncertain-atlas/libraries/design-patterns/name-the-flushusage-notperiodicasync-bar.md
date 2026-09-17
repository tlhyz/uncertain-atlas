# 模式：把 Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[Flush Usage Called periodically ensure async requests actually sent not Echo test ≠ bundled（493）](../../tracks/implementation/worked-example-flushusage-notperiodicasync-vs-bundled.md)。

## 三个名字

1. **Called periodically ensure async requests actually sent 不是 Echo test implementation：** 看见 Methods Flush Usage 定期冲异步请求，不是已经 Echo a string to test an ABCI client/server implementation interchangeable，不是 492 echousage-vs-flush interchangeable / 493 flushusage-vs-echo bundled interchangeable / 672 flushusage-notperiodicasync interchangeable。

2. **periodically / async requests actually sent 不是一条连接就是四门：** 看见定期 Flush 让异步请求真发出去，不是已经一条连接就已经是四门 interchangeable，不是 307 abci-conn-vs-gates interchangeable / 309 haschannel queued interchangeable / 671 flushusage-notechoqueued interchangeable。

3. **ensure async requests are actually sent 不是 Flush bundled 第二件事：** 看见 Called periodically to ensure async requests are actually sent，不是已经 Flush 要把客户端排队的消息冲到服务端 bundled 第二件事 interchangeable，不是 374 flush bundled interchangeable / 374 flush-vs-sent interchangeable / 673 flushusage-notimmediatesync interchangeable。

官方把 Flush Usage periodically ensure async requests 单句、Echo Usage 测实现（492）、一条连接四门（307）、Flush bundled 第二件事（374）写成三个名字。把它们叫成一个「看见 Called periodically ensure async requests actually sent 就已经 Echo 测 implementation interchangeable / 就已经四门 interchangeable / 就已经 Flush bundled 第二件事 interchangeable」，会把 not Echo test、not one connection four gates、not Flush bundled item 2 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量），先数清问的是 Called periodically 是不是 Echo test / 492 / 493 bundled，是不是 periodically async sent 是不是 one connection four gates / 307 / 309，还是 ensure async requests actually sent 是不是 Flush bundled item 2 / 374 / 671，再决定要不要同一次发布。493 flushusage vs echo bundled unbundling 在本页 item 2 完成。
