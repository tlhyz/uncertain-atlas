# 模式：点名 vresp-notinvalid 杠

**层次**：实现 / VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-vresp-notinvalid-vs-bundled.md`](../tracks/implementation/worked-example-vresp-notinvalid-vs-bundled.md)。

- **status 不是已经当成块非法：** 看见回了 REJECT，不是已经当成块非法 interchangeable / 1076 vresp-notinvalid interchangeable。
- **看见拒掉整张票 不是已经不能收这张 Precommit：** 看见拒掉整张票，不是已经不能收这张 Precommit interchangeable。
- **看见 Precommit 被丢掉 不是已经是 Process REJECT：** 看见 Precommit 被丢掉，不是已经是 Process REJECT 那种 prevote nil interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 status 正式三事（433 余量），先数清问的是是不是已经当成块非法、是不是已经不能收这张 Precommit、还是看见 Precommit 被丢掉是不是已经是 Process REJECT，再决定要不要同一次发布。433 verifyresp vs status bundled unbundling 在本页 item 1 启动。
