# 反模式：把 ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量） 写成已经 已经带了公钥 / 已经从本进程抽出 / 已经交差

**层次**：实现 / ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvirc-notkey-vs-bundled.md`](../tracks/implementation/worked-example-extvirc-notkey-vs-bundled.md)。

把 ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量） 写成已经 已经带了公钥 / 已经从本进程抽出 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator 正式三事（425 余量），必须分开 not already has-key、not already extracted、not already settled 三件事，不要和 425 / 369 / 364 / 1053 / 1054 糊成一句。

也不是：

- [preprestr-notpunish-sold-as-bundled](preprestr-notpunish-sold-as-bundled.md) 是 Prepare misbehavior 仍未定奖惩边界（424/1051），不是本页 validator 仍未带公钥边界。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，不是本页能指发票的人仍未抽出边界。
