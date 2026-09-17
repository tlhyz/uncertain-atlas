# 例：看见 OfferSnapshot is called when bootstrapping a node using state sync / application may accept or reject snapshots as appropriate 不是已经 OfferSnapshot 请求 bundled（396） interchangeable；看见 Upon accepting CometBFT will retrieve and apply snapshot chunks via ApplySnapshotChunk 不是已经 Offer 收下就已经装完（321） interchangeable；看见 reject a snapshot in the chunk response / prepared to accept further OfferSnapshot calls 不是已经 Offer 收下之后 bundled（401） interchangeable

**层次**：实现 / OfferSnapshot Usage bootstrap accept/reject 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「bootstrapping state sync / may accept or reject 不是 OfferSnapshot 请求 bundled interchangeable / Upon accepting retrieve and apply chunks 不是 Offer 收下就已经装完 interchangeable / reject in chunk response prepared for further Offer 不是 Offer 收下之后 bundled interchangeable」，不是 OfferSnapshot Usage trust 正式三事 part 2（483），也不是 OfferSnapshot 请求 bundled（396）。不要另写怎样做增量验、怎样封邻居、怎样写 OfferSnapshot。

## 官方三件事

规范把 OfferSnapshot Usage 第一段核心英文句写成三件独立的实现事，不是「看见 Offer 了就已经本地清单 interchangeable、已经装完、已经必须实现快照连接」一件事：

1. **看见 `OfferSnapshot` is called when bootstrapping a node using state sync. The application may accept or reject snapshots as appropriate / 看见用 state sync 引导节点时会叫 OfferSnapshot、应用可以按情况接受或拒绝快照 不是已经 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照 bundled（396） interchangeable，也不是已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照（322） interchangeable，也不是已经四门里有 Snapshot Connection 就必须实现（334） interchangeable，也不是已经切进共识 interchangeable。**  
   官方 Usage 写：`OfferSnapshot` is called when bootstrapping a node using state sync. The application may accept or reject snapshots as appropriate。看见 bootstrapping using state sync，不是已经 OfferSnapshot 在用 state sync 引导节点时叫（396 bundled 第三件事） interchangeable——396 钉 Request/Response 栏和引导时叫，本页钉 Methods Usage bootstrap 语境和 may accept or reject。看见 may accept or reject as appropriate，不是已经 OfferSnapshot 回包 `result` 是这次 Offer 的结果（396 bundled 第二件事） interchangeable——396 钉 result 栏，本页钉 Usage 侧 accept/reject 语义。看见 called when bootstrapping，不是已经 ListSnapshots 问了邻居就已经齐（322） interchangeable——322 钉 Snapshot Discovery，本页钉 OfferSnapshot Usage bootstrap 单句。
2. **看见 Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk` / 看见 Accept 之后引擎会去拉块并经 ApplySnapshotChunk 装 不是已经 Offer 收下就已经装完（321） interchangeable，也不是已经 Offer 收下之后 bundled（401）第一件事 bundled 就代表已经齐 interchangeable，也不是已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable。**  
   官方 Usage 写：Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk`。看见 upon accepting retrieve and apply，不是已经 Offer 收下就已经装完 interchangeable——321 钉 Snapshot Restoration 装回流程，本页钉 Methods Usage upon accepting 单句。看见 retrieve and apply via ApplySnapshotChunk，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装三事 bundled，本页钉 Usage upon accepting 单句。看见 accepting 后才开始拉块，不是已经 ListSnapshots 回了本地清单就可信 interchangeable。
3. **看见 The application may also choose to reject a snapshot in the chunk response, in which case it should be prepared to accept further `OfferSnapshot` calls / 看见应用也可以在装 chunk 的回包里拒掉这份、还要准备再收 OfferSnapshot 不是已经 OfferSnapshot Result `ABORT` 那种中止装回、不再试别份（400） interchangeable，也不是已经 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份换一份（398） interchangeable，也不是已经 Offer 收下之后 bundled（401）第二件事 bundled 就代表已经中止 interchangeable，也不是已经 Only AppHash can be trusted / employ additional verification（483） interchangeable。**  
   官方 Usage 写：The application may also choose to reject a snapshot in the chunk response, in which case it should be prepared to accept further `OfferSnapshot` calls。看见 reject in chunk response，不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT（398） interchangeable——398 钉 Result 枚举，本页钉 Usage 侧 chunk response reject 语义。看见 prepared to accept further OfferSnapshot calls，不是已经 OfferSnapshot Result ABORT（400） interchangeable——400 钉 ABORT 中止，本页钉 further Offer 准备。看见 may choose to reject，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 bundled 三事，本页钉 Usage reject in chunk response 单句。

怎样做增量验、怎样封邻居、怎样写 OfferSnapshot 是规范里的做法，本页不抄。OfferSnapshot 请求 bundled（396）、Offer 收下之后 bundled（401）、Offer 收下就已经装完（321）、ListSnapshots 发现（322）、Snapshot Connection 门（334）、OfferSnapshot Result ABORT（400）、ApplySnapshotChunk REJECT_SNAPSHOT（398）、OfferSnapshot Usage trust（483）是另外那套，本页不抄。

## 官方为什么这样拆

- **bootstrapping state sync / may accept or reject ≠ OfferSnapshot 请求 bundled interchangeable：** 官方把 Usage bootstrap 语境和 Request/Response 栏 bundled 分开。
- **Upon accepting retrieve and apply chunks ≠ Offer 收下就已经装完 interchangeable：** 官方把 Accept 后拉块装块单句和装完 bundled 分开。
- **reject in chunk response / prepared for further Offer ≠ Offer 收下之后 bundled interchangeable：** 官方把 chunk response reject 单句和 bundled 中止/拒份 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| bootstrapping state sync / may accept or reject | 不是 OfferSnapshot 请求 bundled（396） | 不是 ListSnapshots 发现（322） |
| Upon accepting retrieve and apply chunks | 不是 Offer 收下就已经装完（321） | 不是 Offer 收下之后 bundled（401） |
| reject in chunk response / further Offer | 不是 Offer 收下之后 bundled（401） | 不是 REJECT_SNAPSHOT（398） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject 正式三事，必须分开 bootstrapping state sync / may accept or reject 是不是 OfferSnapshot 请求 bundled interchangeable / 已经本地清单 / 已经必须实现快照连接、Upon accepting retrieve and apply chunks 是不是 Offer 收下就已经装完 interchangeable / 已经齐、reject in chunk response prepared for further Offer 是不是 Offer 收下之后 bundled interchangeable / 已经 ABORT / 已经 REJECT_SNAPSHOT。可以跳过「看见 Offer 了就已经本地清单 interchangeable、已经装完」。不要另写怎样做增量验、怎样封邻居。499 offersnapusage unbundling 在本页 item 1 启动；精读 [`worked-example-offersnapusage-notlisted-vs-bundled.md`](worked-example-offersnapusage-notlisted-vs-bundled.md)（不变量 647 item 1）；续 [`worked-example-offersnapusage-notrestored-vs-bundled.md`](worked-example-offersnapusage-notrestored-vs-bundled.md)（不变量 648 item 2）。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 OfferSnapshot、怎样切块。
- OfferSnapshot 请求 bundled。那是不变量 396。
- Offer 收下之后 bundled。那是不变量 401。
- Offer 收下就已经装完。那是不变量 321。
- ListSnapshots 发现。那是不变量 322。
- Snapshot Connection 门。那是不变量 334。
- OfferSnapshot Usage trust。那是不变量 483。
