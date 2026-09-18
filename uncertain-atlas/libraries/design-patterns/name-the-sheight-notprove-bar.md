# 模式：点名 sheight-notprove 杠

**层次**：实现 / Query optional Merkle-proof not already apphash-aligned / not already prove-flagged / not already settled 正式三事（406 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**对应**：[`../tracks/implementation/worked-example-sheight-notprove-vs-bundled.md`](../tracks/implementation/worked-example-sheight-notprove-vs-bundled.md)。

- **Query 可选证明 不是已经对上 AppHash：** 看见能回证明，不是已经对上 AppHash interchangeable / 1108 sheight-notprove interchangeable。
- **看见有证明 不是已经勾了 prove：** 看见有证明，不是已经勾了 prove interchangeable。
- **看见能查 不是已经交差：** 看见能查，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 可选证明 正式三事（406 余量），先数清问的是是不是已经对上 AppHash、是不是已经勾了 prove、还是看见能查是不是已经交差，再决定要不要同一次发布。406 snapheight vs queryh bundled unbundling 在本页 item 3 完成。
