# 模式：把 ExtendVote Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / When。  
**例**：[ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extusage-vs-call.md)。

## 三个名字

1. **ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote：** 看见 precommit nil 不是已经带了扩展。
2. **应用可以选 0 长扩展不是已经不会叫 ExtendVote：** 看见能空不是已经跳过 Verify。
3. **造扩展的应用逻辑可以非确定不是已经必须同一份扩展：** 看见可以非确定不是已经是同一块。

## 为什么要分开叫

官方把 ExtendVote Usage 上 nil 票不调、能选空扩展、造扩展逻辑可非确定这三件事写成三个名字。把它们叫成一个「看见填了 ExtendVote Usage 就已经会调 ExtendVote」，会把已经会调、已经不会叫和已经必须同一份扩展一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote Usage 就已经会调 ExtendVote」，先数清问的是 ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote、应用可以选 0 长扩展不是已经不会叫 ExtendVote，还是造扩展的应用逻辑可以非确定不是已经必须同一份扩展，再决定要不要同一次发布。
