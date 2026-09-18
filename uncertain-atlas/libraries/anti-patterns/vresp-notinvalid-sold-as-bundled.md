# 反模式：把 VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量） 写成已经 已经当成块非法 / 已经不能收这张 Precommit / 已经是 Process REJECT

**层次**：实现 / VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-vresp-notinvalid-vs-bundled.md`](../tracks/implementation/worked-example-vresp-notinvalid-vs-bundled.md)。

把 VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量） 写成已经 已经当成块非法 / 已经不能收这张 Precommit / 已经是 Process REJECT，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 status 正式三事（433 余量），必须分开 not already block-invalid、not already no-precommit、not already process-reject 三件事，不要和 433 / 34 / 430 / 1077 / 1078 糊成一句。

也不是：

- [fend-nottimeout-sold-as-bundled](fend-nottimeout-sold-as-bundled.md) 是 Finalize next_block_delay 仍未是本地 timeout_commit 边界（432/1075），不是本页 Verify status 仍未当成块非法边界。
- 验签拒收整张 Precommit 就已经是块非法是不变量 34，不是本页拒掉整张票仍未不能收这张 Precommit 边界。
