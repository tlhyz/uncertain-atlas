# 反模式：把 VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量） 写成已经 已经带了公钥 / 已经是造这份提案的 proposer_address / 已经能验签

**层次**：实现 / VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notkey-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notkey-vs-bundled.md)。

把 VerifyVoteExtensionRequest.validator_address not already has-key / not already proposer / not already can-verify 正式三事（436 余量） 写成已经 已经带了公钥 / 已经是造这份提案的 proposer_address / 已经能验签，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_address 正式三事（436 余量），必须分开 not already has-key、not already proposer、not already can-verify 三件事，不要和 436 / 364 / 413 / 1080 / 1081 糊成一句。

也不是：

- [vresp-nothonest-sold-as-bundled](vresp-nothonest-sold-as-bundled.md) 是 Verify SHOULD Accept 仍未正确进程必须 Accept 边界（433/1078），不是本页 Verify validator_address 仍未带了公钥边界。
- Validator 用 address 认人就已经带了公钥是不变量 364，不是本页能指签扩展的人仍未是 proposer 边界。
