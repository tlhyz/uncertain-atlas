# 反模式：看见 SHOULD 总是设 ACCEPT 就当成已经 honest proposal 必须 Accept / 看见除非真的知道活性代价就当成已经 REJECT 是免费过滤 / 看见写了默认 Accept 就当成已经 Requirement 3 已经测过

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**例**：[应用 SHOULD 总是设 ACCEPT ≠ 已经 honest proposal 必须 Accept](../../tracks/implementation/worked-example-procaccept-vs-req3.md)。

## 塌法

1. 看见应用 SHOULD 总是设 `ProcessProposalResponse.status` 为 `ACCEPT` / 看见 SHOULD always set to ACCEPT，就当成已经 honest proposal 必须 Accept，或当成已经是 Requirement 3 已经测过。
2. 看见除非他们 _really_ know what the potential liveness implications of returning `REJECT` are / 看见除非真的知道 REJECT 的活性代价，就当成已经 REJECT 是免费过滤，或当成已经 Process REJECT = prevote nil 那种已经结算。
3. 看见 SHOULD Accept 默认策略 / 看见写了默认 Accept，就当成已经不能 Reject，或当成已经 Process 回包栏 bundled 三事 interchangeable。

## 为什么会出事

官方写：application implementers SHOULD always set `ProcessProposalResponse.status` to `ACCEPT`, unless they _really_ know what the potential liveness implications of returning `REJECT` are。Usage 也写：If `ProcessProposalResponse.status` is `REJECT`, consensus assumes the proposal received is not valid。这不是已经 honest proposal 必须 Accept，不是已经 REJECT 没有代价，也不是已经 Requirement 3 已经测过 interchangeable。

## 和相邻反模式

- [procrespstatus-sold-as-procstatus](procrespstatus-sold-as-procstatus.md) 是 Process 回包栏 bundled，不是本页这种 SHOULD Accept 单独切片。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是 honest proposal 必须 Accept，不是本页这种 SHOULD 总是设 ACCEPT 不是已经 honest proposal 必须 Accept。
- [procreject-sold-as-invalid](procreject-sold-as-invalid.md) 是 REJECT 共识假设，不是本页这种除非真的知道 REJECT 的活性代价不是已经 REJECT 是免费过滤。
