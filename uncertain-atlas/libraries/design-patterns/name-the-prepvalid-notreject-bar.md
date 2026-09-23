# 模式：把 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[Prepare 回包验不过引擎崩溃 not already process-reject ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notreject-vs-bundled.md)。

## 三个名字

1. **崩溃了 不是 already process-reject：** 看见崩溃了 / Prepare 回包验不过 / 引擎当应用坏了并崩溃，不是已经是 Process REJECT interchangeable / 已经 process-reject interchangeable / 已经是 Process REJECT 交差 interchangeable，不是 357 preparevalid bundled interchangeable / preparevalid-sold-as-checked interchangeable。

2. **回包坏了 不是 already req3-accept：** 看见回包坏了 / 验不过 PrepareProposalResponse / 回包验不过，不是已经是 Req 3 必须 Accept interchangeable / 已经 req3-accept interchangeable / 已经是 Req 3 必须 Accept 交差 interchangeable，不是 347 req3 interchangeable / 824 prepvalid-notdedup interchangeable。

3. **引擎停了 不是 already settled：** 看见引擎停了 / 崩溃停机 / 应用被当成故障，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 826 prepvalid-notfinalize interchangeable / 33 fourgates interchangeable。

官方把崩溃了、不是已经是 Req 3 必须 Accept、不是已经交差写成三个名字。把它们叫成一个「看见崩溃了就已经是 Process REJECT interchangeable / 就已经是 Req 3 必须 Accept interchangeable / 就已经交差 interchangeable」，会把 not already process-reject、not already req3-accept、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包验不过引擎崩溃不是已经是 Process REJECT not already process-reject / not already req3-accept / not already settled 正式三事（357 余量），先数清问的是崩溃了 是不是 already process-reject / 357 / preparevalid-sold-as-checked，是不是回包坏了 是不是 already req3-accept，还是引擎停了 是不是 already settled，再决定要不要同一次发布。357 prepare-valid vs checked bundled unbundling 在本页 item 2 续。
