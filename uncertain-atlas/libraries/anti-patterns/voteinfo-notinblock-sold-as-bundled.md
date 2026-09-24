# 反模式：把按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量）说成已经进了块 / 已经交差 / 已经罚没

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[排好了 not already in-block ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notinblock-vs-bundled.md)。

## 卖法

把排好了 / `votes` 按投票权降序排、落盘后再从 store 装回 / 按投票权从高到低排 写成已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable / 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable；把从 store 再装 / 造 CommitInfo 时从 store 再装集合 / 从 store 装回 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把顺序在 / 顺序落盘 / 保住这份顺序 写成已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，或已经和 365 voteinfo bundled / voteinfo-sold-as-rewarded interchangeable / 844 voteinfo-notinblock interchangeable。

## 为什么错

官方把排好了、不是已经交差、不是已经罚没写成三件独立的实现事。把它们卖成 already in-block interchangeable / already settled interchangeable / already slashed interchangeable，会把 not already in-block、not already settled、not already slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量），必须分开 not already in-block、not already settled、not already slashed 三件事，不要和 365 / 300 / 842 / 843 糊成一句。

## 和相邻反模式

- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo bundled 全段，不是本页排好了 item 3 单句边界。
- [voteinfo-notslashed-sold-as-bundled](voteinfo-notslashed-sold-as-bundled.md) 是 VoteInfo 能按到场定奖惩 not already slashed（365 item 1），不是本页 not already in-block 边界。
- [voteinfo-notpubkey-sold-as-bundled](voteinfo-notpubkey-sold-as-bundled.md) 是从拟议块或已决块抽出 not already pubkey（365 item 2），不是本页 not already settled 边界。
