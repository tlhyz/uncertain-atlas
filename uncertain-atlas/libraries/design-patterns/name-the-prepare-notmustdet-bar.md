# 模式：把 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**例**：[没有确定性要求 not already must-deterministic ≠ bundled（338）](../../tracks/implementation/worked-example-prepare-notmustdet-vs-bundled.md)。

## 三个名字

1. **没有确定性要求 不是 already must-deterministic：** 看见 PrepareProposal 没有确定性要求 / Prepare 不被要求确定 / 没有这道要求，不是已经必须确定 interchangeable / 已经必须确定交差 interchangeable，不是 338 preparenondet bundled interchangeable / 33 four gates interchangeable / preparenondet-sold-as-deterministic interchangeable。

2. **可以依赖其它值 不是 already same-as-process：** 看见可以依赖其它值或操作 / 准备好的提案可以依赖其它值 / 可以不止 raw 和已提交状态，不是已经和 Process / Finalize 同一把尺 interchangeable / 已经同一把尺交差 interchangeable，不是 340 process-det interchangeable / 338 preparenondet item 2 interchangeable。

3. **Prepare 回了 不是 already settled：** 看见 Prepare 回了 / PrepareProposal 回了 / 准备好的提案回来了，不是已经交差 interchangeable / 已经交差同一句 interchangeable，不是 33 four gates interchangeable / 338 preparenondet item 3 interchangeable。

官方把没有确定性要求单句、already must-deterministic、already same-as-process、already settled 写成三个名字。把它们叫成一个「看见没有确定性要求就已经必须确定 interchangeable / 就已经和 Process 同一把尺 interchangeable / 就已经交差 interchangeable」，会把 not already must-deterministic、not already same-as-process、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal 没有确定性要求不是已经必须确定 not already must-deterministic / not already same-as-process / not already settled 正式三事（338 余量），先数清问的是没有确定性要求 是不是 already must-deterministic / 338 / preparenondet-sold-as-deterministic，是不是可以依赖其它值 是不是 already same-as-process，还是 Prepare 回了 是不是 already settled，再决定要不要同一次发布。338 preparenondet vs process bundled unbundling 在本页 item 1 启动。
