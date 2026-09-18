# 反模式：把 Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量） 写成已经 已经验过块头 / 已经跑过 Process / 已经交差

**层次**：实现 / Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-htmt-notverif-vs-bundled.md`](../tracks/implementation/worked-example-htmt-notverif-vs-bundled.md)。

把 Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量） 写成已经 已经验过块头 / 已经跑过 Process / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process h/t 正式三事（417 余量），必须分开 not already header-verified、not already processed、not already settled 三件事，不要和 417 / 416 / 359 / 1097 / 1099 糊成一句。

也不是：

- [htmt-notskip-sold-as-bundled](htmt-notskip-sold-as-bundled.md) 是提议者先走 Prepare 仍未不用再 Process 单句边界（1097 item 1），不是本页 Process h/t 对上仍未验过块头边界。
- 收到带上头的提案会先验块头就已经跑过 Process 是不变量 416，不是本页字段对上仍未跑过 Process 边界。
