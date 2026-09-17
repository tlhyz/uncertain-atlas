# 例：看见 Signals that messages queued on the client should be flushed to the server is not already Echo a string to test an ABCI client/server implementation interchangeable / HasChannel queued interchangeable / Echo request Message is Flush interchangeable

**层次**：实现 / Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量）/ not 671 flushusage-notechoqueued interchangeable / not 493 flushusage-vs-echo bundled interchangeable」，不是 Flush Usage 正式三事 bundled（493），也不是 Flush 要把客户端排队的消息冲到服务端 bundled（374）或 Echo Usage 正式三事（492）。不要另写怎样写 Flush、怎样排队、怎样做成同步请求。

## 官方三件事

规范把 Flush Usage 里 Signals that messages queued on the client should be flushed to the server 和「已经是 Echo a string to test an ABCI client/server implementation（492） interchangeable / 已经是 HasChannel 就已经入队（309） interchangeable / 已经是 Echo 请求 Message 就已经是 Flush（394） interchangeable / 已经送到 interchangeable」分开写成三件独立的实现事，不是「看见 Signals messages queued should be flushed 就已经 Echo 测 implementation interchangeable / 就已经 HasChannel 入队 interchangeable / 就已经 Echo Message 是 Flush interchangeable」一件事：

1. **看见 Signals that messages queued on the client should be flushed to the server / 看见 Flush 要把客户端排队的消息冲到服务端 is not already 已经 Echo a string to test an ABCI client/server implementation（492） interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage item 1 test implementation interchangeable / 已经 Echo 用来测 client/server implementation interchangeable / 已经 Echo 测实现 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage-vs-echo bundled interchangeable / 493 flushusage item 2 periodically async interchangeable / 493 flushusage item 3 immediately sync interchangeable，也不是已经 Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事 bundled（493 item 1 余量） interchangeable / 493 flushusage item 1 interchangeable，也不是已经 Called periodically to ensure async requests are actually sent bundled（493 item 2 余量 / 672） interchangeable / 374 flush bundled interchangeable / 492 echousage bundled interchangeable。**  
   官方 Usage 写：Signals that messages queued on the client should be flushed to the server。看见 queued on client should be flushed to server，不是已经 Echo 用来测 client/server implementation（492） interchangeable——492 钉 Echo Usage 测实现，本页从 493 item 1 侧钉 not Echo test 单句。看见 Signals messages queued，不是已经 Flush Usage 正式三事 bundled（493） interchangeable——493 钉 bundled 三事，本页钉 Methods Flush Usage 冲队列单句。看见 should be flushed to server，不是已经 Called periodically ensure async requests（493 item 2 余量） interchangeable——672 另钉 item 2，本页钉 item 1 第一件事。493 flushusage vs echo bundled unbundling 在本页 item 1 启动。

2. **看见 Signals messages queued on the client / queued on client should be flushed / 客户端排队的消息要冲到服务端 is not already 已经 HasChannel 就已经入队（309） interchangeable / 309 haschannel queued interchangeable / 已经 HasChannel 入队 interchangeable / 已经 P2P 通道入队 interchangeable / 已经送到 interchangeable / 已经入队 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage item 1 Signals flush interchangeable / 493 flushusage item 3 immediately sync interchangeable / 374 flush bundled item 1 interchangeable，也不是已经 Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事 bundled（493 item 1 余量） interchangeable / 307 abci-conn-vs-gates interchangeable / 310 commit-lock-vs-rpc interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第二件事 interchangeable / 374 flush bundled interchangeable / 492 echousage item 2 Request Message interchangeable。**  
   官方把 Usage Signals messages queued 单句和 HasChannel 就已经入队路径分开——493 bundled 第一件事常与 309 混成「看见 Signals messages queued should be flushed 就已经 HasChannel 入队 interchangeable / 就已经 P2P 通道 interchangeable / 就已经送到 interchangeable」，本页钉 not HasChannel queued 单句。看见 queued on client，不是已经 HasChannel 就已经入队 interchangeable——309 钉 P2P 通道，本页钉 ABCI 客户端排队。看见 should be flushed to server，不是已经一条连接就已经是四门（307） interchangeable——307 另钉四门，本页钉 item 1 第二件事。

