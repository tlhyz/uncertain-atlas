# 模式：点名 candidate-nothash 杠

**层次**：实现 / Prepare 没有头哈希 not already this-header / not already process-had-it / not already settled 正式三事（311 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Immediate execution / candidate state。  
**对应**：[`../tracks/implementation/worked-example-candidate-nothash-vs-bundled.md`](../tracks/implementation/worked-example-candidate-nothash-vs-bundled.md)。

- **Prepare 没有头哈希 不是已经知道本头：** 看见 Prepare 来了，不是已经有本头哈希 interchangeable / 971 candidate-nothash interchangeable。
- **看见 Process 有哈希 不是 Prepare 当时已经有：** 看见 Process 有哈希，不是 Prepare 当时已经有 interchangeable。
- **看见字段齐了 不是已经交差：** 看见字段齐了，不是已经能当决定块的身份 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 没有头哈希 正式三事（311 余量），先数清问的是是不是已经知道本头、是不是 Prepare 当时已经有、还是看见字段齐了是不是已经交差，再决定要不要同一次发布。311 candidate vs execute bundled unbundling 在本页 item 1 启动。
