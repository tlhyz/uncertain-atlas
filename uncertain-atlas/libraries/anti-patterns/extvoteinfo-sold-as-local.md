# 反模式：看见 ExtendedVoteInfo 从本进程抽出就当成已经从块里抽出 / 看见把验过的签交给应用就当成已经按原样签 / 看见扩展关掉则字段全空就当成已经到了启用高度

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo 从本进程抽出 ≠ 已经从块里抽出](../../tracks/implementation/worked-example-extvoteinfo-vs-local.md)。

## 塌法

1. 看见 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / 看见 Prepare 里有这份，就当成已经从拟议块或已决块抽出，或当成已经带了公钥。
2. 看见 `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在；没给 `non_rp` 就签空切片 / 看见有签，就当成已经按原样签，或当成已经有重放保护。
3. 看见扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 看见空着，就当成已经到了启用高度，或当成已经交差。

## 为什么会出事

官方写：这份信息从本进程里 CometBFT 的数据结构抽出。`extension_signature` 已经由 CometBFT 验过，这样才把签交给应用再处理。扩展启用时两份签都会在；没给 `non_rp_vote_extension` 就签空切片。扩展关掉则扩展字段和对应的签都空。

## 和相邻反模式

- [extvoteinfo-notfromblock-sold-as-bundled](extvoteinfo-notfromblock-sold-as-bundled.md) 是 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 not already from-block / not already pubkey / not already settled not already from-block / not already pubkey / not already settled 正式三事（369 item 1），不是本页 bundled 全段 alone。
- [extvoteinfo-notraw-sold-as-bundled](extvoteinfo-notraw-sold-as-bundled.md) 是 把验过的签交给应用不是已经按原样签 not already raw / not already protected / not already must-fill not already raw / not already protected / not already must-fill 正式三事（369 item 2），不是本页 bundled 全段 alone。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是从拟议块或已决块抽出就已经带了公钥，不是本页这种从本进程抽出不是已经从块里抽出。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种把验过的签交给应用不是已经按原样签。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 就已经 Prepare 带了扩展，不是本页这种扩展关掉则字段全空不是已经到了启用高度。
