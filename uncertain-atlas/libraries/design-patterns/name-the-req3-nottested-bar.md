# 模式：把 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**例**：[Req 3 是大量测试和自动验证的目标 not already tested ≠ bundled（347）](../../tracks/implementation/worked-example-req3-nottested-vs-bundled.md)。

## 三个名字

1. **Req 3 是大量测试和自动验证的目标 不是 already tested：** 看见同一份代码库很可能同时踩中、多数 prevote nil / Req 3 因此是大量测试和自动验证的目标 / 写了测试目标，不是已经测过 interchangeable / 已经 tested interchangeable / 已经测过交差 interchangeable，不是 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable。

2. **会 prevote nil 不是 already engine-blocks：** 看见会 prevote nil / 多数或全部进程 prevote nil / 严重伤活性，不是已经是引擎会帮你挡 interchangeable / 已经 engine-blocks interchangeable / 已经引擎挡交差 interchangeable，不是 338 preparenondet interchangeable / 33 four gates interchangeable。

3. **写了测试目标 不是 already settled：** 看见写了测试目标 / 是大量测试和自动验证的目标 / 因此是测试目标，不是已经交差 interchangeable / 已经 settled interchangeable / 已经测试交差 interchangeable，不是 794 req3-notany interchangeable / 795 req3-notbyz interchangeable。

官方把必须测、不是已经是引擎会帮你挡、不是已经交差写成三个名字。把它们叫成一个「看见写了测试目标就已经测过 interchangeable / 就已经是引擎会帮你挡 interchangeable / 就已经交差 interchangeable」，会把 not already tested、not already engine-blocks、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量），先数清问的是 Req 3 是大量测试和自动验证的目标 是不是 already tested / 347 / req3coherence-sold-as-accept，是不是会 prevote nil 是不是 already engine-blocks，还是写了测试目标 是不是 already settled，再决定要不要同一次发布。347 req3 vs accept bundled unbundling 在本页 item 3 完成。
