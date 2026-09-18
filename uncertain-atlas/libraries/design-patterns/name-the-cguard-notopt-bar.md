# 模式：点名 cguard-notopt 杠

**层次**：实现 / CheckTx mempool-guard not already technically-optional / not already four-gates / not already settled 正式三事（405 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-cguard-notopt-vs-bundled.md`](../tracks/implementation/worked-example-cguard-notopt-vs-bundled.md)。

- **CheckTx 守卫 不是已经是技术上可选：** 看见先跑了，不是已经是技术上可选 interchangeable / 1103 cguard-notopt interchangeable。
- **看见守着本地池 不是已经是四门已经结算：** 看见守着本地池，不是已经是四门已经结算 interchangeable。
- **看见每条节点都跑 不是已经交差：** 看见每条节点都跑，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 守卫 正式三事（405 余量），先数清问的是是不是已经是技术上可选、是不是已经是四门已经结算、还是看见每条节点都跑是不是已经交差，再决定要不要同一次发布。405 checktxguard vs optional bundled unbundling 在本页 item 1 启动。
