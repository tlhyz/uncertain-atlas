# 模式：把 Verify 请求栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request / Usage。  
**例**：[VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址 ≠ 已经带了公钥](../../tracks/implementation/worked-example-verifyreqbar-vs-rest.md)。

## 三个名字

1. **VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥：** 看见填了 validator_address 不是已经是 proposer_address。
2. **VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension：** 看见能空不是已经跳过 Verify。
3. **non_rp 相对 vote_extension 签名时不加额外元信息不是已经按原样签：** 看见 CometBFT 按原样签不是已经有 Height / Round / ChainID 包装。

## 为什么要分开叫

官方把 Verify 请求栏上 validator_address、non_rp_vote_extension、相对 vote_extension 不加元信息这三件事写成三个名字。把它们叫成一个「看见填了 Verify 请求栏就已经带了公钥」，会把已经带了公钥、已经是 vote_extension 和已经按原样签一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Verify 请求栏就已经带了公钥」，先数清问的是 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥、VerifyVoteExtensionRequest.non_rp_vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经是 vote_extension，还是 non_rp 相对 vote_extension 签名时不加额外元信息不是已经按原样签，再决定要不要同一次发布。
