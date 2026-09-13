# 反模式：看见 ListSnapshots 请求是空请求、向应用要一份快照清单就当成已经齐 / 看见 ListSnapshots 回包 snapshots 是本地状态快照清单就当成已经是同一份 / 看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照就当成已经在拉块

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ListSnapshots。  
**例**：[ListSnapshots 请求是空请求、向应用要一份快照清单 ≠ 已经齐](../../tracks/implementation/worked-example-listsnapempty-vs-discovery.md)。

## 塌法

1. 看见 ListSnapshots 请求是空请求、向应用要一份快照清单 / 看见填了空请求，就当成已经齐，或当成已经问了邻居。
2. 看见 ListSnapshots 回包 `snapshots` 是本地状态快照清单 / 看见回了清单，就当成已经是同一份，或当成已经装完。
3. 看见 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照 / 看见用来发现，就当成已经在拉块，或当成已经齐。

## 为什么会出事

官方写：请求是空请求，向应用要一份快照清单。`snapshots` 是本地状态快照清单。Usage 是在 state sync 时发现邻居上有哪些快照。

## 和相邻反模式

- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是问了邻居就已经齐，不是本页这种 ListSnapshots 请求是空请求、向应用要一份快照清单不是已经齐。
- [listsnapusage-sold-as-bundled](listsnapusage-sold-as-bundled.md) 是 ListSnapshots Usage discover / Snapshot type 正式二事，不是本页 ListSnapshots 空请求 bundled 三事专用边界。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是全字段（含 Metadata）对上就已经装完，不是本页这种 ListSnapshots 回包 snapshots 是本地状态快照清单不是已经是同一份。
- [loadchunk-sold-as-retrieved](loadchunk-sold-as-retrieved.md) 是 LoadSnapshotChunk 用来从邻居拉快照块就已经齐，不是本页这种 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照不是已经在拉块。
