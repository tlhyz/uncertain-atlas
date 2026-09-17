# 反模式：看见 Finalize 含刚决定那块的字段就当成已经是四门已经结算 / 看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态就当成已经可以像 Prepare 那样 / 看见 Info 用来回应用状态信息就当成已经是握手对齐

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**例**：[Finalize 含刚决定那块的字段 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-finfields-vs-equiv.md)。

## 塌法

1. 看见 Finalize 含刚决定那块的字段 / 看见填了字段，就当成已经是四门已经结算，或当成已经跑过 Process。
2. 看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态 / 看见必须确定，就当成已经可以像 Prepare 那样，或当成已经印进本头。
3. 看见 Info 用来回应用状态信息 / 看见能回，就当成已经是握手对齐，或当成已经是快照重放。

## 为什么会出事

官方写：`FinalizeBlock` 含刚决定那块的字段。`FinalizeBlock` 的实现必须确定，因为它在状态机复制的上下文里推进应用状态。Info 用来回应用状态信息。

## 和相邻反模式

- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算，不是本页这种 Finalize 含刚决定那块的字段不是已经是四门已经结算。
- [finalizedet-sold-as-prepare](finalizedet-sold-as-prepare.md) 是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样，不是本页这种 Finalize 实现必须确定、因为它在状态机复制里推进应用状态不是已经可以像 Prepare 那样。
- [info-sold-as-handshake](info-sold-as-handshake.md) 是 Info 用来握手对齐就已经是快照重放，不是本页这种 Info 用来回应用状态信息不是已经是握手对齐。
