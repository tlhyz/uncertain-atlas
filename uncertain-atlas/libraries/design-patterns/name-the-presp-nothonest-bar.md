# 模式：点名 presp-nothonest 杠

**层次**：实现 / ProcessProposalResponse.status SHOULD Accept not already honest-must / not already req3-tested / not already four-gates 正式三事（430 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-presp-nothonest-vs-bundled.md`](../tracks/implementation/worked-example-presp-nothonest-vs-bundled.md)。

- **SHOULD Accept 不是已经 honest proposal 必须 Accept：** 看见 SHOULD 总是 Accept，不是已经 honest proposal 必须 Accept interchangeable / 1069 presp-nothonest interchangeable。
- **看见除非真的知道活性代价 不是已经是 Req 3 已经测过：** 看见除非真的知道活性代价，不是已经是 Req 3 已经测过 interchangeable。
- **看见写了默认 Accept 不是已经四门默认 Accept：** 看见写了默认 Accept，不是已经四门默认 Accept 那种已经结算 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 SHOULD Accept 正式三事（430 余量），先数清问的是是不是已经 honest must Accept、是不是已经是 Req 3 已经测过、还是看见写了默认 Accept 是不是已经四门默认 Accept，再决定要不要同一次发布。430 procresp vs status bundled unbundling 在本页 item 3 完成。
