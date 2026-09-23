# 反模式：看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址就当成已经带了公钥 / 看见 VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就当成已经是 vote_extension / 看见 non_rp 相对 vote_extension 签名时不加额外元信息就当成已经按原样签

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**例**：[VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 ≠ 已经带了公钥](../../tracks/implementation/worked-example-verifyreqbar-vs-rest.md)。

## 塌法

1. 看见 `VerifyVoteExtensionRequest.validator_address` 是签了这份扩展的验证者地址 / 看见填了 validator_address，就当成已经带了公钥，或当成已经是 ExtendVoteRequest.proposer_address 那种造提案的人。
2. 看见 `VerifyVoteExtensionRequest.non_rp_vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空，就当成已经是 `vote_extension`，或当成已经跳过 Verify。
3. 看见 non_rp 相对 `vote_extension` 签名时不加额外元信息 / 看见 CometBFT 按原样签，就当成已经有 Height / Round / ChainID 包装，或当成已经 `non_rp_extension` 按原样签那种已经有重放保护。

## 为什么会出事

官方写：`validator_address` 是签了这份扩展的验证者地址，不带 PubKey。`non_rp_vote_extension` 可选可空，是应用自己的信息、由 CometBFT 签；相对 `vote_extension`，签名前不再加额外元信息。看见填了 Verify 请求栏，不是已经带了公钥，也不是已经是 vote_extension，也不是已经按原样签。

## 和相邻反模式

- [extreqmis-sold-as-reward](extreqmis-sold-as-reward.md) 是 ExtendVoteRequest.proposer_address 就已经知道本头哈希，不是本页这种 validator_address 不是已经带了公钥。
- [verifyheight-sold-as-extheight](verifyheight-sold-as-extheight.md) 是 Verify 请求余栏三列，不是本页这种 non_rp_vote_extension 不是已经是 vote_extension。
- [extresp-sold-as-wrap](extresp-sold-as-wrap.md) 是 ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension，不是本页这种 non_rp 不加元信息不是已经按原样签。
- [validator-sold-as-update](validator-sold-as-update.md) 是 VoteInfo 里 Validator 就已经带了公钥，不是本页这种 Verify 请求栏 validator_address 不是已经带了公钥。
