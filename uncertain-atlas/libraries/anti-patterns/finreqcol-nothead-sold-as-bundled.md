# 反模式：把 FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量） 写成已经 已经对上了拟议块头 / 已经字段名对上就已经跑过 Process / 已经交差

**层次**：实现 / FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finreqcol-nothead-vs-bundled.md`](../tracks/implementation/worked-example-finreqcol-nothead-vs-bundled.md)。

把 FinalizeBlockRequest.height not already header-aligned / not already processed / not already settled 正式三事（422 余量） 写成已经 已经对上了拟议块头 / 已经字段名对上就已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 正式三事（422 余量），必须分开 not already header-aligned、not already processed、not already settled 三件事，不要和 422 / 419 / 1040 / 1042 糊成一句。

也不是：

- [finreqcol-notlocal-sold-as-bundled](finreqcol-notlocal-sold-as-bundled.md) 是 decided_last_commit 仍未交差 local 单句边界（1040 item 1），不是本页 height 仍未对上拟议块头边界。
- ProcessProposalRequest.height 就已经对上了拟议块头是不变量 419，不是本页有已决块高度仍未 Process 边界。
