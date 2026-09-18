# 模式：点名 extvicol-notgive 杠

**层次**：实现 / ExtendedVoteInfo.extension_signature not already given-to-app / not already replay-protected / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notgive-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notgive-vs-bundled.md)。

- **extension_signature 不是已经把验过的签交给应用：** 看见填了 extension_signature，不是已经把验过的签交给应用 interchangeable / 1045 extvicol-notgive interchangeable。
- **看见验过了 不是已经有重放保护：** 看见验过了，不是已经有重放保护 interchangeable。
- **看见能指签 不是已经交差：** 看见能指签，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 extension_signature 正式三事（421 余量），先数清问的是是不是已经把验过的签交给应用、是不是已经有重放保护、还是看见能指签是不是已经交差，再决定要不要同一次发布。421 extvitable vs usage bundled unbundling 在本页 item 3 完成。
