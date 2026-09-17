# 模式：点名 procrestr-notlocal 杠

**层次**：实现 / ProcessProposalRequest.proposed_last_commit not already local-settled / not already ext-commit / not already processed 正式三事（420 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procrestr-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-procrestr-notlocal-vs-bundled.md)。

- **proposed_last_commit 不是已经交差 local_last_commit：** 看见填了 proposed_last_commit，不是已经交差 local_last_commit interchangeable / 1028 procrestr-notlocal interchangeable。
- **看见从拟议块拿到 不是已经交差：** 看见从拟议块拿到，不是已经交差 interchangeable。
- **看见能指上一份提交 不是已经跑过 Process：** 看见能指上一份提交，不是已经跑过 Process interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposed_last_commit 正式三事（420 余量），先数清问的是是不是已经交差 local_last_commit、是不是已经交差、还是看见能指上一份提交是不是已经跑过 Process，再决定要不要同一次发布。420 procreqrest vs extreq bundled unbundling 在本页 item 1 启动。
