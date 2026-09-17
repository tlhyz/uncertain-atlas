# 模式：把 Verify 请求余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**例**：[VerifyVoteExtensionRequest.height 是块高度（用来对一下） ≠ 已经是拟议块高度](../../tracks/implementation/worked-example-verifyheight-vs-extheight.md)。

## 三个名字

1. **VerifyVoteExtensionRequest.height 是块高度（用来对一下）不是已经是拟议块高度：** 看见填了 height 不是已经对上了拟议块。
2. **VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希不是已经不保证跑过 Process：** 看见填了 hash 不是已经是 ExtendVoteRequest.hash。
3. **VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经跳过 Verify：** 看见能空不是已经按原样签。

## 为什么要分开叫

官方把 VerifyVoteExtension Request 表上 `height` 是块高度（用来对一下）、`hash` 是扩展要指的那份拟议块哈希、`vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长写成三件事。把它们叫成一个「看见填了 Verify 请求余栏就已经是拟议块高度」，会把已经是拟议块高度、已经不保证跑过 Process 和已经跳过 Verify 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Verify 请求余栏就已经是拟议块高度」，先数清问的是 VerifyVoteExtensionRequest.height 是块高度（用来对一下）不是已经是拟议块高度、VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希不是已经不保证跑过 Process，还是 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经跳过 Verify，再决定要不要同一次发布。
