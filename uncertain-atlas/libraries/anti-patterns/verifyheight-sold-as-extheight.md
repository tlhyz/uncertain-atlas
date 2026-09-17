# 反模式：看见 VerifyVoteExtensionRequest.height 是块高度（用来对一下）就当成已经是拟议块高度 / 看见 VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希就当成已经不保证跑过 Process / 看见 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长就当成已经跳过 Verify

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Request。  
**例**：[VerifyVoteExtensionRequest.height 是块高度（用来对一下） ≠ 已经是拟议块高度](../../tracks/implementation/worked-example-verifyheight-vs-extheight.md)。

## 塌法

1. 看见 `VerifyVoteExtensionRequest.height` 是块高度（用来对一下） / 看见填了 height，就当成已经是拟议块高度，或当成已经对上了拟议块。
2. 看见 `VerifyVoteExtensionRequest.hash` 是扩展要指的那份拟议块哈希 / 看见填了 hash，就当成已经不保证跑过 Process，或当成已经是 ExtendVoteRequest.hash。
3. 看见 `VerifyVoteExtensionRequest.vote_extension` 是应用自己的信息、由 CometBFT 签、可以 0 长 / 看见能空，就当成已经跳过 Verify，或当成已经按原样签。

## 为什么会出事

官方写：`height` 是块高度，用来对一下。`hash` 是扩展要指的那份拟议块的哈希。`vote_extension` 是应用自己的信息，由 CometBFT 签，可以 0 长。看见填了栏，不是已经是拟议块高度，也不是已经不保证跑过 Process，也不是已经跳过 Verify。

## 和相邻反模式

- [extreqhash-sold-as-process](extreqhash-sold-as-process.md) 是 ExtendVoteRequest.height 就已经对上了拟议块，不是本页这种 VerifyVoteExtensionRequest.height 是块高度（用来对一下）不是已经是拟议块高度。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是请求里的 hash 就已经对该块跑过 Process，不是本页这种 VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希不是已经不保证跑过 Process。
- [nonrp-sold-as-protected](nonrp-sold-as-protected.md) 是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签，不是本页这种 VerifyVoteExtensionRequest.vote_extension 是应用自己的信息、由 CometBFT 签、可以 0 长不是已经跳过 Verify。
