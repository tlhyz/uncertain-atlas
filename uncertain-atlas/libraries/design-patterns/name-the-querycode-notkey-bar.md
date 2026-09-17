# 模式：把 Query 回包 info not already key lookup / not already AppHash matched / not already settled 正式三事（384 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query ≠ bundled（384）](../../tracks/implementation/worked-example-querycode-notkey-vs-bundled.md)。

## 三个名字

1. **info 不是已经是按键查：** 看见回了信息，不是已经按键查 interchangeable / 778 querycode-notkey interchangeable。
2. **看见回了信息 不是已经对上 AppHash：** 看见有附加字段，不是已经 380 interchangeable。
3. **看见能回 不是已经交差：** 看见 Query info，不是已经交差 interchangeable。

官方把 Query 回包 code / log / info 三条核心句拆成三个名字。把它们叫成一个「看见 Query 回了码就已经过了共识」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 info 正式三事（384 余量），先数清问的是是不是已经是按键查、是不是已经对上 AppHash / 380、还是看见能回是不是已经交差，再决定要不要同一次发布。384 querycode vs consensus bundled unbundling 在本页 item 3 完成。
