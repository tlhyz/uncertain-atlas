# 反模式：把 PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量） 写成已经 已经能回超限列表 / 已经是引擎会帮你裁 / 已经交差

**层次**：实现 / PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-notcap-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-notcap-vs-bundled.md)。

把 PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量） 写成已经 已经能回超限列表 / 已经是引擎会帮你裁 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 max_tx_bytes 正式三事（423 余量），必须分开 not already over-limit-ok、not already engine-trimmed、not already settled 三件事，不要和 423 / 345 / 337 / 1047 / 1048 糊成一句。

也不是：

- [extvicol-notgive-sold-as-bundled](extvicol-notgive-sold-as-bundled.md) 是 extension_signature 仍未交给应用边界（421/1045），不是本页 max_tx_bytes 仍未能回超限列表边界。
- 聚合体积可以超过 max_tx_bytes 就已经能回超限列表是不变量 345，不是本页有当前配置上限仍未引擎裁边界。
