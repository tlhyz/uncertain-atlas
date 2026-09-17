# 反模式：把 ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量） 写成已经 已经验过票上时间 / 已经验过块头 / 已经交差

**层次**：实现 / ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request。  
**对应**：[`../tracks/implementation/worked-example-procrestr-notts-vs-bundled.md`](../tracks/implementation/worked-example-procrestr-notts-vs-bundled.md)。

把 ProcessProposalRequest.time not already vote-ts-checked / not already header-verified / not already settled 正式三事（420 余量） 写成已经 已经验过票上时间 / 已经验过块头 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（420 余量），必须分开 not already vote-ts-checked、not already header-verified、not already settled 三件事，不要和 420 / 410 / 304 / 1028 / 1030 糊成一句。

也不是：

- [procrestr-notlocal-sold-as-bundled](procrestr-notlocal-sold-as-bundled.md) 是 proposed_last_commit 仍未交差 local 单句边界（1028 item 1），不是本页 time 仍未验过票上时间边界。
- ExtendVoteRequest.time 就已经验过票上时间是不变量 410，不是本页有拟议块时间戳仍未验过块头边界。
