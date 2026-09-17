# 模式：点名 extmis-notpunish 杠

**层次**：实现 / ExtendVoteRequest.misbehavior not already rewarded / not already settled / not already slashed 正式三事（413 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-extmis-notpunish-vs-bundled.md`](../tracks/implementation/worked-example-extmis-notpunish-vs-bundled.md)。

- **misbehavior 不是已经定奖惩：** 看见填了 misbehavior，不是已经定奖惩 interchangeable / 1037 extmis-notpunish interchangeable。
- **看见拟议块里有过错信息 不是已经交差：** 看见拟议块里有过错信息，不是已经交差 interchangeable。
- **看见能指过错 不是已经定了奖惩：** 看见能指过错，不是已经定了奖惩 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 misbehavior 正式三事（413 余量），先数清问的是是不是已经定奖惩、是不是已经交差、还是看见能指过错是不是已经定了奖惩，再决定要不要同一次发布。413 extreqmis vs reward bundled unbundling 在本页 item 1 启动。
