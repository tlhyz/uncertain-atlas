# 例：看见 Application executes txs deterministically before returning control 不是已经 committed；看见 Alternatively apply candidate state 不是已经是 ExecuteTxState；看见 previously executed via Prepare or Process 不是已经不用再在 Finalize 执行

**层次**：实现 / FinalizeBlock 套用候选。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlock 套用候选 / not already committed / not ExecuteTxState / not no re-execute in Finalize bundled」，不是 executes txs deterministically not already committed 正式三事（576 余量），也不是 apply candidate state not ExecuteTxState 正式三事（577 余量），也不是 previously executed not no re-execute in Finalize 正式三事（578 余量）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 FinalizeBlock Usage 里 executes txs deterministically before returning control、Alternatively apply candidate state、previously executed via PrepareProposal or ProcessProposal 和「已经交差 / 已经是 ExecuteTxState / 已经不用再在 Finalize 执行 interchangeable」分开写成三件独立的实现事，不是「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差 interchangeable」一件事：

1. **看见 Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT / 看见确定执行 txs is not already committed / Finalize + Commit 交差 interchangeable / 看见 before returning control is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经交差 interchangeable / 已经 Finalize 改了就已经落盘 interchangeable，也不是已经 executes txs deterministically not committed bundled（576 余量） interchangeable / 576 executes txs interchangeable / 470 findet interchangeable / 338 Prepare nondet interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 408 Process whole block interchangeable / 452 candidate interchangeable，也不是已经 FinalizeBlock 套用候选 not apply candidate bundled（577 余量） interchangeable / 577 apply candidate interchangeable / 578 not no re-execute interchangeable。**  
   官方 Usage 写：The Application executes the transactions in `FinalizeBlockRequest.txs` deterministically, according to the rules set up by the Application, before returning control to CometBFT。看见 before returning control，不是已经 Finalize + Commit 那种已经交差——460 bundled 第一件事常被写成「看见确定执行 txs 就已经交差 interchangeable」，本页钉 executes txs not already committed 单句。看见 deterministically，不是已经 Prepare 没有确定性要求（338） interchangeable——338 钉 Prepare 可以不确定，本页钉 fincand item 1 边界。看见 executes txs，不是已经 executes txs not committed（576 余量） interchangeable——576 从 460 item 1 角度钉 not committed 三事，本页钉 460 bundled 三事。
2. **看见 Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal` / 看见 apply candidate state is not already ExecuteTxState / 看见套用了 is not already Finalize 时的 Process 保证 bundled（360） interchangeable / 已经 ExecuteTxState interchangeable / 已经进 ExecuteTxState interchangeable，也不是已经 apply candidate state not ExecuteTxState bundled（577 余量） interchangeable / 577 apply candidate interchangeable / 311 candidate is ExecuteTxState interchangeable / 452 candidate interchangeable，也不是已经 ProcessProposal 候选执行 bundled（452 余量） interchangeable / 544 candidate not committed interchangeable / 430 ACCEPT settled interchangeable，也不是已经 executes txs deterministically not committed bundled（576 余量） interchangeable / 576 executes txs interchangeable / 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable。**  
   官方 Usage 写：Alternatively, it can apply the candidate state corresponding to the same block previously executed via `PrepareProposal` or `ProcessProposal`。看见 apply candidate state，不是已经进 `ExecuteTxState` interchangeable——460 bundled 第二件事常与 311 / 452 混成「看见套用了 candidate 就已经是 ExecuteTxState interchangeable」，本页钉 apply candidate not ExecuteTxState 单句。看见 Alternatively，不是已经 apply candidate not ExecuteTxState（577 余量） interchangeable——577 钉 apply candidate 三事，本页钉 fincand item 2 边界。看见套用了 candidate，不是已经 Process 回了 Accept 就换工作状态（452） interchangeable——452 钉 candidate execution，本页钉 fincand 单句。
3. **看见 the same block previously executed via `PrepareProposal` or `ProcessProposal` / 看见同一块先前执行过 is not already no need to execute txs in Finalize / 看见 previously executed is not already candidate 就不需要 Commit interchangeable / 已经不用再在 Finalize 执行 interchangeable / 已经 Process 跑过就不执行 interchangeable，也不是已经 previously executed not no re-execute in Finalize bundled（578 余量） interchangeable / 578 not no re-execute interchangeable / 477 must provide interchangeable / 335 Finalize 改了就已经落盘 interchangeable，也不是已经 has run ProcessProposal not apply candidate bundled（572 余量） interchangeable / 472 guarantee interchangeable / 544 candidate not committed interchangeable，也不是已经 executes txs deterministically not committed bundled（576 余量） interchangeable / 577 apply candidate interchangeable / 466 executes block v interchangeable。**  
   官方把 previously executed via PrepareProposal or ProcessProposal 和 Finalize 确定执行 txs / 套用 candidate 配成多条路。看见 previously executed，不是已经不用再给 `FinalizeBlockRequest.txs` 那种已经跑过 Process 就不需要 Finalize interchangeable——460 bundled 第三件事常被写成「看见有 candidate 就已经不用再 execute txs interchangeable」，本页钉 previously executed not no re-execute in Finalize 单句。看见 same block previously executed，不是已经 previously executed not no re-execute（578 余量） interchangeable——578 钉 item 3 三事，本页钉 460 bundled 边界。看见 via Prepare or Process，不是已经 has run not apply candidate（572 余量） interchangeable——572 钉 472 guarantee 边界，本页钉 fincand item 3 单句。

怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存是规范里的做法，本页不抄。executes txs deterministically not already committed 正式三事（576 余量）、apply candidate state not ExecuteTxState 正式三事（577 余量）、previously executed not no re-execute in Finalize 正式三事（578 余量）、Finalize 时的 Process 保证 bundled（360）、Finalize 执行余量 bundled（408）、ProcessProposal 候选执行（452）是另外那套，本页不抄。

## 官方为什么这样拆

- **executes txs deterministically not already committed ≠ fincand bundled interchangeable：** 官方把 before returning control 和 Finalize + Commit 交差分开。
- **apply candidate state not ExecuteTxState ≠ fincand bundled interchangeable：** 官方把 apply candidate 和进 ExecuteTxState 分开。
- **previously executed not no re-execute in Finalize ≠ fincand bundled interchangeable：** 官方把 previously executed 和已经不用再在 Finalize 执行分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| executes txs deterministically | 不是 already committed | 不是 executes txs not committed（576） |
| apply candidate state | 不是 already ExecuteTxState | 不是 apply candidate not ExecuteTxState（577） |
| previously executed | 不是 already no re-execute in Finalize | 不是 previously executed not no re-execute（578） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 套用候选，必须分开 executes txs 是不是 already committed interchangeable / 576 executes txs interchangeable / 470 findet interchangeable、apply candidate state 是不是 already ExecuteTxState interchangeable / 577 apply candidate interchangeable / 311 candidate interchangeable / 452 candidate interchangeable、previously executed 是不是 already no re-execute in Finalize interchangeable / 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable / 477 must provide interchangeable。可以跳过「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样实现 candidate 缓存、怎样在 Finalize 套用、怎样限制内存。
- executes txs deterministically not already committed 单句边界。那是不变量 576（460 item 1 余量）。
- apply candidate state not ExecuteTxState 单句边界。那是不变量 577（460 item 2 余量）。
- previously executed not no re-execute in Finalize 单句边界。那是不变量 578（460 item 3 余量）。
- Finalize 时的 Process 保证 bundled 三事。那是不变量 360。
- Finalize 执行余量 bundled 三事。那是不变量 408。
- ProcessProposal 候选执行。那是不变量 452。
