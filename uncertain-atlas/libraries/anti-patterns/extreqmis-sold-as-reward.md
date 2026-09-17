# 反模式：看见 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息就当成已经定奖惩 / 看见 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址就当成已经知道本头哈希 / 看见 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址就当成已经带了公钥

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Request / VerifyVoteExtension Request。  
**例**：[ExtendVoteRequest.misbehavior 是拟议块里那些过错信息 ≠ 已经定奖惩](../../tracks/implementation/worked-example-extreqmis-vs-reward.md)。

## 塌法

1. 看见 `ExtendVoteRequest.misbehavior` 是拟议块里那些过错信息 / 看见填了 misbehavior，就当成已经定奖惩，或当成已经罚没。
2. 看见 `ExtendVoteRequest.proposer_address` 是造这份提案的验证者地址 / 看见填了 proposer_address，就当成已经知道本头哈希，或当成已经交差。
3. 看见 `VerifyVoteExtensionRequest.validator_address` 是签了这份扩展的验证者地址 / 看见填了 validator_address，就当成已经带了公钥，或当成已经能验签。

## 为什么会出事

官方写：`misbehavior` 是拟议块里那些验证者过错信息。`proposer_address` 是造这份提案的验证者地址。`validator_address` 是签了这份扩展的验证者地址。看见填了栏，不是已经定奖惩，也不是已经知道本头哈希，也不是已经带了公钥。

## 和相邻反模式

- [finalizeequiv-sold-as-gates](finalizeequiv-sold-as-gates.md) 是可以用 decided_last_commit 和 misbehavior 定奖惩就已经罚没，不是本页这种 ExtendVoteRequest.misbehavior 是拟议块里那些过错信息不是已经定奖惩。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 的 height / time / proposer_address 对上拟议头就已经知道本头哈希，不是本页这种 ExtendVoteRequest.proposer_address 是造这份提案的验证者地址不是已经知道本头哈希。
- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 用 address 认人就已经带了公钥，不是本页这种 VerifyVoteExtensionRequest.validator_address 是签了这份扩展的验证者地址不是已经带了公钥。
