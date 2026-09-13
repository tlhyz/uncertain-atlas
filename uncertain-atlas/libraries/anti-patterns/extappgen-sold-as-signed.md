# 反模式：看见 ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名就当成已经签过 / 看见 ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit就当成已经和 vote_extension 同一份签法 / 看见 will be signed 并 attached to Precommit 就当成已经广播 Precommit

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage。  
**例**：[ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名 ≠ 已经签过 / 已经包进 CanonicalVoteExtension](../../tracks/implementation/worked-example-extappgen-vs-signed.md)。

## 塌法

1. 看见 `ExtendVoteResponse.vote_extension` 是 application-generated information that will be signed / 看见应用生成的信息、将由 CometBFT 签名，就当成已经签过，或当成已经包进 `CanonicalVoteExtension`。
2. 看见 `ExtendVoteResponse.non_rp_extension` 是 application-generated information that will be signed by CometBFT and attached to the Precommit message / 看见相对 `vote_extension` 不做重放保护，就当成已经和 `vote_extension` 同一份签法，或当成已经有重放保护。
3. 看见 will be signed 并 attached to the Precommit message / 看见规范写「将签名并挂到 Precommit」，就当成已经广播 Precommit，或当成已经写进 last_commit。

## 为什么会出事

官方写：`vote_extension` 和 `non_rp_extension` 都是 application-generated information that will be signed；`non_rp_extension` 相对 `vote_extension` 不做重放保护，给需要 raw data without wrapping structure 的应用用。will be signed and attached 描述的是回包后 CometBFT 还要做的事，不是已经广播 Precommit，也不是已经写进 last_commit。看见 application-generated 正式三事，不是已经签过，也不是已经和 vote_extension 同一份签法，也不是已经广播 Precommit。

## 和相邻反模式

- [extresp-sold-as-wrap](extresp-sold-as-wrap.md) 是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension，不是本页这种 application-generated will be signed 不是已经签过。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种 non_rp 不做重放保护不是已经和 vote_extension 同一份签法。
- [extwhenformal-sold-as-broadcast](extwhenformal-sold-as-broadcast.md) 是应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension 并广播 Precommit，不是本页这种 will be signed and attached 不是已经广播 Precommit。
