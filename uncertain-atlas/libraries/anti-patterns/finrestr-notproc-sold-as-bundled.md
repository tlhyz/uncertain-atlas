# 反模式：把 FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量） 写成已经 已经是 Process 请求末栏 / 已经是 Prepare 请求末栏 / 已经换了人

**层次**：实现 / FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-notproc-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-notproc-vs-bundled.md)。

把 FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量） 写成已经 已经是 Process 请求末栏 / 已经是 Prepare 请求末栏 / 已经换了人，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（428 余量），必须分开 not already process-hash、not already prepare-hash、not already settled 三件事，不要和 428 / 427 / 426 / 1061 / 1062 糊成一句。

也不是：

- [finrestr-notpunish-sold-as-bundled](finrestr-notpunish-sold-as-bundled.md) 是 misbehavior 仍未定奖惩单句边界（1062 item 2），不是本页 next_validators_hash 仍未是 Process 末栏边界。
- ProcessProposalRequest.next_validators_hash 就已经是 Prepare 请求末栏是不变量 427，不是本页能指下一份集合仍未是 Prepare 末栏边界。
