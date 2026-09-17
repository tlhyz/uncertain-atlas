# 例：看见 verify each chunk / incrementally against AppHash is not already Only AppHash can be trusted（483） interchangeable / Snapshot Verification bundled（332） interchangeable / ApplySnapshotChunk Result ACCEPT already complete（401） interchangeable

**层次**：实现 / ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量）/ not 653 applysnapusage-notverify interchangeable / not 654 applysnapusage-notinfo interchangeable / not 655 applysnapusage-notunable interchangeable / not 485 applysnapusage bundled interchangeable」，不是 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485），也不是 OfferSnapshot Usage trust 正式三事 bundled（483）。不要另写怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。

## 官方三件事

规范把 ApplySnapshotChunk Usage 里 The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash` 和「已经是 Only AppHash can be trusted（483）那种 hash/metadata 比对就够 interchangeable / 已经是 Snapshot Verification 增量验 chunk（332） app requirements bundled interchangeable / 已经是 ApplySnapshotChunk Result ACCEPT（401）就已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 verify each chunk 就已经 Only AppHash 可信任就交差 interchangeable / 就已经 Snapshot Verification bundled interchangeable / 就已经 Result ACCEPT 就代表已经齐 interchangeable」一件事：

1. **看见 The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash` / 看见应用可能想验每一块、例如在 Metadata 里挂 chunk hash 或按 AppHash 增量验 is not already 已经 OfferSnapshot Usage trust（483）那种 Only AppHash can be trusted / hash/metadata 比对就够 interchangeable / 483 offersnaptrust interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable / 652 offersnaptrust-nottransition interchangeable / 38 apphash-trust interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 653 applysnapusage-notverify interchangeable / 485 applysnapusage interchangeable / 654 applysnapusage-notinfo interchangeable / 655 applysnapusage-notunable interchangeable，也不是已经 verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事 bundled（485 item 1 余量） interchangeable / 485 applysnapusage item 1 interchangeable，也不是已经 Any other data can be spoofed not hash comparison enough bundled（483 item 2 余量 / 651） interchangeable / 368 snapshot-sold-as-identical interchangeable / 499 offersnapusage bundled interchangeable。**  
   官方 Usage 写：The application may want to verify each chunk, e.g. by attaching chunk hashes in `Snapshot.Metadata` and/or incrementally verifying contents against `AppHash`。看见 may want to verify each chunk，不是已经 Only AppHash can be trusted 就代表不用再验 interchangeable——483 钉 trust 总则，本页从 485 item 1 侧钉 not Only AppHash can be trusted 单句。看见 Metadata / incrementally against AppHash，不是已经 hash/metadata 比对就够 interchangeable——651 另钉 Any other data can be spoofed not hash comparison enough，本页钉 verify each chunk 单句。看见 incrementally verifying contents against AppHash，不是已经 OfferSnapshot Usage trust bundled（483） interchangeable——650 另钉 not Snapshot metadata on Only AppHash，本页钉 item 1 第一件事。485 applysnapusage unbundling 在本页 item 1 启动。

2. **看见 may want to verify each chunk / attaching chunk hashes in `Snapshot.Metadata` / incrementally verifying contents against `AppHash` is not already 已经 Snapshot Verification 增量验 / checksum bundled（332） interchangeable / 332 snapshotverify interchangeable / 已经装 chunk 过程中 Info 对了 interchangeable / 已经 Snapshot Verification app requirements bundled interchangeable / 已经增量验 chunk 就等于 Methods Usage 这句 interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable / 655 applysnapusage-notunable interchangeable / 485 applysnapusage item 2 all chunks accepted 后 Info interchangeable / 485 applysnapusage item 3 unable to retrieve next chunk interchangeable，也不是已经 verified AppHash automatically checked at end not Info during load bundled（483 item 3 余量 / 652） interchangeable / 652 offersnaptrust-nottransition interchangeable / 323 transition interchangeable / 378 applysnap bundled interchangeable，也不是已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 401 offerafter interchangeable。**  
   官方把 Methods Usage verify each chunk 单句和 Snapshot Verification app requirements bundled 分开——485 bundled 第一件事常与 332 混成「看见 verify each chunk 就已经 Snapshot Verification 增量验 interchangeable / 就已经 checksum interchangeable / 就已经装 chunk 过程中 Info 对了 interchangeable」，本页钉 not Snapshot Verification bundled 单句。看见 additional verification against AppHash，不是已经 Snapshot Verification 增量验 / checksum bundled（332） interchangeable——332 钉 app requirements，本页钉 Methods ApplySnapshotChunk Usage 单句。看见 Metadata chunk hashes，不是已经 verified AppHash automatically checked at end（483 item 3 余量 / 652） interchangeable——652 另钉 at end not Info during load，本页钉 item 1 第二件事。

