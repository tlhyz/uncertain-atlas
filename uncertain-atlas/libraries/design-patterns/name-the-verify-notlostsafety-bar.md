# 模式：把 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirements 7–8。  
**例**：[Verify 非确定会伤活性 not already lost-safety ≠ bundled（341）](../../tracks/implementation/worked-example-verify-notlostsafety-vs-bundled.md)。

## 三个名字

1. **活性会被伤 不是 already lost-safety：** 看见活性会被伤 / Verify 里有非确定 bug / 打中的进程无法守 Req 7 或 8，不是已经丢了安全性 interchangeable / 已经丢安全性交差 interchangeable，不是 341 verifydet bundled interchangeable / 340 processdet interchangeable / verifydet-sold-as-extend interchangeable。

2. **必须非常小心 不是 already has-patch：** 看见没有现成解法 / 实现 ExtendVote 和 VerifyVoteExtension 必须非常小心 / 没有协议层补丁，不是已经有引擎补丁 interchangeable / 已经有补丁交差 interchangeable，不是 34 vote-extension interchangeable / 341 verifydet item 1 interchangeable。

3. **SHOULD Accept 不是 already must-reject：** 看见 SHOULD Accept / 通则是一律 Accept / 建议一律 Accept，不是已经必须拒坏扩展 interchangeable / 已经必须拒交差 interchangeable，不是 348 req6-coherence interchangeable / 341 verifydet item 2 interchangeable。

官方把活性会被伤单句、already lost-safety、already has-patch、already must-reject 写成三个名字。把它们叫成一个「看见活性会被伤就已经丢了安全性 interchangeable / 就已经有补丁 interchangeable / 就必须拒坏扩展 interchangeable」，会把 not already lost-safety、not already has-patch、not already must-reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify 非确定会伤活性不是已经丢了安全性 not already lost-safety / not already has-patch / not already must-reject 正式三事（341 余量），先数清问的是活性会被伤 是不是 already lost-safety / 341 / verifydet-sold-as-extend，是不是必须非常小心 是不是 already has-patch，还是 SHOULD Accept 是不是 already must-reject，再决定要不要同一次发布。341 verifydet vs extend bundled unbundling 在本页 item 3 完成。
