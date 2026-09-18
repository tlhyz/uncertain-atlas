# 模式：点名 preprestr-notlocal 杠

**层次**：实现 / PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-preprestr-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-preprestr-notlocal-vs-bundled.md)。

- **local_last_commit 不是已经交差 proposed_last_commit：** 看见填了 local_last_commit，不是已经交差 proposed_last_commit interchangeable / 1049 preprestr-notlocal interchangeable。
- **看见从本进程拿到 不是已经是本高度刚签的扩展：** 看见从本进程拿到，不是已经是本高度刚签的扩展 interchangeable。
- **看见能指上一份提交 不是已经交差：** 看见能指上一份提交，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 正式三事（424 余量），先数清问的是是不是已经交差 proposed_last_commit、是不是已经是本高度刚签的扩展、还是看见能指上一份提交是不是已经交差，再决定要不要同一次发布。424 prepreqrest vs procreq bundled unbundling 在本页 item 1 启动。
