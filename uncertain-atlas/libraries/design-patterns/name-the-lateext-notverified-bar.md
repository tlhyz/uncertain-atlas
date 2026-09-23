# 模式：把 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**例**：[+2/3 之后才进来的扩展写进了 commit info not already verified ≠ bundled（352）](../../tracks/implementation/worked-example-lateext-notverified-vs-bundled.md)。

## 三个名字

1. **写进了 last_commit 不是 already verified：** 看见 +2/3 之后才进来的扩展写进了 commit info / 写进了 last_commit / last_commit 里有扩展，不是已经 Verify 过 interchangeable / 已经 verified interchangeable / 已经 Verify 交差 interchangeable，不是 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable。

2. **有扩展 不是 already accept：** 看见有扩展 / 票上带了扩展 / 扩展字节在，不是已经 Accept interchangeable / 已经 accept interchangeable / 已经 Accept 交差 interchangeable，不是 348 req6coherence interchangeable / 34 vote-extension-block interchangeable。

3. **凑齐了 +2/3 不是 already later-verified：** 看见凑齐了 +2/3 / 过了最低 +2/3 / 最低门槛到了，不是已经后来的也验过 interchangeable / 已经 later-verified interchangeable / 已经后来验过交差 interchangeable，不是 810 lateext-notreverify interchangeable / 811 lateext-notrecall interchangeable。

官方把写进了 last_commit、不是已经 Accept、不是后来的也已经验过写成三个名字。把它们叫成一个「看见写进了 last_commit 就已经 Verify 过 interchangeable / 就已经 Accept interchangeable / 就已经后来的也验过 interchangeable」，会把 not already verified、not already accept、not already later-verified 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 not already verified / not already accept / not already later-verified 正式三事（352 余量），先数清问的是写进了 last_commit 是不是 already verified / 352 / lateext-sold-as-verified，是不是有扩展 是不是 already accept，还是凑齐了 +2/3 是不是 already later-verified，再决定要不要同一次发布。352 lateext vs verified bundled unbundling 在本页 item 1 启动。
