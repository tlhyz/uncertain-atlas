# 模式：点名 cifields-notrnd 杠

**层次**：实现 / CiFields round is commit-round not already voting-power-ordered / not already slashed / not already 394-ext-round 正式三事（445 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应**：[`../tracks/implementation/worked-example-cifields-notrnd-vs-bundled.md`](../tracks/implementation/worked-example-cifields-notrnd-vs-bundled.md)。

- **CommitInfo.round 是提交轮不是已经按投票权排过 不是已经按投票权排过：看见CommitInfo.round 是提交轮不是已经按投票权排过，不是已经按投票权排过 interchangeable / 1359 cifields-notrnd interchangeable。**
- **CommitInfo.round is commit round is not already ordered by voting power 不是已经罚没：看见CommitInfo.round is commit round is not already ordered by voting power，不是已经罚没 interchangeable / 1359 cifields-notrnd interchangeable。**
- **CommitInfo.round 是提交轮不是已经按投票权排过 不是已经是 ExtendedCommitInfo.round：看见CommitInfo.round 是提交轮不是已经按投票权排过，不是已经是 ExtendedCommitInfo.round interchangeable / 1359 cifields-notrnd interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（445 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
