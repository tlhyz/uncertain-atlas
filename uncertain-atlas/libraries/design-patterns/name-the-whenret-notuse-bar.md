# 模式：点名 whenret-notuse 杠

**层次**：实现 / PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notuse-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notuse-vs-bundled.md)。

- **用可能改过的块当这一轮提案 不是已经 validValue 非 nil 跳过 Prepare：看见用可能改过的块当这一轮提案，不是已经 validValue 非 nil 跳过 Prepare interchangeable / 1315 whenret-notuse interchangeable。**
- **possibly modified block 不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs：看见possibly modified block，不是已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable / 1315 whenret-notuse interchangeable。**
- **用可能改过的块当这一轮提案 不是已经 ProcessProposal 八栏齐：看见用可能改过的块当这一轮提案，不是已经 ProcessProposal 八栏齐 interchangeable / 1315 whenret-notuse interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事。
