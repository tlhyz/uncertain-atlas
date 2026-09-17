# 例：看见 Signals that messages queued on the client should be flushed to the server 不是已经 Echo a string to test an ABCI client/server implementation interchangeable；看见 Called periodically to ensure async requests are actually sent 不是已经 Echo 用来测实现 interchangeable；看见 Called immediately for sync request; returns when Flush response comes back 不是已经 Echo 回包 Message 是入参那串 interchangeable

**层次**：实现 / Flush Usage 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Signals messages queued on client should be flushed to server 不是已经 Echo 测实现 interchangeable / Called periodically to ensure async requests are actually sent 不是已经 Echo 用来测实现 interchangeable / Called immediately for sync request returns when Flush response comes back 不是已经 Echo 回包 Message interchangeable / not 671 flushusage-notechoqueued interchangeable / not 493 flushusage-vs-echo bundled interchangeable」，不是 Flush 要把客户端排队的消息冲到服务端 bundled 三事（374），也不是 Echo Usage 正式三事（492）。不要另写怎样写 Flush、怎样排队、怎样做成同步请求。

## 官方三件事

规范把 Flush Usage 三句英文写成三件独立的实现事，不是「看见叫了 Flush 就已经 Echo 测实现 interchangeable、已经送到、已经能往下走」一件事：

1. **看见 Signals that messages queued on the client should be flushed to the server / 看见 Flush 要把客户端排队的消息冲到服务端 不是已经 Echo a string to test an ABCI client/server implementation interchangeable，也不是已经 HasChannel 就已经入队（309） interchangeable，也不是已经送到 / 已经入队 interchangeable。**  
   官方 Usage 写：Signals that messages queued on the client should be flushed to the server。看见 queued on client should be flushed to server，不是已经 Echo 用来测 client/server implementation（492） interchangeable——492 钉 Echo Usage 测实现，本页钉 Methods Flush Usage 冲队列单句。看见 Signals messages queued，不是已经 HasChannel 就已经入队（309） interchangeable——309 钉 P2P 通道，本页钉 ABCI 客户端排队。看见 should be flushed to server，不是已经 Echo 请求 Message 就已经是 Flush（394） interchangeable。
2. **看见 Called periodically to ensure async requests are actually sent / 看见定期 Flush 是为了让异步请求真发出去 不是已经 Echo 用来测实现 interchangeable，也不是已经一条连接就已经是四门（307） interchangeable，也不是已经交差 interchangeable。**  
   官方 Usage 写：Called periodically to ensure async requests are actually sent。看见 periodically / async requests actually sent，不是已经 Echo Usage 测实现（492） interchangeable——492 钉 Echo 测实现 vs Flush 冲队列，本页钉 Flush Usage 定期冲异步请求单句。看见 ensure async requests are actually sent，不是已经一条连接就已经是四门（307） interchangeable——307 钉同进程四门，本页钉客户端定期 Flush。看见 called periodically，不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第二件事 interchangeable——374 钉 Flush 三事 bundled，本页钉 Methods Flush Usage 正式三事。
3. **看见 Called immediately for sync request; returns when Flush response comes back / 看见立刻 Flush 是为了做成同步请求、Flush 回包回来才算这次同步 不是已经 Echo 回包 Message 是入参那串 interchangeable，也不是已经 Commit 里等广播就已经能往下走（310） interchangeable，也不是已经 Commit interchangeable。**  
   官方 Usage 写：Called immediately for sync request; returns when Flush response comes back。看见 immediately for sync request，不是已经 Echo Response Message the input string（492） interchangeable——492 钉 Echo 回包栏，本页钉 Flush 同步请求回包。看见 returns when Flush response comes back，不是已经 Echo 用来测实现就已经刷完（399 bundled 第三件事） interchangeable——399 钉 Commit 空请求 bundled Echo，本页钉 Flush Usage 同步回包。看见 sync request / Flush response comes back，不是已经 Commit 里等广播就已经能往下走（310） interchangeable——310 钉 Commit 锁，本页钉 Flush 同步语义。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。Flush 要把客户端排队的消息冲到服务端 bundled（374）、Echo Usage 正式三事（492）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）、Echo 请求 Message 就已经是 Flush（394）是另外那套，本页不抄。

## 官方为什么这样拆

- **Signals messages queued on client should be flushed to server ≠ Echo a string to test implementation：** 官方把 Flush 冲队列和 Echo 测实现分开。
- **Called periodically to ensure async requests are actually sent ≠ Echo 用来测实现：** 官方把定期冲异步请求和 Echo Usage 测实现分开。
- **Called immediately for sync request; returns when Flush response comes back ≠ Echo 回包 Message the input string：** 官方把 Flush 同步回包和 Echo 回包栏分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Signals messages queued should be flushed to server | 不是 Echo 测 implementation | 不是 HasChannel 就已经入队（309） |
| Called periodically to ensure async requests are actually sent | 不是 Echo 用来测实现 | 不是一条连接就已经是四门（307） |
| Called immediately for sync request; returns when Flush response comes back | 不是 Echo 回包 Message | 不是 Commit 里等广播就已经能往下走（310） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage 正式三事，必须分开 Signals messages queued should be flushed to server 是不是 Echo 测 implementation interchangeable / 已经 HasChannel 入队 / 已经 Echo Message 是 Flush、Called periodically to ensure async requests are actually sent 是不是 Echo 用来测实现 interchangeable / 已经是四门 / 已经 Flush bundled 第二件事、Called immediately for sync request returns when Flush response comes back 是不是 Echo 回包 Message interchangeable / 已经能往下走。可以跳过「看见 Flush 了就已经 Echo 测实现 interchangeable」。不要另写怎样写 Flush。493 flushusage vs echo bundled unbundling 续（671 item 1 完成；672 item 2）；精读 [`worked-example-flushusage-notechoqueued-vs-bundled.md`](worked-example-flushusage-notechoqueued-vs-bundled.md)（不变量 671 item 1）、[`worked-example-flushusage-notperiodicasync-vs-bundled.md`](worked-example-flushusage-notperiodicasync-vs-bundled.md)（不变量 672 item 2）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush 要把客户端排队的消息冲到服务端 bundled。那是不变量 374。
- Echo Usage 正式三事。那是不变量 492。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
