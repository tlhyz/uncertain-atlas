# 例：看见 Any other data can be spoofed / employ additional verification is not already hash / metadata 比对就够（368） interchangeable / Snapshot Verification bundled（332） interchangeable / reject_senders / refetch_chunks 已经防 DoS（378） interchangeable

**层次**：实现 / OfferSnapshot Usage Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事（483 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事（483 余量）/ not 651 offersnaptrust-notverify interchangeable / not 650 offersnaptrust-notmetadata interchangeable / not 652 offersnaptrust-nottransition interchangeable / not 38 apphash trust interchangeable」，不是 OfferSnapshot Usage trust 正式三事 bundled（483），也不是 Snapshot Verification 增量验（332）。不要另写怎样做增量验、怎样封邻居、怎样配轻客户端 RPC。

## 官方三件事

规范把 OfferSnapshot Usage 里 Any other data can be spoofed by adversaries, so applications should employ additional verification schemes to avoid denial-of-service attacks 和「已经是 hash / metadata 比对就够 interchangeable / 已经是 Snapshot Verification bundled interchangeable / 已经是 reject_senders / refetch_chunks 已经防 DoS interchangeable」分开写成三件独立的实现事，不是「看见 Any other data can be spoofed 就已经 hash 比对 interchangeable / 就已经增量验 chunk interchangeable / 就已经防 DoS 交差 interchangeable」一件事：

1. **看见 Any other data can be spoofed by adversaries / 看见其它数据可被伪造 is not already 已经 Snapshot.hash / metadata / 五个字段都对上就不能伪造（368） interchangeable / 已经 Snapshot 全字段（含 Metadata）对上 interchangeable / 368 snapshot-sold-as-identical interchangeable / 已经 hash / metadata 比对就够 interchangeable / 已经引擎不解释 hash 只比较 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 651 offersnaptrust-notverify interchangeable / 483 offersnaptrust interchangeable / 650 offersnaptrust-notmetadata interchangeable / 652 offersnaptrust-nottransition interchangeable，也不是已经 Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事 bundled（483 item 2 余量） interchangeable / 483 offersnaptrust item 2 interchangeable，也不是已经 Only AppHash can be trusted not hash comparison bundled（483 item 1 余量 / 650） interchangeable / 650 offersnaptrust-notmetadata interchangeable / 38 apphash-trust interchangeable / 499 offersnapusage bundled interchangeable。**  
   官方 Usage 写：Any other data can be spoofed by adversaries, so applications should employ additional verification schemes to avoid denial-of-service attacks。看见 can be spoofed，不是已经五个字段都对上就不能伪造 interchangeable——368 钉 Snapshot.hash / metadata / 五个字段，本页从 483 item 2 侧钉 not hash comparison enough 单句。看见 other data，不是已经 Only AppHash can be trusted 就代表其它字段也信 interchangeable——650 另钉 not Snapshot metadata / not hash comparison on Only AppHash 单句，本页钉 Any other data can be spoofed 单句。看见 spoofed，不是已经 ListSnapshots 回了本地清单就可信 interchangeable——395 钉本地清单栏，本页钉 can be spoofed 单句。483 offersnaptrust unbundling 在本页 item 2 续。

2. **看见 employ additional verification schemes / 看见应用还应另做验真 is not already 已经 Snapshot Verification 增量验 / checksum bundled（332） interchangeable / 已经 Snapshot Verification app requirements bundled interchangeable / 332 snapshotverify interchangeable / 已经装 chunk 过程中 Info 对了 interchangeable / 已经增量验 chunk 就等于 Usage 这句 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 651 offersnaptrust-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 3 verified AppHash at end interchangeable，也不是已经 verified AppHash automatically checked at end not Info during load bundled（483 item 3 余量 / 652） interchangeable / 652 offersnaptrust-nottransition interchangeable / 323 transition interchangeable / 485 applysnapusage verify/Info/unable interchangeable，也不是已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable / 378 applysnap bundled interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable。**  
   官方把 Usage employ additional verification 单句和 Snapshot Verification app requirements bundled 分开——483 bundled 第二件事常与 332 混成「看见 employ additional verification 就已经 Snapshot Verification 增量验 interchangeable / 就已经 checksum interchangeable」，本页钉 not Snapshot Verification bundled 单句。看见 additional verification，不是已经 Snapshot Verification 增量验 / checksum bundled（332） interchangeable——332 钉 app requirements，本页钉 Methods Usage 单句。看见 schemes，不是已经 verified AppHash automatically checked at end（483 item 3 余量 / 652） interchangeable——652 另钉 at end not Info during load，本页钉 item 2 第二件事。

