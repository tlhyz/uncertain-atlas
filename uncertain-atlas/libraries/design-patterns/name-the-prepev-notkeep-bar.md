# 模式：点名 prepev-notkeep 杠

**层次**：实现 / PrepEv MUST keep until decided not already handed at Process / not already discarded-on-REJECT / not already settled 正式三事（448 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage events 句。  
**对应**：[`../tracks/implementation/worked-example-prepev-notkeep-vs-bundled.md`](../tracks/implementation/worked-example-prepev-notkeep-vs-bundled.md)。

- **MUST 留到块决定之后不是已经 Process 时就交出去 不是已经 Process 时就交出去：看见MUST 留到块决定之后不是已经 Process 时就交出去，不是已经 Process 时就交出去 interchangeable / 1369 prepev-notkeep interchangeable。**
- **MUST keep until decided is not already handed at Process 不是已经 REJECT 丢掉可以不算：看见MUST keep until decided is not already handed at Process，不是已经 REJECT 丢掉可以不算 interchangeable / 1369 prepev-notkeep interchangeable。**
- **MUST 留到块决定之后不是已经 Process 时就交出去 不是已经因为 Prepare 过了就交差：看见MUST 留到块决定之后不是已经 Process 时就交出去，不是已经因为 Prepare 过了就交差 interchangeable / 1369 prepev-notkeep interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When broadcast Precommit 正式三事（448 余量），必须分开 not already construct-Precommit、not already step7-order、not already last_commit 三件事。
