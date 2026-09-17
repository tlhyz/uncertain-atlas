# 例：看见 Called immediately for sync request; returns when Flush response comes back is not already Echo Response Message the input string interchangeable / Commit lock wait for broadcast interchangeable / commit-empty-echo bundled item 3 interchangeable

**层次**：实现 / Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事（493 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Flush Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事（493 余量）/ not 673 flushusage-notimmediatesync interchangeable / not 672 flushusage-notperiodicasync interchangeable / not 493 flushusage-vs-echo bundled interchangeable」，不是 Flush Usage 正式三事 bundled（493），也不是 Signals messages queued should be flushed to server not Echo test（671）或 Called periodically ensure async requests actually sent not Echo test（672）。不要另写怎样写 Flush、怎样排队、怎样做成同步请求。

## 官方三件事

规范把 Flush Usage 里 Called immediately for sync request; returns when Flush response comes back 和「已经是 Echo Response Message the input string（492） interchangeable / 已经 Commit 里等广播就已经能往下走（310） interchangeable / 已经是 Commit 空请求 bundled（399）第三件事 interchangeable / 已经刷完 interchangeable」分开写成三件独立的实现事，不是「看见 Called immediately for sync request returns when Flush response comes back 就已经 Echo 回包 Message interchangeable / 就已经 Commit 能往下走 interchangeable / 就已经 commit-empty-echo bundled 第三件事 interchangeable」一件事：

1. **看见 Called immediately for sync request; returns when Flush response comes back / 看见立刻 Flush 是为了做成同步请求、Flush 回包回来才算这次同步 is not already 已经 Echo Response Message the input string（492） interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage item 3 Response Message interchangeable / 已经 Echo 回包 Message 是入参那串 interchangeable / 已经 Echo 回包栏 interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 673 flushusage-notimmediatesync interchangeable / 672 flushusage-notperiodicasync interchangeable / 671 flushusage-notechoqueued interchangeable / 493 flushusage-vs-echo bundled interchangeable / 493 flushusage item 1 Signals flush interchangeable / 493 flushusage item 2 periodically async interchangeable，也不是已经 Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事 bundled（493 item 3 余量） interchangeable / 493 flushusage item 3 interchangeable，也不是已经 Signals messages queued should be flushed to server bundled（493 item 1 余量 / 671） interchangeable / 394 echo-message-is-flush interchangeable / 492 echousage bundled interchangeable。**  
   官方 Usage 写：Called immediately for sync request; returns when Flush response comes back。看见 immediately for sync request，不是已经 Echo Response Message the input string（492） interchangeable——492 钉 Echo 回包栏，本页从 493 item 3 侧钉 not Echo Response Message 单句。看见 Flush 回包回来才算这次同步，不是已经 Flush Usage 正式三事 bundled（493） interchangeable——493 钉 bundled 三事，本页钉 Methods Flush Usage 同步回包单句。看见 returns when Flush response comes back，不是已经 Called periodically ensure async requests（672/493 item 2） interchangeable——672 另钉 item 2，本页钉 item 3 第一件事。493 flushusage vs echo bundled unbundling 在本页 item 3 续。

2. **看见 Called immediately for sync request / immediately for sync request / sync request / Flush response comes back is not already 已经 Commit 里等广播就已经能往下走（310） interchangeable / 310 commit-lock-vs-rpc interchangeable / 已经 Commit 锁 interchangeable / 已经等广播 interchangeable / 已经能往下走 interchangeable / 已经 Commit interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 673 flushusage-notimmediatesync interchangeable / 493 flushusage item 3 immediately sync interchangeable / 493 flushusage item 2 periodically async interchangeable / 671 flushusage-notechoqueued interchangeable，也不是已经 Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事 bundled（493 item 3 余量） interchangeable / 307 abci-conn-vs-gates interchangeable / 374 flush bundled interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第三件事 interchangeable / 374 flush bundled item 3 interchangeable / 481 commitpersist interchangeable / 587 finreturn interchangeable。**  
   官方把 Usage immediately for sync request / Flush response comes back 单句和 Commit 里等广播就已经能往下走路径分开——493 bundled 第三件事常与 310 混成「看见 Called immediately for sync request returns when Flush response comes back 就已经 Commit 锁 interchangeable / 就已经等广播 interchangeable / 就已经能往下走 interchangeable」，本页钉 not Commit lock 单句。看见 sync request / Flush response comes back，不是已经 Commit 里等广播就已经能往下走 interchangeable——310 钉 Commit 锁，本页钉 Flush 同步语义。看见 immediately for sync request，不是已经一条连接就已经是四门（307） interchangeable——307 另钉四门，本页钉 item 3 第二件事。

