# 反模式：把 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量） 写成已经 已经对上了拟议块头 / 已经是 PrepareProposalRequest.time / 已经交差

**层次**：实现 / FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-nothead-vs-bundled.md`](../tracks/implementation/worked-example-finend-nothead-vs-bundled.md)。

把 FinalizeBlockRequest.time not already header-aligned / not already prepare-time / not already settled 正式三事（429 余量） 写成已经 已经对上了拟议块头 / 已经是 PrepareProposalRequest.time / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（429 余量），必须分开 not already header-aligned、not already prepare-time、not already settled 三件事，不要和 429 / 426 / 1064 / 1066 糊成一句。

也不是：

- [finend-notmaking-sold-as-bundled](finend-notmaking-sold-as-bundled.md) 是 proposer 仍未正在造单句边界（1064 item 1），不是本页 time 仍未对上拟议块头边界。
- PrepareProposalRequest.time 就已经对上了拟议块头是不变量 426，不是本页有已决块时间戳仍未是 Prepare time 边界。
