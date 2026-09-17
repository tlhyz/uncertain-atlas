# 例：看见 Flush 要把客户端排队的消息冲到服务端 is not already delivered interchangeable / not already queued interchangeable / not already disconnected interchangeable

**层次**：实现 / Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量）/ not 803 flush-notdelivered interchangeable / not 374 flush-vs-sent bundled interchangeable」，不是 Flush bundled（374），也不是 HasChannel 就已经入队（309），也不是 Usage Signals flush 就已经是 Echo 测（493/671），也不是 Echo 请求 Message 就已经是 Flush（394/751）。不要另写怎样写 Flush。

## 官方三件事

1. **看见 Flush 要把客户端排队的消息冲到服务端 / 看见叫了 Flush / 这份冲队列 is not already 已经送到 interchangeable / 309 haschannel interchangeable，也不是已经 Flush bundled（374） interchangeable / 803 flush-notdelivered interchangeable / 804 flush-notgates interchangeable / 374 flush item 2 定期 interchangeable，也不是已经 Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事 bundled（374 item 1 余量） interchangeable / 374 flush item 1 interchangeable。**  
   官方写：Flush 表示客户端排队的消息该冲到服务端。看见叫了，不是已经送到 interchangeable——本页从 374 item 1 侧钉 not already delivered 单句。374 flush vs sent bundled unbundling 在本页 item 1 启动。

2. **看见叫了 Flush / 看见在冲 / 这份冲队列 is not already 已经入队 interchangeable / 309 haschannel interchangeable，也不是已经 Flush bundled（374） interchangeable / 803 flush-notdelivered interchangeable / 374 flush item 3 立刻 interchangeable / 805 flush-notproceed interchangeable，也不是已经 Usage Signals flush 就已经是 Echo 测 interchangeable / 493 flushusage / 671 flushusage-notechoqueued interchangeable，也不是已经 Echo 请求 Message 就已经是 Flush interchangeable / 394 extcommitround / 751 extcommitround-notflush interchangeable。**  
   官方把在冲和已经入队分开——374 bundled 第一件事常与 309 / 493 / 394 混成「看见叫了 Flush 就已经送到或已经入队 interchangeable」，本页钉 not already queued 单句。

3. **看见叫了 Flush / 看见排队了 / 这份冲队列 is not already 已经断开 interchangeable，也不是已经 Flush bundled（374） interchangeable / 803 flush-notdelivered interchangeable / 804 flush-notgates interchangeable。**  
   官方把排队了和已经断开分开。看见排队了，不是已经断开 interchangeable。374 flush vs sent bundled unbundling 在本页 item 1 启动。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Flush 冲队列 not already delivered ≠ 309 interchangeable：** 官方把该冲出去和已经送到分开。
- **看见在冲 not already queued ≠ 已经入队 interchangeable：** 官方把在冲和已经入队分开。
- **看见排队了 not already disconnected ≠ 已经断开 interchangeable：** 官方把排队了和已经断开分开；374 flush vs sent bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Flush 要把客户端排队的消息冲到服务端 | 不是已经送到（309） | 不是定期 Flush（804/374 item 2） |
| 看见叫了 Flush | 不是已经入队 | 不是 Usage Signals flush（493/671） |
| 看见排队了 | 不是已经断开 | 不是 Echo Message 就已经是 Flush（394/751） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush 冲队列 not already delivered / not already queued / not already disconnected 正式三事（374 余量），必须分开是不是已经送到 interchangeable / 309、是不是已经入队、是不是已经断开。可以跳过「看见叫了 Flush 就已经送到」。不要另写怎样写 Flush。374 flush vs sent bundled unbundling 在本页 item 1 启动；续 [`worked-example-flush-notgates-vs-bundled.md`](worked-example-flush-notgates-vs-bundled.md)（不变量 804 item 2）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush bundled。那是不变量 374。
- 定期 Flush。那是不变量 374 item 2 余量 / 804。
- HasChannel 就已经入队。那是不变量 309。
- Usage Signals flush 就已经是 Echo 测。那是不变量 493 / 671。
