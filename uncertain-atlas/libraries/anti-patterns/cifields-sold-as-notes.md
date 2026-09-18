# 反模式：看见 CommitInfo.round 是提交轮就当成已经按投票权排过 / 看见 CommitInfo.votes 就当成已经进了块 / 看见 Fields 栏就当成已经是 CommitInfo Notes 那套票序话

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types CommitInfo Fields。  
**例**：[CommitInfo.round 是提交轮 ≠ 已经按投票权排过](../../tracks/implementation/worked-example-cifields-vs-notes.md)。

## 塌法

1. 看见 `round` is Commit round. Reflects the round at which the block proposer decided in the previous height / 看见 CommitInfo.round 是提交轮，就当成已经按投票权排过，或当成已经罚没。
2. 看见 `votes` is List of validators' addresses in the last validator set with their voting information / 看见 CommitInfo.votes 是上一验证者集合里各人的投票信息，就当成已经进了块，或当成已经交差。
3. 看见 Fields 表里有 round 和 votes / 看见 Fields 栏描述 round 和 votes，就当成已经是 CommitInfo Notes 那套票序话就已经是同一句，或当成已经可以用不变量 444 代替。

## 为什么会出事

官方写：`CommitInfo.round` 是提交轮，反映上一高度块提议者决定时的那一轮。`CommitInfo.votes` 是上一验证者集合里各人的投票信息。Fields 表和 Notes 分开写。这不是已经按投票权排过，不是已经进了块，也不是已经是 Notes 里 engine/store 排序 interchangeable。看见 CommitInfo Fields 栏正式三事，不是已经 ExtendedCommitInfo.round  interchangeable，不是已经 InitChain 回包 app_hash 那种切片 interchangeable。

## 和相邻反模式

- [initapphash-sold-as-header](initapphash-sold-as-header.md) 是 InitChain 回包 app_hash 是起步应用哈希就已经是本头 AppHash，不是本页这种 CommitInfo.round 是提交轮不是已经按投票权排过。
- [cinotes-sold-as-inblock](cinotes-sold-as-inblock.md) 是 CommitInfo Notes 票序，不是本页这种 Fields 栏 votes 列表含义不是已经进了块。
- [extcommitround-sold-as-commitinfo](extcommitround-sold-as-commitinfo.md) 是 ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round，不是本页这种 Fields 栏和 Notes 分开。
