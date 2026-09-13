# 模式：把 FinalizeBlock 等价于 ABCI 1.0 BeginBlock/DeliverTx/EndBlock 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[等价于 ABCI 1.0 那三步 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finequiv-vs-abci1.md)。

## 三个名字

1. **等价于 ABCI 1.0 那三步 不是已经是四门已经结算：** 看见收成一门不是已经交差。
2. **等价于旧三步 不是已经没有 Prepare/Process：** 看见收成一门不是已经 ABCI++ 只剩 Finalize。
3. **等价于旧三步 不是已经是含刚决定那块的字段：** 看见收成一门不是已经 Process 就不需要 Finalize。

## 为什么要分开叫

官方把 FinalizeBlock 等价于 ABCI 1.0 的 `BeginBlock` / `DeliverTx` / `EndBlock`、ABCI++ 仍保留 Prepare/Process 等门、Finalize 仍要在块决定后执行写成三个名字。把它们叫成一个「看见收成一门就已经是四门已经结算」，会把历史映射、ABCI++ 门和 Finalize 执行义务三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收成一门就已经是四门已经结算」，先数清问的是 equiv 是不是已经四门已经结算、是不是已经没有 Prepare/Process，还是是不是已经是含刚决定那块的字段 / 已经 Process 就不需要 Finalize，再决定要不要同一次发布。
