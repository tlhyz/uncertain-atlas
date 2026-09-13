# 反模式：看见 vote_extension 的签已由 CometBFT 验过就当成已经应用验完 / 看见 extension_signature 暴露给应用再处理就当成已经 Verify 过 / 看见两份签都在就当成已经只有一份签

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage。  
**例**：[vote_extension 的签已由 CometBFT 验过、扩展可以空 ≠ 已经应用验完](../../tracks/implementation/worked-example-extviusage-vs-expose.md)。

## 塌法

1. 看见 `vote_extension` contains the sending validator's vote extension, whose signature was verified by CometBFT / 看见 can be empty，就当成已经应用验完，或当成已经必须填内容。
2. 看见 `extension_signature` which was verified by CometBFT / 看见 expose the signature to the application for further processing or verification，就当成已经 Verify 过，或当成已经应用 finished verifying。
3. 看见 the two signatures will be present if vote extensions are enable / 看见没给 `non_rp_vote_extension` 时 signature will sign an empty slice，就当成已经只有一份签，或当成已经没 non_rp 就没有第二份签。

## 为什么会出事

官方写：`vote_extension` 的签已由 CometBFT 验过，可以 empty。`extension_signature` 已由 CometBFT 验过，暴露给应用 for further processing or verification。扩展启用时 two signatures will be present；没给 non_rp 就 sign an empty slice。这不是已经应用验完，不是已经 Verify 过，也不是已经只有一份签。看见 ExtendedVoteInfo Usage 暴露签正式三事，不是已经必须填内容，不是已经 finished verifying，不是已经没 non_rp 就没有第二份签。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，不是本页这种 can be empty 不是已经必须填内容。
- [extvitable-sold-as-usage](extvitable-sold-as-usage.md) 是 ExtendedVoteInfo.extension_signature 表栏就已经把验过的签交给应用，不是本页这种 expose for further processing 不是已经 Verify 过。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 non_rp 按原样签就已经有重放保护，不是本页这种没 non_rp 就签空切片不是已经没 non_rp 就没有第二份签。
