# 模式：点名 htmt-notskip 杠

**层次**：实现 / proposer Prepare-first not already skip-process / not already same-round / not already settled 正式三事（417 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage / FinalizeBlock Usage。  
**对应**：[`../tracks/implementation/worked-example-htmt-notskip-vs-bundled.md`](../tracks/implementation/worked-example-htmt-notskip-vs-bundled.md)。

- **Prepare-first 不是已经不用再 Process：** 看见走完了，不是已经不用再 Process interchangeable / 1097 htmt-notskip interchangeable。
- **看见自己是提议者 不是已经保证是这一次：** 看见自己是提议者，不是已经保证是这一次 interchangeable。
- **看见先走 Prepare 不是已经交差：** 看见先走 Prepare，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare-first 正式三事（417 余量），先数清问的是是不是已经不用再 Process、是不是已经保证是这一次、还是看见先走 Prepare 是不是已经交差，再决定要不要同一次发布。417 htmatch vs header bundled unbundling 在本页 item 1 启动。
