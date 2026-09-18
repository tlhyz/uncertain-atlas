# 例：看见默认 Go 有全局锁不是已经能把状态直接给 RPC；看见 Commit 前锁了内存池不是已经解锁；看见 Commit 里等 broadcast_tx 不是已经能往下走

**层次**：实现 / ABCI 连接状态。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「默认锁不是已经 RPC 安全 / Commit 前上锁不是已经解锁 / Commit 里等广播不是已经能往下走」，不是一条连接已经是四门，也不是半写已经原子。不要另写怎样加锁或怎样调广播。

## 官方三件事

规范把四条 ABCI 连接上的状态和 Commit 写成三件独立的实现事，不是「看见接上就已经并发安全、已经解锁、已经能在 Commit 里广播」一件事：

1. **看见四条连接原则上并发 / 看见默认 Go 有全局锁 不是已经能把状态直接给 RPC，也不是已经没有并发。**  
   官方写：原则上四条 ABCI 连接彼此并发，应用必须保证状态线程安全。默认同进程客户端和默认 Go 套接字服务器都用一把全局锁，跨连接处理事件，所以**一点也不并发**。所有连接的 ABCI 消息按顺序、一次一条。官方还写：Go 应用若把读写都走 ABCI，可以靠这把锁得到线程安全。**直接把应用状态暴露给 RPC 可能不安全**；除非另有措施，查询都应走 ABCI `Query`。看见有锁，不是已经能直接给 RPC 读。看见默认顺序收，不是已经没有并发假设。看见编进同一个二进制，不是已经换了这把锁。
2. **看见 Commit 前锁了内存池 / 看见能一起更新四份状态 不是已经解锁，也不是已经和 Commit 同步做完。**  
   官方写：调用 `Commit` 之前，CometBFT 会锁内存池并冲掉内存池连接，保证这一步收不到新的内存池消息，好同时把四条连接的状态更新到最新已提交。官方还写：CometBFT **在为新块更新完之后**才解锁内存池，而且这次更新和 `Commit` **异步**。看见锁上了，不是已经解锁。看见能一起更新，不是已经更新完。看见 `Commit` 回了，不是内存池锁已经按同一条路径放下。
3. **看见 Commit 里调了 broadcast_tx 并等回执 不是已经能往下走。**  
   官方写警告：若处理 `Commit` 的逻辑去发 `/broadcast_tx_sync` 或 `/broadcast_tx`，并等回执再往下走，**会停死**。因为这些调用要拿内存池锁，而 CometBFT 在 `Commit` 期间正握着这把锁。看见能调广播，不是已经能继续。看见等回执，不是已经交差。看见同步内存池调用，不是已经允许写进 `Commit` 顺序逻辑。

源码行号、怎样实现锁、怎样调广播是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **默认全局锁 ≠ 已经 RPC 安全：** 官方把原则上并发、默认不并发、直接暴露状态可能不安全分开。
- **Commit 前上锁 ≠ 已经解锁：** 官方把锁内存池、一起更新四份状态、异步解锁分开。
- **Commit 里等广播 ≠ 已经能往下走：** 官方把警告写成停死，不是「广播已经发出」。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 默认 Go 全局锁 | 不是已经能把状态直接给 RPC | 不是一条连接已经是四门（307） |
| Commit 前锁内存池 | 不是已经解锁，也不是已经同步做完 | 不是半写已经原子（5） |
| Commit 里等 broadcast_tx | 不是已经能往下走 | 不是提案收了已经从池里删掉（301） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「ABCI 已经接上」，必须分开默认锁是不是已经 RPC 安全、Commit 前上锁是不是已经解锁、Commit 里等广播是不是已经能往下走。可以跳过「看见有锁就已经能直接给 RPC 读」。不要另写怎样加锁或怎样调广播。310 commitlock vs RPC bundled unbundling 完成（689 + 690 + 691）；精读 [`worked-example-commitlock-notrpcsafe-vs-bundled.md`](worked-example-commitlock-notrpcsafe-vs-bundled.md)（不变量 689 item 1）；[`worked-example-commitlock-notunlocked-vs-bundled.md`](worked-example-commitlock-notunlocked-vs-bundled.md)（不变量 690 item 2）；[`worked-example-commitlock-notbroadcast-vs-bundled.md`](worked-example-commitlock-notbroadcast-vs-bundled.md)（不变量 691 item 3）。

## 本页不抄

- 源码行号、怎样实现全局锁、怎样配套接字服务器。
- 怎样调 `/broadcast_tx`、怎样冲内存池、怎样写四份状态。
- 怎样写四门。那是不变量 33。
