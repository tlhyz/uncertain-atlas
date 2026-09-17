# 模式：把两份扩展两份签三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**例**：[vote_extension 会包进 CanonicalVoteExtension ≠ 已经按原样签](../../tracks/implementation/worked-example-nonrp-vs-wrapped.md)。

## 三个名字

1. **vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签：** 看见绑了 Height Round ChainID 不是已经是 CanonicalVote。
2. **non_rp_extension 按原样签不是已经有重放保护：** 看见没有包装不是已经必须填。
3. **要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份：** 看见有第二份字段不是已经是空扩展仍验签。

## 为什么要分开叫

官方把 `vote_extension` 包进 `CanonicalVoteExtension` 再签、`non_rp_extension` 按原样签且没有重放保护、应用要签原样数据才用第二份字段写成三件事。把它们叫成一个「看见有扩展就已经按原样签」，会把 CanonicalVote、一轮一份扩展和空扩展仍会调 Verify 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有扩展就已经按原样签」，先数清问的是 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签、non_rp_extension 按原样签不是已经有重放保护，还是要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份，再决定要不要同一次发布。
