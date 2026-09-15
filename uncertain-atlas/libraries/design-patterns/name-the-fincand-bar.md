# 模式：把 FinalizeBlock 套用候选说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock 套用候选 ≠ bundled](../../tracks/implementation/worked-example-fincand-bundled.md)。

## 三个名字

1. **executes txs deterministically not already committed 不是 Finalize 时的 Process 保证 bundled：** 看见 before returning control 不是已经交差，不是 360 bundled interchangeable / 576 executes txs interchangeable / 470 findet interchangeable / 338 Prepare nondet interchangeable。
2. **apply candidate state not ExecuteTxState 不是 ProcessProposal 候选执行 bundled：** 看见 apply candidate state 不是已经是 ExecuteTxState，不是 577 apply candidate interchangeable / 311 candidate interchangeable / 452 candidate interchangeable / 544 candidate not committed interchangeable。
3. **previously executed not no re-execute in Finalize 不是 has run not apply candidate bundled：** 看见 previously executed 不是已经不用再在 Finalize 执行，不是 578 not no re-execute interchangeable / 572 has run not apply candidate interchangeable / 477 must provide interchangeable / 335 Finalize 改了就已经落盘 interchangeable。

## 为什么要分开叫

官方把 executes txs deterministically、Alternatively apply candidate state、previously executed via PrepareProposal or ProcessProposal 写成三个名字。把它们叫成一个「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差 interchangeable」，会把 not committed、not ExecuteTxState、not no re-execute in Finalize 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 套用候选，先数清问的是 executes txs 是不是 already committed、apply candidate state 是不是 already ExecuteTxState，还是 previously executed 是不是 already no re-execute in Finalize，再决定要不要同一次发布。
