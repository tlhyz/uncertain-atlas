# 例：看见两份状态同时在改 is not already same-state interchangeable / not already merged interchangeable / not already settled interchangeable

**层次**：实现 / 同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量）/ not 969 checktxstate-notsame interchangeable / not 312 checktxstate-vs-execute bundled interchangeable」，不是 CheckTxState bundled（312），也不是默认锁已经 RPC 安全（310），也不是 QueryState 已经是 ExecuteTxState（314/962）。不要另写怎样实现 CheckTx 或怎样再验。

## 官方三件事

1. **看见 CheckTxState 和 ExecuteTxState 同时在改 / 看见共识和内存池两条连接都在说话 这份并发 is not already 已经同一份状态 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 969 checktxstate-notsame interchangeable / 968 checktxstate-notexec interchangeable / 312 checktxstate item 1 CheckTx 过了 interchangeable，也不是已经同时在改 not already same-state / not already merged / not already settled 正式三事 bundled（312 item 2 余量） interchangeable / 312 checktxstate item 2 interchangeable。**  
   官方写：共识实例进行当中，CheckTxState 可以和 ExecuteTxState 同时更新，因为共识连接和内存池连接上的消息可以并发。看见两边都在改，不是已经同一份 interchangeable——本页从 312 item 2 侧钉 not already same-state 单句。312 checktxstate vs execute bundled unbundling 在本页 item 2 续。

2. **看见并发 / 看见两边都在改 / 这份并发 is not already 已经合并 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 969 checktxstate-notsame interchangeable / 312 checktxstate item 3 RECHECK interchangeable / 970 checktxstate-notrecheck interchangeable，也不是已经默认锁已经 RPC 安全 interchangeable / 310 commit-lock interchangeable。**  
   官方把并发和已经合并分开。看见并发，不是已经合并 interchangeable。本页钉 not already merged 单句。

3. **看见都叫 CheckTx / Finalize / 看见两边都在改 / 这份并发 is not already 已经交差 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 969 checktxstate-notsame interchangeable / 968 checktxstate-notexec interchangeable，也不是已经 QueryState 已经是 ExecuteTxState interchangeable / 314/962 querystate-notexec interchangeable。**  
   官方把都叫 CheckTx / Finalize 和已经共用一份工作状态分开。看见都叫 CheckTx / Finalize，不是已经交差 interchangeable。312 checktxstate vs execute bundled unbundling 在本页 item 2 续。

怎样实现两份状态、怎样再验、索引器去重是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **同时在改 not already same-state ≠ 已经同一份 interchangeable：** 官方把两条连接上可以并发更新写成两份状态。
- **看见并发 not already merged ≠ 已经合并 interchangeable：** 官方把并发和已经合并分开。
- **看见都叫 CheckTx / Finalize not already settled ≠ 已经交差 interchangeable：** 官方把同名方法和已经共用一份工作状态分开；312 checktxstate vs execute bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同时在改 | 不是已经同一份 | 不是默认锁已经 RPC 安全（310） |
| 看见并发 | 不是已经合并 | 不是 QueryState 已经是 ExecuteTxState（314/962） |
| 看见都叫 CheckTx / Finalize | 不是已经交差 | 不是 RECHECK 就已经是新交易（970） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看同时在改 not already same-state / not already merged / not already settled 正式三事（312 余量），必须分开是不是已经同一份、是不是已经合并、是不是已经交差。可以跳过「看见过了就已经按将要执行的那份验过」。不要另写怎样实现 CheckTx 或怎样再验。312 checktxstate vs execute bundled unbundling 在本页 item 2 续；续 [`worked-example-checktxstate-notrecheck-vs-bundled.md`](worked-example-checktxstate-notrecheck-vs-bundled.md)（不变量 970 item 3）。

## 本页不抄

- 怎样实现两份状态、怎样再验、索引器去重。
- CheckTxState bundled。那是不变量 312。
- 默认锁已经 RPC 安全。那是不变量 310。
- QueryState 已经是 ExecuteTxState。那是不变量 314/962。
