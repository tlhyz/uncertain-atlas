# 例：看见默认 Go 有全局锁 is not already RPC-safe interchangeable / not already no-concurrency interchangeable / not already settled interchangeable

**层次**：实现 / 默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量）/ not 974 commit-lock-notrpc interchangeable / not 310 commit-lock-vs-rpc bundled interchangeable」，不是锁 bundled（310），也不是一条连接已经是四门（307），也不是立刻执行就已经是 ExecuteTxState（311/972）。不要另写怎样加锁或怎样调广播。

## 官方三件事

1. **看见四条连接原则上并发 / 看见默认 Go 有全局锁 这把锁 is not already 已经能把状态直接给 RPC interchangeable，也不是已经锁 bundled（310） interchangeable / 974 commit-lock-notrpc interchangeable / 975 commit-lock-notunlock interchangeable / 310 commit-lock item 2 Commit 前上锁 interchangeable，也不是已经默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事 bundled（310 item 1 余量） interchangeable / 310 commit-lock item 1 interchangeable。**  
   官方写：原则上四条 ABCI 连接彼此并发，应用必须保证状态线程安全。默认同进程客户端和默认 Go 套接字服务器都用一把全局锁。直接把应用状态暴露给 RPC 可能不安全；除非另有措施，查询都应走 ABCI Query。看见有锁，不是已经能直接给 RPC 读 interchangeable——本页从 310 item 1 侧钉 not already RPC-safe 单句。310 commit-lock vs rpc bundled unbundling 在本页 item 1 启动。

2. **看见默认顺序收 / 看见有锁 / 这把锁 is not already 已经没有并发假设 interchangeable，也不是已经锁 bundled（310） interchangeable / 974 commit-lock-notrpc interchangeable / 310 commit-lock item 3 等广播 interchangeable / 976 commit-lock-notbcast interchangeable，也不是已经一条连接已经是四门 interchangeable / 307 abci-conn interchangeable。**  
   官方把默认顺序收和已经没有并发假设分开——310 bundled 第一件事常与 307 混成「看见有锁就已经 RPC 安全或已经是四门 interchangeable」，本页钉 not already no-concurrency 单句。

3. **看见编进同一个二进制 / 看见有锁 / 这把锁 is not already 已经交差 interchangeable，也不是已经锁 bundled（310） interchangeable / 974 commit-lock-notrpc interchangeable / 975 commit-lock-notunlock interchangeable，也不是已经立刻执行就已经是 ExecuteTxState interchangeable / 311/972 candidate-notexec interchangeable。**  
   官方把编进同一个二进制和已经换了这把锁分开。看见编进同一个二进制，不是已经交差 interchangeable。310 commit-lock vs rpc bundled unbundling 在本页 item 1 启动。

源码行号、怎样实现锁、怎样调广播是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **默认锁 not already RPC-safe ≠ 已经能把状态直接给 RPC interchangeable：** 官方把原则上并发、默认不并发、直接暴露状态可能不安全分开。
- **看见默认顺序收 not already no-concurrency ≠ 已经没有并发假设 interchangeable：** 官方把默认顺序收和已经没有并发假设分开。
- **看见编进同一个二进制 not already settled ≠ 已经交差 interchangeable：** 官方把编进同一个二进制和已经换了这把锁分开；310 commit-lock vs rpc bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 默认锁 | 不是已经能把状态直接给 RPC | 不是一条连接已经是四门（307） |
| 看见默认顺序收 | 不是已经没有并发假设 | 不是立刻执行就已经是 ExecuteTxState（311/972） |
| 看见编进同一个二进制 | 不是已经交差 | 不是 Commit 前上锁就已经解锁（975） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看默认锁 not already RPC-safe / not already no-concurrency / not already settled 正式三事（310 余量），必须分开是不是已经 RPC 安全、是不是已经没有并发假设、是不是已经交差。可以跳过「看见有锁就已经能直接给 RPC 读」。不要另写怎样加锁或怎样调广播。310 commit-lock vs rpc bundled unbundling 在本页 item 1 启动；续 [`worked-example-commit-lock-notunlock-vs-bundled.md`](worked-example-commit-lock-notunlock-vs-bundled.md)（不变量 975 item 2）。

## 本页不抄

- 源码行号、怎样实现全局锁、怎样调广播。
- 锁 bundled。那是不变量 310。
- 一条连接已经是四门。那是不变量 307。
- 立刻执行就已经是 ExecuteTxState。那是不变量 311/972。
