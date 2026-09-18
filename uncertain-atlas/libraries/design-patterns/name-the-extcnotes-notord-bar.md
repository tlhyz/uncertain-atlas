# 模式：点名 extcnotes-notord 杠

**层次**：实现 / ExtCiNotes ext votes ordered by voting-power desc not already in-block / not already settled / not already last_commit 正式三事（441 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedCommitInfo Notes 句。  
**对应**：[`../tracks/implementation/worked-example-extcnotes-notord-vs-bundled.md`](../tracks/implementation/worked-example-extcnotes-notord-vs-bundled.md)。

- **ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 不是已经进了块：看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块，不是已经进了块 interchangeable / 1356 extcnotes-notord interchangeable。**
- **ExtendedCommitInfo.votes ordered by voting power is not already in the block 不是已经交差：看见ExtendedCommitInfo.votes ordered by voting power is not already in the block，不是已经交差 interchangeable / 1356 extcnotes-notord interchangeable。**
- **ExtendedCommitInfo.votes 按投票权降序排不是已经进了块 不是已经写进 last_commit：看见ExtendedCommitInfo.votes 按投票权降序排不是已经进了块，不是已经写进 last_commit interchangeable / 1356 extcnotes-notord interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（441 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