3. **看见 returns when Flush response comes back / Flush response comes back / 回包回来才算这次同步 is not already 已经 Commit 空请求 bundled（399）第三件事 interchangeable / 399 commit-empty-echo bundled interchangeable / 399 commit-empty-echo item 3 interchangeable / 已经 Echo 用来测实现就已经刷完 interchangeable / 已经测实现就已经交差 interchangeable / 492 echousage item 1 test implementation interchangeable，也不是已经 Flush Usage 正式三事 bundled（493） interchangeable / 673 flushusage-notimmediatesync interchangeable / 672 flushusage-notperiodicasync interchangeable / 493 flushusage item 1 Signals flush interchangeable / 493 flushusage item 2 periodically async interchangeable，也不是已经 Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事 bundled（493 item 3 余量） interchangeable / 492 echousage item 3 Response Message interchangeable / 335 finpersist interchangeable / 403 finafter interchangeable，也不是已经 Flush 要把客户端排队的消息冲到服务端 bundled（374）第三件事 interchangeable / 374 flush bundled interchangeable / 587 finreturn interchangeable。**  
   官方把 Usage Flush response comes back 单句和 Commit 空请求 bundled（399）第三件事路径分开——493 bundled 第三件事常与 399 混成「看见 returns when Flush response comes back 就已经 Echo 用来测实现就已经刷完 interchangeable / 就已经测实现就已经交差 interchangeable / 就已经 Commit 空请求 bundled 第三件事 interchangeable」，本页钉 not commit-empty-echo bundled item 3 单句。看见 Flush response comes back，不是已经 Echo 用来测实现就已经刷完 interchangeable——399 钉 Commit 空请求 bundled Echo，本页钉 Flush Usage 同步回包。看见 immediately for sync request，不是已经 Signals messages queued should be flushed interchangeable——671 另钉 item 1，本页钉 item 3 第三件事。493 flushusage vs echo bundled unbundling 在本页 item 3 完成。

怎样写 Flush、怎样排队、怎样做成同步请求是规范里的做法，本页不抄。Flush Usage 正式三事 bundled（493）、Signals messages queued should be flushed to server not Echo test（493 item 1 余量 / 671）、Called periodically ensure async requests actually sent not Echo test（493 item 2 余量 / 672）、Flush 要把客户端排队的消息冲到服务端 bundled（374）、Echo Usage 正式三事（492）、Commit 里等广播就已经能往下走（310）、Commit 空请求 bundled（399）、Echo 请求 Message 就已经是 Flush（394）是另外那套，本页不抄。

## 官方为什么这样拆

- **Called immediately for sync request returns when Flush response comes back not Echo Response Message ≠ 492 echousage-vs-flush interchangeable：** 官方把 Methods Flush Usage 同步回包单句和 Echo Response Message 栏路径分开。
- **immediately sync not Commit lock ≠ 310 commit-lock-vs-rpc interchangeable：** 官方把 Usage immediately for sync request / Flush response comes back 单句和 Commit 里等广播就已经能往下走路径分开。
- **Flush response comes back not commit-empty-echo bundled item 3 ≠ 399 commit-empty-echo bundled interchangeable：** 官方把 Usage Flush response comes back 单句和 Commit 空请求 bundled 第三件事路径分开；493 flushusage vs echo bundled unbundling 完成（673 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Called immediately for sync request returns when Flush response comes back | 不是 Echo Response Message（492） | 不是 Signals messages queued flush（671/493 item 1） |
| immediately for sync request / Flush response comes back | 不是 Commit lock wait for broadcast（310） | 不是 one connection four gates（307） |
| 回包回来才算这次同步 | 不是 commit-empty-echo bundled item 3（399） | 不是 periodically async sent（672/493 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Flush Usage Called immediately for sync request returns when Flush response comes back not Echo Response Message / not Commit lock / not commit-empty-echo bundled item 3 正式三事（493 余量），必须分开 Called immediately for sync request returns when Flush response comes back 是不是 Echo Response Message interchangeable / 492 echousage-vs-flush interchangeable / 492 echousage bundled interchangeable、immediately for sync request / Flush response comes back 是不是 Commit lock wait for broadcast interchangeable / 310 commit-lock-vs-rpc interchangeable / 481 commitpersist interchangeable、returns when Flush response comes back 是不是 commit-empty-echo bundled item 3 interchangeable / 399 commit-empty-echo bundled interchangeable / 335 finpersist interchangeable。可以跳过「看见 Called immediately for sync request returns when Flush response comes back 就已经 Echo 回包 Message interchangeable / 就已经 Commit 能往下走 interchangeable / 就已经 commit-empty-echo bundled 第三件事 interchangeable」。不要另写怎样写 Flush。493 flushusage vs echo bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Flush、怎样排队、怎样做成同步请求。
- Flush Usage 正式三事 bundled。那是不变量 493。
- Signals messages queued should be flushed to server not Echo test。那是不变量 493 item 1 余量 / 671。
- Called periodically ensure async requests actually sent not Echo test。那是不变量 493 item 2 余量 / 672。
- Flush 要把客户端排队的消息冲到服务端 bundled。那是不变量 374。
- Echo Usage 正式三事。那是不变量 492。
- Commit 里等广播就已经能往下走。那是不变量 310。
- Commit 空请求 bundled。那是不变量 399。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
