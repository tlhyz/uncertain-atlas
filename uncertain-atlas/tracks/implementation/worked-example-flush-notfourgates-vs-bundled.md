# 例：看见定期在冲 / 看见发出去了 / 看见异步 is not already already fourgates interchangeable / already received interchangeable / already settled interchangeable

**层次**：实现 / 定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量）/ not 870 flush-notfourgates interchangeable / not 374 flush bundled interchangeable」，不是 flush bundled（374），也不是 Flush 要把客户端排队的消息冲到服务端不是已经送到（869 item 1 余量）或立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走（374 item 3 余量）。不要另写怎样写 Flush。

## 官方三件事

规范把 Methods 里定期 Flush 是为了让异步请求真发出去 和「已经是定期在冲就已经是四门 interchangeable / 已经是发出去了就已经收到 interchangeable / 已经是异步就已经交差 interchangeable / 已经是 flush bundled interchangeable」分开写成三件独立的实现事，不是「看见定期在冲就已经是四门 interchangeable / 就已经收到 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见定期在冲 / 看见定期 Flush 是为了让异步请求真发出去 / 看见定期在冲队列 is not already 已经是四门 interchangeable / 已经 fourgates interchangeable / 已经是四门交差 interchangeable / 374 flush bundled interchangeable / 307 abci-conn interchangeable / flush-sold-as-sent interchangeable，也不是已经 flush bundled（374） interchangeable / 870 flush-notfourgates interchangeable / 374 flush item 2 interchangeable，也不是已经定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事 bundled（374 item 2 余量） interchangeable / 374 flush item 2 interchangeable，也不是已经叫了就已经送到（869） interchangeable / 309 HasChannel interchangeable / 33 four gates interchangeable，也不是已经一条连接就已经是四门（307） interchangeable。**  
   官方写：客户端实现会定期叫 Flush，好让异步请求真的发出去。看见定期在冲，不是已经是四门。看见定期在冲，不是已经 fourgates interchangeable——374 钉 bundled 三事，本页从 item 2 侧钉 not already fourgates 单句。看见定期 Flush 是为了让异步请求真发出去，不是已经 flush bundled（374） interchangeable——374 钉 bundled，本页钉 item 2 第一件事。看见定期在冲，不是已经叫了就已经送到（869） interchangeable——869 另钉 item 1。374 flush-vs-sent bundled unbundling 在本页 item 2 续。

2. **看见发出去了 / 看见异步请求真发出去 / 看见发出去 is not already 已经收到 interchangeable / 已经 received interchangeable / 已经收到交差 interchangeable / 374 flush bundled interchangeable / 309 HasChannel interchangeable，也不是已经 flush bundled（374） interchangeable / 870 flush-notfourgates interchangeable / 374 flush item 1 叫了 interchangeable / 374 flush item 3 立刻 interchangeable，也不是已经定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事 bundled（374 item 2 余量） interchangeable / 374 flush item 2 interchangeable，也不是已经是四门（本页第一件事） interchangeable。**  
   官方写：看见发出去了，不是已经收到。看见异步请求真发出去，不是已经 received interchangeable——本页钉 not already received 单句。看见发出去，不是已经是四门（本页第一件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 2 续。

3. **看见异步 / 看见异步请求 / 看见异步在冲 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 374 flush bundled interchangeable / 33 four gates interchangeable，也不是已经 flush bundled（374） interchangeable / 870 flush-notfourgates interchangeable / 374 flush item 1 / 374 flush item 3，也不是已经定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事 bundled（374 item 2 余量） interchangeable / 374 flush item 2 interchangeable，也不是已经是四门（本页第一件事） interchangeable / 已经收到（本页第二件事） interchangeable。**  
   官方写：看见异步，不是已经交差。看见异步请求，不是已经 settled interchangeable——本页钉 not already settled 单句。看见异步在冲，不是已经收到（本页第二件事） interchangeable——三件事分开钉。374 flush-vs-sent bundled unbundling 在本页 item 2 续。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。flush bundled（374）、Flush 要把客户端排队的消息冲到服务端不是已经送到（374 item 1 余量 / 869）、立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走（374 item 3 余量）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **定期在冲 not already fourgates ≠ 374 / 307 interchangeable：** 官方把定期冲异步请求和一条连接已经是四门分开。
- **发出去了 not already received ≠ 已经收到 interchangeable：** 官方把发出去了和已经收到分开。
- **异步 not already settled ≠ 已经交差 interchangeable：** 官方把异步和已经交差分开；374 flush-vs-sent bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 定期在冲 | 不是 already fourgates | 不是一条连接就已经是四门 alone（307） |
| 发出去了 | 不是 already received | 不是叫了 already sent alone（869） |
| 异步 | 不是 already settled | 不是四门已经结算 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看定期 Flush 是为了让异步请求真发出去不是已经是四门 not already fourgates / not already received / not already settled 正式三事（374 余量），必须分开定期在冲 是不是 already fourgates interchangeable / 374 flush bundled interchangeable / flush-sold-as-sent interchangeable、发出去了 是不是 already received interchangeable、异步 是不是 already settled interchangeable。可以跳过「看见定期在冲就已经是四门 interchangeable / 就已经收到 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Flush。374 flush-vs-sent bundled unbundling 在本页 item 2 续（869 + 870）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- flush bundled。那是不变量 374。
- Flush 要把客户端排队的消息冲到服务端不是已经送到。那是不变量 374 item 1 余量 / 869。
- 立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走。那是不变量 374 item 3 余量。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
- 四门已经结算。那是不变量 33。
