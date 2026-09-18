# 反模式：把 PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量） 写成已经 已经 preliminary raw proposal bundled / 已经 can manipulate transactions bundled / 已经 PrepareProposalResponse.txs 是可能改过的列表

**层次**：实现 / PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When steps 4–5。  
**对应**：[`../tracks/implementation/worked-example-whenret-notlist-vs-bundled.md`](../tracks/implementation/worked-example-whenret-notlist-vs-bundled.md)。

把 PrepareWhenRet return-list not already raw-proposal / not already manipulate / not already Response-txs 正式三事（506 余量） 写成已经 已经 preliminary raw proposal bundled / 已经 can manipulate transactions bundled / 已经 PrepareProposalResponse.txs 是可能改过的列表，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposal When return / use-as-proposal 正式三事（506 余量），必须分开 not already raw-proposal、not already Process-follows-Prepare、not already validValue-skip 三件事，不要和 506 / 503 / 505 / 1314 / 1315 糊成一句。

也不是：

- [whenret-notret-sold-as-bundled](whenret-notret-sold-as-bundled.md) 是 notret 单句边界（1314），不是本页边界。
- [whenret-notuse-sold-as-bundled](whenret-notuse-sold-as-bundled.md) 是 notuse 单句边界（1315），不是本页边界。
- [prepwhen-notmanip-sold-as-bundled](prepwhen-notmanip-sold-as-bundled.md) 是 PrepareWhen 可以改列表仍未是 Prepare 改列表边界（505/1312），不是本页 When return 边界。
