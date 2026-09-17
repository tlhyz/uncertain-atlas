# 模式：把 Snapshot 高度余量三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types Snapshot / Query Usage。  
**例**：[Snapshot.height 是拍快照的高度（Commit 之后） ≠ 已经是 Query 高度](../../tracks/implementation/worked-example-snapheight-vs-queryh.md)。

## 三个名字

1. **Snapshot.height 是拍快照的高度（Commit 之后）不是已经是 Query 高度：** 看见填了 height 不是已经装完。
2. **Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据不是已经全字段对上：** 看见填了 metadata 不是已经增量验过。
3. **Query 可以可选回默克尔证明不是已经对上 AppHash：** 看见能回证明不是已经勾了 prove。

## 为什么要分开叫

官方把 Snapshot.height 是拍快照的高度（Commit 之后）、Snapshot.metadata 是任意应用元数据例如块哈希或其他核对数据、Query 可以可选回默克尔证明写成三件事。把它们叫成一个「看见填了 Snapshot 高度余量就已经是 Query 高度」，会把 Query 高度、全字段对上和勾了 prove 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 Snapshot 高度余量就已经是 Query 高度」，先数清问的是 Snapshot.height 是拍快照的高度（Commit 之后）不是已经是 Query 高度、Snapshot.metadata 是任意应用元数据、例如块哈希或其他核对数据不是已经全字段对上，还是 Query 可以可选回默克尔证明不是已经对上 AppHash，再决定要不要同一次发布。
