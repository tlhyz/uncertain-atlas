# 反模式：把 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量）说成已经罚没 / 已经用 decided_last_commit 算完 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有这列 not already slashed ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notslashed-vs-bundled.md)。

## 卖法

把有这列 / VoteInfo 标明上一块有没有签、能按到场定奖惩 / 有 `block_id_flag` 列 写成已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable；把能定奖惩 / 好按到场定奖惩 / 能按到场定 写成已经是应用已经用 `decided_last_commit` 算完 interchangeable / 已经 decided-commit interchangeable / 已经算完交差 interchangeable；把有 `block_id_flag` / 有 flag / 标明有没有签 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 365 voteinfo bundled / voteinfo-sold-as-rewarded interchangeable / 842 voteinfo-notslashed interchangeable。

## 为什么错

官方把有这列、不是已经用 decided_last_commit 算完、不是已经交差写成三件独立的实现事。把它们卖成 already slashed interchangeable / already decided-commit interchangeable / already settled interchangeable，会把 not already slashed、not already decided-commit、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量），必须分开 not already slashed、not already decided-commit、not already settled 三件事，不要和 365 / 21 / 843 / 844 糊成一句。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo bundled 全段，不是本页有这列 item 1 单句边界。
- [finreward-notslashed-sold-as-bundled](finreward-notslashed-sold-as-bundled.md) 是 can use decided_last_commit + misbehavior not slashed（463），不是本页 not already decided-commit 边界。
- [misbehavior-sold-as-enum](misbehavior-sold-as-enum.md) 相关到场定奖惩边界，不是本页 not already slashed 单句。
