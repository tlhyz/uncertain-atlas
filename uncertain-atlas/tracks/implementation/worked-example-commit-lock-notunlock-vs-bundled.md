# 例：看见 Commit 前锁了内存池 is not already unlocked interchangeable / not already updated interchangeable / not already settled interchangeable

**层次**：实现 / Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量）/ not 975 commit-lock-notunlock interchangeable / not 310 commit-lock-vs-rpc bundled interchangeable」，不是锁 bundled（310），也不是半写已经原子（5），也不是 RECHECK 就已经是新交易（312/970）。不要另写怎样加锁或怎样调广播。

## 官方三件事

1. **看见 Commit 前锁了内存池 / 看见能一起更新四份状态 这把锁 is not already 已经解锁 interchangeable，也不是已经锁 bundled（310） interchangeable / 975 commit-lock-notunlock interchangeable / 974 commit-lock-notrpc interchangeable / 310 commit-lock item 1 默认锁 interchangeable，也不是已经 Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事 bundled（310 item 2 余量） interchangeable / 310 commit-lock item 2 interchangeable。**  
   官方写：调用 Commit 之前，CometBFT 会锁内存池并冲掉内存池连接。CometBFT 在为新块更新完之后才解锁内存池，而且这次更新和 Commit 异步。看见锁上了，不是已经解锁 interchangeable——本页从 310 item 2 侧钉 not already unlocked 单句。310 commit-lock vs rpc bundled unbundling 在本页 item 2 续。

2. **看见能一起更新 / 看见锁上了 / 这把锁 is not already 已经更新完 interchangeable，也不是已经锁 bundled（310） interchangeable / 975 commit-lock-notunlock interchangeable / 310 commit-lock item 3 等广播 interchangeable / 976 commit-lock-notbcast interchangeable，也不是已经半写已经原子 interchangeable / 5 atomic interchangeable。**  
   官方把能一起更新和已经更新完分开。看见能一起更新，不是已经更新完 interchangeable。本页钉 not already updated 单句。

3. **看见 Commit 回了 / 看见锁上了 / 这把锁 is not already 已经交差 interchangeable，也不是已经锁 bundled（310） interchangeable / 975 commit-lock-notunlock interchangeable / 974 commit-lock-notrpc interchangeable，也不是已经 RECHECK 就已经是新交易 interchangeable / 312/970 checktxstate-notrecheck interchangeable。**  
   官方把 Commit 回了和内存池锁已经按同一条路径放下分开。看见 Commit 回了，不是已经交差 interchangeable。310 commit-lock vs rpc bundled unbundling 在本页 item 2 续。

源码行号、怎样实现锁、怎样调广播是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Commit 前上锁 not already unlocked ≠ 已经解锁 interchangeable：** 官方把锁内存池、一起更新四份状态、异步解锁分开。
- **看见能一起更新 not already updated ≠ 已经更新完 interchangeable：** 官方把能一起更新和已经更新完分开。
- **看见 Commit 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Commit 回了和锁已经按同一条路径放下分开；310 commit-lock vs rpc bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 前上锁 | 不是已经解锁，也不是已经同步做完 | 不是半写已经原子（5） |
| 看见能一起更新 | 不是已经更新完 | 不是 RECHECK 就已经是新交易（312/970） |
| 看见 Commit 回了 | 不是已经交差 | 不是 Commit 里等广播就已经能往下走（976） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 前上锁 not already unlocked / not already updated / not already settled 正式三事（310 余量），必须分开是不是已经解锁、是不是已经更新完、是不是已经交差。可以跳过「看见有锁就已经能直接给 RPC 读」。不要另写怎样加锁或怎样调广播。310 commit-lock vs rpc bundled unbundling 在本页 item 2 续；续 [`worked-example-commit-lock-notbcast-vs-bundled.md`](worked-example-commit-lock-notbcast-vs-bundled.md)（不变量 976 item 3）。

## 本页不抄

- 源码行号、怎样实现全局锁、怎样调广播。
- 锁 bundled。那是不变量 310。
- 半写已经原子。那是不变量 5。
- RECHECK 就已经是新交易。那是不变量 312/970。
