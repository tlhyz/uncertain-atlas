# 反模式：把 FinalizeBlock 套用候选说成已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[FinalizeBlock 套用候选 ≠ bundled](../../tracks/implementation/worked-example-fincand-bundled.md)。

## 错在哪里

把 executes the transactions in FinalizeBlockRequest.txs deterministically before returning control 写成已经交差，或已经可以像 Prepare 那样依赖非确定值；把 Alternatively apply candidate state 写成已经是 ExecuteTxState，或已经 Process 回了 Accept 就已经换工作状态；把 previously executed via PrepareProposal or ProcessProposal 写成已经不用再在 Finalize 执行，或已经 candidate 就不需要 Commit，或已经和 360 / 408 / 452 / 311 / 335 / 576 / 577 / 578 interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock 套用候选，必须分开 executes txs deterministically、apply candidate state、previously executed 三件事，不要和 360 / 408 / 452 / 311 / 335 / 576 / 577 / 578 糊成一句。
