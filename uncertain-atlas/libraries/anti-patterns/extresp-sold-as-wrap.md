# 反模式：看见 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就当成已经会包进 CanonicalVoteExtension / 看见 ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就当成已经按原样签 / 看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就当成已经是 vote_extension 表

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**例**：[ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 ≠ 已经会包进 CanonicalVoteExtension](../../tracks/implementation/worked-example-extresp-vs-wrap.md)。

## 塌法

1. 看见 `ExtendVoteResponse.vote_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了扩展，就当成已经会包进 CanonicalVoteExtension，或当成已经没有确定性要求。
2. 看见 `ExtendVoteResponse.non_rp_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了第二份，就当成已经按原样签，或当成已经有重放保护。
3. 看见 `VerifyVoteExtensionRequest.non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空，就当成已经是 vote_extension 表，或当成已经跳过 Verify。

## 为什么会出事

官方写：`vote_extension` 是 CometBFT 签的信息，可以 0 长，表上 Deterministic = No。`non_rp_extension` 是 CometBFT 签的信息，可以 0 长，表上 Deterministic = No。`non_rp_vote_extension` 是应用自己的信息，由 CometBFT 签，可以 0 长。看见回了，不是已经会包进 CanonicalVoteExtension，也不是已经按原样签，也不是已经是 vote_extension 表。

## 和相邻反模式

- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经会包进 CanonicalVoteExtension。
- [verifyheight-sold-as-extheight](verifyheight-sold-as-extheight.md) 是 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就已经跳过 Verify，不是本页这种 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension 表。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 ExtendVote 没有确定性要求就已经是同一份扩展，不是本页这种 ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定不是已经按原样签。
