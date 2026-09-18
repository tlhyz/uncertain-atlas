# 反模式：把 ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量） 写成已经 已经可以像 Prepare 那样依赖其它值 / 已经和对任意块同一裁决一回事 / 已经和对诚实提案同一裁决一回事

**层次**：实现 / ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-presp-notprep-vs-bundled.md`](../tracks/implementation/worked-example-presp-notprep-vs-bundled.md)。

把 ProcessProposalResponse.status exclusive dependence not already prepare-nondet / not already same-ruling / not already settled 正式三事（430 余量） 写成已经 已经可以像 Prepare 那样依赖其它值 / 已经和对任意块同一裁决一回事 / 已经和对诚实提案同一裁决一回事，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 exclusive dependence 正式三事（430 余量），必须分开 not already prepare-nondet、not already same-ruling、not already settled 三件事，不要和 430 / 338 / 340 / 1067 / 1069 糊成一句。

也不是：

- [presp-notinvalid-sold-as-bundled](presp-notinvalid-sold-as-bundled.md) 是 status 仍未当成块非法单句边界（1067 item 1），不是本页 exclusive dependence 仍未可以像 Prepare 那样边界。
- Prepare 没有确定性要求就已经可以像 Prepare 那样是不变量 338，不是本页必须只依赖仍未和对任意块同一裁决一回事边界。