3. **看见 verify each chunk / incrementally verifying contents against `AppHash` is not already 已经 ApplySnapshotChunk Result ACCEPT（401）就已经齐 interchangeable / 401 offerafter interchangeable / 已经 ApplySnapshotChunk Result ACCEPT 是这块收下了就代表已经齐 interchangeable / 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable / 655 applysnapusage-notunable interchangeable / 485 applysnapusage item 2 all chunks accepted 后 Info interchangeable / 485 applysnapusage item 3 unable to retrieve next chunk interchangeable，也不是已经 OfferSnapshot Usage upon accepting retrieve and apply bundled（499 item 2 余量 / 648） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable，也不是已经 verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事 bundled（485 item 1 余量） interchangeable / 378 applysnap bundled interchangeable / 397 chunk 栏 interchangeable / 398 Result 枚举 interchangeable。**  
   官方把 Usage verify each chunk 单句和 ApplySnapshotChunk Result ACCEPT 已经齐 bundled 分开——485 bundled 第一件事常与 401 混成「看见 verify each chunk 就已经 Result ACCEPT 就代表已经齐 interchangeable / 就已经 Offer 收下之后 bundled interchangeable」，本页钉 not ApplySnapshotChunk Result ACCEPT already complete 单句。看见 may want to verify each chunk，不是已经 ApplySnapshotChunk Result ACCEPT（401）就已经齐 interchangeable——401 钉 Accept 后拉块并装，本页钉 verify each chunk 单句。看见 incrementally against AppHash，不是已经 Offer 收下之后 bundled（401） interchangeable——648 另钉 upon accepting not Offer 装完，本页钉 item 1 第三件事。

怎样做增量验、怎样写 Metadata chunk hash、怎样 reset 是规范里的做法，本页不抄。ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485）、all chunks accepted 后 Info not Info during load（485 item 2 余量 / 654）、unable to retrieve next chunk not refetch/reject_senders（485 item 3 余量 / 655）、OfferSnapshot Usage trust 正式三事 bundled（483）、Snapshot Verification app requirements（332）、ApplySnapshotChunk 再拉（378）、Offer 收下之后拉块并装（401）、Offer 装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **verify each chunk not Only AppHash can be trusted ≠ 483 offersnaptrust interchangeable：** 官方把 Methods Usage 侧可选逐块验和 OfferSnapshot trust 总则分开。
- **verify each chunk not Snapshot Verification bundled ≠ 332 snapshotverify interchangeable：** 官方把 ApplySnapshotChunk Usage verify each chunk 单句和 app requirements 增量验 bundled 分开。
- **verify each chunk not ApplySnapshotChunk Result ACCEPT already complete ≠ 401 offerafter interchangeable：** 官方把 Usage verify each chunk 单句和 Result ACCEPT 已经齐 bundled 分开；485 applysnapusage unbundling 启动（653 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| verify each chunk / incrementally against AppHash | 不是 Only AppHash can be trusted（483） | 不是 hash/metadata 比对就够（651） |
| verify each chunk / Metadata chunk hashes | 不是 Snapshot Verification bundled（332） | 不是 verified AppHash at end（652） |
| verify each chunk / incrementally against AppHash | 不是 Result ACCEPT 已经齐（401） | 不是 upon accepting retrieve and apply（648） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage verify each chunk not Only AppHash can be trusted / not Snapshot Verification bundled / not ApplySnapshotChunk Result ACCEPT already complete 正式三事（485 余量），必须分开 verify each chunk 是不是 Only AppHash can be trusted interchangeable / 483 offersnaptrust interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable、verify each chunk 是不是 Snapshot Verification bundled interchangeable / 332 snapshotverify interchangeable / 652 offersnaptrust-nottransition interchangeable、verify each chunk 是不是 Result ACCEPT 已经齐 interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable / 378 applysnap interchangeable。可以跳过「看见 verify each chunk 就已经 Only AppHash 可信任就交差 interchangeable / 就已经增量验 chunk interchangeable」。不要另写怎样做增量验。485 applysnapusage unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。
- ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled。那是不变量 485。
- all chunks accepted 后 Info not Info during load。那是不变量 485 item 2 余量 / 654。
- unable to retrieve next chunk not refetch/reject_senders。那是不变量 485 item 3 余量 / 655。
- OfferSnapshot Usage trust 正式三事 bundled。那是不变量 483。
- Snapshot Verification app requirements。那是不变量 332。
- ApplySnapshotChunk 再拉 refetch/reject_senders。那是不变量 378。
- Offer 收下之后拉块并装。那是不变量 401。
- Offer 装完。那是不变量 321。
