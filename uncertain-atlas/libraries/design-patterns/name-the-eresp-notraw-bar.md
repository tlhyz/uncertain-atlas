# 模式：点名 eresp-notraw 杠

**层次**：实现 / ExtendVoteResponse.non_rp_extension not already signed-as-is / not already replay-protected / not already must-fill 正式三事（418 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应**：[`../tracks/implementation/worked-example-eresp-notraw-vs-bundled.md`](../tracks/implementation/worked-example-eresp-notraw-vs-bundled.md)。

- **non_rp_extension 不是已经按原样签：** 看见回了第二份，不是已经按原样签 interchangeable / 1083 eresp-notraw interchangeable。
- **看见标成非确定 不是已经有重放保护：** 看见标成非确定，不是已经有重放保护 interchangeable。
- **看见可以 0 长 不是已经必须填：** 看见可以 0 长，不是已经必须填 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension 正式三事（418 余量），先数清问的是是不是已经按原样签、是不是已经有重放保护、还是看见可以 0 长是不是已经必须填，再决定要不要同一次发布。418 extresp vs wrap bundled unbundling 在本页 item 2 续。
