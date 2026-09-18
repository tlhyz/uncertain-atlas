# 反模式：把 Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量） 写成已经 已经是刚决定那块的字段 / 已经知道本头哈希 / 已经交差

**层次**：实现 / Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-htmt-notdec-vs-bundled.md`](../tracks/implementation/worked-example-htmt-notdec-vs-bundled.md)。

把 Finalize height/time match not already decided-fields / not already header-known / not already settled 正式三事（417 余量） 写成已经 已经是刚决定那块的字段 / 已经知道本头哈希 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize h/t 正式三事（417 余量），必须分开 not already decided-fields、not already header-known、not already settled 三件事，不要和 417 / 407 / 416 / 1097 / 1098 糊成一句。

也不是：

- [htmt-notverif-sold-as-bundled](htmt-notverif-sold-as-bundled.md) 是 Process h/t 对上仍未验过块头单句边界（1098 item 2），不是本页 Finalize h/t 对上仍未是刚决定那块的字段边界。
- Finalize 含刚决定那块的字段就已经是四门已经结算是不变量 407，不是本页字段对上仍未知道本头哈希边界。
