# 模式：点名 finrestr-notproc 杠

**层次**：实现 / FinalizeBlockRequest.next_validators_hash not already process-hash / not already prepare-hash / not already settled 正式三事（428 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finrestr-notproc-vs-bundled.md`](../tracks/implementation/worked-example-finrestr-notproc-vs-bundled.md)。

- **next_validators_hash 不是已经是 Process 请求末栏：** 看见填了 next_validators_hash，不是已经是 Process 请求末栏 interchangeable / 1063 finrestr-notproc interchangeable。
- **看见能指下一份集合 不是已经是 Prepare 请求末栏：** 看见能指下一份集合，不是已经是 Prepare 请求末栏 interchangeable。
- **看见字段名对得上 不是已经换了人：** 看见字段名对得上，不是已经换了人 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（428 余量），先数清问的是是不是已经是 Process 末栏、是不是已经是 Prepare 末栏、还是看见字段名对得上是不是已经换了人，再决定要不要同一次发布。428 finreqrest vs procreq bundled unbundling 在本页 item 3 完成。
