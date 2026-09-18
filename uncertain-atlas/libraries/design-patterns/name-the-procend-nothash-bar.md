# 模式：点名 procend-nothash 杠

**层次**：实现 / ProcessProposalRequest.next_validators_hash not already prepare-hash / not already finalize-hash / not already settled 正式三事（427 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Request / PrepareProposal Response。  
**对应**：[`../tracks/implementation/worked-example-procend-nothash-vs-bundled.md`](../tracks/implementation/worked-example-procend-nothash-vs-bundled.md)。

- **next_validators_hash 不是已经是 Prepare 请求末栏的 next_validators_hash：** 看见填了 next_validators_hash，不是已经是 Prepare 请求末栏的 next_validators_hash interchangeable / 1058 procend-nothash interchangeable。
- **看见能指下一份集合 不是已经是 Finalize 请求栏：** 看见能指下一份集合，不是已经是 Finalize 请求栏 interchangeable。
- **看见字段名对得上 不是已经交差：** 看见字段名对得上，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（427 余量），先数清问的是是不是已经是 Prepare 请求末栏、是不是已经是 Finalize 请求栏、还是看见字段名对得上是不是已经交差，再决定要不要同一次发布。427 procreqend vs prepreq bundled unbundling 在本页 item 1 启动。
