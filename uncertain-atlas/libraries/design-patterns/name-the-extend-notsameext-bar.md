# 模式：把 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements，Req 11–12 之后。  
**例**：[ExtendVote 没有确定性要求 not already same-extension ≠ bundled（338）](../../tracks/implementation/worked-example-extend-notsameext-vs-bundled.md)。

## 三个名字

1. **同一块 不是 already same-extension：** 看见同一块 / *w^r_p = w^r_q* / 同一份块，不是已经是同一份扩展 interchangeable / 已经同一份扩展交差 interchangeable，不是 338 preparenondet bundled interchangeable / 34 vote-extension interchangeable / preparenondet-sold-as-deterministic interchangeable。

2. **没有确定性要求 不是 already must-same-e：** 看见 ExtendVote 没有确定性要求 / ExtendVote 也可以不确定 / 没有这道要求，不是已经必须同一份 interchangeable / 已经必须同一份交差 interchangeable，不是 341 verifydet interchangeable / 338 preparenondet item 1 interchangeable。

3. **能签扩展 不是 already same-as-verify：** 看见能签扩展 / 扩展可以依赖其它值或操作 / 能签，不是已经和 VerifyVoteExtension 必须确定同一把尺 interchangeable / 已经同一把尺交差 interchangeable，不是 341 verifydet interchangeable / 338 preparenondet item 2 interchangeable。

官方把同一块单句、already same-extension、already must-same-e、already same-as-verify 写成三个名字。把它们叫成一个「看见同一块就已经是同一份扩展 interchangeable / 就已经必须同一份 interchangeable / 就已经和 Verify 同一把尺 interchangeable」，会把 not already same-extension、not already must-same-e、not already same-as-verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 没有确定性要求不是已经是同一份扩展 not already same-extension / not already must-same-e / not already same-as-verify 正式三事（338 余量），先数清问的是同一块 是不是 already same-extension / 338 / preparenondet-sold-as-deterministic，是不是没有确定性要求 是不是 already must-same-e，还是能签扩展 是不是 already same-as-verify，再决定要不要同一次发布。338 preparenondet vs process bundled unbundling 在本页 item 3 完成。
