# 反模式：把 PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量） 写成已经 已经 Process 通常紧跟 Prepare bundled / 已经 The call is synchronous / 已经 ProcessProposal 含执行所需全部信息

**层次**：实现 / PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notret-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notret-vs-bundled.md)。

把 PrepareWhenRet returns not already Process-follows-Prepare / not already sync-blocks / not already Process-all-info 正式三事（506 余量） 写成已经 已经 Process 通常紧跟 Prepare bundled / 已经 The call is synchronous / 已经 ProcessProposal 含执行所需全部信息，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事，不要和 506 / 351 / 453 / 1313 / 1315 糊成一句。

也不是：

- [whenret-notlist-sold-as-bundled](whenret-notlist-sold-as-bundled.md) 是 notlist 单句边界（1313），不是本页边界。
- [whenret-notuse-sold-as-bundled](whenret-notuse-sold-as-bundled.md) 是 notuse 单句边界（1315），不是本页边界。
- [prepwhen-notmanip-sold-as-bundled](prepwhen-notmanip-sold-as-bundled.md) 是 PrepareWhen 可以改列表仍未是 Prepare 改列表边界（505/1312），不是本页 When return 边界。
