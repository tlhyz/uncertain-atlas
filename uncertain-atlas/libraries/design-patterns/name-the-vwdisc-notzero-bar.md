# 模式：点名 vwdisc-notzero 杠

**层次**：实现 / VerifyDiscard zerolen not already still-calls-Verify / not already skip / not already 0-len-illegal 正式三事（514 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应**：[`../tracks/implementation/worked-example-vwdisc-notzero-vs-bundled.md`](../tracks/implementation/worked-example-vwdisc-notzero-vs-bundled.md)。

- **0 长扩展只要伴随签名也合法就算有效 不是已经空扩展仍会调 Verify bundled：看见0 长扩展只要伴随签名也合法就算有效，不是已经空扩展仍会调 Verify bundled interchangeable / 1326 vwdisc-notzero interchangeable。**
- **0-length with valid signature 不是已经跳过 Verify：看见0-length with valid signature，不是已经跳过 Verify interchangeable / 1326 vwdisc-notzero interchangeable。**
- **0 长扩展只要伴随签名也合法就算有效 不是已经 0 长就不合法：看见0 长扩展只要伴随签名也合法就算有效，不是已经 0 长就不合法 interchangeable / 1326 vwdisc-notzero interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事（514 余量），必须分开 not already Verify-When-bundled、not already still-calls-Verify、not already verified 三件事。
