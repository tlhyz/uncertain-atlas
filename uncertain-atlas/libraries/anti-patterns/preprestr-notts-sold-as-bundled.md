# 反模式：把 PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量） 写成已经 已经对上了拟议块头 / 已经验过票上时间 / 已经交差

**层次**：实现 / PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-preprestr-notts-vs-bundled.md`](../tracks/implementation/worked-example-preprestr-notts-vs-bundled.md)。

把 PrepareProposalRequest.time not already header-aligned / not already vote-checked / not already settled 正式三事（424 余量） 写成已经 已经对上了拟议块头 / 已经验过票上时间 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 time 正式三事（424 余量），必须分开 not already header-aligned、not already vote-checked、not already settled 三件事，不要和 424 / 420 / 359 / 1049 / 1051 糊成一句。

也不是：

- [preprestr-notlocal-sold-as-bundled](preprestr-notlocal-sold-as-bundled.md) 是 local_last_commit 仍未交差 proposed 单句边界（1049 item 1），不是本页 time 仍未对上头边界。
- ProcessProposalRequest.time 就已经验过票上时间是不变量 420，不是本页有将要提议的时间戳仍未验票时间边界。
