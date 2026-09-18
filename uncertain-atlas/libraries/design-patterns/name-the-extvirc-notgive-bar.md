# 模式：点名 extvirc-notgive 杠

**层次**：实现 / ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应**：[`../tracks/implementation/worked-example-extvirc-notgive-vs-bundled.md`](../tracks/implementation/worked-example-extvirc-notgive-vs-bundled.md)。

- **non_rp_extension_signature 不是已经把验过的签交给应用：** 看见填了 non_rp_extension_signature，不是已经把验过的签交给应用 interchangeable / 1054 extvirc-notgive interchangeable。
- **看见验过了 不是已经是 extension_signature：** 看见验过了，不是已经是 extension_signature interchangeable。
- **看见能指第二份签 不是已经交差：** 看见能指第二份签，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 non_rp_extension_signature 正式三事（425 余量），先数清问的是是不是已经把验过的签交给应用、是不是已经是 extension_signature、还是看见能指第二份签是不是已经交差，再决定要不要同一次发布。425 extvirest vs voteinfo bundled unbundling 在本页 item 3 完成。
