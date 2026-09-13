# 模式：把 ExtendedVoteInfo Usage 暴露签正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage。  
**例**：[vote_extension 的签已由 CometBFT 验过、扩展可以空 ≠ 已经应用验完](../../tracks/implementation/worked-example-extviusage-vs-expose.md)。

## 三个名字

1. **vote_extension 的签已由 CometBFT 验过、扩展可以空不是已经应用验完 / 已经必须填内容：** 看见 can be empty 不是已经 Verify 过。
2. **extension_signature 已由 CometBFT 验过、暴露给应用再处理不是已经应用验完 / 已经 Verify 过：** 看见 expose for further processing 不是已经 finished verifying。
3. **扩展启用时两份签都在、没给 non_rp 就签空切片不是已经只有一份签 / 已经没 non_rp 就没有第二份签：** 看见 two signatures will be present 不是已经 optional 就跳过。

## 为什么要分开叫

官方把 ExtendedVoteInfo Usage 里 can be empty、expose the signature for further processing、two signatures / empty slice 写成三个名字。把它们叫成一个「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」，会把已经必须填内容、已经 Verify 过和已经只有一份签一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」，先数清问的是 vote_extension 的签已由 CometBFT 验过、扩展可以空不是已经应用验完 / 已经必须填内容、extension_signature 已由 CometBFT 验过、暴露给应用再处理不是已经应用验完 / 已经 Verify 过，还是扩展启用时两份签都在、没给 non_rp 就签空切片不是已经只有一份签 / 已经没 non_rp 就没有第二份签，再决定要不要同一次发布。
