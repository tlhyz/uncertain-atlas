# 反模式：看见 Query 回包 index 是树里这个键的下标就当成已经是按键查 / 看见 Query 回包 key 是对上的那份数据的键就当成已经是 Query 高度 / 看见 Query 回包 value 是对上的那份数据的值就当成已经对上 AppHash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**例**：[Query 回包 index 是树里这个键的下标 ≠ 已经是按键查](../../tracks/implementation/worked-example-queryindex-vs-store.md)。

## 塌法

1. 看见 Query 回包 `index` 是树里这个键的下标 / 看见有下标，就当成已经是按键查，或当成已经对上 AppHash。
2. 看见 Query 回包 `key` 是对上的那份数据的键 / 看见回了键，就当成已经是 Query 高度，或当成已经新鲜。
3. 看见 Query 回包 `value` 是对上的那份数据的值 / 看见回了值，就当成已经对上 AppHash，或当成已经复制到各节点。

## 为什么会出事

官方写：`index` 是树里这个键的下标。`key` 是对上的那份数据的键。`value` 是对上的那份数据的值。

## 和相邻反模式

- [querypath-sold-as-store](querypath-sold-as-store.md) 是 path /store 就必须按键查就已经是引擎在用，不是本页这种 Query 回包 index 是树里这个键的下标不是已经是按键查。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState，不是本页这种 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash，不是本页这种 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash。
