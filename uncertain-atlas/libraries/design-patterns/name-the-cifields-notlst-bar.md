# 模式：点名 cifields-notlst 杠

**层次**：实现 / CiFields votes is last-set voting-info not already in-block / not already settled / not already 444-notes-order 正式三事（445 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields 句。  
**对应**：[`../tracks/implementation/worked-example-cifields-notlst-vs-bundled.md`](../tracks/implementation/worked-example-cifields-notlst-vs-bundled.md)。

- **CommitInfo.votes 是上一集合投票信息不是已经进了块 不是已经进了块：看见CommitInfo.votes 是上一集合投票信息不是已经进了块，不是已经进了块 interchangeable / 1360 cifields-notlst interchangeable。**
- **CommitInfo.votes is last-set voting info is not already in the block 不是已经交差：看见CommitInfo.votes is last-set voting info is not already in the block，不是已经交差 interchangeable / 1360 cifields-notlst interchangeable。**
- **CommitInfo.votes 是上一集合投票信息不是已经进了块 不是已经是 Notes 票序：看见CommitInfo.votes 是上一集合投票信息不是已经进了块，不是已经是 Notes 票序 interchangeable / 1360 cifields-notlst interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（445 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
