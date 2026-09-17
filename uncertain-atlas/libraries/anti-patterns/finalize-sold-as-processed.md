# 反模式：看见引擎保证至少一名非拜占庭验证者对这块跑过 Process 就当成已经每个验证者都跑过 Process / 看见 Finalize 请求把字段再填一遍就当成已经不用再给 / 看见可以套用先前 Prepare / Process 的候选就当成已经是 ExecuteTxState

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**例**：[至少一名非拜占庭验证者跑过 Process ≠ 已经每个验证者都跑过 Process](../../tracks/implementation/worked-example-finalize-vs-processed.md)。

## 塌法

1. 看见引擎保证至少一名非拜占庭验证者对这块跑过 Process / 看见要 Finalize 了，就当成已经每个验证者都跑过 Process，或当成已经是提议者那边也会叫 Process。
2. 看见 Finalize 请求把字段再填一遍 / 看见 Prepare / Process 已经给过，就当成已经不用再给，或当成已经跑过 Process。
3. 看见可以套用先前 Prepare / Process 的候选 / 看见同一块先跑过，就当成已经是 ExecuteTxState，或当成已经交差。

## 为什么会出事

官方写：调用 `FinalizeBlock` 时，共识算法保证至少一名非拜占庭验证者对这块跑过 `ProcessProposal`。目前会把 `FinalizeBlockRequest` 的字段填满，哪怕已经经 Prepare 或 Process 给过。应用按列表确定执行，也可以套用先前对同一块跑出的候选。

## 和相邻反模式

- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫就已经不用再 Process，不是本页这种至少一名非拜占庭验证者跑过 Process 不是已经每个验证者都跑过 Process。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种 Finalize 请求把字段再填一遍不是已经不用再给。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState，不是本页这种可以套用先前候选不是已经是 ExecuteTxState。
