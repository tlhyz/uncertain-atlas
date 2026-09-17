# 反模式：把 FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量） 写成已经 已经交差 local_last_commit / 已经定奖惩 / 已经交差

**层次**：实现 / FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-notlocal-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-notlocal-vs-bundled.md)。

把 FinalizeBlockRequest.decided_last_commit not already local / not already rewarded / not already settled 正式三事（422 余量） 写成已经 已经交差 local_last_commit / 已经定奖惩 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 decided_last_commit 正式三事（422 余量），必须分开 not already local、not already rewarded、not already settled 三件事，不要和 422 / 420 / 363 / 1041 / 1042 糊成一句。

也不是：

- [extmis-notkey-sold-as-bundled](extmis-notkey-sold-as-bundled.md) 是 validator_address 仍未带公钥边界（413/1039），不是本页 decided_last_commit 仍未交差 local 边界。
- ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit 是不变量 420，不是本页从刚决定那块拿到仍未定奖惩边界。
