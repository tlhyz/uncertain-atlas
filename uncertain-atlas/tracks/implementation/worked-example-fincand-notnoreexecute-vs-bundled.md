# 例：看见同一块先前经 Prepare / Process 执行过 is not already no need to execute txs in Finalize / not fincand bundled（460） interchangeable / not apply candidate ExecuteTxState interchangeable

**层次**：实现 / previously executed not no re-execute in Finalize 正式三事（460 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「previously executed not no re-execute in Finalize / not fincand bundled（460） interchangeable / not apply candidate ExecuteTxState（577） interchangeable / not has run not apply candidate（572） interchangeable」，不是 FinalizeBlock 套用候选 bundled（460），也不是 executes txs not committed（576），也不是 apply candidate state not ExecuteTxState（577）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 FinalizeBlock Usage 里 previously executed via `PrepareProposal` or `ProcessProposal` 和「已经不用再在 Finalize 执行 / 已经 candidate 就不需要 Commit / fincand bundled interchangeable」分开写成三件独立的实现事，不是「看见同一块先前 Prepare 或 Process 执行过 就已经不用再 execute txs interchangeable、已经不用再回 app_hash interchangeable、已经 fincand bundled interchangeable」一件事：

1. **看见 the same block previously executed via `PrepareProposal` or `ProcessProposal` / 看见同一块先前执行过 is not already no need to execute txs in Finalize / 看见 previously executed is not already FinalizeBlock 套用候选 bundled（460） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 executes txs deterministically not committed bundled（460 第一件事 / 576 余量） interchangeable / 已经交差 interchangeable / 已经 before returning control interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（460 第二件事 / 577 余量） interchangeable / 已经 ExecuteTxState interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 guarantee satisfied interchangeable / 已经 previously executed means no guarantee needed interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 persist decision interchangeable / 已经 Process 跑过就不执行 interchangeable。**  
   官方 Usage 把 previously executed 和 Alternatively apply candidate state / executes txs deterministically 配成多条路。看见 previously executed，不是已经不用再给 `FinalizeBlockRequest.txs` 那种已经跑过 Process 就不需要 Finalize——460 bundled 第三件事常被写成「看见有 candidate 就已经不用再 execute txs」，本页钉 previously executed not no re-execute txs 单句。看见 same block previously executed，不是已经 executes txs not committed（576 余量） interchangeable——576 钉 execute txs 路，本页钉 previously executed 路。看见 via Prepare or Process，不是已经 apply candidate not ExecuteTxState（577 余量） interchangeable——577 钉 apply candidate 单句，本页钉 item 3 边界。
2. **看见 previously executed via PrepareProposal or ProcessProposal is not already no need to return app_hash / tx_results / 看见先前执行过 is not already candidate 就不需要 Commit interchangeable / 已经不用再回 app_hash interchangeable / 已经 Code/Data 印进本头 interchangeable 不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 已经 Finalize 改了就已经落盘 interchangeable / 已经交差 interchangeable，也不是已经 FinalizeBlock must provide values as a result of executing the block bundled（477 余量） interchangeable / 已经 Process 跑过就不用再回 tx_results interchangeable / 已经空更新就没有 must provide 义务 interchangeable，也不是已经 apply candidate state not no return app_hash bundled（577 余量） interchangeable / 已经套用了就不需要 Commit interchangeable / 已经 previously executed means no re-execute interchangeable，也不是已经 Finalize 改了就已经落盘 bundled（335 余量） interchangeable / 已经 Finalize + Commit interchangeable / 已经印进 LastResultsHash interchangeable，也不是已经 ProcessProposal Contains all information not already executed bundled（546 余量） interchangeable / 已经执行那些交易 interchangeable / 已经 Finalize 跑过 interchangeable。**  
   官方把 previously executed 和 must provide app_hash / tx_results as a result of executing the block 分开——460 bundled 常与 477 混成「看见 previously executed 就已经不用再回 app_hash / tx_results interchangeable」，本页钉 previously executed not no return app_hash 单句。看见 previously executed，不是已经 must provide values（477 余量） interchangeable——477 钉 Finalize 必须回四列，本页钉 460 item 3 边界。看见 same block previously executed，不是已经 Finalize 改了就已经落盘（335 余量） interchangeable——335 钉 Code/Data 印进本头，本页钉 previously executed 单句。
