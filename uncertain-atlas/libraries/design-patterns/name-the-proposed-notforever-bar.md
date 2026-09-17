# 模式：点名 proposed-notforever 杠

**层次**：共识 / CheckTx 过了 not already in-block / not already settled / not already forever-valid 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notforever-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notforever-vs-bundled.md)。

- **CheckTx 过了 不是已经进块：** 看见 CheckTx 过了，不是已经进块 interchangeable / 994 proposed-notforever interchangeable。
- **看见进了池 不是已经结算：** 看见进了池，不是已经结算 interchangeable。
- **看见曾经绿过 不是已经永远有效：** 看见曾经绿过，不是已经永远有效 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 过了 正式三事（301 余量），先数清问的是是不是已经进块、是不是已经结算、还是看见曾经绿过是不是已经永远有效，再决定要不要同一次发布。301 proposed vs removed bundled unbundling 在本页 item 3 完成。
