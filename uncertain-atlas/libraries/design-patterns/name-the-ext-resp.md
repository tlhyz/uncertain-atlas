# 模式：把扩展回包栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**例**：[ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 ≠ 已经会包进 CanonicalVoteExtension](../../tracks/implementation/worked-example-extresp-vs-wrap.md)。

## 三个名字

1. **ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经会包进 CanonicalVoteExtension：** 看见回了扩展不是已经没有确定性要求。
2. **ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经按原样签：** 看见回了第二份不是已经有重放保护。
3. **VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension 表：** 看见能空不是已经跳过 Verify。

## 为什么要分开叫

官方把 ExtendVote Response 表上 `vote_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定、`non_rp_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定、Verify 请求表上 `non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长写成三件事。把它们叫成一个「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」，会把已经会包进 CanonicalVoteExtension、已经按原样签和已经是 vote_extension 表一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」，先数清问的是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经会包进 CanonicalVoteExtension、ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经按原样签，还是 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension 表，再决定要不要同一次发布。
