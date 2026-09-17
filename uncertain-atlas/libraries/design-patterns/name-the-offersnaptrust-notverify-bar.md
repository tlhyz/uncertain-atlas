# 模式：把 OfferSnapshot Usage Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事（483 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**例**：[OfferSnapshot Usage Any other data can be spoofed not hash comparison enough ≠ bundled（483）](../../tracks/implementation/worked-example-offersnaptrust-notverify-vs-bundled.md)。

## 三个名字

1. **Any other data can be spoofed 不是 hash / metadata 比对就够：** 看见 Any other data can be spoofed by adversaries，不是已经 Snapshot.hash / metadata / 五个字段都对上就不能伪造 interchangeable，不是 368 snapshot-sold-as-identical interchangeable / 368 hash comparison interchangeable，也不是 483 offersnaptrust bundled interchangeable / 651 offersnaptrust-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable。
2. **employ additional verification 不是 Snapshot Verification bundled：** 看见 employ additional verification schemes，不是已经 Snapshot Verification 增量验 / checksum bundled interchangeable，不是 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable，也不是 652 offersnaptrust-nottransition interchangeable / 323 transition interchangeable。
3. **avoid DoS 不是 reject_senders / refetch_chunks：** 看见 avoid denial-of-service attacks，不是已经 ApplySnapshotChunk Result REJECT_SENDER / REFETCH_CHUNK interchangeable，不是 378 applysnap bundled interchangeable / 397 chunk 栏 interchangeable / 398 Result 枚举 interchangeable。

## 为什么要分开叫

官方把 OfferSnapshot Usage Any other data can be spoofed、employ additional verification、avoid DoS 和 Snapshot 元数据/hash 比对、Snapshot Verification app requirements、ApplySnapshotChunk reject/refetch 写成三个名字。把它们叫成一个「看见 Any other data can be spoofed 就已经 hash 比对 interchangeable / 就已经增量验 chunk interchangeable / 就已经防 DoS 交差 interchangeable」，会把 not hash comparison enough、not Snapshot Verification bundled、not ApplySnapshotChunk reject refetch DoS 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事（483 余量），先数清问的是 Any other data can be spoofed 是不是 hash / metadata 比对就够 / 368 / 650，employ additional verification 是不是 Snapshot Verification bundled / 332 / 652，还是 avoid DoS 是不是 reject_senders / refetch_chunks / 378 / 401，再决定要不要同一次发布。483 offersnaptrust unbundling 在本页 item 2 续。
