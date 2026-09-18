# 模式：点名 finend-notmaking 杠

**层次**：实现 / FinalizeBlockRequest.proposer_address not already making / not already header-known / not already settled 正式三事（429 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Request。  
**对应**：[`../tracks/implementation/worked-example-finend-notmaking-vs-bundled.md`](../tracks/implementation/worked-example-finend-notmaking-vs-bundled.md)。

- **proposer_address 不是已经正在造这份提案：** 看见填了 proposer_address，不是已经正在造这份提案 interchangeable / 1064 finend-notmaking interchangeable。
- **看见造了 不是已经知道本头哈希：** 看见造了，不是已经知道本头哈希 interchangeable。
- **看见能指造了的人 不是已经交差：** 看见能指造了的人，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 proposer_address 正式三事（429 余量），先数清问的是是不是已经正在造、是不是已经知道本头哈希、还是看见能指造了的人是不是已经交差，再决定要不要同一次发布。429 finreqend vs procreq bundled unbundling 在本页 item 1 启动。
