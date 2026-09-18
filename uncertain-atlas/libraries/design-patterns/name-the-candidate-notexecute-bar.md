# 模式：把候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[候选不是已经是 ExecuteTxState ≠ bundled（311）](../../tracks/implementation/worked-example-candidate-notexecute-vs-bundled.md)。

## 三个名字

1. **立刻执行 不是 already ExecuteTxState：** 看见立刻执行出一份候选 / 跑过了 / Prepare 或 Process 立刻执行了，不是已经是 ExecuteTxState interchangeable / 已经进工作状态 interchangeable，不是 311 candidate bundled interchangeable / 33 four gates interchangeable / candidate-sold-as-execute interchangeable。

2. **内存里有 不是 already can name this height final：** 看见候选状态留在内存 / 可能的最终，不是已经能点名本高度最终 interchangeable / 已经能预测 Finalize 会交哪一块 interchangeable，不是 311 candidate item 1 interchangeable / 692 candidate-notheader interchangeable。

3. **能加快 Finalize 不是 already settled：** 看见更快套用内存里那份 / Quick FinalizeBlock execution，不是已经交差 interchangeable / 已经 Finalize + Commit interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable / 694 candidate-notdiscarded interchangeable。

官方把立刻执行单句、already ExecuteTxState、already can name this height final、already settled 写成三个名字。把它们叫成一个「看见立刻执行 就已经进工作状态 interchangeable / 就已经能预测 Finalize 交哪一块 interchangeable / 就已经交差 interchangeable」，会把 not already ExecuteTxState、not already can name this height final、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看候选不是已经是 ExecuteTxState not already ExecuteTxState / not already can name this height final / not already settled 正式三事（311 余量），先数清问的是立刻执行 是不是 already ExecuteTxState / 311 / 33，是不是内存里有 是不是 already can name this height final，还是能加快 Finalize 是不是 already settled，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 2 完成。
