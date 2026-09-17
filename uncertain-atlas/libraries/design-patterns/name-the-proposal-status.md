# 模式：把 ProposalStatus 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**例**：[UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-proposalstatus-vs-prevote.md)。

## 三个名字

1. **UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算：** 看见回了 UNKNOWN 不是已经交差。
2. **ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差：** 看见回了 ACCEPT 不是已经必须 Accept。
3. **REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决：** 看见回了 REJECT 不是已经没进块。

## 为什么要分开叫

官方把 UNKNOWN 一律是错、ACCEPT 会发 Prevote、REJECT 会发 Prevote nil 写成三件事。把它们叫成一个「看见回了 ProposalStatus 就已经是四门已经结算」，会把四门、必须 Accept 和同步裁决一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ProposalStatus 就已经是四门已经结算」，先数清问的是 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算、ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差，还是 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决，再决定要不要同一次发布。
