# 反模式：看见 Misbehavior.validator 就当成已经 slashed / 看见 Misbehavior.validator 就当成已经是 VoteInfo.validator 按到场定奖惩 / 看见 Misbehavior.validator 就当成已经是 ValidatorUpdate

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior Fields。  
**例**：[Misbehavior.validator 是过错验证者 ≠ 已经 slashed](../../tracks/implementation/worked-example-misbvalidator-vs-voteinfo.md)。

## 塌法

1. 看见 Misbehavior.validator 是过错验证者 / 看见填了 validator，就当成已经 slashed，或当成已经罚没。
2. 看见 Misbehavior.validator 只是 address+power 的 Validator 结构 / 看见填了 validator，就当成已经是 VoteInfo.validator 那种按到场定奖惩，或当成已经 CommitInfo.votes 里那份 interchangeable。
3. 看见 Misbehavior.validator / 看见有 address 和 power，就当成已经是 ValidatorUpdate，或当成已经改了集合。

## 为什么会出事

官方写：`validator` is The offending validator。`Validator` 也出现在 VoteInfo / ExtendedVoteInfo 里按到场定奖惩，但 Misbehavior 里的 validator 另指过错的人。`ValidatorUpdate` 另用来更新集合。这不是已经 slashed，不是已经 VoteInfo.validator interchangeable，也不是已经改了集合。看见 Misbehavior.validator 栏正式三事，不是已经 Misbehavior 结构栏 type/height/time 那种已经验过时间，不是已经 misbehavior 列表定奖惩。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 Misbehavior 结构栏 type/height/time/total_voting_power，不是本页这种 Misbehavior.validator 栏。
- [misbtype-sold-as-slashed](misbtype-sold-as-slashed.md) 是 MisbehaviorType enum 三值不是已经罚没，不是本页这种 offending validator 字段。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 列表不是已经定奖惩，不是本页这种 validator 字段不是已经 VoteInfo 按到场定奖惩。
