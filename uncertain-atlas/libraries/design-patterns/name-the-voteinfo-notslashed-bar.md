# 模式：把 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**例**：[有这列 not already slashed ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notslashed-vs-bundled.md)。

## 三个名字

1. **有这列 不是 already slashed：** 看见有这列 / VoteInfo 标明上一块有没有签、能按到场定奖惩 / 有 `block_id_flag` 列，不是已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，不是 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable。

2. **能定奖惩 不是 already decided-commit：** 看见能定奖惩 / 好按到场定奖惩 / 能按到场定，不是已经是应用已经用 `decided_last_commit` 算完 interchangeable / 已经 decided-commit interchangeable / 已经算完交差 interchangeable，不是 463 finreward interchangeable / 843 voteinfo-notpubkey interchangeable。

3. **有 block_id_flag 不是 already settled：** 看见有 `block_id_flag` / 有 flag / 标明有没有签，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 844 voteinfo-notinblock interchangeable / 33 fourgates interchangeable。

官方把有这列、不是已经用 decided_last_commit 算完、不是已经交差写成三个名字。把它们叫成一个「看见有这列就已经罚没 interchangeable / 就已经用 decided_last_commit 算完 interchangeable / 就已经交差 interchangeable」，会把 not already slashed、not already decided-commit、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VoteInfo 能按到场定奖惩不是已经罚没 not already slashed / not already decided-commit / not already settled 正式三事（365 余量），先数清问的是有这列 是不是 already slashed / 365 / voteinfo-sold-as-rewarded，是不是能定奖惩 是不是 already decided-commit，还是有 block_id_flag 是不是 already settled，再决定要不要同一次发布。365 voteinfo-vs-reward bundled unbundling 在本页 item 1 启动。
