# 模式：把 ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notverify-vs-bundled.md)。

## 三个名字

1. **verify each chunk 不是 Only AppHash can be trusted：** 看见 The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash`，不是已经 Only AppHash can be trusted / hash/metadata 比对就够 interchangeable，不是 483 offersnaptrust bundled interchangeable / 653 applysnapusage-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable。
2. **verify each chunk 不是 Snapshot Verification bundled：** 看见 may want to verify each chunk / incrementally against AppHash，不是已经 Snapshot Verification 增量验 / checksum bundled interchangeable，不是 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 652 offersnaptrust-nottransition interchangeable。
3. **verify each chunk 不是 Result ACCEPT 已经齐：** 看见 verify each chunk / incrementally verifying contents against AppHash，不是已经 ApplySnapshotChunk Result ACCEPT interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / 378 applysnap bundled interchangeable。

## 为什么要分开叫

官方把 ApplySnapshotChunk Usage verify each chunk、Only AppHash can be trusted、Snapshot Verification app requirements、ApplySnapshotChunk Result ACCEPT 已经齐 写成三个名字。把它们叫成一个「看见 verify each chunk 就已经 Only AppHash 可信任就交差 interchangeable / 就已经 Snapshot Verification bundled interchangeable / 就已经 Result ACCEPT 就代表已经齐 interchangeable」，会把 not Only AppHash can be trusted、not Snapshot Verification bundled、not ApplySnapshotChunk Result ACCEPT already complete 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量），先数清问的是 verify each chunk 是不是 Only AppHash can be trusted / 483 / 650 / 651，是不是 Snapshot Verification bundled / 332 / 652，还是 verify each chunk 是不是 Result ACCEPT 已经齐 / 401 / 648 / 378，再决定要不要同一次发布。485 applysnapusage unbundling 在本页 item 1 启动。
