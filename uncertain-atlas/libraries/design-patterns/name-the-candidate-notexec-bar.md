# 模式：点名 candidate-notexec 杠

**层次**：实现 / 立刻执行出候选 not already ExecuteTxState / not already this-final / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-notexec-vs-bundled.md`](../tracks/implementation/worked-example-candidate-notexec-vs-bundled.md)。

- **立刻执行出候选 不是已经是 ExecuteTxState：** 看见跑过了，不是已经进工作状态 interchangeable / 972 candidate-notexec interchangeable。
- **看见内存里有 不是已经能点名本高度最终：** 看见内存里有，不是已经能点名本高度最终 interchangeable。
- **看见能加快 Finalize 不是已经交差：** 看见能加快 Finalize，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看立刻执行出候选 正式三事（311 余量），先数清问的是是不是已经是 ExecuteTxState、是不是已经能点名本高度最终、还是看见能加快 Finalize 是不是已经交差，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 2 续。
