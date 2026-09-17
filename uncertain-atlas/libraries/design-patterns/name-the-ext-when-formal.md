# 模式：把 ExtendVote When 正式流程三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名 ≠ 已经按原样签](../../tracks/implementation/worked-example-extwhenformal-vs-broadcast.md)。

## 三个名字

1. **应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名不是已经按原样签：** 看见填进包装不是已经广播 Precommit。
2. **会构造并签名 CanonicalVote不是已经验过扩展：** 看见有 CanonicalVote不是已经 Accept。
3. **用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播不是已经写进 last_commit：** 看见广播了不是已经 Verify 过迟到扩展。

## 为什么要分开叫

官方把 ExtendVote When 正式流程里填 CanonicalVoteExtension、构造 CanonicalVote、构造 Precommit 并广播这三步写成三个名字。把它们叫成一个「看见 ExtendVote 回了 extension 就已经广播 Precommit」，会把已经按原样签、已经验过扩展和已经写进 last_commit 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 ExtendVote 回了 extension 就已经广播 Precommit」，先数清问的是应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名不是已经按原样签、会构造并签名 CanonicalVote 不是已经验过扩展，还是用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播不是已经写进 last_commit，再决定要不要同一次发布。
