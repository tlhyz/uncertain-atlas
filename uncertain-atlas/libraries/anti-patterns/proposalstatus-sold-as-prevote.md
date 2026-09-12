# 反模式：看见 UNKNOWN 一律是错、引擎当应用坏了会崩就当成已经是四门已经结算 / 看见 ACCEPT 表示应用认为提案合法、共识会发 Prevote 就当成已经交差 / 看见 REJECT 表示应用认为提案非法、共识会发 Prevote nil 就当成已经能稍后改裁决

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-proposalstatus-vs-prevote.md)。

## 塌法

1. 看见 `UNKNOWN` 一律是错、引擎当应用坏了会崩 / 看见回了 `UNKNOWN`，就当成已经是四门已经结算，或当成已经交差。
2. 看见 `ACCEPT` 表示应用认为提案合法、共识会发 Prevote / 看见回了 `ACCEPT`，就当成已经交差，或当成已经必须 Accept。
3. 看见 `REJECT` 表示应用认为提案非法、共识会发 Prevote nil / 看见回了 `REJECT`，就当成已经能稍后改裁决，或当成已经没进块。

## 为什么会出事

官方写：`ProposalStatus` 用在 `ProcessProposal` 回包。回 `UNKNOWN` 一律是错；CometBFT 会当应用坏了，然后崩。`ACCEPT` 表示应用认为这份提案合法，共识算法收下这份提案并给它发 Prevote。`REJECT` 表示应用认为这份提案非法，共识算法拒掉这份提案，改发 Prevote nil。

## 和相邻反模式

- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept，不是本页这种 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差。
- [processwhen-sold-as-later](processwhen-sold-as-later.md) 是 Process 调用是同步的就已经能在返回之后再改裁决，不是本页这种 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决。
