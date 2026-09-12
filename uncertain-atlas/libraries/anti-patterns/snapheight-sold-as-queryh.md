# 反模式：看见 Snapshot.height 是拍快照的高度（Commit 之后）就当成已经是 Query 高度 / 看见 Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据就当成已经全字段对上 / 看见 Query 可以可选回默克尔证明就当成已经对上 AppHash

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**例**：[Snapshot.height 是拍快照的高度（Commit 之后） ≠ 已经是 Query 高度](../../tracks/implementation/worked-example-snapheight-vs-queryh.md)。

## 塌法

1. 看见 Snapshot `height` 是拍快照的高度（Commit 之后） / 看见填了 height，就当成已经是 Query 高度，或当成已经装完。
2. 看见 Snapshot `metadata` 是任意应用元数据、例如块哈希或其他核对数据 / 看见填了 metadata，就当成已经全字段对上，或当成已经增量验过。
3. 看见 Query 可以可选回默克尔证明 / 看见能回证明，就当成已经对上 AppHash，或当成已经勾了 prove。

## 为什么会出事

官方写：`height` 是拍这份快照的高度（在 `Commit` 之后）。`metadata` 是任意应用元数据，例如 chunk 哈希或其他核对数据。Query 可以可选回默克尔证明。

## 和相邻反模式

- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是这个 height 是含 Merkle 根的那块、代表 Height-1 提交后的状态就已经印进本头 AppHash，不是本页这种 Snapshot.height 是拍快照的高度（Commit 之后）不是已经是 Query 高度。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是快照全字段（含 Metadata）对上就已经装完，不是本页这种 Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据不是已经全字段对上。
- [queryprove-sold-as-proof](queryprove-sold-as-proof.md) 是 Query 请求 prove 就已经对上 AppHash，不是本页这种 Query 可以可选回默克尔证明不是已经对上 AppHash。
