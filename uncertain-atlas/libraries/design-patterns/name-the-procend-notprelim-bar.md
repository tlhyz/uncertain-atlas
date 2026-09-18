# 模式：点名 procend-notprelim 杠

**层次**：实现 / PrepareProposalResponse.txs not already preliminary / not already same-round / not already settled 正式三事（427 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应**：[`../tracks/implementation/worked-example-procend-notprelim-vs-bundled.md`](../tracks/implementation/worked-example-procend-notprelim-vs-bundled.md)。

- **txs 不是已经是初步交易列表：** 看见回了 txs，不是已经是初步交易列表 interchangeable / 1060 procend-notprelim interchangeable。
- **看见可能改过 不是已经保证是这一次：** 看见可能改过，不是已经保证是这一次 interchangeable。
- **看见能指回包列表 不是已经交差：** 看见能指回包列表，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalResponse.txs 正式三事（427 余量），先数清问的是是不是已经是初步交易列表、是不是已经保证是这一次、还是看见能指回包列表是不是已经交差，再决定要不要同一次发布。427 procreqend vs prepreq bundled unbundling 在本页 item 3 完成。
