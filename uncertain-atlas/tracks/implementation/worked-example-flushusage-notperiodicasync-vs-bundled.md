# 例：看见 Called periodically to ensure async requests are actually sent is not already Echo a string to test an ABCI client/server implementation interchangeable / one connection four gates interchangeable / Flush bundled item 2 interchangeable

**层次**：实现 / Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量）/ not 672 flushusage-notperiodicasync interchangeable / not 671 flushusage-notechoqueued interchangeable / not 493 flushusage-vs-echo bundled interchangeable」，不是 Flush Usage 正式三事 bundled（493），也不是 Signals messages queued should be flushed to server not Echo test（671）或 Flush 要把客户端排队的消息冲到服务端 bundled（374）。不要另写怎样写 Flush、怎样排队、怎样做成同步请求。

## 官方三件事

规范把 Flush Usage 里 Called periodically to ensure async requests are actually sent 和「已经是 Echo a string to test an ABCI client/server implementation（492） interchangeable / 已经一条连接就已经是四门（307） interchangeable / 已经是 Flush 要把客户端排队的消息冲到服务端 bundled（374）第二件事 interchangeable / 已经交差 interchangeable」分开写成三件独立的实现事，不是「看见 Called periodically ensure async requests actually sent 就已经 Echo 测 implementation interchangeable / 就已经四门 interchangeable / 就已经 Flush bundled 第二件事 interchangeable」一件事：

1. **看见 Called periodically to ensure async requests are actually sent / 看见定期 Flush 是为了让异步请求真发出去 is not already 已经 Echo a string to test an ABCI client/server implementation（492） interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage item 1 test implementation interchangeable / 已经 Echo 用来测 client/server implementation interchangeable / 已经 Echo 测实现 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 672 flushusage-notperiodicasync interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage-vs-echo bundled interchangeable / 493 flushusage item 1 Signals flush interchangeable / 493 flushusage item 3 immediately sync interchangeable，也不是已经 Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事 bundled（493 item 2 余量） interchangeable / 493 flushusage item 2 interchangeable，也不是已经 Signals messages queued should be flushed to server bundled（493 item 1 余量 / 671） interchangeable / 374 flush bundled interchangeable / 492 echousage bundled interchangeable。**  
   官方 Usage 写：Called periodically to ensure async requests are actually sent。看见 periodically / async requests actually sent，不是已经 Echo 用来测 client/server implementation（492） interchangeable——492 钉 Echo Usage 测实现，本页从 493 item 2 侧钉 not Echo test 单句。看见定期 Flush 是为了让异步请求真发出去，不是已经 Flush Usage 正式三事 bundled（493） interchangeable——493 钉 bundled 三事，本页钉 Methods Flush Usage 定期冲异步请求单句。看见 called periodically，不是已经 Signals messages queued should be flushed（671/493 item 1） interchangeable——671 另钉 item 1，本页钉 item 2 第一件事。493 flushusage vs echo bundled unbundling 在本页 item 2 续。

2. **看见 Called periodically / periodically / async requests are actually sent / 定期 Flush 让异步请求真发出去 is not already 已经一条连接就已经是四门（307） interchangeable / 307 abci-conn-vs-gates interchangeable / 已经同进程四门 interchangeable / 已经一条连接就是四门 interchangeable / 已经 ABCI 连接就是四门 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 672 flushusage-notperiodicasync interchangeable / 493 flushusage item 2 periodically async interchangeable / 493 flushusage item 3 immediately sync interchangeable / 671 flushusage-notechoqueued interchangeable，也不是已经 Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事 bundled（493 item 2 余量） interchangeable / 309 haschannel queued interchangeable / 310 commit-lock-vs-rpc interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第一件事 interchangeable / 374 flush bundled item 1 interchangeable / 492 echousage item 2 Request Message interchangeable。**  
   官方把 Usage periodically ensure async requests 单句和一条连接就已经是四门路径分开——493 bundled 第二件事常与 307 混成「看见 Called periodically ensure async requests actually sent 就已经一条连接就是四门 interchangeable / 就已经同进程四门 interchangeable / 就已经 ABCI 连接 interchangeable」，本页钉 not one connection four gates 单句。看见 async requests actually sent，不是已经一条连接就已经是四门 interchangeable——307 钉同进程四门，本页钉客户端定期 Flush。看见 called periodically，不是已经 HasChannel 就已经入队（309） interchangeable——309 另钉 P2P 通道，本页钉 item 2 第二件事。

