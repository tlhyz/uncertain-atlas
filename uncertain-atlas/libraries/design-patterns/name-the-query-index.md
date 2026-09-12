# 模式：把 Query 回包三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query 回包 index 是树里这个键的下标 ≠ 已经是按键查](../../tracks/implementation/worked-example-queryindex-vs-store.md)。

## 三个名字

1. **Query 回包 index 是树里这个键的下标不是已经是按键查：** 看见有下标不是已经对上 AppHash。
2. **Query 回包 key 是对上的那份数据的键不是已经是 Query 高度：** 看见回了键不是已经新鲜。
3. **Query 回包 value 是对上的那份数据的值不是已经对上 AppHash：** 看见回了值不是已经复制到各节点。

## 为什么要分开叫

官方把 Query 回包 `index` 是树里这个键的下标、`key` 是对上的那份数据的键、`value` 是对上的那份数据的值写成三件事。把它们叫成一个「看见 Query 回了键值就已经是按键查」，会把按键查、查询高度和证明对上一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Query 回了键值就已经是按键查」，先数清问的是 Query 回包 index 是树里这个键的下标不是已经是按键查、Query 回包 key 是对上的那份数据的键不是已经是 Query 高度，还是 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash，再决定要不要同一次发布。
