# 模式：把 FinalizeBlock When persist decision / synchronous call 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When steps 1–2。  
**例**：[persist decision ≠ 已经 executes block v](../../tracks/implementation/worked-example-finpersist-vs-commit.md)。

## 三个名字

1. **persist decision 不是已经 executes block v：** 看见 persists _v_ as the decision for height _h_ 不是已经 Application executes block _v_ / 已经交差 interchangeable。
2. **calls FinalizeBlock 不是已经 persist outputs：** 看见 calls FinalizeBlock with _v_'s data 不是已经 persist tx outputs / AppHash / ResultsHash interchangeable。
3. **synchronous call 不是已经决定触发 interchangeable：** 看见 The call is synchronous 不是已经 +2/3 precommit 决定就已经会调 Finalize interchangeable。

## 为什么要分开叫

官方把 persist decision、calls FinalizeBlock、synchronous call 和 executes block v、persist outputs、decides trigger 写成三个名字。把它们叫成一个「看见决定了就已经 executes block v、已经 persist outputs」，会把 persist decision、sync call、outputs persist 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「_p_ persists _v_ … calls FinalizeBlock … synchronous」，先数清问的是 persist decision 是不是已经 executes block v、calls FinalizeBlock 是不是已经 persist outputs，还是 synchronous call 是不是已经决定触发 interchangeable，再决定要不要同一次发布。
