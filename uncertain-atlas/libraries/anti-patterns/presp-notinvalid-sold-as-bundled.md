# 反模式：把 ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量） 写成已经 已经当成块非法 / 已经不能整块执行候选 / 已经交差

**层次**：实现 / ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-presp-notinvalid-vs-bundled.md`](../tracks/implementation/worked-example-presp-notinvalid-vs-bundled.md)。

把 ProcessProposalResponse.status not already block-invalid / not already no-exec / not already settled 正式三事（430 余量） 写成已经 已经当成块非法 / 已经不能整块执行候选 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 status 正式三事（430 余量），必须分开 not already block-invalid、not already no-exec、not already settled 三件事，不要和 430 / 376 / 340 / 1068 / 1069 糊成一句。

也不是：

- [finend-nothist-sold-as-bundled](finend-nothist-sold-as-bundled.md) 是 Finalize syncing_to_height 仍未有完整历史边界（429/1066），不是本页 Process status 仍未当成块非法边界。
- ProposalStatus REJECT 就已经不能稍后改裁决是不变量 376，不是本页共识假设不合法仍未不能整块执行候选边界。
