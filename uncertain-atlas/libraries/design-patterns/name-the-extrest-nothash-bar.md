# 模式：点名 extrest-nothash 杠

**层次**：实现 / ExtendVoteRequest.next_validators_hash not already same-field / not already swapped / not already settled 正式三事（411 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request。  
**对应**：[`../tracks/implementation/worked-example-extrest-nothash-vs-bundled.md`](../tracks/implementation/worked-example-extrest-nothash-vs-bundled.md)。

- **next_validators_hash 不是已经是 Finalize 请求栏的 next_validators_hash：** 看见填了 next_validators_hash，不是已经是 Finalize 请求栏 interchangeable / 1036 extrest-nothash interchangeable。
- **看见能指下一份集合 不是已经换了人：** 看见能指下一份集合，不是已经换了人 interchangeable。
- **看见有哈希 不是已经交差：** 看见有哈希，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 next_validators_hash 正式三事（411 余量），先数清问的是是不是已经是 Finalize 请求栏、是不是已经换了人、还是看见有哈希是不是已经交差，再决定要不要同一次发布。411 extreqtxs vs fintxs bundled unbundling 在本页 item 3 完成。
