# 反模式：看见 MisbehaviorType UNKNOWN 就当成已经归类成 DUPLICATE_VOTE / 看见 DUPLICATE_VOTE 就当成已经罚没 / 看见 LIGHT_CLIENT_ATTACK 就当成已经是 DUPLICATE_VOTE

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**例**：[MisbehaviorType UNKNOWN 只是未知过错枚举 ≠ 已经归类成 DUPLICATE_VOTE](../../tracks/implementation/worked-example-misbtype-vs-slashed.md)。

## 塌法

1. 看见 MisbehaviorType `UNKNOWN` / 看见填了 UNKNOWN，就当成已经归类成 `DUPLICATE_VOTE`，或当成已经罚没。
2. 看见 MisbehaviorType `DUPLICATE_VOTE` / 看见填了 DUPLICATE_VOTE，就当成已经 slashed，或当成已经 LIGHT_CLIENT_ATTACK interchangeable。
3. 看见 MisbehaviorType `LIGHT_CLIENT_ATTACK` / 看见填了 LIGHT_CLIENT_ATTACK，就当成已经是 `DUPLICATE_VOTE`，或当成已经罚没。

## 为什么会出事

官方写：MisbehaviorType is an enum with the listed fields: `UNKNOWN` (0), `DUPLICATE_VOTE` (1), `LIGHT_CLIENT_ATTACK` (2)。这不是已经归类，不是已经 slashed，也不是 enum 三值 interchangeable。看见 MisbehaviorType 枚举正式三事，不是已经 Misbehavior 结构栏 height/time/total_voting_power 那种已经验过时间，不是已经 misbehavior 列表定奖惩。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 Misbehavior 结构栏 type/height/time/total_voting_power，不是本页这种 MisbehaviorType enum 三值。
- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.misbehavior 列表不是已经定奖惩，不是本页这种 DUPLICATE_VOTE enum 不是已经罚没。
- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没，不是本页这种 enum 名不是已经 slashed。
