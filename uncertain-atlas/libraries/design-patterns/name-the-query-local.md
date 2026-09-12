# 模式：把 Query 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**例**：[Query 回了 ≠ 已经复制到各节点](../../tracks/implementation/worked-example-query-vs-replicated.md)。

## 三个名字

1. **Query 回了不是已经复制到各节点：** 看见 RPC 绿了不是已经过了共识。
2. **查到了不是已经新鲜：** 看见本地有这份不是已经是当前尖。
3. **实现了 Query 不是已经是正常运转必须有：** 看见规范写了不是已经必须实现。

## 为什么要分开叫

官方把本地查询、可能读到旧的、正常运转可以不实现写成三件事。把它们叫成一个「看见查到了就已经共识」，会把 QueryState、证明和邻居过滤一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「查到了就已经共识」，先数清问的是 Query 回了不是已经复制到各节点、查到了不是已经新鲜，还是实现了 Query 不是已经是正常运转必须有，再决定要不要同一次发布。
