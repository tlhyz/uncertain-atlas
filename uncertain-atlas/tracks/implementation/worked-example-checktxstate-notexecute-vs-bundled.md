# 例：看见 CheckTx 过了 / 进了池并开始流言 is not already already checked against ExecuteTxState interchangeable / already checked against to-be-executed state interchangeable / already same as ExecuteTxState after reset interchangeable

**层次**：实现 / CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量）/ not 695 checktxstate-notexecute interchangeable / not 312 checktxstate bundled interchangeable」，不是 CheckTxState vs ExecuteTxState bundled（312），也不是同时在改不是已经同一份（696 item 2 余量）或 RECHECK 不是已经是新交易（697 item 3 余量）。不要另写怎样实现 CheckTx 或怎样再验。

## 官方三件事

规范把 Requirements 里内存池连接维持一份 *CheckTxState*、进来的交易按这份状态顺序验、没报错才进池才开始流言、*CheckTxState* 应在每次 `Commit` 结束时重置成最新已提交状态、CheckTx 只是弱过滤器不能保证验的就是以后作为（可能的）决定块去执行时那一份状态 和「已经是 CheckTx 过了就已经按 ExecuteTxState 验过 interchangeable / 已经是进了池就已经按将要执行的那份验过 interchangeable / 已经是重置了就已经和 ExecuteTxState 同一份 interchangeable / 已经是 CheckTxState vs ExecuteTxState bundled interchangeable」分开写成三件独立的实现事，不是「看见过了 就已经按工作状态验 interchangeable / 就已经按将要执行的那份验 interchangeable / 就已经同一份 interchangeable」一件事：

1. **看见 CheckTx 过了 / 看见没报错 / 看见按 CheckTxState 顺序验过 is not already 已经按 ExecuteTxState 验过 interchangeable / 已经 checked against ExecuteTxState interchangeable / 已经按工作状态验 interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable / checktxstate-sold-as-execute interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 695 checktxstate-notexecute interchangeable / 312 checktxstate item 1 interchangeable，也不是已经 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事 bundled（312 item 1 余量） interchangeable / 312 checktxstate item 1 interchangeable，也不是已经同时在改不是已经同一份（696） interchangeable / 697 checktxstate-notrecheck interchangeable / 311 candidate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：进来的交易按 *CheckTxState* 顺序验；CheckTx 只是弱过滤器，不能保证验的就是以后作为（可能的）决定块去执行时那一份状态。看见过了，不是已经按工作状态验 interchangeable——312 钉 bundled 三事，本页从 item 1 侧钉 not already checked against ExecuteTxState 单句。看见没报错，不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable——312 钉 bundled，本页钉 item 1 第一件事。看见按 CheckTxState 顺序验过，不是已经候选已经是 ExecuteTxState（311） interchangeable——311 另钉，本页钉 CheckTxState 边界。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。

2. **看见进了池并开始流言 / 看见 Accepted into the mempool / 看见 CometBFT 开始 gossip is not already 已经按将要执行的那份状态验过 interchangeable / 已经 checked against to-be-executed state interchangeable / 已经按决定块那份验 interchangeable / 312 checktxstate bundled interchangeable / 301 proposed-removed interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 695 checktxstate-notexecute interchangeable / 312 checktxstate item 2 同时在改 interchangeable / 312 checktxstate item 3 RECHECK interchangeable，也不是已经 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事 bundled（312 item 1 余量） interchangeable / 312 checktxstate item 1 interchangeable，也不是已经按 ExecuteTxState 验过（本页第一件事） interchangeable。**  
   官方把没报错才进池、CometBFT 才开始流言 和已经按将要执行的那份验过路径分开——进池是 CheckTxState 绿了，不等于按将要执行的那份（可能的决定块）验过。看见进了池，不是已经按将要执行的那份验 interchangeable——本页钉 not already checked against to-be-executed state 单句。看见开始流言，不是已经同时在改不是已经同一份（696） interchangeable——696 另钉 item 2，本页钉 item 1 第二件事。看见 Accepted into the mempool，不是已经 RECHECK 不是已经是新交易（697） interchangeable——697 另钉 item 3，本页钉 item 1 第二件事。312 checktxstate vs execute bundled unbundling 在本页 item 1 启动。

