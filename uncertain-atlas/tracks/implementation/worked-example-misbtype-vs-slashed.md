# 例：看见 MisbehaviorType UNKNOWN 只是未知过错枚举不是已经归类成 DUPLICATE_VOTE；看见 MisbehaviorType DUPLICATE_VOTE 只是双签枚举不是已经罚没；看见 MisbehaviorType LIGHT_CLIENT_ATTACK 只是轻客户端攻击枚举不是已经 DUPLICATE_VOTE

**层次**：实现 / MisbehaviorType 枚举正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「MisbehaviorType UNKNOWN 只是未知过错枚举不是已经归类成 DUPLICATE_VOTE / MisbehaviorType DUPLICATE_VOTE 只是双签枚举不是已经罚没 / MisbehaviorType LIGHT_CLIENT_ATTACK 只是轻客户端攻击枚举不是已经 DUPLICATE_VOTE」，不是 Misbehavior.type 只是过错枚举就已经罚没，也不是 misbehavior 列表就已经定奖惩。不要另写怎样写 MisbehaviorType 枚举。

## 官方三件事

规范把 MisbehaviorType 里 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK` 三个枚举值写成三件独立的实现事，不是「看见 Misbehavior.type 填了枚举就已经罚没、已经归类、已经交差」一件事：

1. **看见 MisbehaviorType `UNKNOWN` 只是未知过错枚举 / 看见填了 UNKNOWN 不是已经归类成 `DUPLICATE_VOTE`，也不是已经罚没。**  
   官方写：MisbehaviorType is an enum with the listed fields. `UNKNOWN` is 0。看见有 UNKNOWN，不是已经知道是双签。看见只是未知，不是已经定了奖惩。看见 enum 默认值，不是已经交差。
2. **看见 MisbehaviorType `DUPLICATE_VOTE` 只是双签枚举 / 看见填了 DUPLICATE_VOTE 不是已经罚没，也不是已经 LIGHT_CLIENT_ATTACK interchangeable。**  
   官方写：`DUPLICATE_VOTE` is 1。看见枚举名是双签，不是已经 slashed。看见 type 字段，不是已经证据上链就罚没那种已经交差。看见过错种类，不是已经改了集合。
3. **看见 MisbehaviorType `LIGHT_CLIENT_ATTACK` 只是轻客户端攻击枚举 / 看见填了 LIGHT_CLIENT_ATTACK 不是已经 DUPLICATE_VOTE，也不是已经罚没。**  
   官方写：`LIGHT_CLIENT_ATTACK` is 2。看见枚举名是轻客户端攻击，不是已经双签。看见另一种过错种类，不是已经 interchange 成 DUPLICATE_VOTE。看见 type 字段，不是已经轻客户端已经安全那种已经交差。

怎样写 MisbehaviorType 枚举、怎样填 type、怎样区分三种过错是规范里的做法，本页不抄。Misbehavior.type 只是过错枚举就已经罚没是不变量 372 的另一切片，Prepare/Process/Finalize 请求 misbehavior 列表就已经定奖惩是不变量 413/420/428，本页不抄。

## 官方为什么这样拆

- **MisbehaviorType UNKNOWN ≠ 已经归类成 DUPLICATE_VOTE / 已经罚没：** 官方把未知枚举和已经知道过错种类分开。
- **MisbehaviorType DUPLICATE_VOTE ≠ 已经罚没 / 已经是 LIGHT_CLIENT_ATTACK：** 官方把双签枚举名和已经 slashed 分开，也和另一种 enum 分开。
- **MisbehaviorType LIGHT_CLIENT_ATTACK ≠ 已经 DUPLICATE_VOTE / 已经罚没：** 官方把轻客户端攻击 enum 和双签 enum、已经罚没分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MisbehaviorType UNKNOWN | 不是已经归类成 DUPLICATE_VOTE | 不是 Misbehavior.type 只是过错枚举就已经罚没（372） |
| MisbehaviorType DUPLICATE_VOTE | 不是已经罚没 | 不是 misbehavior 列表就已经定奖惩（413） |
| MisbehaviorType LIGHT_CLIENT_ATTACK | 不是已经 DUPLICATE_VOTE | 不是证据上链就已经罚没（21） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Misbehavior.type 填了枚举就已经罚没、已经归类、已经交差」，必须分开 MisbehaviorType UNKNOWN 是不是已经归类成 DUPLICATE_VOTE、MisbehaviorType DUPLICATE_VOTE 是不是已经罚没、MisbehaviorType LIGHT_CLIENT_ATTACK 是不是已经 DUPLICATE_VOTE。可以跳过「看见 Misbehavior.type 填了枚举就已经罚没」。不要另写怎样写 MisbehaviorType 枚举。

## 本页不抄

- 怎样写 MisbehaviorType 枚举、怎样填 type、怎样区分三种过错。
- Misbehavior.type 只是过错枚举。那是不变量 372 的 Misbehavior 结构栏，不是本页 enum 三值。
- misbehavior 列表就已经定奖惩。那是不变量 413 / 420 / 428 的请求栏。
- 证据上链就已经罚没。那是不变量 21。
