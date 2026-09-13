# 模式：把 ExtendVote When lock values 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 1。  
**例**：[lock values ≠ bundled](../../tracks/implementation/worked-example-extwhen-lock-vs-bundled.md)。

## 三个名字

1. **sets lockedValue/validValue to v 不是 +2/3 prevote 锁住 bundled：** 看见 sets lockedValue and validValue to v，不是 361 +2/3 prevote 才锁住再调 interchangeable。
2. **sets lockedRound/validRound to r 不是 validValue 跳过 Prepare：** 看见 sets lockedRound and validRound to r，不是 356 validValue 跳过 Prepare interchangeable。
3. **step 1 before ExtendVote call 不是 ExtendVote When 正式流程 bundled：** 看见 sets lock values before ExtendVote with v，不是 438 填 CanonicalVoteExtension / 广播 Precommit interchangeable。

## 为什么要分开叫

官方把 sets lockedValue/validValue、sets lockedRound/validRound、step 1 before ExtendVote call、+2/3 prevote 锁住 bundled（361）、validValue 跳过 Prepare（356）、ExtendVote When 正式流程 bundled（438）写成三个名字。把它们叫成一个「看见 +2/3 prevote 就已经 lockedValue/validValue interchangeable、已经 validValue 跳过 Prepare interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」，会把 lock values、round 赋值、call 顺序三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When lock values 正式三事，先数清问的是 sets lockedValue/validValue 是不是 +2/3 prevote 锁住 bundled interchangeable、sets lockedRound/validRound 是不是 validValue 跳过 Prepare interchangeable、step 1 before ExtendVote call 是不是 ExtendVote When 正式流程 bundled interchangeable，再决定要不要同一次发布。
