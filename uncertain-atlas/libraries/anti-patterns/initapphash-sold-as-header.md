# 反模式：看见 InitChain 回包 app_hash 是起步应用哈希就当成已经是本头 AppHash / 看见 Finalize 请求 hash 是这块的哈希就当成已经知道本头哈希 / 看见 CommitInfo.round 是提交轮就当成已经按投票权排过

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**例**：[InitChain 回包 app_hash 是起步应用哈希 ≠ 已经是本头 AppHash](../../tracks/implementation/worked-example-initapphash-vs-header.md)。

## 塌法

1. 看见 InitChain 回包 `app_hash` 是起步应用哈希 / 看见回了起步哈希，就当成已经是本头 AppHash，或当成已经没有集合。
2. 看见 Finalize 请求 `hash` 是这块的哈希 / 看见填了 hash，就当成已经知道本头哈希，或当成已经跑过 Process。
3. 看见 CommitInfo `round` 是提交轮 / 看见填了 round，就当成已经按投票权排过，或当成已经罚没。

## 为什么会出事

官方写：`app_hash` 是起步应用哈希。Finalize 请求 `hash` 是这块的哈希。CommitInfo `round` 是提交轮，反映上一高度块提议者决定时的那一轮。

## 和相邻反模式

- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种 InitChain 回包 app_hash 是起步应用哈希不是已经是本头 AppHash。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是 Prepare 没有头哈希就已经知道本头，不是本页这种 Finalize 请求 hash 是这块的哈希不是已经知道本头哈希。
- [voteinfo-sold-as-rewarded](voteinfo-sold-as-rewarded.md) 是 VoteInfo 按投票权降序排就已经进了块，不是本页这种 CommitInfo.round 是提交轮不是已经按投票权排过。
