# 模式：点名 htmt-notverif 杠

**层次**：实现 / Process height/time match not already header-verified / not already processed / not already settled 正式三事（417 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-htmt-notverif-vs-bundled.md`](../tracks/implementation/worked-example-htmt-notverif-vs-bundled.md)。

- **Process h/t 对上 不是已经验过块头：** 看见对上了，不是已经验过块头 interchangeable / 1098 htmt-notverif interchangeable。
- **看见字段对上 不是已经跑过 Process：** 看见字段对上，不是已经跑过 Process interchangeable。
- **看见能对 不是已经交差：** 看见能对，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Process h/t 正式三事（417 余量），先数清问的是是不是已经验过块头、是不是已经跑过 Process、还是看见能对是不是已经交差，再决定要不要同一次发布。417 htmatch vs header bundled unbundling 在本页 item 2 续。
