# 模式：点名 query-proof-notfinal 杠

**层次**：实现 / 一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-notfinal-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-notfinal-vs-bundled.md)。

- **一层 ProofOp 的根 不是已经对上最终 AppHash：** 看见一层对上，不是已经对上最终 AppHash interchangeable / 949 query-proof-notfinal interchangeable。
- **看见一层对上 不是已经交给下一层：** 看见一层对上，不是已经交给下一层 interchangeable。
- **看见能证缺席 不是已经交差：** 看见能证缺席，不是已经比对着块哈希 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根 正式三事（325 余量），先数清问的是是不是已经对上最终 AppHash、是不是已经交给下一层、还是看见能证缺席是不是已经交差，再决定要不要同一次发布。325 query-proof vs apphash bundled unbundling 在本页 item 3 完成。
