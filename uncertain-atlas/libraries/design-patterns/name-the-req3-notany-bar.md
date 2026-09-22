# 模式：把正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**例**：[正确提议者的准备提案必须被正确接收者 Accept not already any-block ≠ bundled（347）](../../tracks/implementation/worked-example-req3-notany-vs-bundled.md)。

## 三个名字

1. **正确提议者的准备提案必须被正确接收者 Accept 不是 already any-block：** 看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 正确进程之间永远过 / 正确提议者交出来的必须过，不是已经是任意块都会 Accept interchangeable / 已经 any-block interchangeable / 已经任意块过交差 interchangeable，不是 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable。

2. **必须 Accept 不是 already default-accept：** 看见必须 Accept / 正确接收者 Process 必须回 Accept / 正确进程之间永远过，不是已经写了默认 Accept interchangeable / 已经 default-accept interchangeable / 已经默认 Accept 交差 interchangeable，不是 33 four gates interchangeable / 348 req6coherence interchangeable。

3. **正确进程之间过 不是 already settled：** 看见正确进程之间过 / 正确提议者交出来的必须过 / 正确接收者必须 Accept，不是已经交差 interchangeable / 已经 settled interchangeable / 已经 Accept 交差 interchangeable，不是 795 req3-notbyz interchangeable / 796 req3-nottested interchangeable。

官方把正确进程之间必须过、不是已经写了默认 Accept、不是已经交差写成三个名字。把它们叫成一个「看见必须 Accept 就已经任意块都会过 interchangeable / 就已经写了默认 Accept interchangeable / 就已经交差 interchangeable」，会把 not already any-block、not already default-accept、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量），先数清问的是正确提议者的准备提案必须被正确接收者 Accept 是不是 already any-block / 347 / req3coherence-sold-as-accept，是不是必须 Accept 是不是 already default-accept，还是正确进程之间过 是不是 already settled，再决定要不要同一次发布。347 req3 vs accept bundled unbundling 在本页 item 1 启动。
