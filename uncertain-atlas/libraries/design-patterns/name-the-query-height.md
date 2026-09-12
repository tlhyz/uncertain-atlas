# 模式：把 Query 高度三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[Query 可以对当前或过去高度查 ≠ 已经是 QueryState](../../tracks/implementation/worked-example-queryheight-vs-committed.md)。

## 三个名字

1. **Query 可以对当前或过去高度查不是已经是 QueryState：** 看见能查不是已经复制到各节点。
2. **height 默认 0 回最新已提交不是已经新鲜：** 看见没填高度不是已经是握手对齐。
3. **这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash：** 看见填了高度不是已经对上 Proof。

## 为什么要分开叫

官方把 Query 可以对当前或过去高度查、`height` 默认 0 回最新已提交、这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态写成三件事。把它们叫成一个「看见能查就已经是 QueryState」，会把 Query 本地查询、本头 AppHash 和查询证明一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能查就已经是 QueryState」，先数清问的是 Query 可以对当前或过去高度查不是已经是 QueryState、height 默认 0 回最新已提交不是已经新鲜，还是这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash，再决定要不要同一次发布。
