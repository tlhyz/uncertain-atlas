# 反模式：看见 LoadSnapshotChunk 用来从邻居拉快照块就当成已经齐 / 看见请求用 height / format / chunk（从 0 起）认这块就当成已经是同一份 / 看见回包块含元数据不能超过 16 MB 就当成已经是快照报文 4 MB

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) LoadSnapshotChunk Usage。  
**例**：[LoadSnapshotChunk 用来从邻居拉快照块 ≠ 已经齐](../../tracks/implementation/worked-example-loadchunk-vs-retrieved.md)。

## 塌法

1. 看见 LoadSnapshotChunk 用来从邻居拉快照块 / 看见在拉，就当成已经齐，或当成已经有了全部快照。
2. 看见请求用 height / format / chunk（从 0 起）认这块 / 看见填了三列，就当成已经是同一份，或当成已经装完。
3. 看见回包块含元数据不能超过 16 MB / 看见有上限，就当成已经是快照报文 4 MB，或当成已经装完。

## 为什么会出事

官方写：LoadSnapshotChunk 用在 state sync 里，从邻居拉快照块。请求用这份快照的 `height`、应用自己的 `format`、从 `0` 起的块下标认这块。回包是任意格式的二进制块。块报文含元数据不能超过 16 MB，所以 10 MB 是个好起点。

## 和相邻反模式

- [loadchunk-notcomplete-sold-as-bundled](loadchunk-notcomplete-sold-as-bundled.md) 是 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐 not already complete / not already all / not already restored 正式三事（375 item 1），不是本页 bundled 全段 alone。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了就已经齐，不是本页这种 LoadSnapshotChunk 用来从邻居拉快照块不是已经齐。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是全字段（含 Metadata）对上就已经装完，不是本页这种请求用 height / format / chunk（从 0 起）认这块不是已经是同一份。
- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下就已经装完，不是本页这种回包块含元数据不能超过 16 MB 不是已经是快照报文 4 MB。
