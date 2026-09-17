# 例：看见 Only AppHash can be trusted, as it has been verified by the light client is not already Snapshot 字段都可信（368） interchangeable / hash 比对就够 interchangeable / OfferSnapshot 请求 app_hash 填了 interchangeable

**层次**：实现 / OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量）/ not 650 offersnaptrust-notmetadata interchangeable / not 651 offersnaptrust-notverify interchangeable / not 652 offersnaptrust-nottransition interchangeable / not 38 apphash trust interchangeable」，不是 OfferSnapshot Usage trust 正式三事 bundled（483），也不是 Snapshot 全字段对上（368）。不要另写怎样做增量验、怎样封邻居、怎样配轻客户端 RPC。

## 官方三件事

规范把 OfferSnapshot Usage 里 Only `AppHash` can be trusted, as it has been verified by the light client 和「已经是 Snapshot 字段都可信 interchangeable / 已经是 hash 比对就够 interchangeable / 已经是 OfferSnapshot 请求 app_hash 填了 interchangeable」分开写成三件独立的实现事，不是「看见 Only AppHash can be trusted 就已经 Snapshot.hash / metadata / 五个字段都可信 interchangeable / 就已经 hash 比对 interchangeable / 就已经 Offer 了 AppHash interchangeable」一件事：

1. **看见 Only `AppHash` can be trusted, as it has been verified by the light client / 看见只有 AppHash 可信任、且已由轻客户端验过 is not already 已经 Snapshot.hash / metadata / 五个字段都对上就可信（368） interchangeable / 已经 Snapshot 全字段（含 Metadata）对上 interchangeable / 368 snapshot-sold-as-identical interchangeable / 已经 ListSnapshots 回了本地清单就可信 interchangeable / 395 本地清单 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 650 offersnaptrust-notmetadata interchangeable / 483 offersnaptrust interchangeable / 651 offersnaptrust-notverify interchangeable / 652 offersnaptrust-nottransition interchangeable，也不是已经 Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事 bundled（483 item 1 余量） interchangeable / 483 offersnaptrust item 1 interchangeable，也不是已经只有轻客户端验过的 AppHash 可信任总则 bundled（38） interchangeable / 38 apphash-trust interchangeable / 332 snapshotverify interchangeable / 499 offersnapusage bundled interchangeable。**  
   官方 Usage 写：Only `AppHash` can be trusted, as it has been verified by the light client。看见 only AppHash，不是已经 Snapshot 全字段（含 Metadata）对上 interchangeable——368 钉 Snapshot.hash / metadata / 五个字段，本页从 483 item 1 侧钉 not Snapshot metadata 单句。看见 light client verified，不是已经 ListSnapshots 回了本地清单就可信 interchangeable——395 钉本地清单栏，本页钉 Only AppHash 单句。看见 can be trusted，不是已经只有轻客户端验过的 AppHash 可信任总则 bundled（38） interchangeable——38 钉总则 bundled，本页钉 Methods Usage Only AppHash 单句。483 offersnaptrust unbundling 在本页 item 1 启动。

2. **看见 Only AppHash can be trusted / light client verified is not already 已经引擎不解释 hash 只比较（368） interchangeable / 已经 hash 比对就等于轻验 interchangeable / 已经 hash / metadata 对齐 interchangeable / 368 snapshot-sold-as-identical interchangeable / 已经 Snapshot.hash 对上 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 2 Any other data can be spoofed interchangeable，也不是已经 Any other data can be spoofed / employ additional verification not hash comparison bundled（483 item 2 余量 / 651） interchangeable / 651 offersnaptrust-notverify interchangeable / 332 snapshotverify interchangeable / 378 applysnap bundled interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 396 offersnap interchangeable / 398 result 栏 interchangeable / 647 offersnapusage-notlisted interchangeable。**  
   官方把 Usage Only AppHash 单句和引擎 hash 比较 bundled 分开——483 bundled 第一件事常与 368 混成「看见 Only AppHash can be trusted 就已经 hash 比对 interchangeable / 就已经 metadata 对齐 interchangeable」，本页钉 not hash comparison 单句。看见 light client verified，不是已经引擎不解释 hash 只比较 interchangeable——368 钉 hash 比对，本页钉 Only AppHash / light client verified 单句。看见 only AppHash，不是已经 hash / metadata 比对就够 interchangeable——651 另钉 not hash comparison enough / not 332 verify，本页钉 item 1 第二件事。

