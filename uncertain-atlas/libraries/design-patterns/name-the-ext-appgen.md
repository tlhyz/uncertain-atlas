# 模式：把 ExtendVote Response Usage application-generated 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage。  
**例**：[ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名 ≠ 已经签过 / 已经包进 CanonicalVoteExtension](../../tracks/implementation/worked-example-extappgen-vs-signed.md)。

## 三个名字

1. **ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名不是已经签过 / 已经包进 CanonicalVoteExtension：** 看见 application-generated 不是已经 CometBFT 签完。
2. **ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit、相对 vote_extension 不做重放保护不是已经和 vote_extension 同一份签法 / 已经有重放保护：** 看见 raw data without wrapping 不是已经有 Height / Round / ChainID 包装。
3. **will be signed 并 attached to Precommit 不是已经广播 Precommit / 已经写进 last_commit：** 看见 Usage 里的将来时不是已经 When 里广播完。

## 为什么要分开叫

官方把 ExtendVote Response Usage 里 application-generated、will be signed、attached to Precommit、non_rp 不做重放保护写成三个名字。把它们叫成一个「看见应用回了扩展就已经签过、已经包进 CanonicalVoteExtension、已经广播 Precommit」，会把已经签过、已经包装和已经写进 last_commit 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见应用回了扩展就已经签过、已经包进 CanonicalVoteExtension、已经广播 Precommit」，先数清问的是 ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名不是已经签过 / 已经包进 CanonicalVoteExtension、ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit、相对 vote_extension 不做重放保护不是已经和 vote_extension 同一份签法 / 已经有重放保护，还是 will be signed 并 attached to Precommit 不是已经广播 Precommit / 已经写进 last_commit，再决定要不要同一次发布。
