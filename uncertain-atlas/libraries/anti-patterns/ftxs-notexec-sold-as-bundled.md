# 反模式：把 Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量） 写成已经 已经是 ExecuteTxState / 已经 Finalize + Commit / 已经交差

**层次**：实现 / Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notexec-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notexec-vs-bundled.md)。

把 Process whole-block-like-Finalize not already ExecuteTxState / not already Finalize-plus-Commit / not already settled 正式三事（408 余量） 写成已经 已经是 ExecuteTxState / 已经 Finalize + Commit / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 整块像 Finalize 正式三事（408 余量），必须分开 not already ExecuteTxState、not already Finalize-plus-Commit、not already settled 三件事，不要和 408 / 311 / 316 / 1112 / 1113 糊成一句。

也不是：

- [ftxs-notdec-sold-as-bundled](ftxs-notdec-sold-as-bundled.md) 是全部执行信息仍未是刚决定那块的字段单句边界（1113 item 2），不是本页整块像 Finalize 仍未是 ExecuteTxState 边界。
- 候选已经是 ExecuteTxState 是不变量 311，不是本页像 Finalize 仍未 Finalize + Commit 边界。
