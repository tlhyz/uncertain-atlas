# 模式：把 Finalize 请求 hash not already known header hash / not already Process / not already settled 正式三事（392 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**例**：[Finalize ≠ bundled（392）](../../tracks/implementation/worked-example-initapphash-notknownhash-vs-bundled.md)。

## 三个名字

1. **hash 不是已经知道本头哈希：** 看见填了 hash，不是已经 311 interchangeable / 756 initapphash-notknownhash interchangeable。
2. **看见填了 hash 不是已经跑过 Process：** 看见有块哈希，不是已经知道本头 interchangeable。
3. **看见能填 不是已经交差：** 看见 Finalize 请求 hash，不是已经交差 interchangeable。

官方把 InitChain 回包 app_hash / Finalize 请求 hash / CommitInfo.round 三条核心句拆成三个名字。把它们叫成一个「看见填了 InitChain 回包余栏就已经是本头 AppHash」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 请求 hash 正式三事（392 余量），先数清问的是 hash 是不是已经知道本头哈希 / 311、是不是已经跑过 Process、还是看见能填是不是已经交差，再决定要不要同一次发布。392 initapphash vs header bundled unbundling 在本页 item 2 续。
