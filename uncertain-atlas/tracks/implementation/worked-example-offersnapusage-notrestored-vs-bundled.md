# 例：看见 Upon accepting, CometBFT will retrieve and apply snapshot chunks via ApplySnapshotChunk is not already Offer 收下就已经装完（321） interchangeable / Offer 收下之后 bundled（401） interchangeable / LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable

**层次**：实现 / OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完（321）/ not Offer 收下之后 bundled（401）/ not LoadSnapshotChunk 已经齐（375）/ not 648 offersnapusage-notrestored interchangeable / not 647 offersnapusage-notlisted interchangeable / not 649 offersnapusage-notreject interchangeable / not 483 Only AppHash trusted interchangeable」，不是 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499），也不是 Offer 收下就已经装完（321）。不要另写怎样做增量验、怎样封邻居、怎样写 OfferSnapshot。

## 官方三件事

规范把 OfferSnapshot Usage 第二段 upon accepting retrieve and apply 和「已经是 Offer 装完 interchangeable / 已经是 Offer 收下之后 bundled interchangeable / 已经是 LoadSnapshotChunk 已经齐 interchangeable」分开写成三件独立的实现事，不是「看见 Accept 之后 retrieve and apply 就已经 Offer 装完 interchangeable / 就已经 Offer 收下之后 bundled interchangeable / 就已经 LoadSnapshotChunk 齐 interchangeable」一件事：

