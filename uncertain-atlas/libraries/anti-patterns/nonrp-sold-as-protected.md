# 反模式：看见 vote_extension 会包进 CanonicalVoteExtension 就当成已经按原样签 / 看见 non_rp_extension 按原样签就当成已经有重放保护 / 看见应用要签原样数据可以用 non_rp 就当成已经和 vote_extension 同一份

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**例**：[vote_extension 会包进 CanonicalVoteExtension ≠ 已经按原样签](../../tracks/implementation/worked-example-nonrp-vs-wrapped.md)。

## 塌法

1. 看见 `vote_extension` 会包进 `CanonicalVoteExtension` / 看见绑了 Height Round ChainID，就当成已经按原样签，或当成已经是 `CanonicalVote`。
2. 看见 `non_rp_extension` 按应用给的字节原样签 / 看见没有包装，就当成已经有重放保护，或当成已经必须填。
3. 看见应用要签原样数据可以用 `non_rp` / 看见有第二份字段，就当成已经和 `vote_extension` 同一份，或当成已经是空扩展仍验签。

## 为什么会出事

官方写：`vote_extension` 会进 `CanonicalVoteExtension`，再填 Height、Round、ChainID 后签名。`non_rp_extension` 按原样签，**不**再套一层重放保护。应用若要把原样扩展数据签出去、不要包装，才用第二份字段；`non_rp_vote_extension` 可选，也可以空。

## 和相邻反模式

- [nonrp-notraw-sold-as-bundled](nonrp-notraw-sold-as-bundled.md) 是 vote_extension 包进 CanonicalVoteExtension not already raw-signed / not already canon-vote / not already settled 正式三事（358 item 1），不是本页 bundled 全段 alone。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是 CanonicalVoteExtension 就已经是 CanonicalVote，不是本页这种 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签。
- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展就已经是每一高度一份，不是本页这种 non_rp_extension 按原样签不是已经有重放保护。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify 就已经跳过 Verify，不是本页这种要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份。
