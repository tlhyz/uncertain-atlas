# 模式：点名 ftxs-notsettle 杠

**层次**：实现 / Finalize exec-txs-return-control not already settled / not already like-Prepare / not already last-state-only 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notsettle-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notsettle-vs-bundled.md)。

- **Finalize 执行再交还 不是已经交差：** 看见先跑了，不是已经交差 interchangeable / 1112 ftxs-notsettle interchangeable。
- **看见必须确定 不是已经可以像 Prepare 那样：** 看见必须确定，不是已经可以像 Prepare 那样 interchangeable。
- **看见按自己的规则 不是已经只依赖上一份状态和决定块：** 看见按自己的规则，不是已经只依赖上一份状态和决定块 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 执行再交还 正式三事（408 余量），先数清问的是是不是已经交差、是不是已经可以像 Prepare 那样、还是看见按自己的规则是不是已经只依赖上一份状态和决定块，再决定要不要同一次发布。408 fintxs vs control bundled unbundling 在本页 item 1 启动。
