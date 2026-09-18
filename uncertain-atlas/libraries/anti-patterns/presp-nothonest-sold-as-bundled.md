# 反模式：把 ProcessProposalResponse.status SHOULD Accept not already honest-must / not already req3-tested / not already four-gates 正式三事（430 余量） 写成已经 已经 honest proposal 必须 Accept / 已经是 Req 3 已经测过 / 已经四门默认 Accept

**层次**：实现 / ProcessProposalResponse.status SHOULD Accept not already honest-must / not already req3-tested / not already four-gates 正式三事（430 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-presp-nothonest-vs-bundled.md`](../tracks/implementation/worked-example-presp-nothonest-vs-bundled.md)。

把 ProcessProposalResponse.status SHOULD Accept not already honest-must / not already req3-tested / not already four-gates 正式三事（430 余量） 写成已经 已经 honest proposal 必须 Accept / 已经是 Req 3 已经测过 / 已经四门默认 Accept，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 SHOULD Accept 正式三事（430 余量），必须分开 not already honest-must、not already req3-tested、not already four-gates 三件事，不要和 430 / 347 / 1067 / 1068 糊成一句。

也不是：

- [presp-notprep-sold-as-bundled](presp-notprep-sold-as-bundled.md) 是 exclusive dependence 仍未可以像 Prepare 那样单句边界（1068 item 2），不是本页 SHOULD Accept 仍未 honest must Accept 边界。
- 正确提议者的准备提案必须被正确接收者 Accept 是不变量 347，不是本页除非真的知道活性代价仍未是 Req 3 已经测过边界。
