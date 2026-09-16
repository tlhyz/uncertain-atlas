# 模式：把 FinalizeBlock Contains newly decided block fields not already settled 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[FinalizeBlock Contains newly decided block fields not already settled ≠ bundled](../../tracks/implementation/worked-example-finnewfields-notsettled-vs-bundled.md)。

## 三个名字

1. **Contains newly decided block fields not already four gates settled 不是 FinalizeBlock 含刚决定那块字段 bundled：** 看见含刚决定那块的字段不是已经四门已经结算，不是 461 bundled interchangeable / 363 fill all fields interchangeable / 465 ABCI 1.0 equiv interchangeable。
2. **Contains newly decided block fields not already ran Process 不是 Finalize Process guarantee：** 看见 newly decided block 不是已经跑过 Process，不是 461 bundled interchangeable / 360 Process guarantee interchangeable / 546 not already executed interchangeable。
3. **Contains newly decided block fields not Process ACCEPT switched working state 不是 452 candidate：** 看见含刚决定那块的字段不是已经 Process 回了 Accept 就换工作状态，不是 461 bundled interchangeable / 452 candidate interchangeable / 544 candidate not committed interchangeable。

## 为什么要分开叫

官方把 FinalizeBlock Contains newly decided block fields not already settled 写成三个名字。把它们叫成一个「看见含刚决定那块的字段就已经四门已经结算」，会把 Contains newly decided、Process 跑过、Process ACCEPT 换工作状态三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlock Contains newly decided block fields not already settled 正式三事，先数清问的是 Contains newly decided block fields 是不是 already four gates settled、Contains newly decided block fields 是不是 already ran Process、Contains newly decided block fields 是不是 Process ACCEPT switched working state，再决定要不要同一次发布。
