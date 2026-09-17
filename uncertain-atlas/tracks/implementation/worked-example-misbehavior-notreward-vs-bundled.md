# 例：看见 total_voting_power 是那一高验证者集合的总权 is not already rewarded by presence interchangeable / not already changed set interchangeable / not already slashed interchangeable

**层次**：实现 / total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Misbehavior。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量）/ not 811 misbehavior-notreward interchangeable / not 372 misbehavior-vs-enum bundled interchangeable」，不是 Misbehavior bundled（372），也不是 VoteInfo 能按到场定奖惩就已经罚没（365），也不是 Finalize misbehavior 就已经是 VoteInfo（569），也不是 InitChain validators 就已经无集合（388/765）。不要另写怎样写 Misbehavior。

## 官方三件事

1. **看见 `total_voting_power` 是那一高验证者集合的总权 / 看见有总权 / 这份总权 is not already 已经按到场定奖惩 interchangeable / 365 voteinfo interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 811 misbehavior-notreward interchangeable / 809 misbehavior-notslashed interchangeable / 372 misbehavior item 1 type interchangeable，也不是已经 total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事 bundled（372 item 3 余量） interchangeable / 372 misbehavior item 3 interchangeable。**  
   官方写：`total_voting_power` 是那一高验证者集合的总投票权。看见有总权，不是已经按到场定奖惩 interchangeable——本页从 372 item 3 侧钉 not already rewarded by presence 单句。372 misbehavior vs enum bundled unbundling 在本页 item 3 完成。

2. **看见有总权 / 看见填了权 / 这份总权 is not already 已经改了集合 interchangeable / 365 voteinfo interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 811 misbehavior-notreward interchangeable / 372 misbehavior item 2 height interchangeable / 810 misbehavior-nottime interchangeable，也不是已经 Finalize misbehavior 就已经是 VoteInfo interchangeable / 569 finmisbeh-notvoteinfo interchangeable，也不是已经 InitChain validators 就已经无集合 interchangeable / 388 initparams / 765 initparams-notnoset interchangeable。**  
   官方把填了权和已经改了集合分开——372 bundled 第三件事常与 365 / 569 / 388 混成「看见有总权就已经按到场定奖惩或已经改了集合 interchangeable」，本页钉 not already changed set 单句。

3. **看见有总权 / 看见有集合 / 这份总权 is not already 已经罚没 interchangeable，也不是已经 Misbehavior bundled（372） interchangeable / 811 misbehavior-notreward interchangeable / 809 misbehavior-notslashed interchangeable。**  
   官方把有集合和已经罚没分开。看见有集合，不是已经罚没 interchangeable。372 misbehavior vs enum bundled unbundling 在本页 item 3 完成。

怎样编 Misbehavior、怎样填枚举、怎样算总权是规范里的做法，本页不抄。

## 官方为什么这样拆

- **total_voting_power not already rewarded by presence ≠ 365 interchangeable：** 官方把那一高总权和按到场定奖惩分开。
- **看见填了权 not already changed set ≠ 已经改了集合 interchangeable：** 官方把填了权和已经改了集合分开。
- **看见有集合 not already slashed ≠ 已经罚没 interchangeable：** 官方把有集合和已经罚没分开；372 misbehavior vs enum bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| total_voting_power 是那一高验证者集合的总权 | 不是已经按到场定奖惩（365） | 不是 type 枚举（809/372 item 1） |
| 看见有总权 | 不是已经改了集合 | 不是 Finalize misbehavior（569） |
| 看见有集合 | 不是已经罚没 | 不是 InitChain validators（388/765） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power not already rewarded by presence / not already changed set / not already slashed 正式三事（372 余量），必须分开是不是已经按到场定奖惩 interchangeable / 365、是不是已经改了集合、是不是已经罚没。可以跳过「看见有总权就已经按到场定奖惩」。不要另写怎样写 Misbehavior。372 misbehavior vs enum bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 Misbehavior、怎样填枚举、怎样算总权。
- Misbehavior bundled。那是不变量 372。
- type 枚举。那是不变量 372 item 1 余量 / 809。
- VoteInfo 能按到场定奖惩就已经罚没。那是不变量 365。
- Finalize misbehavior 就已经是 VoteInfo。那是不变量 569。
