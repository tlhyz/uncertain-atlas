# 模式：把 Query 回包 key not already Query height / not already fresh / not already settled 正式三事（380 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notheight-vs-bundled.md)。

## 三个名字

1. **key 不是已经是 Query 高度：** 看见回了键，不是已经 371 interchangeable / 789 queryindex-notheight interchangeable。
2. **看见回了键 不是已经新鲜：** 看见有键，不是已经新鲜 interchangeable。
3. **看见能回 不是已经交差：** 看见 Query key，不是已经交差 interchangeable。

官方把 Query 回包 index / key / value 三条核心句拆成三个名字。把它们叫成一个「看见 Query 回了键值就已经是按键查」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 key 正式三事（380 余量），先数清问的是是不是已经是 Query 高度 / 371、是不是已经新鲜、还是看见能回是不是已经交差，再决定要不要同一次发布。380 queryindex vs store bundled unbundling 在本页 item 2 续。
