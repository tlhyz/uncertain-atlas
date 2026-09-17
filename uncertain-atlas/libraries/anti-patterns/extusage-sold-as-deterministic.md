# 反模式：看见 ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上就当成已经会调 ExtendVote / 看见应用可以选 0 长扩展就当成已经不会叫 ExtendVote / 看见造扩展的应用逻辑可以非确定就当成已经必须同一份扩展

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / When。  
**例**：[ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit 上、precommit nil 不会叫 ExtendVote ≠ 已经会调 ExtendVote](../../tracks/implementation/worked-example-extusage-vs-call.md)。

## 塌法

1. 看见 `ExtendVoteResponse.vote_extension` 只会挂在非 nil Precommit 上 / 看见 precommit nil 不会叫 ExtendVote，就当成已经会调 ExtendVote，或当成已经签了 nil 票仍带扩展。
2. 看见应用可以选 0 长扩展 / 看见能空，就当成已经不会叫 ExtendVote，或当成已经跳过 Verify。
3. 看见造扩展的应用逻辑可以非确定 / 看见可以非确定，就当成已经必须同一份扩展，或当成已经是 ExtendVote 没有确定性要求那种已经是同一块。

## 为什么会出事

官方写：precommit nil 时不会叫 `ExtendVote`。应用可以选 0 长扩展，但仍会叫 ExtendVote。造扩展的应用逻辑可以非确定，同一块并不蕴涵同一份扩展。看见填了 ExtendVote Usage，不是已经会调 ExtendVote，也不是已经不会叫，也不是已经必须同一份扩展。

## 和相邻反模式

- [extendonce-sold-as-height](extendonce-sold-as-height.md) 是一轮只能交出一份扩展，不是本页这种 precommit nil 不会叫 ExtendVote 不是已经会调 ExtendVote。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是空扩展仍会调 Verify，不是本页这种应用可以选 0 长扩展不是已经不会叫 ExtendVote。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 ExtendVote 没有确定性要求，不是本页这种造扩展逻辑可以非确定不是已经必须同一份扩展。
