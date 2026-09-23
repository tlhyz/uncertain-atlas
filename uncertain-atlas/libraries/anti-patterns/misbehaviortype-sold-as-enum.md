# 反模式：misbehaviortype-sold-as-enum

**层次**：实现 / MisbehaviorType。  
**分类**：反模式（会把三件事写成一件）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**例**：[MisbehaviorType 只有三个枚举名 ≠ 已经能认过错种类](../../tracks/implementation/worked-example-misbehaviortype-vs-enum.md)。

## 病症

把「看见有 `MisbehaviorType`」写成已经从枚举认出了过错种类，或写成 `UNKNOWN` 一律是错、引擎当应用坏了会崩，或写成看见 `DUPLICATE_VOTE` / `LIGHT_CLIENT_ATTACK` 就已经凑出了可验的证据、已经罚没。

## 为什么错

规范在 `MisbehaviorType` 这一节只列了三个枚举项。它没有为 `UNKNOWN` 写 `VerifyStatus` 那种「一律是错、引擎当应用坏了会崩」，也没有说枚举名对上就等于证据轮廓成立。枚举是名字，罚没是应用侧另一件事。

## 正确写法

分开三句：MisbehaviorType 只有三个枚举名不是已经能认过错种类；UNKNOWN 是第 0 项不是已经是引擎判的应用坏了；DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名不是已经是双签证据已经成立。

## 边界

不是 [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md)（那是 `Misbehavior` 结构体，不变量 364），不是 [verifystatus-sold-as-vote](verifystatus-sold-as-vote.md)（那是 `VerifyStatus` 的 `UNKNOWN`，不变量 434），不是双签证据形状成立就已经罚没（不变量 21）。

## 本页不抄

- 怎样编 `MisbehaviorType`、怎样挑枚举、怎样把过错归进这三类。
- 怎样写利用步骤。
