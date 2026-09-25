# 例：看见有总权 / 看见填了权 / 看见有集合 is not already already rewarded interchangeable / already setchanged interchangeable / already slashed interchangeable

**层次**：实现 / total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量）/ not 865 misbehavior-notrewarded interchangeable / not 372 misbehavior bundled interchangeable」，不是 misbehavior bundled（372），也不是 Misbehavior.type 只是过错枚举不是已经罚没（863 item 1 余量）或 height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间（864 item 2 余量）。不要另写怎样写 Misbehavior。

## 官方三件事

规范把 Methods 里 `total_voting_power` 是那一高验证者集合的总权 和「已经是有总权就已经按到场定奖惩 interchangeable / 已经是填了权就已经改了集合 interchangeable / 已经是有集合就已经罚没 interchangeable / 已经是 misbehavior bundled interchangeable」分开写成三件独立的实现事，不是「看见有总权就已经按到场定奖惩 interchangeable / 就已经改了集合 interchangeable / 就已经罚没 interchangeable」一件事：

1. **看见有总权 / 看见 `total_voting_power` 是那一高验证者集合的总权 / 看见有总权 is not already 已经按到场定奖惩 interchangeable / 已经 rewarded interchangeable / 已经按到场定奖惩交差 interchangeable / 372 misbehavior bundled interchangeable / 365 VoteInfo rewards interchangeable / misbehavior-sold-as-enum interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 865 misbehavior-notrewarded interchangeable / 372 misbehavior item 3 interchangeable，也不是已经 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事 bundled（372 item 3 余量） interchangeable / 372 misbehavior item 3 interchangeable，也不是已经有类型就已经罚没（863） interchangeable / 已经有高度就已经验过（864） interchangeable / 21 evidence-slash interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没（365） interchangeable。**  
   官方写：`total_voting_power` 是那一高验证者集合的总投票权。看见有总权，不是已经按到场定奖惩。看见有总权，不是已经 rewarded interchangeable——372 钉 bundled 三事，本页从 item 3 侧钉 not already rewarded 单句。看见 `total_voting_power` 是那一高验证者集合的总权，不是已经 misbehavior bundled（372） interchangeable——372 钉 bundled，本页钉 item 3 第一件事。看见有总权，不是已经有类型就已经罚没（863） interchangeable——863 另钉 item 1。看见有总权，不是已经有高度就已经验过（864） interchangeable——864 另钉 item 2。372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成。

2. **看见填了权 / 看见填了总权 / 看见权在 is not already 已经改了集合 interchangeable / 已经 setchanged interchangeable / 已经改了集合交差 interchangeable / 372 misbehavior bundled interchangeable / 318 ValidatorUpdate interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 865 misbehavior-notrewarded interchangeable / 372 misbehavior item 1 罚没 interchangeable / 372 misbehavior item 2 验过时间 interchangeable，也不是已经 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事 bundled（372 item 3 余量） interchangeable / 372 misbehavior item 3 interchangeable，也不是已经按到场定奖惩（本页第一件事） interchangeable。**  
   官方写：看见填了权，不是已经改了集合。看见填了总权，不是已经 setchanged interchangeable——本页钉 not already setchanged 单句。看见权在，不是已经按到场定奖惩（本页第一件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成。

3. **看见有集合 / 看见那一高验证者集合 / 看见集合在 is not already 已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 372 misbehavior bundled interchangeable / 21 evidence-slash interchangeable / 863 misbehavior-notslashed interchangeable，也不是已经 misbehavior bundled（372） interchangeable / 865 misbehavior-notrewarded interchangeable / 372 misbehavior item 1 / 372 misbehavior item 2，也不是已经 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事 bundled（372 item 3 余量） interchangeable / 372 misbehavior item 3 interchangeable，也不是已经按到场定奖惩（本页第一件事） interchangeable / 已经改了集合（本页第二件事） interchangeable。**  
   官方写：看见有集合，不是已经罚没。看见那一高验证者集合，不是已经 slashed interchangeable——本页钉 not already slashed 单句。看见集合在，不是已经改了集合（本页第二件事） interchangeable——三件事分开钉。372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。misbehavior bundled（372）、Misbehavior.type 只是过错枚举不是已经罚没（372 item 1 余量 / 863）、height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间（372 item 2 余量 / 864）、证据上链就已经罚没（21）、票上 Timestamp 就已经验过（304）、VoteInfo 能按到场定奖惩就已经罚没（365）、InitChain 空名单 / ValidatorUpdate（318）是另外那套，本页不抄。

## 官方为什么这样拆

- **有总权 not already rewarded ≠ 372 / 365 interchangeable：** 官方把那一高总权和按到场定奖惩分开。
- **填了权 not already setchanged ≠ 已经改了集合 interchangeable：** 官方把填了权和已经改了集合分开。
- **有集合 not already slashed ≠ 已经罚没 interchangeable：** 官方把有集合和已经罚没分开；372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有总权 | 不是 already rewarded | 不是 VoteInfo 能按到场定奖惩就已经罚没 alone（365） |
| 填了权 | 不是 already setchanged | 不是 ValidatorUpdate alone（318） |
| 有集合 | 不是 already slashed | 不是有类型 already slashed alone（863） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量），必须分开有总权 是不是 already rewarded interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable、填了权 是不是 already setchanged interchangeable、有集合 是不是 already slashed interchangeable。可以跳过「看见有总权就已经按到场定奖惩 interchangeable / 就已经改了集合 interchangeable / 就已经罚没 interchangeable」。不要另写怎样写 Misbehavior。372 misbehavior-vs-enum bundled unbundling 在本页 item 3 完成（863 + 864 + 865）。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- misbehavior bundled。那是不变量 372。
- Misbehavior.type 只是过错枚举不是已经罚没。那是不变量 372 item 1 余量 / 863。
- height 是过错发生的高度、time 是那一高已提交块的时间不是已经验过这个时间。那是不变量 372 item 2 余量 / 864。
- 证据上链就已经罚没。那是不变量 21。
- 票上 Timestamp 就已经验过。那是不变量 304。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
- InitChain 空名单 / ValidatorUpdate。那是不变量 318。
