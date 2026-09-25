# 例：看见有类型 / 看见写成双签 / 看见枚举在 is not already already slashed interchangeable / already settled interchangeable / already rewarded interchangeable

**层次**：实现 / Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量）/ not 863 misbehavior-notslashed interchangeable / not 372 misbehavior bundled interchangeable」，不是 misbehavior bundled（372），也不是 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间（372 item 2 余量）或 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩（372 item 3 余量）。不要另写怎样写 Misbehavior。

## 官方三件事

规范把 Methods 里 `Misbehavior.type` 只是过错枚举 和「已经是有类型就已经罚没 interchangeable / 已经是写成双签就已经交差 interchangeable / 已经是枚举在就已经定了奖惩 interchangeable / 已经是 misbehavior bundled interchangeable」分开写成三件独立的实现事，不是「看见有类型就已经罚没 interchangeable / 就已经交差 interchangeable / 就已经定了奖惩 interchangeable」一件事：

1. **看见有类型 / 看见 `Misbehavior.type` 只是过错枚举 / 看见有类型 is not already 已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 372 misbehavior bundled interchangeable / 21 evidence-slash interchangeable / misbehavior-sold-as-enum interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 863 misbehavior-notslashed interchangeable / 372 misbehavior item 1 interchangeable，也不是已经 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事 bundled（372 item 1 余量） interchangeable / 372 misbehavior item 1 interchangeable，也不是已经 height/time 就已经验过（372 item 2） interchangeable / 304 Timestamp verified interchangeable / 365 VoteInfo rewards interchangeable，也不是已经证据上链就已经罚没（21） interchangeable。**  
   官方写：`type` 是可能过错的枚举。枚举里有 `UNKNOWN`、`DUPLICATE_VOTE`、`LIGHT_CLIENT_ATTACK`。看见有类型，不是已经罚没。看见有类型，不是已经 slashed interchangeable——372 钉 bundled 三事，本页从 item 1 侧钉 not already slashed 单句。看见 `Misbehavior.type` 只是过错枚举，不是已经 misbehavior bundled（372） interchangeable——372 钉 bundled，本页钉 item 1 第一件事。看见有类型，不是已经证据上链就已经罚没（21） interchangeable——21 另钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动。

2. **看见写成双签 / 看见写成 `DUPLICATE_VOTE` / 看见枚举写成双签 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 372 misbehavior bundled interchangeable / 21 evidence-slash interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 863 misbehavior-notslashed interchangeable / 372 misbehavior item 2 验过时间 interchangeable / 372 misbehavior item 3 按到场定奖惩 interchangeable，也不是已经 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事 bundled（372 item 1 余量） interchangeable / 372 misbehavior item 1 interchangeable，也不是已经罚没（本页第一件事） interchangeable。**  
   官方写：看见写成双签，不是已经交差。看见写成 `DUPLICATE_VOTE`，不是已经 settled interchangeable——本页钉 not already settled 单句。看见枚举写成双签，不是已经罚没（本页第一件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动。

3. **看见枚举在 / 看见枚举种类在 / 看见有枚举 is not already 已经定了奖惩 interchangeable / 已经 rewarded interchangeable / 已经定了奖惩交差 interchangeable / 372 misbehavior bundled interchangeable / 365 VoteInfo rewards interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 863 misbehavior-notslashed interchangeable / 372 misbehavior item 2 / 372 misbehavior item 3，也不是已经 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事 bundled（372 item 1 余量） interchangeable / 372 misbehavior item 1 interchangeable，也不是已经罚没（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见枚举在，不是已经定了奖惩。看见枚举种类在，不是已经 rewarded interchangeable——本页钉 not already rewarded 单句。看见有枚举，不是已经交差（本页第二件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。misbehavior bundled（372）、height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间（372 item 2 余量）、total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩（372 item 3 余量）、证据上链就已经罚没（21）、票上 Timestamp 就已经验过（304）、VoteInfo 能按到场定奖惩就已经罚没（365）是另外那套，本页不抄。

## 官方为什么这样拆

- **有类型 not already slashed ≠ 372 / 21 interchangeable：** 官方把过错枚举和已经罚没分开。
- **写成双签 not already settled ≠ 已经交差 interchangeable：** 官方把写成双签和已经交差分开。
- **枚举在 not already rewarded ≠ 已经定了奖惩 interchangeable：** 官方把枚举种类和已经定了奖惩分开；372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有类型 | 不是 already slashed | 不是证据上链就已经罚没 alone（21） |
| 写成双签 | 不是 already settled | 不是票上 Timestamp 就已经验过 alone（304） |
| 枚举在 | 不是 already rewarded | 不是 VoteInfo 能按到场定奖惩就已经罚没 alone（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Misbehavior.type 只是过错枚举不是已经罚没 not already slashed / not already settled / not already rewarded 正式三事（372 余量），必须分开有类型 是不是 already slashed interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable、写成双签 是不是 already settled interchangeable、枚举在 是不是 already rewarded interchangeable。可以跳过「看见有类型就已经罚没 interchangeable / 就已经交差 interchangeable / 就已经定了奖惩 interchangeable」。不要另写怎样写 Misbehavior。372 misbehavior-vs-enum bundled unbundling 在本页 item 1 启动（863）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- misbehavior bundled。那是不变量 372。
- height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间。那是不变量 372 item 2 余量。
- total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩。那是不变量 372 item 3 余量。
- 证据上链就已经罚没。那是不变量 21。
- 票上 Timestamp 就已经验过。那是不变量 304。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
