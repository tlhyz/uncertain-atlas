# 反模式：看见立刻整块执行就当成已经离开关键路径 / 看见填了 TimeoutPropose 就当成已经装得下 / 看见又开一轮就当成已经丢了活性

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 1 [`PrepareProposal`, timeliness]。  
**例**：[立刻整块执行 ≠ 已经离开关键路径](../../tracks/implementation/worked-example-prepare-timeout-vs-liveness.md)。

## 塌法

1. 看见 Prepare 里立刻整块执行 / 看见执行回了，就当成已经离开提议超时的关键路径，或当成已经不挡 q 的提议钟。
2. 看见填了 TimeoutPropose / 看见同步期，就当成已经装得下这次 Prepare 执行，或当成 q 的提议钟已经不会响。
3. 看见又开一轮 / 看见 TimeoutPropose 只是初值，就当成已经丢了活性，或当成超时已经不再涨。

## 为什么会出事

官方写：Prepare 里整块执行站在关键路径上。同步期里 *q* 的 `TimeoutPropose` 必须装得下这次执行，否则 *q* prevote `nil`。违反 Requirement 1 可能再开一轮，但初值会涨，不是丢掉活性。

## 和相邻反模式

- [preparetimeout-notlivenesslost-sold-as-bundled](preparetimeout-notlivenesslost-sold-as-bundled.md) 是又开一轮不是已经丢了活性 item 3 单句边界，不是本页 PrepareProposal 及时性 bundled 全段。
- [preparetimeout-notfit-sold-as-bundled](preparetimeout-notfit-sold-as-bundled.md) 是填了 TimeoutPropose 不是已经装得下 item 2 单句边界，不是本页 PrepareProposal 及时性 bundled 全段。
- [preparetimeout-notcriticalpath-sold-as-bundled](preparetimeout-notcriticalpath-sold-as-bundled.md) 是立刻整块执行不是已经离开关键路径 item 1 单句边界，不是本页 PrepareProposal 及时性 bundled 全段。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 Prepare 及时性。
- [timeout-commit-sold-as-finality](timeout-commit-sold-as-finality.md) 是本地超时 ≠ 已经是最终性，不是本页。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选 ≠ 已经是 ExecuteTxState，不是本页。
