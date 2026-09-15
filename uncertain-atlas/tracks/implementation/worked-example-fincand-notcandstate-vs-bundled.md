# 例：看见 apply candidate state / Alternatively apply candidate is not already ExecuteTxState / not fincand bundled（460） interchangeable / not Process ACCEPT switched interchangeable

**层次**：实现 / apply candidate state not ExecuteTxState 正式三事（460 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「apply candidate state not ExecuteTxState / not fincand bundled（460） interchangeable / not Process ACCEPT switched interchangeable」，不是 FinalizeBlock 套用候选 bundled（460），也不是 ProcessProposal 候选执行（452）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 FinalizeBlock Usage 里 Alternatively apply the candidate state corresponding to the same block previously executed via PrepareProposal or ProcessProposal 和「已经是 ExecuteTxState / 已经 Process 回了 Accept 就换工作状态 / fincand bundled interchangeable」分开写成三件独立的实现事，不是「看见套用了 candidate 就已经是 ExecuteTxState interchangeable、已经 Process 回了 Accept interchangeable、已经 fincand bundled interchangeable」一件事：

1. **看见 Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal` / 看见 apply candidate state is not already ExecuteTxState / 看见套用了 is not already FinalizeBlock 套用候选 bundled（460） interchangeable / 已经 ExecuteTxState interchangeable / 已经进 ExecuteTxState interchangeable，也不是已经候选已经是 ExecuteTxState bundled（311 余量） interchangeable / 已经 candidate 不是 ExecuteTxState interchangeable / 已经 Prepare/Process 立刻执行出候选 interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 candidate state interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 FinalizeBlock When Application executes block v bundled（466 余量） interchangeable / 已经 Process 跑过就不执行 interchangeable / 已经 persist decision interchangeable，也不是已经 executes txs deterministically not committed bundled（460 第一件事 / 576 余量） interchangeable / 已经交差 interchangeable / 已经 before returning control interchangeable。**  
   官方 Usage 写 Alternatively apply candidate state。看见 apply candidate，不是已经进 ExecuteTxState——460 bundled 第二件事常被写成「看见套用了就已经是 ExecuteTxState」，本页钉 apply candidate not ExecuteTxState 单句。看见 candidate state，不是已经候选已经是 ExecuteTxState（311 余量） interchangeable——311 钉 candidate vs ExecuteTxState 边界，本页钉 460 item 2 单句。看见 previously executed via Prepare or Process，不是已经 ProcessProposal 候选执行（452 余量） interchangeable——452 钉 MAY execute / candidate / read-only 三事，本页钉 apply candidate 单句。
2. **看见 apply candidate state is not already Process ACCEPT switched working state / 看见套用了 is not already Process 回了 Accept 就换工作状态 interchangeable / 已经 ACCEPT settled interchangeable / 已经 prevote interchangeable 不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 已经 Process 回了 Accept interchangeable / 已经 candidate not committed interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 已经 ACCEPT switched working state interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经 ready to discard interchangeable / 已经 Process ACCEPT switched interchangeable，也不是已经 ProcessProposal read-only checks/processes bundled（545 余量） interchangeable / 已经 mutate committed interchangeable / 已经 immediate execution committed interchangeable，也不是已经 Finalize 时的 Process 保证 bundled（360 余量） interchangeable / 已经可以套用先前 candidate interchangeable / 已经字段再填一遍 interchangeable。**  
   官方把 apply candidate state 和 Process 回了 Accept 就换工作状态分开——460 bundled 常与 452 混成「套用 candidate = Process ACCEPT = ExecuteTxState interchangeable」，本页钉 apply candidate not ACCEPT switched 单句。看见 apply candidate，不是已经 candidate state must be kept（544 余量） interchangeable——544 钉 candidate not committed，本页钉 460 item 2 边界。看见 Alternatively，不是已经 read-only checks/processes（545 余量） interchangeable——545 钉 read-only not mutate committed，本页钉 apply candidate 单句。
3. **看见 apply candidate state is not already no need to return app_hash / tx_results / 看见套用了 is not already previously executed means no re-execute in Finalize interchangeable / 已经不用再回 app_hash interchangeable / 已经 candidate 就不需要 Commit interchangeable 不是已经 FinalizeBlock 套用候选 bundled（460） interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 previously executed interchangeable，也不是已经 FinalizeBlock 套用候选 not no re-execute bundled（460 第三件事 / 578 余量） interchangeable / 已经 guarantee satisfied interchangeable / 已经 has run not apply candidate interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（472 第三件事 / 572 余量） interchangeable / 已经 previously executed via Prepare or Process interchangeable / 已经 guarantee satisfied interchangeable，也不是已经 Finalize 改了就已经落盘 bundled（335 余量） interchangeable / 已经 Code/Data 印进本头 interchangeable / 已经交差 interchangeable。**  
   官方把 apply candidate state 和 previously executed 不用再 execute txs / 不用再回 app_hash 分开——460 bundled 三事常被写成「看见套用了就已经不用再回 app_hash / 已经交差 interchangeable」，本页钉 apply candidate not no re-execute / not no return app_hash 单句。看见 apply candidate，不是已经 previously executed not no re-execute（578 余量） interchangeable——578 钉 item 3 边界，本页钉 item 2 单句。看见 Alternatively，不是已经 has run not apply candidate（572 余量） interchangeable——572 钉 472 guarantee，本页钉 460 apply candidate 单句。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存是规范里的做法，本页不抄。executes txs not committed（576 余量）、previously executed not no re-execute（578 余量）、FinalizeBlock 套用候选 bundled（460）是另外那套，本页不抄。

## 官方为什么这样拆

- **apply candidate state not ExecuteTxState ≠ fincand bundled interchangeable：** 官方把 apply candidate 和进 ExecuteTxState 分开。
- **apply candidate state not Process ACCEPT switched ≠ ProcessProposal 候选执行 bundled interchangeable：** 官方把 apply candidate 和 Process 回了 Accept 就换工作状态 分开。
- **apply candidate state not no re-execute / no return app_hash ≠ previously executed not no re-execute interchangeable：** 官方把 apply candidate 路和 previously executed 不用再 Finalize 执行 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| apply candidate state | 不是 already ExecuteTxState | 不是候选已经是 ExecuteTxState（311） |
| apply candidate state | 不是 already Process ACCEPT switched | 不是 ProcessProposal 候选执行（452） |
| apply candidate state | 不是 already no re-execute / no return app_hash | 不是 previously executed not no re-execute（578） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 apply candidate state not ExecuteTxState 正式三事（460 余量），必须分开 apply candidate 是不是 already ExecuteTxState interchangeable / 460 bundled interchangeable / 311 candidate interchangeable、apply candidate 是不是 already Process ACCEPT switched interchangeable / 452 candidate interchangeable / 544 candidate not committed interchangeable、apply candidate 是不是 already no re-execute / no return app_hash interchangeable / 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable。可以跳过「看见套用了 candidate 就已经是 ExecuteTxState interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存。
- executes txs not already committed。那是不变量 576（460 item 1 余量）。
- previously executed not no re-execute in Finalize。那是不变量 578（460 item 3 余量）。
- FinalizeBlock 套用候选 bundled 三事。那是不变量 460。
