# 模式：把 ExtendedVoteInfo 表栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**例**：[ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 ≠ 已经从本进程抽出](../../tracks/implementation/worked-example-extvitable-vs-usage.md)。

## 三个名字

1. **ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展不是已经从本进程抽出：** 看见填了 vote_extension 不是已经是 ExtendVoteResponse.vote_extension。
2. **ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展不是已经按原样签：** 看见填了 non_rp_vote_extension 不是已经是 ExtendVoteResponse.non_rp_extension。
3. **ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签不是已经把验过的签交给应用：** 看见填了 extension_signature 不是已经有重放保护。

## 为什么要分开叫

官方把 ExtendedVoteInfo 表上 `vote_extension` 是发送验证者的应用给的非确定扩展、`non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展、`extension_signature` 是发送验证者造、CometBFT 验过的扩展签写成三件事。把它们叫成一个「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出」，会把已经从本进程抽出、已经按原样签和已经把验过的签交给应用一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出」，先数清问的是 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展不是已经从本进程抽出、ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展不是已经按原样签，还是 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签不是已经把验过的签交给应用，再决定要不要同一次发布。
