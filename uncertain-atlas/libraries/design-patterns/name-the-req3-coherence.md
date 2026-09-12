# 模式：把 Prepare–Process 一致性三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**例**：[正确提议者的准备提案必须被正确接收者 Accept ≠ 已经是任意块都会 Accept](../../tracks/implementation/worked-example-req3-coherence-vs-accept.md)。

## 三个名字

1. **正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept：** 看见正确进程之间必须过不是任意块已经都会过。
2. **Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题：** 看见有确定 bug 不是已经只伤活性。
3. **Req 3 是大量测试和自动验证的目标不是已经测过：** 看见写了测试目标不是已经交差。

## 为什么要分开叫

官方把正确进程之间必须过、确定 bug 算拜占庭、因此必须大量测写成三件事。把它们叫成一个「看见必须 Accept 就已经交差」，会把四门、Process 确定性和 Prepare 可以不确定一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须 Accept 就已经交差」，先数清问的是正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept、Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题，还是 Req 3 是大量测试和自动验证的目标不是已经测过，再决定要不要同一次发布。
