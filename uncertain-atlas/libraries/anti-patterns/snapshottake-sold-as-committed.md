# 反模式：看见拍了这个高度就当成已经交差之后拍的 / 看见没停链就当成已经一致 / 看见只留最近两份就当成已经有了全部历史快照

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Taking Snapshots。  
**例**：[拍了这个高度 ≠ 已经交差之后拍的](../../tracks/implementation/worked-example-snapshot-take-vs-commit.md)。

## 塌法

1. 看见标了这个高度 / 看见拍了快照，就当成已经在交差之后拍的，或当成已经没有更高高度的数据。
2. 看见在后台拍 / 看见没停链，就当成已经隔离在单一高度，或当成已经各节点字节相同。
3. 看见只留最近两份 / 看见 Hash 对上了，就当成已经有了全部历史快照，或当成已经是同一份。

## 为什么会出事

官方写：高度必须在该高度 Commit 之后拍，且不得含更高高度。Consistent / Asynchronous / Deterministic 是三件保证。一般只留最近两份；同一份要五个字段都相同，Hash 对上不是已经是轻验 AppHash。

## 和相邻反模式

- [snapshotrestore-sold-as-offered](snapshotrestore-sold-as-offered.md) 是 Offer 收下 ≠ 已经装完，不是本页这种生产者还没交差。
- [snapshotdiscover-sold-as-listed](snapshotdiscover-sold-as-listed.md) 是 ListSnapshots 回了 ≠ 已经齐，不是本页。
- [snapshotswitch-sold-as-full-history](snapshotswitch-sold-as-full-history.md) 是切进共识 ≠ 已经有完整历史，不是本页。
