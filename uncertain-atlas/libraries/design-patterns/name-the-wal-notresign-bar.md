# 模式：点名 wal-notresign 杠

**层次**：实现 / 回放时再签 not already double-signed / not already new-vote / not already settled 正式三事（298 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [WAL](https://github.com/cometbft/cometbft/blob/main/spec/consensus/wal.md) Software / Consensus pre-write log。  
**对应**：[`../tracks/implementation/worked-example-wal-notresign-vs-bundled.md`](../tracks/implementation/worked-example-wal-notresign-vs-bundled.md)。

- **回放时再签 不是已经双签：** 看见签名器又要签，不是已经双签 interchangeable / 981 wal-notresign interchangeable。
- **看见回放 不是已经发出新票：** 看见回放，不是已经对外发出新票 interchangeable。
- **看见这次失败 不是已经交差：** 看见这次失败，不是回放已经坏了 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回放时再签 正式三事（298 余量），先数清问的是是不是已经双签、是不是已经发出新票、还是看见这次失败是不是已经交差，再决定要不要同一次发布。298 wal vs signed bundled unbundling 在本页 item 2 续。
