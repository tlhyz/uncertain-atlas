# 模式：把 FinalizeBlock 套用候选正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[确定执行 txs ≠ 已经交差](../../tracks/implementation/worked-example-fincand-vs-reexecute.md)。

## 三个名字

1. **确定执行 txs 再交还控制权不是已经交差：** 看见 before returning control 不是已经可以像 Prepare 那样依赖非确定值。
2. **也可以套用 candidate state 不是已经是 ExecuteTxState：** 看见 apply candidate state 不是已经 Process 回了 Accept 就已经换工作状态。
3. **同一块先前 Prepare 或 Process 执行过不是已经不用再在 Finalize 执行：** 看见 previously executed 不是已经 candidate 就不需要 Commit。

## 为什么要分开叫

官方把确定执行 txs、Alternatively apply candidate state、previously executed via Prepare or ProcessProposal 写成三个名字。把它们叫成一个「看见 Process 跑过就已经在 Finalize 套用、已经是 ExecuteTxState、已经交差」，会把确定执行、套用候选和先前执行三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 candidate 就已经交差」，先数清问的是确定执行 txs 是不是已经交差、套用 candidate state 是不是已经是 ExecuteTxState，还是同一块先前 Prepare 或 Process 执行过是不是已经不用再在 Finalize 执行，再决定要不要同一次发布。