3. **看见重置了 / 看见 Commit 结束时 CheckTxState 重置成最新已提交 / 看见 reset to the latest committed state is not already 已经和 ExecuteTxState 同一份 interchangeable / 已经 same as ExecuteTxState after reset interchangeable / 已经两份合并 interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable，也不是已经 CheckTxState vs ExecuteTxState bundled（312） interchangeable / 695 checktxstate-notexecute interchangeable / 312 checktxstate item 2 / 312 checktxstate item 3，也不是已经 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事 bundled（312 item 1 余量） interchangeable / 312 checktxstate item 1 interchangeable，也不是已经按 ExecuteTxState 验过（本页第一件事） interchangeable / 已经按将要执行的那份验过（本页第二件事） interchangeable。**  
   官方把每次 `Commit` 结束时重置成最新已提交状态 和已经和 ExecuteTxState 同一份路径分开——重置到最新已提交，不等于已经是工作状态那份，也不等于两份已经合并。看见重置了，不是已经和 ExecuteTxState 同一份 interchangeable——本页钉 not already same as ExecuteTxState after reset 单句。看见 Commit 结束时重置，不是已经按 ExecuteTxState 验过（本页第一件事） interchangeable——三件事分开钉。看见 reset to latest committed，不是已经四门已经结算（33） interchangeable——33 另钉。312 checktxstate vs execute bundled unbundling 在本页 item 1 完成。

怎样实现 CheckTx、怎样再验、怎样写四门是规范里的做法，本页不抄。CheckTxState vs ExecuteTxState bundled（312）、同时在改不是已经同一份（312 item 2 余量 / 696）、RECHECK 不是已经是新交易（312 item 3 余量 / 697）、候选已经是 ExecuteTxState（311）、提案收了已经从池里删掉（301）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **CheckTx 过了 not already checked against ExecuteTxState ≠ 312 / 33 interchangeable：** 官方把过了单句和已经按工作状态验路径分开。
- **进了池 not already checked against to-be-executed state ≠ 已经按决定块那份验 interchangeable：** 官方把进池流言单句和已经按将要执行的那份验路径分开。
- **重置了 not already same as ExecuteTxState after reset ≠ 已经两份合并 interchangeable：** 官方把重置到最新已提交单句和已经和 ExecuteTxState 同一份路径分开；312 checktxstate vs execute bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 过了 | 不是 already checked against ExecuteTxState | 不是候选 already ExecuteTxState（311） |
| 进了池并开始流言 | 不是 already checked against to-be-executed state | 不是同时在改 alone（696） |
| Commit 结束重置 | 不是 already same as ExecuteTxState after reset | 不是 RECHECK alone（697） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTxState 不是已经按 ExecuteTxState 验过 not already checked against ExecuteTxState / not already checked against to-be-executed state / not already same as ExecuteTxState after reset 正式三事（312 余量），必须分开 CheckTx 过了 是不是 already checked against ExecuteTxState interchangeable / 312 checktxstate bundled interchangeable / 33 four gates interchangeable、进了池 是不是 already checked against to-be-executed state interchangeable、重置了 是不是 already same as ExecuteTxState after reset interchangeable。可以跳过「看见过了 就已经按工作状态验 interchangeable / 就已经按将要执行的那份验 interchangeable / 就已经同一份 interchangeable」。不要另写怎样实现 CheckTx。312 checktxstate vs execute bundled unbundling 在本页 item 1 完成；续 [`worked-example-checktxstate-notsame-vs-bundled.md`](worked-example-checktxstate-notsame-vs-bundled.md)（不变量 696 item 2）。

## 本页不抄

- 怎样实现 CheckTx、怎样再验、怎样写四门。
- CheckTxState vs ExecuteTxState bundled。那是不变量 312。
- 同时在改不是已经同一份。那是不变量 312 item 2 余量 / 696。
- RECHECK 不是已经是新交易。那是不变量 312 item 3 余量 / 697。
- 候选已经是 ExecuteTxState。那是不变量 311。
- 提案收了已经从池里删掉。那是不变量 301。
- 四门已经结算。那是不变量 33。
