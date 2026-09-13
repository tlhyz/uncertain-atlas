# 模式：把 ProcessProposal 候选执行正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**例**：[Process MAY 像 Finalize 整块执行 ≠ 已经交差](../../tracks/implementation/worked-example-proccand-vs-execute.md)。

## 三个名字

1. **Process MAY 像 Finalize 整块执行不是已经交差 / 已经是 ExecuteTxState：** 看见 immediate execution 跑过不是已经 Finalize + Commit。
2. **须留 candidate state、另一块决定时要能丢掉不是已经改了已提交状态：** 看见留着候选不是已经改了 *s<sub>p,h-1</sub>*。
3. **read-only 处理不是已经改了上一份已提交状态：** 看见 checks/processes read-only 不是已经 mutate committed state。

## 为什么要分开叫

官方把 ProcessProposal 候选执行写成三个名字。把它们叫成一个「看见 Process 跑过就已经交差」，会把 MAY 整块执行、须留 candidate state 和 read-only 处理一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Process 跑过就已经交差」，先数清问的是 Process MAY 像 Finalize 整块执行是不是已经交差 / 已经是 ExecuteTxState、须留 candidate state 是不是已经改了已提交状态，还是 read-only 处理是不是已经改了上一份已提交状态，再决定要不要同一次发布。
