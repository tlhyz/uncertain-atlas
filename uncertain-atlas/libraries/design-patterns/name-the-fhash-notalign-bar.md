# 模式：点名 fhash-notalign 杠

**层次**：实现 / Query proof-anchor not already apphash-aligned / not already keyed-lookup / not already settled 正式三事（404 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-fhash-notalign-vs-bundled.md`](../tracks/implementation/worked-example-fhash-notalign-vs-bundled.md)。

- **Query 锚 不是已经对上 AppHash：** 看见能回证明，不是已经对上 AppHash interchangeable / 1101 fhash-notalign interchangeable。
- **看见有锚 不是已经是按键查：** 看见有锚，不是已经是按键查 interchangeable。
- **看见能查 不是已经交差：** 看见能查，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 锚 正式三事（404 余量），先数清问的是是不是已经对上 AppHash、是不是已经是按键查、还是看见能查是不是已经交差，再决定要不要同一次发布。404 finapphash vs header bundled unbundling 在本页 item 2 续。
