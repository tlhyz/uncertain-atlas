# 反模式：看见 Misbehavior.total_voting_power 就当成已经是 VoteInfo.validator.power / Misbehavior.validator.power / 看见 Misbehavior.total_voting_power 就当成已经按到场定奖惩 / 看见 Misbehavior.total_voting_power 就当成已经定了奖惩

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权 ≠ 已经 VoteInfo.validator.power](../../tracks/implementation/worked-example-misbtvp-vs-attendance.md)。

## 塌法

1. 看见 Misbehavior.total_voting_power 是 height 那一高验证者集合的总投票权 / 看见填了 total_voting_power，就当成已经是 VoteInfo.validator.power / Misbehavior.validator.power 那种单个验证者权，或当成已经 CommitInfo.votes 里按投票权降序排过那种已经奖罚完。
2. 看见 Misbehavior.total_voting_power 是 offense height 那一高的集合总权 / 看见填了 total_voting_power，就当成已经按到场定奖惩，或当成已经是 VoteInfo / ExtendedVoteInfo Usage 里 allowing for rewards based on validator availability interchangeable。
3. 看见 Misbehavior.total_voting_power / 看见有总权，就当成已经定了奖惩，或当成已经 slashed，或当成已经改了集合。

## 为什么会出事

官方写：`total_voting_power` is Total voting power of the validator set at height `height`。这不是已经 VoteInfo / ExtendedVoteInfo 里某个 Validator.power interchangeable，不是已经按到场定奖惩，也不是已经定了奖惩。看见 Misbehavior total_voting_power 栏正式三事，不是已经 Misbehavior 结构栏 type/height/time 那种已经罚没，不是已经 misbehavior 列表定奖惩。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 Misbehavior 结构栏 type/height/time/total_voting_power，不是本页这种 total_voting_power 栏单独切片。
- [misbvalidator-sold-as-voteinfo](misbvalidator-sold-as-voteinfo.md) 是 Misbehavior.validator 不是已经 VoteInfo 按到场定奖惩，不是本页这种 total_voting_power 不是已经单个验证者 power。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 列表不是已经定奖惩，不是本页这种 total_voting_power 不是已经定了奖惩。
