# 模式：把候选状态三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md)。  
**例**：[候选 ≠ 已经是 ExecuteTxState](../../tracks/implementation/worked-example-candidate-vs-execute.md)。

## 三个名字

1. **Prepare 没有头哈希：** 看见 Prepare 披露了提案不是已经知道本头哈希。
2. **候选不是已经是 ExecuteTxState：** 看见立刻执行出一份状态不是已经能预测本高度 Finalize 会交哪一块。
3. **丢掉不是已经永远不用再执行：** 看见还没 Finalize 不是已经能无界攒着。

## 为什么要分开叫

官方把 Prepare 还不知道头哈希、立刻执行不得改 ExecuteTxState、提案数没有上界必须能丢掉，写成三件事。把它们叫成一个「看见立刻执行就已经是本高度最终」，会把四门、Commit 锁和半写原子一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「Prepare 已经执行」，先数清问的是 Prepare 没有头哈希、候选不是已经是 ExecuteTxState，还是丢掉不是已经永远不用再执行，再决定要不要同一次发布。
