# 模式：把 LoadSnapshotChunk 三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[LoadSnapshotChunk 用来从邻居拉快照块 ≠ 已经齐](../../tracks/implementation/worked-example-loadchunk-vs-retrieved.md)。

## 三个名字

1. **LoadSnapshotChunk 用来从邻居拉快照块不是已经齐：** 看见在拉不是已经有了全部快照。
2. **请求用 height / format / chunk（从 0 起）认这块不是已经是同一份：** 看见填了三列不是已经装完。
3. **回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB：** 看见有上限不是已经交差。

## 为什么要分开叫

官方把 LoadSnapshotChunk 用来从邻居拉快照块、请求用 height / format / chunk（从 0 起）认这块、回包块含元数据不能超过 16 MB 写成三件事。把它们叫成一个「看见叫了 LoadSnapshotChunk 就已经齐」，会把发现清单、同一份快照和装回一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 LoadSnapshotChunk 就已经齐」，先数清问的是 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐、请求用 height / format / chunk（从 0 起）认这块不是已经是同一份，还是回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB，再决定要不要同一次发布。
