# 模式：把 InitChain 回包余栏三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**例**：[InitChain 回包 app_hash 是起步应用哈希 ≠ 已经是本头 AppHash](../../tracks/implementation/worked-example-initapphash-vs-header.md)。

## 三个名字

1. **InitChain 回包 app_hash 是起步应用哈希不是已经是本头 AppHash：** 看见回了起步哈希不是已经没有集合。
2. **Finalize 请求 hash 是这块的哈希不是已经知道本头哈希：** 看见填了 hash 不是已经跑过 Process。
3. **CommitInfo.round 是提交轮不是已经按投票权排过：** 看见填了 round 不是已经罚没。

## 为什么要分开叫

官方把 InitChain 回包 `app_hash` 是起步应用哈希、Finalize 请求 `hash` 是这块的哈希、CommitInfo `round` 是提交轮写成三件事。把它们叫成一个「看见填了 InitChain 回包余栏就已经是本头 AppHash」，会把本头 AppHash、已经知道本头哈希和票序一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain 回包余栏就已经是本头 AppHash」，先数清问的是 InitChain 回包 app_hash 是起步应用哈希不是已经是本头 AppHash、Finalize 请求 hash 是这块的哈希不是已经知道本头哈希，还是 CommitInfo.round 是提交轮不是已经按投票权排过，再决定要不要同一次发布。
