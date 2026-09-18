# 模式：点名 prepreqcol-notcap 杠

**层次**：实现 / PrepareProposalRequest.max_tx_bytes not already over-limit-ok / not already engine-trimmed / not already settled 正式三事（423 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应**：[`../tracks/implementation/worked-example-prepreqcol-notcap-vs-bundled.md`](../tracks/implementation/worked-example-prepreqcol-notcap-vs-bundled.md)。

- **max_tx_bytes 不是已经能回超限列表：** 看见填了 max_tx_bytes，不是已经能回超限列表 interchangeable / 1046 prepreqcol-notcap interchangeable。
- **看见有当前配置上限 不是已经是引擎会帮你裁：** 看见有当前配置上限，不是已经是引擎会帮你裁 interchangeable。
- **看见能指上限 不是已经交差：** 看见能指上限，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 max_tx_bytes 正式三事（423 余量），先数清问的是是不是已经能回超限列表、是不是已经是引擎会帮你裁、还是看见能指上限是不是已经交差，再决定要不要同一次发布。423 prepreq vs return bundled unbundling 在本页 item 1 启动。
