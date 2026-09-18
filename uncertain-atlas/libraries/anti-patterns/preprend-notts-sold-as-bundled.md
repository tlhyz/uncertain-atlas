# 反模式：把 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量） 写成已经 已经对上了拟议块头 / 已经是 PrepareProposalRequest.time / 已经交差

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request / FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-preprend-notts-vs-bundled.md`](../tracks/implementation/worked-example-preprend-notts-vs-bundled.md)。

把 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（426 余量） 写成已经 已经对上了拟议块头 / 已经是 PrepareProposalRequest.time / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockRequest.time 正式三事（426 余量），必须分开 not already header-aligned、not already prepare-time、not already settled 三件事，不要和 426 / 424 / 420 / 1055 / 1056 糊成一句。

也不是：

- [preprend-notmade-sold-as-bundled](preprend-notmade-sold-as-bundled.md) 是 proposer 仍未造完单句边界（1056 item 2），不是本页 Finalize time 仍未对上头边界。
- PrepareProposalRequest.time 就已经对上了拟议块头是不变量 424，不是本页有已决块时间戳仍未是 Prepare time 边界。
