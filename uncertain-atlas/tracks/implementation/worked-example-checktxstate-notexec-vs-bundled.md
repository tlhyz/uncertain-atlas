# 例：看见 CheckTx 过了 is not already ExecuteTxState interchangeable / not already future-exec interchangeable / not already settled interchangeable

**层次**：实现 / CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) CheckTxState。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量）/ not 968 checktxstate-notexec interchangeable / not 312 checktxstate-vs-execute bundled interchangeable」，不是 CheckTxState bundled（312），也不是候选已经是 ExecuteTxState（311），也不是内存池去重已经保证不重复（313/965）。不要另写怎样实现 CheckTx 或怎样再验。

## 官方三件事

1. **看见 CheckTx 过了 / 看见进了池并开始流言 这份滤过 is not already 已经按 ExecuteTxState 验过 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 968 checktxstate-notexec interchangeable / 969 checktxstate-notsame interchangeable / 312 checktxstate item 2 同时在改 interchangeable，也不是已经 CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事 bundled（312 item 1 余量） interchangeable / 312 checktxstate item 1 interchangeable。**  
   官方写：内存池连接维持一份 CheckTxState。进来的交易按这份状态顺序验。没报错才进池，CometBFT 才开始流言。CheckTx 只是弱过滤器，不能保证验的就是以后作为（可能的）决定块去执行时那一份状态。看见过了，不是已经按工作状态验 interchangeable——本页从 312 item 1 侧钉 not already ExecuteTxState 单句。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。

2. **看见进了池 / 看见过了 / 这份滤过 is not already 已经按将要执行的那份状态验过 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 968 checktxstate-notexec interchangeable / 312 checktxstate item 3 RECHECK interchangeable / 970 checktxstate-notrecheck interchangeable，也不是已经候选已经是 ExecuteTxState interchangeable / 311 candidate interchangeable。**  
   官方把进了池和已经按将要执行的那份验分开——312 bundled 第一件事常与 311 混成「看见过了就已经按工作状态或候选状态验过 interchangeable」，本页钉 not already future-exec 单句。

3. **看见重置了 / 看见过了 / 这份滤过 is not already 已经交差 interchangeable，也不是已经 CheckTxState bundled（312） interchangeable / 968 checktxstate-notexec interchangeable / 969 checktxstate-notsame interchangeable，也不是已经内存池去重已经保证不重复 interchangeable / 313/965 replayprot-notguar interchangeable。**  
   官方把 Commit 结束时重置成最新已提交和已经和 ExecuteTxState 同一份分开。看见重置了，不是已经交差 interchangeable。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。

怎样实现两份状态、怎样再验、索引器去重是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **CheckTx 过了 not already ExecuteTxState ≠ 已经按 ExecuteTxState 验过 interchangeable：** 官方把 CheckTxState、最新已提交、将要执行的那份分开。
- **看见进了池 not already future-exec ≠ 已经按将要执行的那份状态验过 interchangeable：** 官方把进了池和已经按将要执行的那份验分开。
- **看见重置了 not already settled ≠ 已经交差 interchangeable：** 官方把重置成最新已提交和已经同一份分开；312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 过了 | 不是已经按 ExecuteTxState 验过 | 不是候选已经是 ExecuteTxState（311） |
| 看见进了池 | 不是已经按将要执行的那份验过 | 不是内存池去重已经保证不重复（313/965） |
| 看见重置了 | 不是已经交差 | 不是同时在改就已经同一份（969） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 not already ExecuteTxState / not already future-exec / not already settled 正式三事（312 余量），必须分开是不是已经按 ExecuteTxState 验过、是不是已经按将要执行的那份验过、是不是已经交差。可以跳过「看见过了就已经按将要执行的那份验过」。不要另写怎样实现 CheckTx 或怎样再验。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动；续 [`worked-example-checktxstate-notsame-vs-bundled.md`](worked-example-checktxstate-notsame-vs-bundled.md)（不变量 969 item 2）。

## 本页不抄

- 怎样实现两份状态、怎样再验、索引器去重。
- CheckTxState bundled。那是不变量 312。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 内存池去重已经保证不重复。那是不变量 313/965。
