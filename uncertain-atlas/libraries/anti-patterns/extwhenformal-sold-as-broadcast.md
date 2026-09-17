# 反模式：看见应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension 就当成已经按原样签 / 看见会构造并签名 CanonicalVote 就当成已经验过扩展 / 看见用 CanonicalVoteExtension 和 CanonicalVote 构造 Precommit 并广播就当成已经写进 last_commit

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**例**：[应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension、填其它字段并签名 ≠ 已经按原样签](../../tracks/implementation/worked-example-extwhenformal-vs-broadcast.md)。

## 塌法

1. 看见应用回 extension 后 CometBFT 会填进 `CanonicalVoteExtension`、填其它字段并签名 / 看见填进包装，就当成已经按原样签，或当成已经广播 Precommit。
2. 看见会构造并签名 `CanonicalVote` / 看见有 CanonicalVote，就当成已经验过扩展，或当成已经 Accept。
3. 看见用 `CanonicalVoteExtension` 和 `CanonicalVote` 构造 Precommit 并广播 / 看见广播了，就当成已经写进 last_commit，或当成已经 Verify 过迟到扩展。

## 为什么会出事

官方写：ExtendVote 回包后，CometBFT 把 extension 填进 `CanonicalVoteExtension` 并签名，再构造 `CanonicalVote`，再用两者构造 Precommit 并广播。这不是按原样签，不是 Verify 他人扩展，也不是已经写进 last_commit。看见 ExtendVote When 正式流程，不是已经按原样签，也不是已经验过扩展，也不是已经写进 last_commit。

## 和相邻反模式

- [extendwhen-sold-as-locked](extendwhen-sold-as-locked.md) 是 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote，不是本页这种填进 CanonicalVoteExtension 不是已经按原样签。
- [extresp-sold-as-wrap](extresp-sold-as-wrap.md) 是 ExtendVoteResponse.vote_extension 就已经会包进 CanonicalVoteExtension，不是本页这种构造 CanonicalVote 不是已经验过扩展。
- [verifyformalwhen-sold-as-verified](verifyformalwhen-sold-as-verified.md) 是收到 Precommit 就已经验过扩展，不是本页这种构造 Precommit 并广播不是已经写进 last_commit。
