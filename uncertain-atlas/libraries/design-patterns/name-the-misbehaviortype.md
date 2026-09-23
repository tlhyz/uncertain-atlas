# 模式：把 MisbehaviorType 枚举三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**例**：[MisbehaviorType 只有三个枚举名 ≠ 已经能认过错种类](../../tracks/implementation/worked-example-misbehaviortype-vs-enum.md)。

## 三个名字

1. **MisbehaviorType 只有三个枚举名不是已经能认过错种类：** 看见名字在不是已经验过。
2. **UNKNOWN 是第 0 项不是已经是引擎判的应用坏了：** 这一节没有给 UNKNOWN 写 VerifyStatus 那种「一律是错」。
3. **DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名不是已经是双签证据已经成立：** 看见能归名不是已经罚没。

## 为什么要分开叫

官方把 `MisbehaviorType` 的枚举项清单、第 0 项 `UNKNOWN`、两个具名过错写成三件事。把它们叫成一个「看见有 MisbehaviorType 就已经能认过错种类」，会把枚举清单、兜底项语义和证据能不能凑齐一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 MisbehaviorType 就已经能认过错种类」，先数清问的是 MisbehaviorType 只有三个枚举名不是已经能认过错种类、UNKNOWN 是第 0 项不是已经是引擎判的应用坏了，还是 DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名不是已经是双签证据已经成立，再决定要不要同一次发布。
