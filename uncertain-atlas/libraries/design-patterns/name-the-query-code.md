# 模式：把 Query 回包码三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query 回包 code 是回包码 ≠ 已经过了共识](../../tracks/implementation/worked-example-querycode-vs-consensus.md)。

## 三个名字

1. **Query 回包 code 是回包码不是已经过了共识：** 看见回了码不是已经没进块。
2. **Query 回包 log 是应用日志输出不是已经新鲜：** 看见回了日志不是已经复制到各节点。
3. **Query 回包 info 是附加信息不是已经是按键查：** 看见回了信息不是已经对上 AppHash。

## 为什么要分开叫

官方把 Query 回包 `code` 是回包码、`log` 是应用日志输出、`info` 是附加信息写成三件事。把它们叫成一个「看见 Query 回了码就已经过了共识」，会把回包码、新鲜和按键查一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Query 回了码就已经过了共识」，先数清问的是 Query 回包 code 是回包码不是已经过了共识、Query 回包 log 是应用日志输出不是已经新鲜，还是 Query 回包 info 是附加信息不是已经是按键查，再决定要不要同一次发布。
