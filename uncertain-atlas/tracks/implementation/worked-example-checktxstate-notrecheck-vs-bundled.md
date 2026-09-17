# 例：看见 RECHECK is not already new-tx interchangeable / not already unlocked interchangeable / not already settled interchangeable

**层次**：实现 / RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量）/ not 970 checktxstate-notrecheck interchangeable / not 312 checktxstate-vs-execute bundled interchangeable」，不是 CheckTxState bundled（312），也不是提案收了已经从池里删掉（301），也不是 CheckTx 最终不再振荡（328）。不要另写怎样实现 CheckTx 或怎样再验。

## 官方三件事

1. **看见 Commit 之后又跑了 CheckTx / 看见 Type 是 RECHECK 这份再验 is not already 已经是一笔新交易 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 970 checktxstate-notrecheck interchangeable / 968 checktxstate-notexec interchangeable / 969 checktxstate-notsame interchangeable / 312 checktxstate item 1 CheckTx 过了 interchangeable，也不是已经 RECHECK not already new-tx / not already unlocked / not already settled 正式三事 bundled（312 item 3 余量） interchangeable / 312 checktxstate item 3 interchangeable。**  
   官方写：Commit 返回之后，还握着内存池锁，会对本地池里剩下的、已经滤掉本块交易的那些，再跑一遍 CheckTx。CheckTxRequest 的 Type 标明这是新交易还是再验。看见又跑了，不是已经是新交易 interchangeable——本页从 312 item 3 侧钉 not already new-tx 单句。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

2. **看见 Type 在 / 看见又跑了 / 这份再验 is not already 已经当 NEW 处理 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 970 checktxstate-notrecheck interchangeable / 312 checktxstate item 2 同时在改 interchangeable / 969 checktxstate-notsame interchangeable，也不是已经提案收了已经从池里删掉 interchangeable / 301 pool-delete interchangeable。**  
   官方把 Type 在和已经当 NEW 处理分开。看见 Type 在，不是已经当 NEW 处理 interchangeable。本页钉 not already unlocked 侧的 Type 单句，并钉 not already new-as-NEW。

3. **看见 Commit 回了 / 看见又跑了 / 这份再验 is not already 已经交差 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 970 checktxstate-notrecheck interchangeable / 968 checktxstate-notexec interchangeable，也不是已经 CheckTx 最终不再振荡 interchangeable / 328 checktx-oscillate interchangeable。**  
   官方把 Commit 回了和锁已经放下分开。看见 Commit 回了，不是已经交差 interchangeable。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

怎样实现两份状态、怎样再验、索引器去重是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **RECHECK not already new-tx ≠ 已经是新交易 interchangeable：** 官方把 Commit 之后还握着锁再验，和新交易进来分开。
- **看见 Type 在 not already unlocked ≠ 已经当 NEW 处理 interchangeable：** 官方把 Type 在和已经当 NEW 处理分开。
- **看见 Commit 回了 not already settled ≠ 已经交差 interchangeable：** 官方把 Commit 回了和锁已经放下分开；312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| RECHECK | 不是已经是新交易，也不是已经解锁 | 不是提案收了已经从池里删掉（301） |
| 看见 Type 在 | 不是已经当 NEW 处理 | 不是 CheckTx 最终不再振荡（328） |
| 看见 Commit 回了 | 不是已经交差 | 不是 CheckTx 过了就已经按 ExecuteTxState 验过（968） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 RECHECK not already new-tx / not already unlocked / not already settled 正式三事（312 余量），必须分开是不是已经是新交易、是不是已经当 NEW 处理、是不是已经交差。可以跳过「看见过了就已经按将要执行的那份验过」。不要另写怎样实现 CheckTx 或怎样再验。312 checktxstate vs execute bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样实现两份状态、怎样再验、索引器去重。
- CheckTxState bundled。那是不变量 312。
- 提案收了已经从池里删掉。那是不变量 301。
- CheckTx 最终不再振荡。那是不变量 328。
