# 模式：把 Query 请求 prove not already AppHash matched / not already one-layer tree / not already settled 正式三事（383 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[Query ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notapphash-vs-bundled.md)。

## 三个名字

1. **prove 不是已经对上 AppHash：** 看见勾了 prove，不是已经 325 interchangeable / 779 queryprove-notapphash interchangeable。
2. **看见勾了 prove 不是已经是一层树：** 看见能回证明，不是已经是一层树 interchangeable。
3. **看见请求了 不是已经交差：** 看见 Query prove，不是已经交差 interchangeable。

官方把 Query 请求 prove / 回包 proof_ops / 回包 height 三条核心句拆成三个名字。把它们叫成一个「看见勾了 prove 就已经对上 AppHash」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 请求 prove 正式三事（383 余量），先数清问的是是不是已经对上 AppHash / 325、是不是已经是一层树、还是看见请求了是不是已经交差，再决定要不要同一次发布。383 queryprove vs proof bundled unbundling 在本页 item 1 启动。
