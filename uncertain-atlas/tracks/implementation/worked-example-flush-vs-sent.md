# 例：看见 Flush 要把客户端排队的消息冲到服务端不是已经送到；看见定期 Flush 是为了让异步请求真发出去不是已经是四门；看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走

**层次**：实现 / Flush。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Flush 要把客户端排队的消息冲到服务端不是已经送到 / 定期 Flush 是为了让异步请求真发出去不是已经是四门 / 立刻 Flush 是为了做成同步请求、回包回来才算这次同步不是已经能往下走」，不是 HasChannel 就已经入队，也不是一条连接就已经是四门。不要另写怎样写 Flush。374 flush-vs-sent bundled unbundling 完成（869+870+871）；精读 [`worked-example-flush-notsent-vs-bundled.md`](worked-example-flush-notsent-vs-bundled.md)（不变量 869 item 1）；精读 [`worked-example-flush-notfourgates-vs-bundled.md`](worked-example-flush-notfourgates-vs-bundled.md)（不变量 870 item 2）；精读 [`worked-example-flush-notproceed-vs-bundled.md`](worked-example-flush-notproceed-vs-bundled.md)（不变量 871 item 3）。

## 官方三件事

规范把 Flush 要把客户端排队的消息冲到服务端、定期 Flush 是为了让异步请求真发出去、立刻 Flush 是为了做成同步请求、回包回来才算这次同步写成三件独立的实现事，不是「看见叫了 Flush 就已经送到、已经是四门、已经能往下走」一件事：

1. **看见 Flush 要把客户端排队的消息冲到服务端 / 看见叫了 Flush 不是已经送到，也不是已经入队。**  
   官方写：Flush 表示客户端排队的消息该冲到服务端。看见叫了，不是已经送到。看见在冲，不是已经入队。看见排队了，不是已经断开。
2. **看见定期 Flush 是为了让异步请求真发出去 / 看见定期在冲 不是已经是四门，也不是已经交差。**  
   官方写：客户端实现会定期叫 Flush，好让异步请求真的发出去。看见定期在冲，不是已经是四门。看见发出去了，不是已经收到。看见异步，不是已经交差。
3. **看见立刻 Flush 是为了做成同步请求、回包回来才算这次同步 / 看见立刻叫了 不是已经能往下走，也不是已经 Commit。**  
   官方写：立刻叫 Flush 是为了做成同步请求；Flush 回包回来，这次同步才算完。看见立刻叫了，不是已经能往下走。看见回包回来，不是已经 Commit。看见同步了，不是已经解锁。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。HasChannel 就已经入队是不变量 309，本页不抄。

## 官方为什么这样拆

- **Flush 要把客户端排队的消息冲到服务端 ≠ 已经送到：** 官方把该冲出去和已经送到分开。
- **定期 Flush 是为了让异步请求真发出去 ≠ 已经是四门：** 官方把定期冲异步请求和一条连接已经是四门分开。
- **立刻 Flush 是为了做成同步请求、回包回来才算这次同步 ≠ 已经能往下走：** 官方把立刻同步和已经能往下走分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Flush 要把客户端排队的消息冲到服务端 | 不是已经送到 | 不是 HasChannel 就已经入队（309） |
| 定期 Flush 是为了让异步请求真发出去 | 不是已经是四门 | 不是一条连接就已经是四门（307） |
| 立刻 Flush 是为了做成同步请求、回包回来才算这次同步 | 不是已经能往下走 | 不是 Commit 里等广播就已经能往下走（310） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 Flush 就已经送到、已经是四门、已经能往下走」，必须分开 Flush 要把客户端排队的消息冲到服务端是不是已经送到、定期 Flush 是为了让异步请求真发出去是不是已经是四门、立刻 Flush 是为了做成同步请求、回包回来才算这次同步是不是已经能往下走。可以跳过「看见叫了 Flush 就已经送到」。不要另写怎样写 Flush。374 flush-vs-sent bundled unbundling 完成（869+870+871）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
