# 反模式：看见 Misbehavior.type 只是过错枚举就当成已经罚没 / 看见 height 是过错发生的高度、time 是那一高已提交块的时间就当成已经验过这个时间 / 看见 total_voting_power 是那一高验证者集合的总权就当成已经按到场定奖惩

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**例**：[Misbehavior.type 只是过错枚举 ≠ 已经罚没](../../tracks/implementation/worked-example-misbehavior-vs-enum.md)。

## 塌法

1. 看见 `Misbehavior.type` 只是过错枚举 / 看见有类型，就当成已经罚没，或当成已经定了奖惩。
2. 看见 `height` 是过错发生的高度、`time` 是那一高已提交块的时间 / 看见有时间，就当成已经验过这个时间，或当成已经交差。
3. 看见 `total_voting_power` 是那一高验证者集合的总权 / 看见有总权，就当成已经按到场定奖惩，或当成已经改了集合。

## 为什么会出事

官方写：`type` 是可能过错的枚举。枚举里有 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK`。`height` 是过错发生的高度。`time` 是那一高已提交块的时间戳。`total_voting_power` 是那一高验证者集合的总投票权。

## 和相邻反模式

- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没，不是本页这种 Misbehavior.type 只是过错枚举不是已经罚没。
- [timestamp-sold-as-checked](timestamp-sold-as-checked.md) 是票上 Timestamp 就已经验过，不是本页这种 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没，不是本页这种 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩。
