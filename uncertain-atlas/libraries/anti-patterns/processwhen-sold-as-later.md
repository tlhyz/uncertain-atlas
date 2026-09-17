# 反模式：看见 Process 调用是同步的就当成已经能在返回之后再改裁决 / 看见只做基本检查再异步 Process 就当成已经还能再 Reject / 看见非验证者可以立刻回 ACCEPT 就当成已经验过这块

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[Process 调用是同步的 ≠ 已经能在返回之后再改裁决](../../tracks/implementation/worked-example-process-when-vs-later.md)。

## 塌法

1. 看见 Process 调用是同步的 / 看见引擎在等回包，就当成已经能在返回之后再改裁决，或当成已经离开关键路径。
2. 看见只做基本检查再异步 Process / 看见已经回了 `ACCEPT`，就当成已经还能再 Reject，或当成已经还能强迫 prevote/precommit `nil`。
3. 看见非验证者可以立刻回 `ACCEPT` / 看见不是验证者，就当成已经验过这块，或当成已经是验证者也可以立刻交差。

## 为什么会出事

官方写：CometBFT 调 `ProcessProposal` 是同步的。应用可以先做基本检查再异步处理这块；这时不能再 Reject，也不能再强迫 prevote/precommit `nil`。若 *p* 不是验证者，且应用不想让非验证者处理 `ProcessProposal`，可以立刻回 `ACCEPT`。

## 和相邻反模式

- [preparetimeout-sold-as-liveness](preparetimeout-sold-as-liveness.md) 是立刻整块执行就已经离开关键路径，不是本页这种 Process 调用是同步的不是已经能在返回之后再改裁决。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种只做基本检查再异步 Process 不是已经还能再 Reject。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 Process 也会在提议者那边叫不是已经不用再 Process，不是本页这种非验证者可以立刻回 ACCEPT 不是已经验过这块。
