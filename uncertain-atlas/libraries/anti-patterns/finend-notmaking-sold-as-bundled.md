# 反模式：把 FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量） 写成已经 已经正在造这份提案 / 已经知道本头哈希 / 已经交差

**层次**：实现 / FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-notmaking-vs-bundled.md`](../tracks/implementation/worked-example-finend-notmaking-vs-bundled.md)。

把 FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量） 写成已经 已经正在造这份提案 / 已经知道本头哈希 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（429 余量），必须分开 not already making、not already header-known、not already settled 三件事，不要和 429 / 427 / 413 / 1065 / 1066 糊成一句。

也不是：

- [finrestr-notproc-sold-as-bundled](finrestr-notproc-sold-as-bundled.md) 是 Finalize next_validators_hash 仍未是 Process 末栏边界（428/1063），不是本页 Finalize proposer 仍未正在造边界。
- ProcessProposalRequest.proposer_address 就已经正在造这份提案是不变量 427，不是本页造了仍未知道本头哈希边界。
