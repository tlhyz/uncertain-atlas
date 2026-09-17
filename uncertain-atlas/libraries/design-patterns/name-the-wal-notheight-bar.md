# 模式：点名 wal-notheight 杠

**层次**：实现 / LastSignBytes 对上 not already new-height / not already new-commit / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notheight-vs-bundled.md`](../tracks/implementation/worked-example-wal-notheight-vs-bundled.md)。

- **LastSignBytes 对上 不是已经换了高度：** 看见 LastSignBytes 对上，不是已经换了高度 interchangeable / 982 wal-notheight interchangeable。
- **看见回放走到 precommit 不是已经发出另一张承诺：** 看见回放走到 precommit，不是已经发出另一张承诺 interchangeable。
- **看见签名器这次肯签 不是已经交差：** 看见签名器这次肯签，不是已经是崩溃之后的新一轮 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LastSignBytes 对上 正式三事（298 余量），先数清问的是是不是已经换了高度、是不是已经发出另一张承诺、还是看见这次肯签是不是已经交差，再决定要不要同一次发布。298 wal vs signed bundled unbundling 在本页 item 3 完成。
