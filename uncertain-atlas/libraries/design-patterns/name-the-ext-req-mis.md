# 模式：把 ExtendVote 请求末栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**例**：[ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 ≠ 已经定奖惩](../../tracks/implementation/worked-example-extreqmis-vs-reward.md)。

## 三个名字

1. **ExtendVoteRequest.misbehavior 是拟议块里那些过错信息不是已经定奖惩：** 看见填了 misbehavior 不是已经罚没。
2. **ExtendVoteRequest.proposer_address 是造这份提案的验证者地址不是已经知道本头哈希：** 看见填了 proposer_address 不是已经交差。
3. **VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥：** 看见填了 validator_address 不是已经能验签。

## 为什么要分开叫

官方把 `misbehavior` 是拟议块里那些过错信息、`proposer_address` 是造这份提案的验证者地址、`validator_address` 是签了这份扩展的验证者地址写成三件事。把它们叫成一个「看见填了 ExtendVote 请求末栏就已经定奖惩」，会把已经定奖惩、已经知道本头哈希和已经带了公钥一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求末栏就已经定奖惩」，先数清问的是 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息不是已经定奖惩、ExtendVoteRequest.proposer_address 是造这份提案的验证者地址不是已经知道本头哈希，还是 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥，再决定要不要同一次发布。
