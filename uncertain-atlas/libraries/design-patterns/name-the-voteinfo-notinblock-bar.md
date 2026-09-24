# 模式：把按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo / CommitInfo。  
**例**：[排好了 not already in-block ≠ bundled（365）](../../tracks/implementation/worked-example-voteinfo-notinblock-vs-bundled.md)。

## 三个名字

1. **排好了 不是 already in-block：** 看见排好了 / `votes` 按投票权降序排、落盘后再从 store 装回 / 按投票权从高到低排，不是已经进了块 interchangeable / 已经 in-block interchangeable / 已经进了块交差 interchangeable，不是 365 voteinfo bundled interchangeable / voteinfo-sold-as-rewarded interchangeable。

2. **从 store 再装 不是 already settled：** 看见从 store 再装 / 造 CommitInfo 时从 store 再装集合 / 从 store 装回，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 300 localstate interchangeable / 842 voteinfo-notslashed interchangeable。

3. **顺序在 不是 already slashed：** 看见顺序在 / 顺序落盘 / 保住这份顺序，不是已经罚没 interchangeable / 已经 slashed interchangeable / 已经罚没交差 interchangeable，不是 843 voteinfo-notpubkey interchangeable / 33 fourgates interchangeable。

官方把排好了、不是已经交差、不是已经罚没写成三个名字。把它们叫成一个「看见排好了就已经进了块 interchangeable / 就已经交差 interchangeable / 就已经罚没 interchangeable」，会把 not already in-block、not already settled、not already slashed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看按投票权降序排不是已经进了块 not already in-block / not already settled / not already slashed 正式三事（365 余量），先数清问的是排好了 是不是 already in-block / 365 / voteinfo-sold-as-rewarded，是不是从 store 再装 是不是 already settled，还是顺序在 是不是 already slashed，再决定要不要同一次发布。365 voteinfo-vs-reward bundled unbundling 在本页 item 3 完成。
