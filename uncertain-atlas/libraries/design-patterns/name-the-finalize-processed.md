# 模式：把 Finalize 时的 Process 保证三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[至少一名非拜占庭验证者跑过 Process ≠ 已经每个验证者都跑过 Process](../../tracks/implementation/worked-example-finalize-vs-processed.md)。

## 三个名字

1. **至少一名非拜占庭验证者跑过 Process 不是已经每个验证者都跑过 Process：** 看见要 Finalize 了不是已经是提议者那边也会叫 Process。
2. **Finalize 请求把字段再填一遍不是已经不用再给：** 看见 Prepare / Process 已经给过不是已经跑过 Process。
3. **可以套用先前候选不是已经是 ExecuteTxState：** 看见同一块先跑过不是已经交差。

## 为什么要分开叫

官方把决定一块时至少一名非拜占庭验证者跑过 Process、Finalize 请求仍把字段再填一遍、可以套用先前候选写成三件事。把它们叫成一个「看见要 Finalize 了就已经每个验证者都跑过 Process」，会把提议者那边也会叫 Process、同一套字段和候选状态一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见要 Finalize 了就已经每个验证者都跑过 Process」，先数清问的是至少一名非拜占庭验证者跑过 Process 不是已经每个验证者都跑过 Process、Finalize 请求把字段再填一遍不是已经不用再给，还是可以套用先前候选不是已经是 ExecuteTxState，再决定要不要同一次发布。
