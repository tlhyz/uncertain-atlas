# 反模式：看见 Misbehavior.height 就当成已经是 Prepare/Process 请求 height / 看见 Misbehavior.time 就当成已经验过票上 Timestamp / 看见 height 和 time 一起就当成已经定了奖惩

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.height 是过错发生的高度 ≠ 已经 Prepare/Process 请求 height](../../tracks/implementation/worked-example-misbheighttime-vs-votetime.md)。

## 塌法

1. 看见 Misbehavior.height 是过错发生的高度 / 看见填了 height，就当成已经是 PrepareProposalRequest.height / ProcessProposalRequest.height，或当成已经验过块头。
2. 看见 Misbehavior.time 是 height 那一高已提交块的时间戳 / 看见填了 time，就当成已经验过票上 Timestamp，或当成已经是 Prepare/Process 请求 time interchangeable。
3. 看见 Misbehavior.height 和 time 一起 / 看见对上了 height 和 time，就当成已经定了奖惩，或当成已经 slashed。

## 为什么会出事

官方写：`height` is Height when the offense occurred。`time` is Timestamp of the block that was committed at height `height`。这不是已经 Prepare/Process 请求 height/time interchangeable，不是已经验过票上时间，也不是已经定了奖惩。看见 Misbehavior height/time 栏正式三事，不是已经 Misbehavior 结构栏 type/total_voting_power 那种已经罚没，不是已经 misbehavior 列表定奖惩。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 Misbehavior 结构栏 type/height/time/total_voting_power，不是本页这种 height/time 栏单独切片。
- [misbvalidator-sold-as-voteinfo](misbvalidator-sold-as-voteinfo.md) 是 Misbehavior.validator 不是已经 VoteInfo 按到场定奖惩，不是本页这种 height/time 不是已经验过票上时间。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 列表不是已经定奖惩，不是本页这种 height/time 不是已经定了奖惩。
