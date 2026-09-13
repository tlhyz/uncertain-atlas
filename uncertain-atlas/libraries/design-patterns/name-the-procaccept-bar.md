# 模式：把 ProcessProposal SHOULD Accept 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[应用 SHOULD 总是设 ACCEPT ≠ 已经 honest proposal 必须 Accept](../../tracks/implementation/worked-example-procaccept-vs-req3.md)。

## 三个名字

1. **SHOULD 总是设 ACCEPT 不是已经 honest proposal 必须 Accept：** 看见 SHOULD always set to ACCEPT 不是已经 Requirement 3 已经测过。
2. **除非真的知道 REJECT 的活性代价不是已经 REJECT 是免费过滤：** 看见 unless they really know liveness implications 不是已经 Process REJECT = prevote nil 那种已经结算。
3. **SHOULD Accept 默认策略不是已经不能 Reject：** 看见 SHOULD Accept 不是已经 Process 340 那种 SHOULD Accept 通则 interchangeable。

## 为什么要分开叫

官方把 ProcessProposal SHOULD Accept 写成三个名字。把它们叫成一个「看见写了默认 Accept 就已经 honest proposal 必须 Accept」，会把 SHOULD 建议、REJECT 活性代价和 Requirement 3 测试目标一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见写了默认 Accept 就已经 honest proposal 必须 Accept」，先数清问的是 SHOULD 总是设 ACCEPT 是不是已经 honest proposal 必须 Accept、除非真的知道 REJECT 的活性代价是不是已经 REJECT 是免费过滤，还是 SHOULD Accept 默认策略是不是已经 Requirement 3 已经测过，再决定要不要同一次发布。
