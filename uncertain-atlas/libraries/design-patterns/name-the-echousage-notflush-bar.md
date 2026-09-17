# 模式：把 Echo Usage Echo a string to test implementation not Flush flush queue / not commit-empty-echo bundled / not Flush sync response 正式三事（492 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Echo Usage。  
**例**：[Echo Usage Echo a string to test implementation not Flush flush queue ≠ bundled（492）](../../tracks/implementation/worked-example-echousage-notflush-vs-bundled.md)。

## 三个名字

1. **Echo a string to test implementation 不是 Flush flush queue：** 看见 Methods Echo Usage 测 client/server，不是已经 Flush 要把客户端排队的消息冲到服务端 interchangeable，不是 374 flush bundled interchangeable / 493 flushusage-vs-echo interchangeable / 674 echousage-notflush interchangeable。

2. **Echo 用来测实现 不是 commit-empty-echo bundled：** 看见 Echo a string to test an ABCI client/server implementation，不是已经 Commit 空请求 bundled interchangeable，不是 399 commit-empty-echo bundled interchangeable / 335 finpersist interchangeable / 673 flushusage-notimmediatesync interchangeable。

3. **测 client/server implementation 不是 Flush sync response：** 看见 Echo 能叫 / 用来测实现，不是已经 Flush 回包回来就算这次同步 interchangeable，不是 673 flushusage-notimmediatesync interchangeable / 374 flush-vs-sent interchangeable / 676 echousage-notdone interchangeable。

官方把 Echo Usage 测实现单句、Flush 冲队列（374）、Commit 空请求 bundled（399）、Flush 同步回包（673）写成三个名字。把它们叫成一个「看见 Echo 用来测实现 就已经 Flush flush queue interchangeable / 就已经 commit-empty-echo bundled interchangeable / 就已经 Flush sync response interchangeable」，会把 not Flush flush queue、not commit-empty-echo bundled、not Flush sync response 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo Usage Echo a string to test implementation not Flush flush queue / not commit-empty-echo bundled / not Flush sync response 正式三事（492 余量），先数清问的是 Echo a string to test implementation 是不是 Flush flush queue / 374 / 493 bundled，是不是 Echo 用来测实现 是不是 commit-empty-echo bundled / 399 / 335，还是测 client/server implementation 是不是 Flush sync response / 673 / 671，再决定要不要同一次发布。492 echousage vs flush bundled unbundling 在本页 item 1 完成。