3. **看见 Called periodically to ensure async requests are actually sent / ensure async requests are actually sent / 让异步请求真发出去 is not already 已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第二件事 interchangeable / 374 flush bundled interchangeable / 374 flush bundled item 2 interchangeable / 374 flush-vs-sent interchangeable / 已经 Flush bundled 第二件事 interchangeable / 已经送到 interchangeable / 已经交差 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 672 flushusage-notperiodicasync interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage item 1 Signals flush interchangeable / 493 flushusage item 3 immediately sync interchangeable，也不是已经 Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事 bundled（493 item 2 余量） interchangeable / 374 flush bundled item 1 interchangeable / 492 echousage-vs-flush interchangeable / 394 echo-message-is-flush interchangeable，也不是已经 Called immediately for sync request returns when Flush response comes back bundled（493 item 3 余量 / 673） interchangeable / 310 commit-lock-vs-rpc interchangeable / 399 commit-empty-echo bundled interchangeable。**  
   官方把 Usage periodically ensure async requests 单句和 Flush bundled（374）第二件事路径分开——493 bundled 第二件事常与 374 混成「看见 Called periodically ensure async requests actually sent 就已经 Flush bundled 第二件事 interchangeable / 就已经送到 interchangeable / 就已经交差 interchangeable」，本页钉 not Flush bundled item 2 单句。看见 ensure async requests are actually sent，不是已经 Flush 要把客户端排队的消息冲到服务端 bundled 第二件事 interchangeable——374 钉 bundled 三事，本页钉 Methods Flush Usage 定期冲异步请求单句。看见 called periodically，不是已经 Called immediately for sync request returns when Flush response comes back interchangeable——673 另钉 item 3，本页钉 item 2 第三件事。493 flushusage vs echo bundled unbundling 在本页 item 2 完成。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。Flush Usage 正式三事 bundled（493）、Signals messages queued should be flushed to server not Echo test（493 item 1 余量 / 671）、Called immediately for sync request returns when Flush response comes back（493 item 3 余量 / 673）、Flush 要把客户端排队的消息冲到服务端 bundled（374）、Echo Usage 正式三事（492）、HasChannel 就已经入队（309）、一条连接就已经是四门（307）、Commit 里等广播就已经能往下走（310）、Echo 请求 Message 就已经是 Flush（394）是另外那套，本页不抄。

## 官方为什么这样拆

- **Called periodically ensure async requests actually sent not Echo test ≠ 492 echousage-vs-flush interchangeable：** 官方把 Methods Flush Usage 定期冲异步请求单句和 Echo Usage 测实现路径分开。
- **periodically async sent not one connection four gates ≠ 307 abci-conn-vs-gates interchangeable：** 官方把 Usage periodically ensure async requests 单句和一条连接就已经是四门路径分开。
- **periodically async sent not Flush bundled item 2 ≠ 374 flush bundled interchangeable：** 官方把 Usage periodically ensure async requests 单句和 Flush bundled（374）第二件事路径分开；493 flushusage vs echo bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Called periodically ensure async requests actually sent | 不是 Echo test implementation（492） | 不是 Signals messages queued flush（671/493 item 1） |
| periodically / async requests actually sent | 不是 one connection four gates（307） | 不是 HasChannel queued（309） |
| 让异步请求真发出去 | 不是 Flush bundled item 2（374） | 不是 immediately sync Flush response（673/493 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Called periodically ensure async requests actually sent not Echo test / not one connection four gates / not Flush bundled item 2 正式三事（493 余量），必须分开 Called periodically ensure async requests actually sent 是不是 Echo test implementation interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage bundled interchangeable、periodically / async requests actually sent 是不是 one connection four gates interchangeable / 307 abci-conn-vs-gates interchangeable / 309 haschannel queued interchangeable、ensure async requests are actually sent 是不是 Flush bundled item 2 interchangeable / 374 flush bundled interchangeable / 374 flush-vs-sent interchangeable。可以跳过「看见 Called periodically ensure async requests actually sent 就已经 Echo 测 implementation interchangeable / 就已经四门 interchangeable / 就已经 Flush bundled 第二件事 interchangeable」。不要另写怎样写 Flush。493 flushusage vs echo bundled unbundling 在本页 item 2 完成；续 [`worked-example-flushusage-notimmediatesync-vs-bundled.md`](worked-example-flushusage-notimmediatesync-vs-bundled.md)（不变量 673 item 3）。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush Usage 正式三事 bundled。那是不变量 493。
- Signals messages queued should be flushed to server not Echo test。那是不变量 493 item 1 余量 / 671。
- Called immediately for sync request returns when Flush response comes back。那是不变量 493 item 3 余量 / 673。
- Flush 要把客户端排队的消息冲到服务端 bundled。那是不变量 374。
- Echo Usage 正式三事。那是不变量 492。
- HasChannel 就已经入队。那是不变量 309。
- 一条连接就已经是四门。那是不变量 307。
- Commit 里等广播就已经能往下走。那是不变量 310。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
