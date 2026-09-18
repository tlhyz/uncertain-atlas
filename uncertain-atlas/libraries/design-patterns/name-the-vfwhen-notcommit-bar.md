# 模式：点名 vfwhen-notcommit 杠

**层次**：实现 / ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notcommit-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notcommit-vs-bundled.md)。

- **ACCEPT/REJECT 不是已经写进 last_commit：** 看见收下了，不是已经写进 last_commit interchangeable / 1087 vfwhen-notcommit interchangeable。
- **看见留给下一高 不是已经迟到已验：** 看见留给下一高，不是已经 Verify 过迟到扩展 interchangeable。
- **看见丢掉了 不是已经当成块非法：** 看见丢掉了，不是已经当成块非法 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT/REJECT 正式三事（435 余量），先数清问的是是不是已经写进 last_commit、是不是已经 Verify 过迟到扩展、还是看见丢掉了是不是已经当成块非法，再决定要不要同一次发布。435 verify-formal-when vs flow bundled unbundling 在本页 item 3 完成。
