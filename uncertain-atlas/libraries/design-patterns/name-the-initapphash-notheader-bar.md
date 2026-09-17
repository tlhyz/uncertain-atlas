# 模式：把 InitChain 回包 app_hash not already header AppHash / not already no set / not already settled 正式三事（392 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**例**：[InitChain ≠ bundled（392）](../../tracks/implementation/worked-example-initapphash-notheader-vs-bundled.md)。

## 三个名字

1. **app_hash 不是已经是本头 AppHash：** 看见回了起步哈希，不是已经是本头 AppHash / 755 initapphash-notheader interchangeable。
2. **看见回了起步哈希 不是已经没有集合：** 看见有起步根，不是已经 495 interchangeable。
3. **看见能回 不是已经交差：** 看见起步哈希，不是已经 147 interchangeable。

官方把 InitChain 回包 app_hash / Finalize 请求 hash / CommitInfo.round 三条核心句拆成三个名字。把它们叫成一个「看见填了 InitChain 回包余栏就已经是本头 AppHash」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 回包 app_hash 正式三事（392 余量），先数清问的是 app_hash 是不是已经是本头 AppHash、是不是已经没有集合、还是看见能回是不是已经交差 / 147，再决定要不要同一次发布。392 initapphash vs header bundled unbundling 在本页 item 1 启动。
