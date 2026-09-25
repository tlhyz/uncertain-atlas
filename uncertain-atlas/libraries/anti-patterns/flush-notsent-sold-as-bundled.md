# 反模式：把 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量）说成已经送到 / 已经入队 / 已经断开

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[叫了 not already sent ≠ bundled（374）](../../tracks/implementation/worked-example-flush-notsent-vs-bundled.md)。

## 卖法

把叫了 / Flush 要把客户端排队的消息冲到服务端 / 叫了 Flush 写成已经送到 interchangeable / 已经 sent interchangeable / 已经送到交差 interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable；把在冲 / 该冲到服务端 / 在冲队列 写成已经入队 interchangeable / 已经 queued interchangeable / 已经入队交差 interchangeable；把排队了 / 客户端排队了 / 消息排队了 写成已经断开 interchangeable / 已经 disconnected interchangeable / 已经断开交差 interchangeable，或已经和 374 flush bundled / flush-sold-as-sent interchangeable / 869 flush-notsent interchangeable。

## 为什么错

官方把叫了、不是已经入队、不是已经断开写成三件独立的实现事。把它们卖成 already sent interchangeable / already queued interchangeable / already disconnected interchangeable，会把 not already sent、not already queued、not already disconnected 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量），必须分开 not already sent、not already queued、not already disconnected 三件事，不要和 374 / 309 / 307 / 310 糊成一句。

## 和相邻反模式

- [flush-sold-as-sent](flush-sold-as-sent.md) 是 flush bundled 全段，不是本页叫了 item 1 单句边界。
- [send-sold-as-enqueued](send-sold-as-enqueued.md) 是 HasChannel 就已经入队（309），不是本页 not already sent 单句。
- [conn-sold-as-gates](conn-sold-as-gates.md) 是一条连接就已经是四门（307），不是本页 not already disconnected 边界。
- [commitlock-sold-as-rpc](commitlock-sold-as-rpc.md) 是 Commit 里等广播就已经能往下走（310），不是本页 not already queued 边界。
