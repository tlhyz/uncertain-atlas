# 例：看见 `OfferSnapshot` is called when bootstrapping a node using state sync / application may accept or reject snapshots as appropriate is not already OfferSnapshot 请求 bundled（396） interchangeable / ListSnapshots 发现（322） interchangeable / offersnapusage bundled（499） interchangeable

**层次**：实现 / OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot 请求 bundled（396）/ not ListSnapshots 发现（322）/ not Snapshot Connection 门（334）/ not offersnapusage bundled（499）/ not 647 offersnapusage-notlisted interchangeable / not 648 offersnapusage-notrestored interchangeable / not 483 Only AppHash trusted interchangeable」，不是 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499），也不是 OfferSnapshot 请求 bundled（396）。不要另写怎样做增量验、怎样封邻居、怎样写 OfferSnapshot。

## 官方三件事

规范把 OfferSnapshot Usage 第一段 bootstrap / may accept or reject 和「已经是 OfferSnapshot 请求 bundled interchangeable / 已经是 ListSnapshots 发现 interchangeable / 已经是 offersnapusage bundled interchangeable」分开写成三件独立的实现事，不是「看见 bootstrapping state sync / may accept or reject 就已经 OfferSnapshot 请求 bundled interchangeable / 就已经 ListSnapshots 问了邻居 interchangeable / 就已经必须实现快照连接 interchangeable」一件事：

1. **看见 `OfferSnapshot` is called when bootstrapping a node using state sync. The application may accept or reject snapshots as appropriate / 看见用 state sync 引导节点时会叫 OfferSnapshot、应用可以按情况接受或拒绝快照 is not already 已经 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照 bundled（396） interchangeable / 已经 OfferSnapshot 回包 `result` 是这次 Offer 的结果 bundled（396） interchangeable / 已经 OfferSnapshot 在用 state sync 引导节点时叫 bundled（396 第三件事） interchangeable，也不是已经 FinalizeBlock When calls Commit instruct persist 正式三事 bundled（590） interchangeable / 644 fincommit-notsettled interchangeable / 645 fincommit-notpersist interchangeable / 646 fincommit-notcommitlock interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable，也不是已经 OfferSnapshot 请求栏 height / format / hash / chunks bundled（396 第一件事） interchangeable / 396 offersnap interchangeable / 398 OfferSnapshot Result 枚举 interchangeable / 400 ABORT interchangeable。**  
   官方 Usage 写：`OfferSnapshot` is called when bootstrapping a node using state sync. The application may accept or reject snapshots as appropriate。看见 bootstrapping using state sync，不是已经 OfferSnapshot 请求 bundled（396） interchangeable——396 钉 Request/Response 栏和引导时叫，本页从 499 item 1 侧钉 not OfferSnapshot bundled 单句。看见 may accept or reject as appropriate，不是已经 OfferSnapshot 回包 `result` 是这次 Offer 的结果（396 bundled 第二件事） interchangeable——396 钉 result 栏，本页钉 Usage 侧 accept/reject 语义。看见 called when bootstrapping，不是已经 Offer 收下就已经装完（321） interchangeable——321 钉 Snapshot Restoration，本页钉 bootstrap 语境单句。499 offersnapusage unbundling 在本页 item 1 启动。

2. **看见 bootstrapping state sync / may accept or reject is not already 已经 ListSnapshots 用来在 state sync 时发现邻居上有哪些快照（322） interchangeable / 已经 Snapshot Discovery 问了邻居就已经齐（322） interchangeable / 已经 ListSnapshots 空请求 bundled（395） interchangeable / 已经本地清单 interchangeable / 已经 ListSnapshots Usage discover on peers（500） interchangeable / 已经 Used during state sync to discover available snapshots on peers interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage interchangeable / 648 offersnapusage-notrestored interchangeable，也不是已经 OfferSnapshot 请求 bundled（396） interchangeable / 396 offersnap interchangeable / 322 listsnap interchangeable / 395 ListSnapshots 空请求 interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 332 snapshotverify interchangeable / 378 applysnap interchangeable。**  
   官方把 Usage bootstrap 语境和 Snapshot Discovery 分开——499 bundled 第一件事常与 322 / 395 混成「看见 bootstrapping may accept/reject 就已经 ListSnapshots 问了邻居 interchangeable / 就已经本地清单 interchangeable」，本页钉 not ListSnapshots 单句。看见 called when bootstrapping，不是已经 ListSnapshots 问了邻居就已经齐（322） interchangeable——322 钉 Snapshot Discovery app requirements，本页钉 OfferSnapshot Usage bootstrap 单句。看见 may accept or reject，不是已经 ListSnapshots 回包 snapshots 是本地状态快照清单（395） interchangeable——395 钉本地清单栏，本页钉 not ListSnapshots 单句。

