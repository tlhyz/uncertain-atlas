# 模式：点名 vfwhen-notverif 杠

**层次**：实现 / signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应**：[`../tracks/implementation/worked-example-vfwhen-notverif-vs-bundled.md`](../tracks/implementation/worked-example-vfwhen-notverif-vs-bundled.md)。

- **calls Verify 不是已经验过扩展：** 看见会叫，不是已经验过扩展 interchangeable / 1086 vfwhen-notverif interchangeable。
- **看见会调 不是已经 Accept：** 看见会调，不是已经 Accept interchangeable。
- **看见收到他人票 不是已经本地票：** 看见收到他人票，不是已经不对本进程自己发出的 Precommit 调用 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 calls Verify 正式三事（435 余量），先数清问的是是不是已经验过扩展、是不是已经 Accept、还是看见收到他人票是不是已经本地票，再决定要不要同一次发布。435 verify-formal-when vs flow bundled unbundling 在本页 item 2 续。