3. **看见 Signals that messages queued on the client should be flushed to the server / should be flushed to server / 要冲到服务端 is not already 已经 Echo 请求 Message 就已经是 Flush（394） interchangeable / 394 echo-message-is-flush interchangeable / 已经 Echo 请求 Message 是 Flush interchangeable / 已经 Echo Message 是 Flush interchangeable / 492 echousage item 2 Request Message interchangeable / 492 echousage item 3 Response Message interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage item 2 periodically async interchangeable / 493 flushusage item 1 Signals flush interchangeable，也不是已经 Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事 bundled（493 item 1 余量） interchangeable / 374 flush bundled interchangeable / 399 commit-empty-echo bundled interchangeable / 310 commit-lock-vs-rpc interchangeable，也不是已经 Called immediately for sync request returns when Flush response comes back bundled（493 item 3 余量 / 673） interchangeable / 492 echousage item 3 Response Message interchangeable / 399 commit-empty-echo item 3 interchangeable。**  
   官方把 Usage Signals messages queued 单句和 Echo 请求 Message 就已经是 Flush 路径分开——493 bundled 第一件事常与 394 混成「看见 Signals messages queued should be flushed 就已经 Echo 请求 Message 是 Flush interchangeable / 就已经 Echo Message 是 Flush interchangeable / 就已经送到 interchangeable」，本页钉 not Echo request Message is Flush 单句。看见 should be flushed to server，不是已经 Echo 请求 Message 就已经是 Flush interchangeable——394 钉 Request vs Flush，本页钉 Flush Usage 冲队列语义。看见 Signals messages queued，不是已经 Echo 回包 Message 是入参那串 interchangeable——492 另钉 Response 栏，本页钉 item 1 第三件事。493 flushusage vs echo bundled unbundling 在本页 item 1 启动。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。Flush Usage 正式三事 bundled（493）、Called periodically to ensure async requests are actually sent（493 item 2 余量 / 672）、Called immediately for sync request returns when Flush response comes back（493 item 3 余量 / 673）、Flush 要把客户端排队的消息冲到服务端 bundled（374）、Echo Usage 正式三事（492）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）、Echo 请求 Message 就已经是 Flush（394）是另外那套，本页不抄。

## 官方为什么这样拆

- **Signals messages queued should be flushed to server not Echo test ≠ 492 echousage-vs-flush interchangeable：** 官方把 Methods Flush Usage 冲队列单句和 Echo Usage 测实现路径分开。
- **Signals messages queued not HasChannel queued ≠ 309 haschannel queued interchangeable：** 官方把 Usage Signals messages queued 单句和 HasChannel 就已经入队路径分开。
- **Signals messages queued not Echo request Message is Flush ≠ 394 echo-message-is-flush interchangeable：** 官方把 Usage Signals messages queued 单句和 Echo 请求 Message 就已经是 Flush 路径分开；493 flushusage vs echo bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Signals messages queued should be flushed to server | 不是 Echo test implementation（492） | 不是 Called periodically async（672/493 item 2） |
| queued on client should be flushed | 不是 HasChannel queued（309） | 不是 一条连接就是四门（307） |
| should be flushed to server | 不是 Echo request Message is Flush（394） | 不是 immediately sync Flush response（673/493 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Signals messages queued should be flushed to server not Echo test / not HasChannel queued / not Echo request Message is Flush 正式三事（493 余量），必须分开 Signals messages queued should be flushed to server 是不是 Echo test implementation interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage bundled interchangeable、queued on client should be flushed 是不是 HasChannel queued interchangeable / 309 haschannel queued interchangeable / 307 abci-conn-vs-gates interchangeable、should be flushed to server 是不是 Echo request Message is Flush interchangeable / 394 echo-message-is-flush interchangeable / 374 flush bundled interchangeable。可以跳过「看见 Signals messages queued should be flushed 就已经 Echo 测 implementation interchangeable / 就已经 HasChannel 入队 interchangeable / 就已经 Echo Message 是 Flush interchangeable」。不要另写怎样写 Flush。493 flushusage vs echo bundled unbundling 在本页 item 1 完成；续 [`worked-example-flushusage-notperiodicasync-vs-bundled.md`](worked-example-flushusage-notperiodicasync-vs-bundled.md)（不变量 672 item 2）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush Usage 正式三事 bundled。那是不变量 493。
- Called periodically to ensure async requests are actually sent。那是不变量 493 item 2 余量 / 672。
- Called immediately for sync request returns when Flush response comes back。那是不变量 493 item 3 余量 / 673。
- Flush 要把客户端排队的消息冲到服务端 bundled。那是不变量 374。
- Echo Usage 正式三事。那是不变量 492。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
