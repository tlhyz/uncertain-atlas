# 反模式：看见 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展就当成已经从本进程抽出 / 看见 ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展就当成已经按原样签 / 看见 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签就当成已经把验过的签交给应用

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 ≠ 已经从本进程抽出](../../tracks/implementation/worked-example-extvitable-vs-usage.md)。

## 塌法

1. 看见 `ExtendedVoteInfo.vote_extension` 是发送验证者的应用给的非确定扩展 / 看见填了 vote_extension，就当成已经从本进程抽出，或当成已经是 ExtendVoteResponse.vote_extension。
2. 看见 `ExtendedVoteInfo.non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展 / 看见填了 non_rp_vote_extension，就当成已经按原样签，或当成已经是 ExtendVoteResponse.non_rp_extension。
3. 看见 `ExtendedVoteInfo.extension_signature` 是发送验证者造、CometBFT 验过的扩展签 / 看见填了 extension_signature，就当成已经把验过的签交给应用，或当成已经有重放保护。

## 为什么会出事

官方写：`vote_extension` 是发送验证者的应用给的非确定扩展。`non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展。`extension_signature` 是发送验证者造、CometBFT 验过的扩展签。看见填了栏，不是已经从本进程抽出，也不是已经按原样签，也不是已经把验过的签交给应用。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展不是已经从本进程抽出。
- [extresp-sold-as-wrap](extresp-sold-as-wrap.md) 是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension，不是本页这种 ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展不是已经按原样签。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签不是已经把验过的签交给应用。
