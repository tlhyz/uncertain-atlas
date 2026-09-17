# 模式：把 Query 回包 height not already request height / not already fresh / not already header AppHash 正式三事（383 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[Query ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notreqh-vs-bundled.md)。

## 三个名字

1. **height 不是已经是请求高度：** 看见回了高度，不是已经是请求高度 interchangeable / 781 queryprove-notreqh interchangeable。
2. **看见回了高度 不是已经新鲜：** 看见填了回包高度，不是已经新鲜 interchangeable。
3. **看见是含 Merkle 根的那块 不是已经印进本头 AppHash：** 看见 Query height，不是已经印进本头 AppHash interchangeable。

官方把 Query 请求 prove / 回包 proof_ops / 回包 height 三条核心句拆成三个名字。把它们叫成一个「看见勾了 prove 就已经对上 AppHash」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 height 正式三事（383 余量），先数清问的是是不是已经是请求高度、是不是已经新鲜、还是看见是含 Merkle 根的那块是不是已经印进本头 AppHash，再决定要不要同一次发布。383 queryprove vs proof bundled unbundling 在本页 item 3 完成。
