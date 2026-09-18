# 反模式：把 Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量） 写成已经 已经是刚决定那块的字段 / 已经跑过 Process / 已经交差

**层次**：实现 / Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / ProcessProposal Usage。  
**对应**：[`../tracks/implementation/worked-example-ftxs-notdec-vs-bundled.md`](../tracks/implementation/worked-example-ftxs-notdec-vs-bundled.md)。

把 Process all-exec-info not already just-decided-fields / not already processed / not already settled 正式三事（408 余量） 写成已经 已经是刚决定那块的字段 / 已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process 全部执行信息 正式三事（408 余量），必须分开 not already just-decided-fields、not already processed、not already settled 三件事，不要和 408 / 359 / 1109 / 1112 / 1114 糊成一句。

也不是：

- [ftxs-notsettle-sold-as-bundled](ftxs-notsettle-sold-as-bundled.md) 是执行再交还仍未交差单句边界（1112 item 1），不是本页全部执行信息仍未是刚决定那块的字段边界。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process 是不变量 359，不是本页能执行仍未跑过 Process 边界。
