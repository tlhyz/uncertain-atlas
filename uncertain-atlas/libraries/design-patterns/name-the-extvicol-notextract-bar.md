# 模式：点名 extvicol-notextract 杠

**层次**：实现 / ExtendedVoteInfo.vote_extension not already extracted / not already packed / not already settled 正式三事（421 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvicol-notextract-vs-bundled.md`](../tracks/implementation/worked-example-extvicol-notextract-vs-bundled.md)。

- **vote_extension 不是已经从本进程抽出：** 看见填了 vote_extension，不是已经从本进程抽出 interchangeable / 1043 extvicol-notextract interchangeable。
- **看见是应用给的 不是已经会包进 CanonicalVoteExtension：** 看见是应用给的，不是已经会包进 CanonicalVoteExtension interchangeable。
- **看见能指扩展 不是已经交差：** 看见能指扩展，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 vote_extension 正式三事（421 余量），先数清问的是是不是已经从本进程抽出、是不是已经会包进 CanonicalVoteExtension、还是看见能指扩展是不是已经交差，再决定要不要同一次发布。421 extvitable vs usage bundled unbundling 在本页 item 1 启动。
