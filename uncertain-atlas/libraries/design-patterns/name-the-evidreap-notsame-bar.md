# 模式：点名 evidreap-notsame 杠

**层次**：共识 / 两条收交易上限 not already same-cap / not already pool-fits / not already settled 正式三事（299 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应**：[`../tracks/consensus/worked-example-evidreap-notsame-vs-bundled.md`](../tracks/consensus/worked-example-evidreap-notsame-vs-bundled.md)。

- **两条收交易上限 不是已经同一条：** 看见提案这边的交易上限，不是内存池已经按同一条收 interchangeable / 990 evidreap-notsame interchangeable。
- **看见内存池收得下 不是提案扣掉证据之后还收得下：** 看见内存池收得下，不是提案扣掉证据之后还收得下 interchangeable。
- **看见两套扣法 不是已经交差：** 看见两套扣法，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看两条收交易上限 正式三事（299 余量），先数清问的是是不是已经同一条、是不是提案扣掉证据之后还收得下、还是看见两套扣法是不是已经交差，再决定要不要同一次发布。299 evidence vs reap bundled unbundling 在本页 item 2 续。
