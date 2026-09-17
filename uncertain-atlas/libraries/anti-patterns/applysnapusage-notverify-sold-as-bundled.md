# 反模式：把 ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量）说成已经 Only AppHash 可信任就交差 / 已经 Snapshot Verification bundled / 已经 Result ACCEPT 就代表已经齐

**层次**：实现 / 文案。  
**分类**：推断（产品）。  
**例**：[ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted ≠ bundled（485）](../../tracks/implementation/worked-example-applysnapusage-notverify-vs-bundled.md)。

## 错在哪里

把 The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash` 写成已经 Only AppHash can be trusted / hash/metadata 比对就够 interchangeable / 已经 OfferSnapshot Usage trust bundled interchangeable / 已经 483 offersnaptrust interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable；把 may want to verify each chunk / incrementally against AppHash 写成已经 Snapshot Verification 增量验 / checksum bundled interchangeable / 已经 Snapshot Verification app requirements bundled interchangeable / 已经装 chunk 过程中 Info 对了 interchangeable / 332 snapshotverify interchangeable；把 verify each chunk 写成已经 ApplySnapshotChunk Result ACCEPT interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / 378 applysnap bundled interchangeable / 397 chunk 栏 interchangeable，或已经和 485 applysnapusage bundled / 654 applysnapusage-notinfo / 655 applysnapusage-notunable / 499 offersnapusage bundled interchangeable。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量），必须分开 not Only AppHash can be trusted、not Snapshot Verification bundled、not ApplySnapshotChunk Result ACCEPT already complete 三件事，不要和 485 / 483 / 332 / 378 / 401 / 650 / 651 / 652 / 648 / 499 / 647 糊成一句。

## 和相邻反模式

- [applysnapusage-sold-as-restored](applysnapusage-sold-as-restored.md) 是 ApplySnapshotChunk Usage verify/Info/unable 专用 bundled（485），不是本页 485 item 1 单句边界。
- [offersnaptrust-sold-as-metadata](offersnaptrust-sold-as-metadata.md) 是 trust 专用 bundled（483），不是本页 not Only AppHash can be trusted 单句边界。
- [offersnaptrust-notmetadata-sold-as-bundled](offersnaptrust-notmetadata-sold-as-bundled.md) 是 483 item 1 余量 / 650 专用，不是本页 verify each chunk 单句边界。
- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是 Snapshot Verification（332）专用，不是本页 not Snapshot Verification bundled 单句边界。
- [offeraccept-sold-as-restored](offeraccept-sold-as-restored.md) 是 Offer 收下之后（401）专用，不是本页 not Result ACCEPT already complete 单句边界。
