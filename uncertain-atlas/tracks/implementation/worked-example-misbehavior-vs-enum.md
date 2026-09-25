# 例：看见 Misbehavior.type 只是过错枚举不是已经罚没；看见 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间；看见 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩

**层次**：实现 / Misbehavior 类型。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Misbehavior.type 只是过错枚举不是已经罚没 / height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间 / total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩」，不是证据上链就已经罚没，也不是票上 Timestamp 就已经验过。不要另写怎样写 Misbehavior。372 misbehavior-vs-enum bundled unbundling 完成（863+864+865）；精读 [`worked-example-misbehavior-notslashed-vs-bundled.md`](worked-example-misbehavior-notslashed-vs-bundled.md)（不变量 863 item 1）；精读 [`worked-example-misbehavior-notverified-vs-bundled.md`](worked-example-misbehavior-notverified-vs-bundled.md)（不变量 864 item 2）；精读 [`worked-example-misbehavior-notrewarded-vs-bundled.md`](worked-example-misbehavior-notrewarded-vs-bundled.md)（不变量 865 item 3）。

## 官方三件事

规范把 `Misbehavior.type` 只是过错枚举、`height` 是过错发生的高度、`time` 是那一高已提交块的时间、`total_voting_power` 是那一高验证者集合的总权写成三件独立的实现事，不是「看见有 Misbehavior 就已经罚没、已经验过时间、已经按到场定奖惩」一件事：

1. **看见 `Misbehavior.type` 只是过错枚举 / 看见有类型 不是已经罚没，也不是已经定了奖惩。**  
   官方写：`type` 是可能过错的枚举。枚举里有 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK`。看见有类型，不是已经罚没。看见写成双签，不是已经交差。看见枚举在，不是已经定了奖惩。
2. **看见 `height` 是过错发生的高度、`time` 是那一高已提交块的时间 / 看见有时间 不是已经验过这个时间，也不是已经交差。**  
   官方写：`height` 是过错发生的高度。`time` 是那一高已提交块的时间戳。看见有高度，不是已经验过票上的时间。看见有时间，不是已经交差。看见对上了高度，不是已经是本高 +2/3。
3. **看见 `total_voting_power` 是那一高验证者集合的总权 / 看见有总权 不是已经按到场定奖惩，也不是已经改了集合。**  
   官方写：`total_voting_power` 是那一高验证者集合的总投票权。看见有总权，不是已经按到场定奖惩。看见填了权，不是已经改了集合。看见有集合，不是已经罚没。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。证据上链就已经罚没是不变量 21，本页不抄。

## 官方为什么这样拆

- **Misbehavior.type 只是过错枚举 ≠ 已经罚没：** 官方把枚举种类和已经罚没分开。
- **height 是过错发生的高度、time 是那一高已提交块的时间 ≠ 已经验过这个时间：** 官方把过错高度 / 已提交块时间和票上时间已经验过分开。
- **total_voting_power 是那一高验证者集合的总权 ≠ 已经按到场定奖惩：** 官方把那一高总权和按到场定奖惩分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Misbehavior.type 只是过错枚举 | 不是已经罚没 | 不是证据上链就已经罚没（21） |
| height 是过错发生的高度、time 是那一高已提交块的时间 | 不是已经验过这个时间 | 不是票上 Timestamp 就已经验过（304） |
| total_voting_power 是那一高验证者集合的总权 | 不是已经按到场定奖惩 | 不是 VoteInfo 能按到场定奖惩就已经罚没（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有 Misbehavior 就已经罚没、已经验过时间、已经按到场定奖惩」，必须分开 Misbehavior.type 只是过错枚举是不是已经罚没、height 是过错发生的高度、time 是那一高已提交块的时间是不是已经验过这个时间、total_voting_power 是那一高验证者集合的总权是不是已经按到场定奖惩。可以跳过「看见有 Misbehavior 就已经罚没」。不要另写怎样写 Misbehavior。372 misbehavior-vs-enum bundled unbundling 完成（863+864+865）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- 证据上链就已经罚没。那是不变量 21。
- 票上 Timestamp 就已经验过。那是不变量 304。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
