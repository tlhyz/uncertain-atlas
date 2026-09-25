# 反模式：把 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量）说成已经按到场定奖惩 / 已经改了集合 / 已经罚没

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有总权 not already rewarded ≠ bundled（372）](../../tracks/implementation/worked-example-misbehavior-notrewarded-vs-bundled.md)。

## 卖法

把有总权 / `total_voting_power` 是那一高验证者集合的总权 / 有总权 写成已经按到场定奖惩 interchangeable / 已经 rewarded interchangeable / 已经按到场定奖惩交差 interchangeable / 372 misbehavior bundled interchangeable / misbehavior-sold-as-enum interchangeable；把填了权 / 填了总权 / 权在 写成已经改了集合 interchangeable / 已经 setchanged interchangeable / 已经改了集合交差 interchangeable；把有集合 / 那一高验证者集合 / 集合在 写成已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，或已经和 372 misbehavior bundled / misbehavior-sold-as-enum interchangeable / 865 misbehavior-notrewarded interchangeable。

## 为什么错

官方把有总权、不是已经改了集合、不是已经罚没写成三件独立的实现事。把它们卖成 already rewarded interchangeable / already setchanged interchangeable / already slashed interchangeable，会把 not already rewarded、not already setchanged、not already slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 total_voting_power 是那一高验证者集合的总权不是已经按到场定奖惩 not already rewarded / not already setchanged / not already slashed 正式三事（372 余量），必须分开 not already rewarded、not already setchanged、not already slashed 三件事，不要和 372 / 365 / 318 / 863 / 864 糊成一句。

## 和相邻反模式

- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 是 misbehavior bundled 全段，不是本页有总权 item 3 单句边界。
- [misbehavior-notslashed-sold-as-bundled](misbehavior-notslashed-sold-as-bundled.md) 是有类型 not already slashed（372 item 1），不是本页 not already rewarded 边界。
- [misbehavior-notverified-sold-as-bundled](misbehavior-notverified-sold-as-bundled.md) 是有高度 not already verified（372 item 2），不是本页 not already setchanged 边界。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 能按到场定奖惩就已经罚没（365），不是本页 not already rewarded 单句。
- [evidence-equals-slash](evidence-equals-slash.md) 是证据上链就已经罚没（21），不是本页 not already slashed 单句。
