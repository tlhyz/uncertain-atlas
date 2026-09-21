# 模式：把 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8。  
**例**：[Verify 必须只依赖扩展、这块和上一份状态 not already like-extend ≠ bundled（341）](../../tracks/implementation/worked-example-verify-notlikeextend-vs-bundled.md)。

## 三个名字

1. **必须确定 不是 already like-extend：** 看见 VerifyVoteExtension 必须只依赖扩展、这块和 *s_{h-1}* / 必须确定 / 是确定函数，不是已经可以像 ExtendVote 那样依赖其它值 interchangeable / 已经可以依赖其它值交差 interchangeable，不是 341 verifydet bundled interchangeable / 338 preparenondet interchangeable / verifydet-sold-as-extend interchangeable。

2. **只依赖扩展、这块和上一份状态 不是 already same-as-nondet：** 看见只依赖扩展、这块和上一份状态 / 只依赖 *e*、*w* 和 *s_{h-1}* / 不能另依赖其它值，不是已经和 ExtendVote 没有确定性要求同一句 interchangeable / 已经和 ExtendVote 同一把尺交差 interchangeable，不是 338 preparenondet interchangeable / 341 verifydet item 2 interchangeable。

3. **Verify 回了 不是 already settled：** 看见 Verify 回了 / VerifyVoteExtension 回了 / Accept 或 Reject 回来了，不是已经交差 interchangeable / 已经交差同一句 interchangeable，不是 34 vote-extension interchangeable / 341 verifydet item 3 interchangeable。

官方把必须确定单句、already like-extend、already same-as-nondet、already settled 写成三个名字。把它们叫成一个「看见必须确定就可以像 ExtendVote 那样 interchangeable / 就已经和 ExtendVote nondet 同一句 interchangeable / 就已经交差 interchangeable」，会把 not already like-extend、not already same-as-nondet、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 必须只依赖扩展、这块和上一份状态不是已经可以像 ExtendVote 那样依赖其它值 not already like-extend / not already same-as-nondet / not already settled 正式三事（341 余量），先数清问的是必须确定 是不是 already like-extend / 341 / verifydet-sold-as-extend，是不是只依赖扩展、这块和上一份状态 是不是 already same-as-nondet，还是 Verify 回了 是不是 already settled，再决定要不要同一次发布。341 verifydet vs extend bundled unbundling 在本页 item 1 启动。
