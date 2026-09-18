# 反模式：把 PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量） 写成已经 已经 validValue 非 nil 跳过 Prepare / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs / 已经 ProcessProposal 八栏齐

**层次**：实现 / PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notuse-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notuse-vs-bundled.md)。

把 PrepareWhenRet use-as-proposal not already validValue-skip / not already txs-equal / not already eight-cols 正式三事（506 余量） 写成已经 已经 validValue 非 nil 跳过 Prepare / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs / 已经 ProcessProposal 八栏齐，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事，不要和 506 / 356 / 351 / 1313 / 1314 糊成一句。

也不是：

- [whenret-notlist-sold-as-bundled](whenret-notlist-sold-as-bundled.md) 是 notlist 单句边界（1313），不是本页边界。
- [whenret-notret-sold-as-bundled](whenret-notret-sold-as-bundled.md) 是 notret 单句边界（1314），不是本页边界。
- [prepwhen-notmanip-sold-as-bundled](prepwhen-notmanip-sold-as-bundled.md) 是 PrepareWhen 可以改列表仍未是 Prepare 改列表边界（505/1312），不是本页 When return 边界。
