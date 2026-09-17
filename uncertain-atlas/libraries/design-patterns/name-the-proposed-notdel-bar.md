# 模式：点名 proposed-notdel 杠

**层次**：共识 / 提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notdel-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notdel-vs-bundled.md)。

- **提案收了 不是已经从池里删掉：** 看见提案带了这些交易，不是池里已经没有它们 interchangeable / 992 proposed-notdel interchangeable。
- **看见收了前缀 不是已经进块：** 看见按上限收了前缀，不是这些交易已经进块 interchangeable。
- **看见收了 不是已经过了 Process：** 看见收了，不是已经过了 Process interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看提案收了 正式三事（301 余量），先数清问的是是不是已经从池里删掉、是不是已经进块、还是看见收了是不是已经过了 Process，再决定要不要同一次发布。301 proposed vs removed bundled unbundling 在本页 item 1 启动。
