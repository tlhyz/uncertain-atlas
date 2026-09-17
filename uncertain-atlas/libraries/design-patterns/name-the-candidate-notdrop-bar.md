# 模式：点名 candidate-notdrop 杠

**层次**：实现 / 丢掉候选 not already never-rerun / not already unbounded-ok / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-notdrop-vs-bundled.md`](../tracks/implementation/worked-example-candidate-notdrop-vs-bundled.md)。

- **丢掉候选 不是已经永远不用再执行：** 看见丢掉了，不是已经永远不用再跑 interchangeable / 973 candidate-notdrop interchangeable。
- **看见还没 Finalize 不是已经能一直攒：** 看见还没 Finalize，不是已经能一直攒 interchangeable。
- **看见有上界 不是已经交差：** 看见有上界，不是规范已经写死条数 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看丢掉候选 正式三事（311 余量），先数清问的是是不是已经永远不用再执行、是不是已经能一直攒、还是看见有上界是不是已经交差，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 3 完成。