3. **看见 Only AppHash can be trusted is not already 已经 OfferSnapshot 请求 `app_hash` 填了（396） interchangeable / 已经 OfferSnapshot 请求栏 height / format / hash / chunks bundled（396） interchangeable / 396 offersnap interchangeable / 已经 OfferSnapshot 回包 result 栏 interchangeable / 398 OfferSnapshot Result 枚举 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 3 verified AppHash at end interchangeable，也不是已经 verified AppHash automatically checked at end not Info during load bundled（483 item 3 余量 / 652） interchangeable / 652 offersnaptrust-nottransition interchangeable / 323 transition interchangeable / 332 snapshotverify interchangeable / 401 offerafter interchangeable，也不是已经 Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事 bundled（483 item 1 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable。**  
   官方把 Usage Only AppHash 单句和 OfferSnapshot 请求 app_hash 栏分开——483 bundled 第一件事常与 396 混成「看见 Only AppHash can be trusted 就已经 OfferSnapshot 请求 app_hash 填了 interchangeable / 就已经验完 interchangeable」，本页钉 not OfferSnapshot app_hash 单句。看见 can be trusted，不是已经 OfferSnapshot 请求 bundled（396） interchangeable——396 钉 Request/Response 栏，本页钉 Usage Only AppHash 单句。看见 light client verified，不是已经 verified AppHash automatically checked at end（483 item 3 余量 / 652） interchangeable——652 另钉 at end not Info during load，本页钉 item 1 第三件事。

怎样做增量验、怎样封邻居、怎样配轻客户端 RPC 是规范里的做法，本页不抄。OfferSnapshot Usage trust 正式三事 bundled（483）、Any other data can be spoofed not hash comparison enough（483 item 2 余量 / 651）、verified AppHash at end not Info during load（483 item 3 余量 / 652）、Snapshot 全字段对上（368）、只有轻客户端验过的 AppHash 可信任总则（38）、Snapshot Verification（332）、Transition to Consensus（323）、OfferSnapshot 请求 bundled（396）是另外那套，本页不抄。

## 官方为什么这样拆

- **Only AppHash can be trusted not Snapshot metadata ≠ 368 snapshot-sold-as-identical interchangeable：** 官方把轻客户端验过的 AppHash 和 Snapshot 元数据、全字段对上 分开。
- **Only AppHash can be trusted not hash comparison ≠ 368 hash 比对 = 轻验 interchangeable：** 官方把 Usage Only AppHash 单句和引擎 hash 比较 分开。
- **Only AppHash can be trusted not OfferSnapshot app_hash ≠ 396 offersnap interchangeable：** 官方把 Usage Only AppHash 单句和 OfferSnapshot 请求 app_hash 栏 分开；483 offersnaptrust unbundling 启动（650 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Only AppHash can be trusted | 不是 Snapshot metadata（368） | 不是 ListSnapshots 本地清单（395） |
| Only AppHash can be trusted | 不是 hash 比对 = 轻验（368） | 不是 Snapshot Verification（332） |
| Only AppHash can be trusted | 不是 OfferSnapshot app_hash（396） | 不是 verified AppHash at end（652） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash 正式三事（483 余量），必须分开 Only AppHash can be trusted 是不是 Snapshot metadata interchangeable / 368 snapshot-sold-as-identical interchangeable / 395 本地清单 interchangeable、Only AppHash can be trusted 是不是 hash 比对 interchangeable / 368 hash comparison interchangeable / 651 offersnaptrust-notverify interchangeable / 332 snapshotverify interchangeable、Only AppHash can be trusted 是不是 OfferSnapshot app_hash interchangeable / 396 offersnap interchangeable / 398 result 栏 interchangeable / 652 offersnaptrust-nottransition interchangeable。可以跳过「看见 Only AppHash can be trusted 就已经 Snapshot.hash / metadata 可信 interchangeable」。不要另写怎样做增量验。483 offersnaptrust unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样配轻客户端 RPC、怎样写 OfferSnapshot。
- OfferSnapshot Usage trust 正式三事 bundled。那是不变量 483。
- Any other data can be spoofed not hash comparison enough。那是不变量 483 item 2 余量 / 651。
- verified AppHash at end not Info during load。那是不变量 483 item 3 余量 / 652。
- Snapshot 全字段对上。那是不变量 368。
- 只有轻客户端验过的 AppHash 可信任总则。那是不变量 38。
- Snapshot Verification。那是不变量 332。
- OfferSnapshot 请求 bundled。那是不变量 396。
