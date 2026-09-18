# 模式：点名 vreqb-notraw 杠

**层次**：实现 / VerifyVoteExtensionRequest.non_rp raw-sign not already signed-as-is / not already wrapped / not already replay-protected 正式三事（436 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**对应**：[`../tracks/implementation/worked-example-vreqb-notraw-vs-bundled.md`](../tracks/implementation/worked-example-vreqb-notraw-vs-bundled.md)。

- **non_rp raw-sign 不是已经按原样签：** 看见按原样签，不是已经按原样签 interchangeable / 1081 vreqb-notraw interchangeable。
- **看见不加元信息 不是已经包进 CanonicalVoteExtension：** 看见不加元信息，不是已经包进 CanonicalVoteExtension interchangeable。
- **看见按原样签 不是已经有重放保护：** 看见按原样签，不是已经有重放保护 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 raw-sign 正式三事（436 余量），先数清问的是是不是已经按原样签、是不是已经包进 CanonicalVoteExtension、还是看见按原样签是不是已经有重放保护，再决定要不要同一次发布。436 verifyreqbar vs rest bundled unbundling 在本页 item 3 完成。
