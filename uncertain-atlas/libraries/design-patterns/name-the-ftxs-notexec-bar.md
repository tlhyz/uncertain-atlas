# 模式：点名 ftxs-notexec 杠

**层次**：实现 / Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notexec-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notexec-vs-bundled.md)。

- **Process 整块像 Finalize 不是已经是 ExecuteTxState：** 看见整块跑了，不是已经是 ExecuteTxState interchangeable / 1114 ftxs-notexec interchangeable。
- **看见像 Finalize 不是已经 Finalize + Commit：** 看见像 Finalize，不是已经 Finalize + Commit interchangeable。
- **看见能跑 不是已经交差：** 看见能跑，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 整块像 Finalize 正式三事（408 余量），先数清问的是是不是已经是 ExecuteTxState、是不是已经 Finalize + Commit、还是看见能跑是不是已经交差，再决定要不要同一次发布。408 fintxs vs control bundled unbundling 在本页 item 3 完成。
