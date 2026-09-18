# 反模式：把 PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量） 写成已经 已经是初步交易列表 / 已经保证是这一次 / 已经交差

**层次**：实现 / PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应**：[`../tracks/implementation/worked-example-procend-notprelim-vs-bundled.md`](../tracks/implementation/worked-example-procend-notprelim-vs-bundled.md)。

把 PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量） 写成已经 已经是初步交易列表 / 已经保证是这一次 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalResponse.txs 正式三事（427 余量），必须分开 not already preliminary、not already same-round、not already settled 三件事，不要和 427 / 423 / 422 / 1058 / 1059 糊成一句。

也不是：

- [procend-notmaking-sold-as-bundled](procend-notmaking-sold-as-bundled.md) 是 proposer 仍未正在造单句边界（1059 item 2），不是本页回包 txs 仍未是初步列表边界。
- PrepareProposalRequest.txs 就已经跑过 Process 是不变量 423，不是本页可能改过仍未保证是这一次边界。
