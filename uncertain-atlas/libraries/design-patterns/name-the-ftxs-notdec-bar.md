# 模式：点名 ftxs-notdec 杠

**层次**：实现 / Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notdec-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notdec-vs-bundled.md)。

- **Process 全部执行信息 不是已经是刚决定那块的字段：** 看见填了信息，不是已经是刚决定那块的字段 interchangeable / 1113 ftxs-notdec interchangeable。
- **看见能执行 不是已经跑过 Process：** 看见能执行，不是已经跑过 Process interchangeable。
- **看见有提案块 不是已经交差：** 看见有提案块，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 全部执行信息 正式三事（408 余量），先数清问的是是不是已经是刚决定那块的字段、是不是已经跑过 Process、还是看见有提案块是不是已经交差，再决定要不要同一次发布。408 fintxs vs control bundled unbundling 在本页 item 2 续。
