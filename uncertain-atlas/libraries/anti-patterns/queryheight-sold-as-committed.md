# 反模式：看见 Query 可以对当前或过去高度查就当成已经是 QueryState / 看见 height 默认 0 回最新已提交就当成已经新鲜 / 看见这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就当成已经印进本头 AppHash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[Query 可以对当前或过去高度查 ≠ 已经是 QueryState](../../tracks/implementation/worked-example-queryheight-vs-committed.md)。

## 塌法

1. 看见 Query 可以对当前或过去高度查 / 看见能查，就当成已经是 QueryState，或当成已经复制到各节点。
2. 看见 `height` 默认 0 回最新已提交 / 看见没填高度，就当成已经新鲜，或当成已经是握手对齐。
3. 看见这个 `height` 是含 Merkle 根的那块、代表 Height-1 提交后的状态 / 看见填了高度，就当成已经印进本头 AppHash，或当成已经对上 Proof。

## 为什么会出事

官方写：Query 查应用在当前或过去高度的数据。`height` 默认是 0，回最新已提交那块的数据。这个高度是含应用 Merkle 根的那块，这份根代表 Height-1 提交之后的状态。

## 和相邻反模式

- [query-sold-as-replicated](query-sold-as-replicated.md) 是 Query 回了就已经复制到各节点，不是本页这种 Query 可以对当前或过去高度查不是已经是 QueryState。
- [apphash-sold-as-this-block](apphash-sold-as-this-block.md) 是本头 AppHash 就已经是本高度交差，不是本页这种 height 默认 0 回最新已提交不是已经新鲜。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash，不是本页这种这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态不是已经印进本头 AppHash。