3. **看见 avoid denial-of-service attacks / 看见防 DoS is not already 已经 ApplySnapshotChunk Result REJECT_SENDER / REFETCH_CHUNK 那种再拉 / 封邻居 bundled（378） interchangeable / 378 applysnap bundled interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 398 ApplySnapshotChunk Result 枚举 interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 已经 reject_senders / refetch_chunks 就等于已经防无效快照 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 651 offersnaptrust-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 1 Only AppHash can be trusted interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 401 offerafter interchangeable / 321 Offer 装完 interchangeable / 649 offersnapusage-notreject interchangeable，也不是已经 Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事 bundled（483 item 2 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable。**  
   官方把 Usage avoid DoS 单句和 ApplySnapshotChunk reject_senders / refetch_chunks bundled 分开——483 bundled 第二件事常与 378 混成「看见 avoid DoS 就已经 reject_senders / refetch_chunks interchangeable / 就已经防无效快照 interchangeable」，本页钉 not ApplySnapshotChunk reject refetch DoS 单句。看见 denial-of-service，不是已经 ApplySnapshotChunk Result REJECT_SENDER / REFETCH_CHUNK bundled（378） interchangeable——378 钉 Result 枚举与再拉，本页钉 Usage avoid DoS 单句。看见 attacks，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装，本页钉 item 2 第三件事。

怎样做增量验、怎样封邻居、怎样配轻客户端 RPC 是规范里的做法，本页不抄。OfferSnapshot Usage trust 正式三事 bundled（483）、Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash（483 item 1 余量 / 650）、verified AppHash at end not Info during load（483 item 3 余量 / 652）、Snapshot 全字段对上（368）、只有轻客户端验过的 AppHash 可信任总则（38）、Snapshot Verification app requirements（332）、Transition to Consensus（323）、OfferSnapshot 请求 bundled（396）是另外那套，本页不抄。

## 官方为什么这样拆

- **Any other data can be spoofed not hash comparison enough ≠ 368 snapshot-sold-as-identical interchangeable：** 官方把其它数据可被伪造和 Snapshot 元数据、hash 比对 分开。
- **employ additional verification not Snapshot Verification bundled ≠ 332 snapshotverify interchangeable：** 官方把 Methods Usage 侧另做验真和 app requirements 增量验 分开。
- **avoid DoS not ApplySnapshotChunk reject refetch DoS ≠ 378 applysnap interchangeable：** 官方把 Usage avoid DoS 单句和 ApplySnapshotChunk reject_senders / refetch_chunks 分开；483 offersnaptrust unbundling 续（651 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Any other data can be spoofed | 不是 hash/metadata 比对就够（368） | 不是 Only AppHash can be trusted（650） |
| employ additional verification | 不是 Snapshot Verification bundled（332） | 不是 verified AppHash at end（652） |
| avoid DoS | 不是 reject_senders / refetch_chunks（378） | 不是 Offer 收下之后（401） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS 正式三事（483 余量），必须分开 Any other data can be spoofed 是不是 hash / metadata 比对就够 interchangeable / 368 snapshot-sold-as-identical interchangeable / 650 offersnaptrust-notmetadata interchangeable、employ additional verification 是不是 Snapshot Verification bundled interchangeable / 332 snapshotverify interchangeable / 652 offersnaptrust-nottransition interchangeable、avoid DoS 是不是 reject_senders / refetch_chunks interchangeable / 378 applysnap interchangeable / 401 offerafter interchangeable。可以跳过「看见 Any other data can be spoofed 就已经 hash 比对 interchangeable / 就已经防 DoS 交差 interchangeable」。不要另写怎样做增量验。483 offersnaptrust unbundling 在本页 item 2 续。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样配轻客户端 RPC、怎样写 OfferSnapshot。
- OfferSnapshot Usage trust 正式三事 bundled。那是不变量 483。
- Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash。那是不变量 483 item 1 余量 / 650。
- verified AppHash at end not Info during load。那是不变量 483 item 3 余量 / 652。
- Snapshot 全字段对上。那是不变量 368。
- 只有轻客户端验过的 AppHash 可信任总则。那是不变量 38。
- Snapshot Verification app requirements。那是不变量 332。
- OfferSnapshot 请求 bundled。那是不变量 396。
