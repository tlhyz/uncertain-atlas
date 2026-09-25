# 例：看见叫了 / 看见在冲 / 看见排队了 is not already already sent interchangeable / already queued interchangeable / already disconnected interchangeable

**层次**：实现 / Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量）/ not 869 flush-notsent interchangeable / not 374 flush bundled interchangeable」，不是 flush bundled（374），也不是定期 Flush 是为了让异步请求真发出去不是已经是四门（374 item 2 余量）或立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走（374 item 3 余量）。不要另写怎样写 Flush。

## 官方三件事

规范把 Methods 里 Flush 要把客户端排队的消息冲到服务端 和「已经是叫了就已经送到 interchangeable / 已经是在冲就已经入队 interchangeable / 已经是排队了就已经断开 interchangeable / 已经是 flush bundled interchangeable」分开写成三件独立的实现事，不是「看见叫了就已经送到 interchangeable / 就已经入队 interchangeable / 就已经断开 interchangeable」一件事：

1. **看见叫了 / 看见 Flush 要把客户端排队的消息冲到服务端 / 看见叫了 Flush is not already 已经送到 interchangeable / 已经 sent interchangeable / 已经送到交差 interchangeable / 374 flush bundled interchangeable / 309 HasChannel interchangeable / flush-sold-as-sent interchangeable，也不是已经 flush bundled（374） interchangeable / 869 flush-notsent interchangeable / 374 flush item 1 interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事 bundled（374 item 1 余量） interchangeable / 374 flush item 1 interchangeable，也不是已经定期就已经是四门（374 item 2） interchangeable / 立刻就已经能往下走（374 item 3） interchangeable / 307 abci-conn interchangeable，也不是已经 HasChannel 就已经入队（309） interchangeable。**  
   官方写：Flush 表示客户端排队的消息该冲到服务端。看见叫了，不是已经送到。看见叫了，不是已经 sent interchangeable——374 钉 bundled 三事，本页从 item 1 侧钉 not already sent 单句。看见 Flush 要把客户端排队的消息冲到服务端，不是已经 flush bundled（374） interchangeable——374 钉 bundled，本页钉 item 1 第一件事。看见叫了，不是已经 HasChannel 就已经入队（309） interchangeable——309 另钉。374 flush-vs-sent bundled unbundling 在本页 item 1 启动。

2. **看见在冲 / 看见该冲到服务端 / 看见在冲队列 is not already 已经入队 interchangeable / 已经 queued interchangeable / 已经入队交差 interchangeable / 374 flush bundled interchangeable / 309 HasChannel interchangeable，也不是已经 flush bundled（374） interchangeable / 869 flush-notsent interchangeable / 374 flush item 2 定期 interchangeable / 374 flush item 3 立刻 interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事 bundled（374 item 1 余量） interchangeable / 374 flush item 1 interchangeable，也不是已经送到（本页第一件事） interchangeable。**  
   官方写：看见在冲，不是已经入队。看见该冲到服务端，不是已经 queued interchangeable——本页钉 not already queued 单句。看见在冲队列，不是已经送到（本页第一件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 1 启动。

3. **看见排队了 / 看见客户端排队了 / 看见消息排队了 is not already 已经断开 interchangeable / 已经 disconnected interchangeable / 已经断开交差 interchangeable / 374 flush bundled interchangeable / 307 abci-conn interchangeable，也不是已经 flush bundled（374） interchangeable / 869 flush-notsent interchangeable / 374 flush item 2 / 374 flush item 3，也不是已经 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事 bundled（374 item 1 余量） interchangeable / 374 flush item 1 interchangeable，也不是已经送到（本页第一件事） interchangeable / 已经入队（本页第二件事） interchangeable。**  
   官方写：看见排队了，不是已经断开。看见客户端排队了，不是已经 disconnected interchangeable——本页钉 not already disconnected 单句。看见消息排队了，不是已经入队（本页第二件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 1 启动。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。flush bundled（374）、定期 Flush 是为了让异步请求真发出去不是已经是四门（374 item 2 余量）、立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走（374 item 3 余量）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）是另外那套，本页不抄。

## 官方为什么这样拆

- **叫了 not already sent ≠ 374 / 309 interchangeable：** 官方把该冲出去和已经送到分开。
- **在冲 not already queued ≠ 已经入队 interchangeable：** 官方把在冲和已经入队分开。
- **排队了 not already disconnected ≠ 已经断开 interchangeable：** 官方把排队了和已经断开分开；374 flush-vs-sent bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 叫了 | 不是 already sent | 不是 HasChannel 就已经入队 alone（309） |
| 在冲 | 不是 already queued | 不是一条连接就已经是四门 alone（307） |
| 排队了 | 不是 already disconnected | 不是 Commit 里等广播就已经能往下走 alone（310） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 要把客户端排队的消息冲到服务端不是已经送到 not already sent / not already queued / not already disconnected 正式三事（374 余量），必须分开叫了 是不是 already sent interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable、在冲 是不是 already queued interchangeable、排队了 是不是 already disconnected interchangeable。可以跳过「看见叫了就已经送到 interchangeable / 就已经入队 interchangeable / 就已经断开 interchangeable」。不要另写怎样写 Flush。374 flush-vs-sent bundled unbundling 在本页 item 1 启动（869）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- flush bundled。那是不变量 374。
- 定期 Flush 是为了让异步请求真发出去不是已经是四门。那是不变量 374 item 2 余量。
- 立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走。那是不变量 374 item 3 余量。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
