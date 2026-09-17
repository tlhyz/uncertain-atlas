# 模式：把 Query 回包 value not already AppHash matched / not already replicated / not already settled 正式三事（380 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query ≠ bundled（380）](../../tracks/implementation/worked-example-queryindex-notapphash-vs-bundled.md)。

## 三个名字

1. **value 不是已经对上 AppHash：** 看见回了值，不是已经 325 interchangeable / 790 queryindex-notapphash interchangeable。
2. **看见回了值 不是已经复制到各节点：** 看见有字节，不是已经 329 interchangeable。
3. **看见能读 不是已经交差：** 看见 Query value，不是已经交差 interchangeable。

官方把 Query 回包 index / key / value 三条核心句拆成三个名字。把它们叫成一个「看见 Query 回了键值就已经是按键查」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 value 正式三事（380 余量），先数清问的是是不是已经对上 AppHash / 325、是不是已经复制到各节点 / 329、还是看见能读是不是已经交差，再决定要不要同一次发布。380 queryindex vs store bundled unbundling 在本页 item 3 完成。
