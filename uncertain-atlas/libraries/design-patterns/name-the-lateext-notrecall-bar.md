# 模式：把下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**例**：[下一高度 round 0 写进 ExtendedCommitInfo not already called-again ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notrecall-vs-bundled.md)。

## 三个名字

1. **写进去了 不是 already called-again：** 看见下一高度 round 0 收到上一高度 `CommitRound` 的 Precommit / 写进 `ExtendedCommitInfo` / 写进去了，不是已经又叫了 Verify interchangeable / 已经 called-again interchangeable / 已经又 Verify 交差 interchangeable，不是 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable。

2. **规范允许 不是 already must-recall：** 看见规范允许 / MAY 写进 / 可以不叫，不是已经必须再叫 interchangeable / 已经 must-recall interchangeable / 已经必须再 Verify 交差 interchangeable，不是 348 req6coherence interchangeable / 810 lateext-notreverify interchangeable。

3. **是上一高度 不是 already this-round-verify：** 看见是上一高度 / *h-1* / 上一高度 `CommitRound` *r*，不是已经是本轮那次 Verify interchangeable / 已经 this-round-verify interchangeable / 已经本轮 Verify 交差 interchangeable，不是 809 lateext-notverified interchangeable / 330 veheight interchangeable。

官方把写进去了、不是已经必须再叫、不是已经是本轮那次 Verify 写成三个名字。把它们叫成一个「看见写进去了就已经又叫了 Verify interchangeable / 就已经必须再叫 interchangeable / 就已经是本轮那次 Verify interchangeable」，会把 not already called-again、not already must-recall、not already this-round-verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量），先数清问的是写进去了 是不是 already called-again / 352 / lateext-sold-as-verified，是不是规范允许 是不是 already must-recall，还是是上一高度 是不是 already this-round-verify，再决定要不要同一次发布。352 lateext vs verified bundled unbundling 在本页 item 3 完成。
