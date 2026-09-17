# 模式：点名 query-proof-notmatch 杠

**层次**：实现 / Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应**：[`../tracks/implementation/worked-example-query-proof-notmatch-vs-bundled.md`](../tracks/implementation/worked-example-query-proof-notmatch-vs-bundled.md)。

- **Query 回了 Proof 不是已经对上 AppHash：** 看见回了 Proof，不是已经验过 interchangeable / 948 query-proof-notmatch interchangeable。
- **看见有 type 不是已经是同一棵树：** 看见有 type，不是已经是同一棵树 interchangeable。
- **看见能证存在 不是已经交差：** 看见能证存在，不是已经能证不存在 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof 正式三事（325 余量），先数清问的是是不是已经对上 AppHash、是不是已经是同一棵树、还是看见能证存在是不是已经交差，再决定要不要同一次发布。325 query-proof vs apphash bundled unbundling 在本页 item 2 续。
