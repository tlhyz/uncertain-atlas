# 模式：把建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**例**：[建议按 Verify 同款逻辑再看一遍 not already engine-reverify ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notreverify-vs-bundled.md)。

## 三个名字

1. **建议再看 不是 already engine-reverify：** 看见建议按 `VerifyVoteExtension` 同款逻辑再看一遍 / 建议再看 / 同款逻辑再看，不是已经是引擎会再 Verify interchangeable / 已经 engine-reverify interchangeable / 已经引擎再 Verify 交差 interchangeable，不是 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable。

2. **Prepare 在用扩展 不是 already req6-done：** 看见 Prepare 在用扩展 / Prepare 要用这些扩展改提案 / 用扩展改提案，不是已经过了 Req 6 interchangeable / 已经 req6-done interchangeable / 已经 Req 6 交差 interchangeable，不是 348 req6coherence interchangeable / 809 lateext-notverified interchangeable。

3. **能改提案 不是 already settled：** 看见能改提案 / MAY 用扩展改提案 / 可以改提案，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 811 lateext-notrecall interchangeable / 330 veheight interchangeable。

官方把建议再看、不是已经过了 Req 6、不是已经交差写成三个名字。把它们叫成一个「看见建议再看就已经是引擎会再 Verify interchangeable / 就已经过了 Req 6 interchangeable / 就已经交差 interchangeable」，会把 not already engine-reverify、not already req6-done、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify not already engine-reverify / not already req6-done / not already settled 正式三事（352 余量），先数清问的是建议再看 是不是 already engine-reverify / 352 / lateext-sold-as-verified，是不是 Prepare 在用扩展 是不是 already req6-done，还是能改提案 是不是 already settled，再决定要不要同一次发布。352 lateext vs verified bundled unbundling 在本页 item 2 续。
