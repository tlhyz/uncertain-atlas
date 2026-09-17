# 模式：把 Finalize 字段余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**例**：[Finalize 含刚决定那块的字段 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finfields-vs-equiv.md)。

## 三个名字

1. **Finalize 含刚决定那块的字段不是已经是四门已经结算：** 看见填了字段不是已经跑过 Process。
2. **Finalize 实现必须确定、因为它在状态机复制里推进应用状态不是已经可以像 Prepare 那样：** 看见必须确定不是已经印进本头。
3. **Info 用来回应用状态信息不是已经是握手对齐：** 看见能回不是已经是快照重放。

## 为什么要分开叫

官方把 Finalize 含刚决定那块的字段、Finalize 实现必须确定因为它在状态机复制里推进应用状态、Info 用来回应用状态信息写成三件事。把它们叫成一个「看见填了 Finalize 字段余量就已经是四门已经结算」，会把四门已经结算、可以像 Prepare 那样和握手对齐一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Finalize 字段余量就已经是四门已经结算」，先数清问的是 Finalize 含刚决定那块的字段不是已经是四门已经结算、Finalize 实现必须确定、因为它在状态机复制里推进应用状态不是已经可以像 Prepare 那样，还是 Info 用来回应用状态信息不是已经是握手对齐，再决定要不要同一次发布。
