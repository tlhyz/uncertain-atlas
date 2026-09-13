# 模式：把 FinalizeBlock 含刚决定那块字段正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[Contains the fields of the newly decided block ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finnewfields-vs-gates.md)。

## 三个名字

1. **Contains the fields of the newly decided block 不是已经是四门已经结算：** 看见含刚决定那块的字段不是已经跑过 Process。
2. **newly decided block 的字段不是已经是 ProcessProposal 含执行所需全部信息：** 看见 decided block 不是已经 proposed block 字段 interchangeable。
3. **全部字段填齐即使 Prepare/Process 已经传过不是已经 decided 和 proposed 就可以混用：** 看见又填一遍不是已经 Prepare/Process 同一套字段就已经是刚决定那块的字段。

## 为什么要分开叫

官方把 Contains the fields of the newly decided block、newly decided block 的字段对象、CometBFT will fill up all fields even if already passed via Prepare/Process 写成三个名字。把它们叫成一个「看见填了 Finalize 字段就已经是四门已经结算」，会把刚决定那块的字段、拟议块执行信息和 decided vs proposed 语义一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 字段就已经是四门已经结算」，先数清问的是 Contains the fields of the newly decided block 是不是已经是四门已经结算、newly decided block 的字段是不是已经是 ProcessProposal 含执行所需全部信息，还是全部字段填齐即使 Prepare/Process 已经传过是不是已经 decided 和 proposed 就可以混用，再决定要不要同一次发布。
