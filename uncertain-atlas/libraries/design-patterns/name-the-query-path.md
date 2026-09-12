# 模式：把 Query 路径三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 ≠ 已经是 Query 高度](../../tracks/implementation/worked-example-querypath-vs-store.md)。

## 三个名字

1. **data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度：** 看见填了 data 不是已经新鲜。
2. **path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用：** 看见写了 /store 不是已经是过滤。
3. **规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有：** 看见写了类型路径不是已经复制到各节点。

## 为什么要分开叫

官方把 data 按 URI 查询分量解释、path 按 URI 路径解释且 /store 必须按键查、建议允许按类型查写成三件事。把它们叫成一个「看见能带 data / path 就已经是 Query 高度」，会把 Query 高度、邻居过滤和本地查询一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能带 data / path 就已经是 Query 高度」，先数清问的是 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度、path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用，还是规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有，再决定要不要同一次发布。
