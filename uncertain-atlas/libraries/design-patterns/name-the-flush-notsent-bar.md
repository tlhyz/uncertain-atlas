# 模式：把 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**例**：[叫了 not already sent ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notsent-vs-bundled.md)。

## 三个名字

1. **叫了 不是 already sent：** 看见叫了 / Flush 要把客户端排队的消息冲到服务端 / 叫了 Flush，不是已经送到 interchangeable / 已经 sent interchangeable / 已经送到交差 interchangeable，不是 374 flush bundled interchangeable / flush-sold-as-sent interchangeable。

2. **在冲 不是 already queued：** 看见在冲 / 该冲到服务端 / 在冲队列，不是已经入队 interchangeable / 已经 queued interchangeable / 已经入队交差 interchangeable，不是 309 HasChannel interchangeable / 307 abci-conn interchangeable。

3. **排队了 不是 already disconnected：** 看见排队了 / 客户端排队了 / 消息排队了，不是已经断开 interchangeable / 已经 disconnected interchangeable / 已经断开交差 interchangeable，不是 310 commit-lock interchangeable / 374 flush item 2 interchangeable。

官方把叫了、不是已经入队、不是已经断开写成三个名字。把它们叫成一个「看见叫了就已经送到 interchangeable / 就已经入队 interchangeable / 就已经断开 interchangeable」，会把 not already sent、not already queued、not already disconnected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量），先数清问的是叫了 是不是 already sent / 374 / flush-sold-as-sent，是不是在冲 是不是 already queued，还是排队了 是不是 already disconnected，再决定要不要同一次发布。374 flush-vs-sent bundled unbundling 在本页 item 1 启动。
