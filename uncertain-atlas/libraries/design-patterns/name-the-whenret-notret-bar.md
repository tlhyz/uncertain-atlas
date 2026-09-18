# 模式：点名 whenret-notret 杠

**层次**：实现 / PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notret-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notret-vs-bundled.md)。

- **从 PrepareProposal 调用返回 不是已经 Process 通常紧跟 Prepare bundled：看见从 PrepareProposal 调用返回，不是已经 Process 通常紧跟 Prepare bundled interchangeable / 1314 whenret-notret interchangeable。**
- **返回了 不是已经 The call is synchronous：看见返回了，不是已经 The call is synchronous interchangeable / 1314 whenret-notret interchangeable。**
- **从 PrepareProposal 调用返回 不是已经 ProcessProposal 含执行所需全部信息：看见从 PrepareProposal 调用返回，不是已经 ProcessProposal 含执行所需全部信息 interchangeable / 1314 whenret-notret interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事。
