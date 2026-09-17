# 模式：点名 evidreap-notfull 杠

**层次**：共识 / 先装证据 not already full-of-txs / not already executed / not already settled 正式三事（299 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应**：[`../tracks/consensus/worked-example-evidreap-notfull-vs-bundled.md`](../tracks/consensus/worked-example-evidreap-notfull-vs-bundled.md)。

- **先装证据 不是已经装满交易：** 看见先装证据，不是这块已经装满交易 interchangeable / 989 evidreap-notfull interchangeable。
- **看见证据进了提案 不是已经执行：** 看见证据进了提案，不是这些证据已经执行 interchangeable。
- **看见证据占了位置 不是已经交差：** 看见证据占了位置，不是已经过了验收 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看先装证据 正式三事（299 余量），先数清问的是是不是已经装满交易、是不是已经执行、还是看见证据占了位置是不是已经交差，再决定要不要同一次发布。299 evidence vs reap bundled unbundling 在本页 item 1 启动。
