# 反模式：看见 Process 也会在提议者那边叫就当成已经不用再 Process / 看见通常紧跟 Prepare、列表对得上就当成已经保证是这一次 / 看见失败时可能对上更早一次或根本不调就当成已经每轮都会叫

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[Process 也会在提议者那边叫 ≠ 已经不用再 Process](../../tracks/implementation/worked-example-process-also-vs-prepare.md)。

## 塌法

1. 看见 `ProcessProposal` 也会在这一轮的提议者那边叫 / 看见自己刚 Prepare 过，就当成已经不用再 Process，或当成已经交差。
2. 看见通常紧跟 Prepare、`ProcessProposalRequest.txs` 等于 `PrepareProposalResponse.txs` / 看见列表对得上，就当成已经保证是这一次 Prepare 的回包，或当成已经必须对上。
3. 看见失败时可能对上更早一次 Prepare / 看见根本不调 Process，就当成已经是这一次 Prepare，或当成已经每轮都会叫 Process。

## 为什么会出事

官方写：`ProcessProposal` 也会在这一轮的提议者那边叫。通常紧跟 Prepare，而且列表对得上。失败时不保证：可能对上更早一次 Prepare 的回包，或者根本不调 Process。

## 和相邻反模式

- [process-notskip-sold-as-bundled](process-notskip-sold-as-bundled.md) 是 Process 也会在提议者那边叫 not already skip-process / not already settled / not already already-processed 正式三事（351 item 1），不是本页 bundled 全段 alone。
- [process-notguaranteed-sold-as-bundled](process-notguaranteed-sold-as-bundled.md) 是通常紧跟 Prepare、列表对得上 not already guaranteed-this / not already must-match / not already same-call 正式三事（351 item 2），不是本页 bundled 全段 alone。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 Process 也会在提议者那边叫不是已经不用再 Process。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept，不是本页这种通常紧跟 Prepare、列表对得上不是已经保证是这一次。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选不是已经是 ExecuteTxState，不是本页这种失败时可能对上更早一次或根本不调不是已经每轮都会叫。
