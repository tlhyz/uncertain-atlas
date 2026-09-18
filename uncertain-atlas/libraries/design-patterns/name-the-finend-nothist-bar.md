# 模式：点名 finend-nothist 杠

**层次**：实现 / FinalizeBlockRequest.syncing_to_height not already full-history / not already snapshot-restore / not already consensus 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-nothist-vs-bundled.md`](../tracks/implementation/worked-example-finend-nothist-vs-bundled.md)。

- **syncing_to_height 不是已经有完整历史：** 看见填了 syncing_to_height，不是已经有完整历史 interchangeable / 1066 finend-nothist interchangeable。
- **看见在同步或重放 不是已经是快照重放：** 看见在同步或重放，不是已经是快照重放 interchangeable。
- **看见能指同步状态 不是已经切进共识：** 看见能指同步状态，不是已经切进共识 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 syncing_to_height 正式三事（429 余量），先数清问的是是不是已经有完整历史、是不是已经是快照重放、还是看见能指同步状态是不是已经切进共识，再决定要不要同一次发布。429 finreqend vs procreq bundled unbundling 在本页 item 3 完成。