3. **看见 previously executed via PrepareProposal or ProcessProposal is not already candidate 就不需要 Commit / guarantee satisfied / 看见先前执行过 is not already has run ProcessProposal not apply candidate interchangeable / 已经 previously executed means no guarantee needed interchangeable / 已经套用 candidate 就不需要 guarantee interchangeable 不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 已经 guarantee satisfied interchangeable / 已经 has run not apply candidate interchangeable，也不是已经 FinalizeBlock When calling ProcessProposal guarantee not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 previously executed via Prepare or Process interchangeable / 已经 Process MAY fully execute committed interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经 candidate not committed interchangeable / 已经 Process ACCEPT switched interchangeable，也不是已经 even if passed not previously executed bundled（473 第三件事 / 568 余量） interchangeable / 已经 even if passed interchangeable / 已经 apply candidate interchangeable，也不是已经 Finalize + Commit 交差 bundled interchangeable / 已经 Finalize 改了就已经落盘 interchangeable / 已经 committed interchangeable。**  
   官方把 previously executed 和 has run ProcessProposal guarantee / candidate not committed 分开——460 bundled 三事常与 572 混成「看见 previously executed 就已经 guarantee satisfied / candidate 就不需要 Commit interchangeable」，本页钉 previously executed not guarantee satisfied / not no Commit 单句。看见 previously executed，不是已经 has run not apply candidate（572 余量） interchangeable——572 钉 472 guarantee 边界，本页钉 460 item 3 单句。看见 same block previously executed，不是已经 candidate state must be kept（544 余量） interchangeable——544 钉 candidate not committed，本页钉 previously executed 边界。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存是规范里的做法，本页不抄。executes txs not committed（576 余量）、apply candidate state not ExecuteTxState（577 余量）、FinalizeBlock 套用候选 bundled（460）是另外那套，本页不抄。

## 官方为什么这样拆

- **previously executed not no re-execute txs ≠ fincand bundled interchangeable：** 官方把 previously executed 和已经不用再在 Finalize 执行 分开。
- **previously executed not no return app_hash / tx_results ≠ must provide values bundled interchangeable：** 官方把 previously executed 和 Finalize 必须回四列 分开。
- **previously executed not guarantee satisfied / not no Commit ≠ has run not apply candidate interchangeable：** 官方把 previously executed 路和 472 guarantee 路 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| previously executed | 不是 already no re-execute txs in Finalize | 不是 executes txs not committed（576） |
| previously executed | 不是 already no return app_hash / tx_results | 不是 must provide values（477） |
| previously executed | 不是 already guarantee satisfied / no Commit | 不是 has run not apply candidate（572） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 previously executed not no re-execute in Finalize 正式三事（460 余量），必须分开 previously executed 是不是 already no re-execute txs interchangeable / 460 bundled interchangeable / 577 apply candidate interchangeable、previously executed 是不是 already no return app_hash / tx_results interchangeable / 477 must provide interchangeable / 335 Finalize 改了就已经落盘 interchangeable、previously executed 是不是 already guarantee satisfied / no Commit interchangeable / 572 has run not apply candidate interchangeable / 544 candidate not committed interchangeable。可以跳过「看见 previously executed 就已经不用再在 Finalize 执行 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存。
- executes txs not already committed。那是不变量 576（460 item 1 余量）。
- apply candidate state not ExecuteTxState。那是不变量 577（460 item 2 余量）。
- FinalizeBlock 套用候选 bundled 三事。那是不变量 460。
