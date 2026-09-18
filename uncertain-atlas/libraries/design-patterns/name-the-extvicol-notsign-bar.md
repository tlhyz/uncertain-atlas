# 模式：点名 extvicol-notsign 杠

**层次**：实现 / ExtendedVoteInfo.non_rp_vote_extension not already signed-as-is / not already replay-protected / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notsign-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notsign-vs-bundled.md)。

- **non_rp_vote_extension 不是已经按原样签：** 看见填了 non_rp_vote_extension，不是已经按原样签 interchangeable / 1044 extvicol-notsign interchangeable。
- **看见是应用给的第二份 不是已经有重放保护：** 看见是应用给的第二份，不是已经有重放保护 interchangeable。
- **看见能指第二份 不是已经交差：** 看见能指第二份，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_vote_extension 正式三事（421 余量），先数清问的是是不是已经按原样签、是不是已经有重放保护、还是看见能指第二份是不是已经交差，再决定要不要同一次发布。421 extvitable vs usage bundled unbundling 在本页 item 2 续。
