# 模式：把 MisbehaviorType 枚举正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**例**：[MisbehaviorType UNKNOWN 只是未知过错枚举 ≠ 已经归类成 DUPLICATE_VOTE](../../tracks/implementation/worked-example-misbtype-vs-slashed.md)。

## 三个名字

1. **MisbehaviorType UNKNOWN 只是未知过错枚举不是已经归类成 DUPLICATE_VOTE / 已经罚没：** 看见 UNKNOWN 不是已经知道是双签。
2. **MisbehaviorType DUPLICATE_VOTE 只是双签枚举不是已经罚没：** 看见 DUPLICATE_VOTE 不是已经 slashed。
3. **MisbehaviorType LIGHT_CLIENT_ATTACK 只是轻客户端攻击枚举不是已经 DUPLICATE_VOTE：** 看见 LIGHT_CLIENT_ATTACK 不是已经 interchange 成双签 enum。

## 为什么要分开叫

官方把 MisbehaviorType 里 UNKNOWN、DUPLICATE_VOTE、LIGHT_CLIENT_ATTACK 三个枚举值写成三个名字。把它们叫成一个「看见 Misbehavior.type 填了枚举就已经罚没」，会把 enum 三值和 Misbehavior 结构栏、请求 misbehavior 列表一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior.type 填了枚举就已经罚没」，先数清问的是 MisbehaviorType UNKNOWN 是不是已经归类成 DUPLICATE_VOTE、MisbehaviorType DUPLICATE_VOTE 是不是已经罚没，还是 MisbehaviorType LIGHT_CLIENT_ATTACK 是不是已经 DUPLICATE_VOTE，再决定要不要同一次发布。
