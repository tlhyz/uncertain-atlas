# 反模式：把 ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量） 写成已经 已经是 Finalize 请求栏的 next_validators_hash / 已经换了人 / 已经交差

**层次**：实现 / ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-nothash-vs-bundled.md`](../tracks/implementation/worked-example-extrest-nothash-vs-bundled.md)。

把 ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量） 写成已经 已经是 Finalize 请求栏的 next_validators_hash / 已经换了人 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（411 余量），必须分开 not already same-field、not already swapped、not already settled 三件事，不要和 411 / 394 / 318 / 1034 / 1035 糊成一句。

也不是：

- [extrest-notlocal-sold-as-bundled](extrest-notlocal-sold-as-bundled.md) 是 proposed_last_commit 仍未交差 local 单句边界（1035 item 2），不是本页 next_validators_hash 仍未同一套字段边界。
- Finalize 请求 next_validators_hash 就已经是同一套字段是不变量 394，不是本页能指下一份集合仍未换人边界。
