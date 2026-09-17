# 例：看见 Commit 里等 broadcast_tx is not already proceeding interchangeable / not already allowed interchangeable / not already settled interchangeable

**层次**：实现 / Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) ABCI connections / Commit lock。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量）/ not 976 commit-lock-notbcast interchangeable / not 310 commit-lock-vs-rpc bundled interchangeable」，不是锁 bundled（310），也不是提案收了已经从池里删掉（301），也不是四门已经结算（33）。不要另写怎样加锁或怎样调广播。

## 官方三件事

1. **看见 Commit 里调了 broadcast_tx 并等回执 这份等待 is not already 已经能往下走 interchangeable，也不是已经锁 bundled（310） interchangeable / 976 commit-lock-notbcast interchangeable / 974 commit-lock-notrpc interchangeable / 975 commit-lock-notunlock interchangeable / 310 commit-lock item 1 默认锁 interchangeable，也不是已经 Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事 bundled（310 item 3 余量） interchangeable / 310 commit-lock item 3 interchangeable。**  
   官方写警告：若处理 Commit 的逻辑去发 /broadcast_tx_sync 或 /broadcast_tx，并等回执再往下走，会停死。因为这些调用要拿内存池锁，而 CometBFT 在 Commit 期间正握着这把锁。看见能调广播，不是已经能继续 interchangeable——本页从 310 item 3 侧钉 not already proceeding 单句。310 commit-lock vs rpc bundled unbundling 在本页 item 3 完成。

2. **看见能调广播 / 看见等回执 / 这份等待 is not already 已经允许写进 Commit 顺序逻辑 interchangeable，也不是已经锁 bundled（310） interchangeable / 976 commit-lock-notbcast interchangeable / 310 commit-lock item 2 Commit 前上锁 interchangeable / 975 commit-lock-notunlock interchangeable，也不是已经提案收了已经从池里删掉 interchangeable / 301 pool-delete interchangeable。**  
   官方把能调广播和已经允许写进 Commit 顺序逻辑分开。看见能调广播，不是已经允许 interchangeable。本页钉 not already allowed 单句。

3. **看见同步内存池调用 / 看见等回执 / 这份等待 is not already 已经交差 interchangeable，也不是已经锁 bundled（310） interchangeable / 976 commit-lock-notbcast interchangeable / 974 commit-lock-notrpc interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把同步内存池调用和已经交差分开。看见同步内存池调用，不是已经交差 interchangeable。310 commit-lock vs rpc bundled unbundling 在本页 item 3 完成。

源码行号、怎样实现锁、怎样调广播是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Commit 里等广播 not already proceeding ≠ 已经能往下走 interchangeable：** 官方把警告写成停死，不是广播已经发出。
- **看见能调广播 not already allowed ≠ 已经允许写进 Commit 顺序逻辑 interchangeable：** 官方把能调广播和已经允许写进 Commit 分开。
- **看见同步内存池调用 not already settled ≠ 已经交差 interchangeable：** 官方把同步内存池调用和已经交差分开；310 commit-lock vs rpc bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 里等广播 | 不是已经能往下走 | 不是提案收了已经从池里删掉（301） |
| 看见能调广播 | 不是已经允许写进 Commit | 不是四门已经结算（33） |
| 看见同步内存池调用 | 不是已经交差 | 不是默认锁就已经 RPC 安全（974） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit 里等广播 not already proceeding / not already allowed / not already settled 正式三事（310 余量），必须分开是不是已经能往下走、是不是已经允许、是不是已经交差。可以跳过「看见有锁就已经能直接给 RPC 读」。不要另写怎样加锁或怎样调广播。310 commit-lock vs rpc bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 源码行号、怎样实现全局锁、怎样调广播。
- 锁 bundled。那是不变量 310。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
