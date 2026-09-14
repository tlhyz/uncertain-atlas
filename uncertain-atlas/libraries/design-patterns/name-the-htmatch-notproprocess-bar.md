# 模式：把头字段对上余量 proposer prepare five steps not already no Process 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When / ProcessProposal Usage。  
**例**：[头字段对上余量 proposer prepare five steps not already no Process ≠ bundled](../../tracks/implementation/worked-example-htmatch-notproprocess-vs-bundled.md)。

## 三个名字

1. **proposer prepare five steps not already no Process 不是头字段对上余量 bundled：** 看见自己是提议者走完了 Prepare 那五步不是已经不用再 Process，不是 417 bundled interchangeable / 351 Process also on proposer interchangeable / 351 Process follows Prepare interchangeable。
2. **proposer prepare five steps not already guarantee this proposal 不是 351 列表对得上：** 看见走完了 Prepare 不是已经保证是这一次，不是 417 bundled interchangeable / 351 list matches interchangeable / 506 Prepare return interchangeable。
3. **proposer prepare five steps not already Process follows Prepare 不是 351 txs equals PrepareResponse：** 看见先走 Prepare 不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs，不是 417 bundled interchangeable / 351 Process follows Prepare interchangeable / 354 When async interchangeable。

## 为什么要分开叫

官方把头字段对上余量 proposer prepare five steps not already no Process 写成三个名字。把它们叫成一个「看见自己是提议者走完了 Prepare 就已经不用再 Process / 已经保证是这一次」，会把 proposer vs no Process、proposer vs guarantee this round、proposer vs Process follows Prepare 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 proposer prepare five steps not already no Process 正式三事，先数清问的是 proposer prepare five steps 是不是 already no Process、proposer prepare five steps 是不是 already guarantee this proposal、proposer prepare five steps 是不是 already Process follows Prepare，再决定要不要同一次发布。