3. **看见 bootstrapping state sync / may accept or reject is not already 已经四门里有 Snapshot Connection 就必须实现（334） interchangeable / 已经切进共识 interchangeable / 已经必须实现快照连接 interchangeable / 334 snapshotconn interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 2 Upon accepting retrieve ApplySnapshotChunk interchangeable / 499 offersnapusage item 3 reject in chunk response interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 615 offersnaptrust bundled interchangeable / 332 snapshotverify interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 401 offerafter interchangeable / 321 Offer 收下就已经装完 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable。**  
   官方把 Usage bootstrap may accept/reject 和 Snapshot Connection 门 / offersnapusage bundled 三事分开——499 bundled 常与 334 / 483 混成「看见 Offer 了就已经必须实现快照连接 interchangeable / 就已经 Only AppHash 可信任 interchangeable」，本页钉 not Snapshot Connection / not offersnapusage bundled 单句。看见 bootstrapping，不是已经 Snapshot Connection 门（334） interchangeable——334 钉 app requirements 必须实现快照连接，本页钉 not Snapshot Connection 单句。看见 may accept or reject，不是已经 Upon accepting retrieve and apply chunks（499 item 2 余量 / 648） interchangeable——648 另钉 Upon accepting not Offer 装完，本页钉 item 1 第三件事。

怎样做增量验、怎样封邻居、怎样写 OfferSnapshot 是规范里的做法，本页不抄。OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499）、Upon accepting retrieve ApplySnapshotChunk not Offer 装完（499 item 2 余量 / 648）、reject in chunk response not ABORT bundled（499 item 3 余量 / 649）、OfferSnapshot 请求 bundled（396）、ListSnapshots 发现（322）、Snapshot Connection 门（334）、Offer 收下之后 bundled（401）、Offer 收下就已经装完（321）、Only AppHash trusted（483）是另外那套，本页不抄。

## 官方为什么这样拆

- **bootstrapping may accept/reject ≠ OfferSnapshot 请求 bundled interchangeable：** 官方把 Usage bootstrap 语境和 Request/Response 栏 bundled 分开。
- **bootstrapping may accept/reject ≠ ListSnapshots 发现 interchangeable：** 官方把 OfferSnapshot Usage bootstrap 和 ListSnapshots / Snapshot Discovery 分开。
- **bootstrapping may accept/reject ≠ Snapshot Connection / offersnapusage bundled interchangeable：** 官方把 item 1 和 Snapshot Connection 门 / 499 bundled 三事 / item 2 / item 3 分开；499 offersnapusage unbundling 启动（647 item 1）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| bootstrapping may accept/reject | 不是 OfferSnapshot 请求 bundled（396） | 不是 ListSnapshots 发现（322） |
| bootstrapping may accept/reject | 不是 ListSnapshots / 本地清单 | 不是 Snapshot Discovery 已经齐（322） |
| bootstrapping may accept/reject | 不是 Snapshot Connection / offersnapusage bundled | 不是 Upon accepting 装完（648） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage bootstrap accept/reject not OfferSnapshot bundled / not ListSnapshots / not Snapshot Connection 正式三事（499 余量），必须分开 bootstrapping may accept/reject 是不是 OfferSnapshot 请求 bundled interchangeable / 396 offersnap interchangeable / 398 result 栏 interchangeable、bootstrapping may accept/reject 是不是 ListSnapshots 发现 interchangeable / 322 listsnap interchangeable / 395 本地清单 interchangeable / 500 discover interchangeable、bootstrapping may accept/reject 是不是 Snapshot Connection interchangeable / offersnapusage bundled interchangeable / 483 Only AppHash interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable。可以跳过「看见 bootstrapping may accept/reject 就已经 ListSnapshots 问了邻居 interchangeable」。不要另写怎样做增量验。499 offersnapusage unbundling 在本页 item 1 启动。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 OfferSnapshot、怎样切块。
- OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled。那是不变量 499。
- Upon accepting retrieve ApplySnapshotChunk not Offer 装完。那是不变量 499 item 2 余量 / 648。
- reject in chunk response not ABORT bundled。那是不变量 499 item 3 余量 / 649。
- OfferSnapshot 请求 bundled。那是不变量 396。
- ListSnapshots 发现。那是不变量 322。
- Snapshot Connection 门。那是不变量 334。
- Offer 收下之后 bundled。那是不变量 401。
- Only AppHash trusted。那是不变量 483。
