# 模式：把一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**例**：[收下一块 not already complete ≠ bundled（321）](../../tracks/implementation/worked-example-snapshotrestore-notchunkcomplete-vs-bundled.md)。

## 三个名字

1. **收下一块 不是 already complete：** 看见 ApplySnapshotChunk 收下了一块 / 回了收下这块等下一块，不是已经齐 interchangeable / 已经 chunk 齐交差 interchangeable，不是 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable。

2. **回了再拉 不是 already banned：** 看见要再拉当前这块 / 再拉前面若干块，不是已经封禁 interchangeable / 已经封禁邻居交差 interchangeable，不是 321 snapshotrestore item 3 interchangeable / 721 snapshotrestore-notresume interchangeable。

3. **能回指令 不是 already settled：** 看见能回封禁邻居 / 能回拒掉或重试这份快照，不是已经交差 interchangeable / 已经装回交差 interchangeable，不是 321 snapshotrestore item 1 interchangeable / 719 snapshotrestore-notrestored interchangeable。

官方把收下一块单句、already complete、already banned、already settled 写成三个名字。把它们叫成一个「看见 ApplySnapshotChunk 收下了一块就已经齐 interchangeable / 就已经封禁 interchangeable / 就已经交差 interchangeable」，会把 not already complete、not already banned、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一块 chunk 收下不是已经齐 not already complete / not already banned / not already settled 正式三事（321 余量），先数清问的是收下一块 是不是 already complete / 321 / snapshotrestore-sold-as-offered，是不是回了再拉 是不是 already banned，还是能回指令 是不是 already settled，再决定要不要同一次发布。321 snapshotrestore vs offer bundled unbundling 在本页 item 2 续。
