# 例：看见 MisbehaviorType 只有三个枚举名不是已经能认过错种类；看见 UNKNOWN 是第 0 项不是已经是引擎判的应用坏了；看见 DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名不是已经是双签证据已经成立

**层次**：实现 / MisbehaviorType。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types MisbehaviorType。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「MisbehaviorType 只有三个枚举名不是已经能认过错种类 / UNKNOWN 是第 0 项不是已经是引擎判的应用坏了 / DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名不是已经是双签证据已经成立」，不是 Misbehavior.type 只是过错枚举就已经罚没，也不是双签证据形状成立就已经罚没。不要另写怎样写 MisbehaviorType。

## 官方三件事

规范把 `MisbehaviorType` 的 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK` 写成三个独立的枚举项，不是「看见有枚举名就已经能认过错种类、已经是引擎判的应用坏了、已经是双签证据已经成立」一件事：

1. **看见 `MisbehaviorType` 只有三个枚举名 / 看见名字在 不是已经能认过错种类，也不是已经验过。**  
   官方写：`MisbehaviorType` 是一个枚举，列的字段就是那三项。看见只有三个名字，不是已经能把任意过错归进这三类。看见枚举在，不是已经验过是哪一类。
2. **看见 `UNKNOWN` 是第 0 项 / 看见有第 0 项 不是已经是引擎判的应用坏了，也不是已经能停。**  
   官方写：`UNKNOWN` 是第 0 项。规范在 `MisbehaviorType` 这一节只给出枚举项，没有为 `UNKNOWN` 写「一律是错」或「引擎当应用坏了会崩」那种语义。看见第 0 项在，不是已经等于 `VerifyStatus` 那种「`UNKNOWN` 一律是错」。看见有兜底项，不是已经能停链。
3. **看见 `DUPLICATE_VOTE` 和 `LIGHT_CLIENT_ATTACK` 是枚举名 / 看见名字对上 不是已经是双签证据已经成立，也不是已经罚没。**  
   官方写：这两项是枚举里的名字。看见名字在，不是已经凑齐同一 `(addr, height, round, type)`、不同 `BlockID` 的两张合法签。看见枚举对上了，不是已经能验成 `DuplicateVoteEvidence`。看见能归名，不是已经罚没。

怎样编 `MisbehaviorType`、怎样挑枚举、怎样把过错归进这三类是规范里的做法，本页不抄。证据上链就已经罚没是不变量 21，本页不抄。双签证据形状成立就已经罚没是不变量 21，本页不抄。

## 官方为什么这样拆

- **`MisbehaviorType` 只有三个枚举名 ≠ 已经能认过错种类：** 官方把枚举项清单和「已经能归类任意过错」分开。
- **`UNKNOWN` 是第 0 项 ≠ 已经是引擎判的应用坏了：** 官方在 `MisbehaviorType` 这一节没有给 `UNKNOWN` 写 `VerifyStatus` 那种「一律是错」。两个 `UNKNOWN` 不是同一把尺。
- **`DUPLICATE_VOTE` 和 `LIGHT_CLIENT_ATTACK` 是枚举名 ≠ 已经是双签证据已经成立：** 官方把枚举名字和能不能凑出可验证的证据分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MisbehaviorType 只有三个枚举名 | 不是已经能认过错种类 | 不是 Misbehavior.type 只是过错枚举就已经罚没（364） |
| UNKNOWN 是第 0 项 | 不是已经是引擎判的应用坏了 | 不是 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩（434） |
| DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名 | 不是已经是双签证据已经成立 | 不是双签证据形状成立就已经罚没（21） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 MisbehaviorType 就已经能认过错种类、已经是引擎判的应用坏了、已经是双签证据已经成立」，必须分开 MisbehaviorType 只有三个枚举名是不是已经能认过错种类、UNKNOWN 是第 0 项是不是已经是引擎判的应用坏了、DUPLICATE_VOTE 和 LIGHT_CLIENT_ATTACK 是枚举名是不是已经是双签证据已经成立。可以跳过「看见有 MisbehaviorType 就已经能认过错种类」。不要另写怎样写 MisbehaviorType。

## 本页不抄

- 怎样编 MisbehaviorType、怎样挑枚举、怎样把过错归进这三类。
- 证据上链就已经罚没。那是不变量 21。
- Misbehavior.type 只是过错枚举就已经罚没。那是不变量 364。
- VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩。那是不变量 434。