1. **看见 Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk` / 看见 Accept 之后引擎会去拉块并经 ApplySnapshotChunk 装 is not already 已经 Offer 收下就已经装完（321） interchangeable / 已经 Snapshot Restoration 装回流程 bundled interchangeable / 已经 Offer 收下就已经齐 interchangeable / 已经 Transition to Consensus 已经切进共识（323） interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 499 offersnapusage interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable，也不是已经 OfferSnapshot Usage upon accepting retrieve and apply 正式三事 bundled（499 item 2 余量） interchangeable / 499 offersnapusage item 2 interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 332 snapshotverify interchangeable / 378 applysnap interchangeable。**  
   官方 Usage 写：Upon accepting, CometBFT will retrieve and apply snapshot chunks via `ApplySnapshotChunk`。看见 upon accepting retrieve and apply，不是已经 Offer 收下就已经装完 interchangeable——321 钉 Snapshot Restoration 装回流程，本页从 499 item 2 侧钉 not Offer 装完 单句。看见 retrieve and apply via ApplySnapshotChunk，不是已经 Transition to Consensus 已经能出块 interchangeable——323 钉切进共识，本页钉 Usage upon accepting 单句。看见 accepting 后才开始拉块装块，不是已经 Offer 收下就已经齐 interchangeable——321 钉装完 bundled，本页钉 not Offer 装完 单句。499 offersnapusage unbundling 在本页 item 2 续。

2. **看见 Upon accepting retrieve and apply snapshot chunks via ApplySnapshotChunk is not already 已经 Offer 收下之后 bundled（401） interchangeable / 已经 Accept 后拉块并装三事 bundled interchangeable / 401 offerafter interchangeable / 已经 Offer 收下之后才去拉块并装 bundled 第一件事就代表已经齐 interchangeable / 已经 ApplySnapshotChunk Result ACCEPT 是这块收下了就代表已经齐 interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 3 reject in chunk response interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable / 321 offerrestored interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 398 ApplySnapshotChunk Result 枚举 interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 485 applysnapusage verify/Info/unable interchangeable。**  
   官方把 Usage upon accepting 单句和 Offer 收下之后 bundled 三事分开——499 bundled 第二件事常与 401 混成「看见 upon accepting retrieve and apply 就已经 Offer 收下之后 bundled interchangeable / 就已经 Accept 后拉块装块 interchangeable」，本页钉 not Offer 收下之后 bundled 单句。看见 retrieve and apply via ApplySnapshotChunk，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装三事 bundled，本页钉 Usage upon accepting 单句。看见 accepting 后才开始拉块，不是已经 ApplySnapshotChunk Result ACCEPT 是这块收下了就代表已经齐 interchangeable——401 钉 bundled 第三件事，本页钉 not Offer 收下之后 bundled 单句。

3. **看见 Upon accepting retrieve and apply snapshot chunks is not already 已经 LoadSnapshotChunk 用来从邻居拉快照块就已经齐（375） interchangeable / 已经 LoadSnapshotChunk height/format/chunk bundled（375） interchangeable / 已经 LoadSnapshotChunk Usage retrieve from peers bundled（501） interchangeable / 已经 Used during state sync to retrieve snapshot chunks from peers interchangeable / 501 loadsnapusage-retrieve interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 2 Upon accepting retrieve ApplySnapshotChunk interchangeable，也不是已经 ApplySnapshotChunk 请求 chunk 是 LoadSnapshotChunk 回的那块二进制内容 bundled（397） interchangeable / 397 applysnap-chunk interchangeable / 378 applysnap bundled interchangeable / 485 applysnapusage verify/Info/unable interchangeable，也不是已经 Only AppHash can be trusted（483） interchangeable / 483 offersnaptrust interchangeable / 332 snapshotverify interchangeable / 375 loadsnap bundled interchangeable。**  
   官方把 Usage upon accepting retrieve and apply 和 LoadSnapshotChunk 拉块 bundled 分开——499 bundled 第二件事常与 375 / 501 混成「看见 upon accepting retrieve and apply 就已经 LoadSnapshotChunk 齐 interchangeable / 就已经 retrieve from peers interchangeable」，本页钉 not LoadSnapshotChunk 已经齐 单句。看见 retrieve snapshot chunks，不是已经 LoadSnapshotChunk bundled（375） interchangeable——375 钉 Request/Response 栏和 Usage 拉块 bundled 三事，本页钉 Usage upon accepting retrieve 单句。看见 via ApplySnapshotChunk，不是已经 LoadSnapshotChunk Usage retrieve from peers（501） interchangeable——501 钉 LoadSnapshotChunk Methods Usage retrieve 单句，本页钉 OfferSnapshot Usage upon accepting 单句。

怎样做增量验、怎样封邻居、怎样写 OfferSnapshot 是规范里的做法，本页不抄。OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499）、bootstrap accept/reject not OfferSnapshot bundled（499 item 1 余量 / 647）、reject in chunk response not ABORT bundled（499 item 3 余量 / 649）、Offer 收下就已经装完（321）、Offer 收下之后 bundled（401）、LoadSnapshotChunk bundled（375）、LoadSnapshotChunk Usage retrieve（501）、ApplySnapshotChunk chunk 栏（397）、Only AppHash trusted（483）是另外那套，本页不抄。

## 官方为什么这样拆

- **upon accepting retrieve and apply ≠ Offer 装完 interchangeable：** 官方把 Accept 后拉块装块单句和 Snapshot Restoration 装完 bundled 分开。
- **upon accepting retrieve and apply ≠ Offer 收下之后 bundled interchangeable：** 官方把 Usage upon accepting 单句和 Offer 收下之后 bundled 三事 分开。
- **upon accepting retrieve and apply ≠ LoadSnapshotChunk 已经齐 interchangeable：** 官方把 Usage upon accepting retrieve and apply 和 LoadSnapshotChunk 拉块 bundled / retrieve Usage 分开；499 offersnapusage unbundling 续（648 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| upon accepting retrieve and apply | 不是 Offer 装完（321） | 不是 Transition to Consensus（323） |
| upon accepting retrieve and apply | 不是 Offer 收下之后 bundled（401） | 不是 ApplySnapshotChunk ACCEPT 已经齐（401） |
| upon accepting retrieve and apply | 不是 LoadSnapshotChunk 已经齐（375） | 不是 LoadSnapshotChunk Usage retrieve（501） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage upon accepting retrieve and apply not Offer 装完 / not Offer 收下之后 bundled / not LoadSnapshotChunk 正式三事（499 余量），必须分开 upon accepting retrieve and apply 是不是 Offer 装完 interchangeable / 321 offerrestored interchangeable / 323 transition interchangeable、upon accepting retrieve and apply 是不是 Offer 收下之后 bundled interchangeable / 401 offerafter interchangeable / 397 chunk 栏 interchangeable / 398 Result 枚举 interchangeable、upon accepting retrieve and apply 是不是 LoadSnapshotChunk 已经齐 interchangeable / 375 loadsnap interchangeable / 501 loadsnapusage-retrieve interchangeable / 378 applysnap interchangeable。可以跳过「看见 Accept 之后 retrieve and apply 就已经 Offer 装完 interchangeable」。不要另写怎样做增量验。499 offersnapusage unbundling 在本页 item 2 续。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 OfferSnapshot、怎样切块。
- OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled。那是不变量 499。
- bootstrap accept/reject not OfferSnapshot bundled。那是不变量 499 item 1 余量 / 647。
- reject in chunk response not ABORT bundled。那是不变量 499 item 3 余量 / 649。
- Offer 收下就已经装完。那是不变量 321。
- Offer 收下之后 bundled。那是不变量 401。
- LoadSnapshotChunk bundled。那是不变量 375。
- LoadSnapshotChunk Usage retrieve。那是不变量 501。
- Only AppHash trusted。那是不变量 483。
