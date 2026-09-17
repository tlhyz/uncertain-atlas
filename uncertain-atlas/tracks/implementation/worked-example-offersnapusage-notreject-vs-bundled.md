# 例：看见 reject a snapshot in the chunk response / prepared to accept further OfferSnapshot calls is not already OfferSnapshot Result ABORT（400） interchangeable / ApplySnapshotChunk Result REJECT_SNAPSHOT（398） interchangeable / Offer 收下之后 bundled（401） interchangeable

**层次**：实现 / OfferSnapshot Usage reject in chunk response not ABORT / not REJECT_SNAPSHOT / not Offer 收下之后 bundled 正式三事（499 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage reject in chunk response not ABORT（400）/ not REJECT_SNAPSHOT（398）/ not Offer 收下之后 bundled（401）/ not 649 offersnapusage-notreject interchangeable / not 647 offersnapusage-notlisted interchangeable / not 648 offersnapusage-notrestored interchangeable / not 483 Only AppHash trusted interchangeable」，不是 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499），也不是 OfferSnapshot Result ABORT（400）。不要另写怎样做增量验、怎样封邻居、怎样写 OfferSnapshot。

## 官方三件事

规范把 OfferSnapshot Usage 第三段 reject in chunk response / prepared for further Offer 和「已经是 OfferSnapshot Result ABORT interchangeable / 已经是 ApplySnapshotChunk Result REJECT_SNAPSHOT interchangeable / 已经是 Offer 收下之后 bundled interchangeable」分开写成三件独立的实现事，不是「看见 reject in chunk response 就已经 ABORT interchangeable / 就已经 REJECT_SNAPSHOT interchangeable / 就已经 Offer 收下之后 bundled interchangeable」一件事：

1. **看见 The application may also choose to reject a snapshot in the chunk response, in which case it should be prepared to accept further `OfferSnapshot` calls / 看见应用也可以在装 chunk 的回包里拒掉这份、还要准备再收 OfferSnapshot is not already 已经 OfferSnapshot Result `ABORT` 那种中止装回、不再试别份（400） interchangeable / 已经 OfferSnapshot Result ABORT 中止装回 bundled interchangeable / 400 offerabort interchangeable / 已经中止装回 interchangeable / 已经不再试别份 interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 3 reject in chunk response interchangeable，也不是已经 OfferSnapshot Usage reject in chunk response not ABORT / not REJECT_SNAPSHOT / not Offer 收下之后 bundled 正式三事 bundled（499 item 3 余量） interchangeable / 499 offersnapusage item 3 interchangeable，也不是已经 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER bundled（376） interchangeable / 376 offerfmt interchangeable / 400 offerabort bundled interchangeable / 398 OfferSnapshot Result 枚举 interchangeable。**  
   官方 Usage 写：The application may also choose to reject a snapshot in the chunk response, in which case it should be prepared to accept further `OfferSnapshot` calls。看见 reject in chunk response / prepared for further OfferSnapshot calls，不是已经 OfferSnapshot Result ABORT 中止装回 interchangeable——400 钉 ABORT 中止装回、不再试别份，本页从 499 item 3 侧钉 not ABORT 单句。看见 prepared to accept further OfferSnapshot calls，不是已经 ABORT 就不再试别份 interchangeable——400 钉 ABORT 语义，本页钉 further Offer 准备单句。看见 may choose to reject in chunk response，不是已经 OfferSnapshot Result REJECT_FORMAT / REJECT_SENDER（376） interchangeable——376 钉 Offer 请求侧拒 format / 拒 sender，本页钉 Usage chunk response reject 单句。499 offersnapusage unbundling 在本页 item 3 完成。

2. **看见 reject a snapshot in the chunk response / prepared to accept further OfferSnapshot calls is not already 已经 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份换一份（398） interchangeable / 已经 ApplySnapshotChunk Result 枚举 bundled interchangeable / 398 applysnap-result interchangeable / 已经 ApplySnapshotChunk 回包 result 栏 interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 2 Upon accepting retrieve ApplySnapshotChunk interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 401 offerafter interchangeable / 401 item 2 reject in chunk response bundled interchangeable / 321 Offer 收下就已经装完 interchangeable，也不是已经 ApplySnapshotChunk Result RETRY / ACCEPT bundled（398） interchangeable / 378 applysnap bundled interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 483 Only AppHash can be trusted interchangeable。**  
   官方把 Usage reject in chunk response 单句和 ApplySnapshotChunk Result REJECT_SNAPSHOT 枚举分开——499 bundled 第三件事常与 398 混成「看见 reject in chunk response 就已经 REJECT_SNAPSHOT interchangeable / 就已经 ApplySnapshotChunk 回包 result 栏 interchangeable」，本页钉 not REJECT_SNAPSHOT 单句。看见 reject in chunk response，不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT（398） interchangeable——398 钉 Result 枚举，本页钉 Usage 侧 chunk response reject 语义。看见 prepared for further OfferSnapshot calls，不是已经 REJECT_SNAPSHOT 换一份 interchangeable——398 钉拒份换份，本页钉 further Offer 准备单句。

3. **看见 reject in chunk response / prepared for further OfferSnapshot calls is not already 已经 Offer 收下之后 bundled（401） interchangeable / 已经 Accept 后拉块并装三事 bundled interchangeable / 401 offerafter interchangeable / 已经 Offer 收下之后才去拉块并装 bundled 第二件事 bundled 就代表已经中止 interchangeable / 已经 ApplySnapshotChunk Result ACCEPT 是这块收下了就代表已经齐 interchangeable，也不是已经 OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499） interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 499 offersnapusage item 2 Upon accepting retrieve ApplySnapshotChunk interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable / 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable，也不是已经 Only AppHash can be trusted / employ additional verification（483） interchangeable / 483 offersnaptrust interchangeable / 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable。**  
   官方把 Usage reject in chunk response 单句和 Offer 收下之后 bundled 三事分开——499 bundled 第三件事常与 401 混成「看见 reject in chunk response 就已经 Offer 收下之后 bundled interchangeable / 就已经 Accept 后拉块装块 bundled interchangeable」，本页钉 not Offer 收下之后 bundled 单句。看见 may choose to reject in chunk response，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装三事 bundled，本页钉 Usage reject in chunk response 单句。看见 prepared for further OfferSnapshot calls，不是已经 Offer 收下之后 bundled 第二件事 bundled 就代表已经中止 interchangeable——401 钉 bundled 中止/拒份，本页钉 not Offer 收下之后 bundled 单句。

怎样做增量验、怎样封邻居、怎样写 OfferSnapshot 是规范里的做法，本页不抄。OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled（499）、bootstrap accept/reject not OfferSnapshot bundled（499 item 1 余量 / 647）、Upon accepting retrieve and apply not Offer 装完（499 item 2 余量 / 648）、OfferSnapshot Result ABORT（400）、ApplySnapshotChunk REJECT_SNAPSHOT（398）、Offer 收下之后 bundled（401）、Offer 收下就已经装完（321）、Only AppHash trusted（483）是另外那套，本页不抄。

## 官方为什么这样拆

- **reject in chunk response not ABORT ≠ 400 offerabort interchangeable：** 官方把 Usage chunk response reject / further Offer 和 OfferSnapshot Result ABORT 中止装回 分开。
- **reject in chunk response not REJECT_SNAPSHOT ≠ 398 applysnap-result interchangeable：** 官方把 Usage reject in chunk response 单句和 ApplySnapshotChunk Result 枚举 分开。
- **reject in chunk response not Offer 收下之后 bundled ≠ 401 offerafter interchangeable：** 官方把 Usage reject in chunk response 单句和 Offer 收下之后 bundled 三事 分开；499 offersnapusage unbundling 完成（649 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| reject in chunk response / further Offer | 不是 ABORT（400） | 不是 REJECT_FORMAT / REJECT_SENDER（376） |
| reject in chunk response | 不是 REJECT_SNAPSHOT（398） | 不是 RETRY / ACCEPT（398） |
| reject in chunk response / further Offer | 不是 Offer 收下之后 bundled（401） | 不是 Offer 装完（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage reject in chunk response not ABORT / not REJECT_SNAPSHOT / not Offer 收下之后 bundled 正式三事（499 余量），必须分开 reject in chunk response / prepared for further Offer 是不是 ABORT interchangeable / 400 offerabort interchangeable / 376 offerfmt interchangeable、reject in chunk response 是不是 REJECT_SNAPSHOT interchangeable / 398 applysnap-result interchangeable / 397 chunk 栏 interchangeable / 378 applysnap interchangeable、reject in chunk response 是不是 Offer 收下之后 bundled interchangeable / 401 offerafter interchangeable / 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable。可以跳过「看见 reject in chunk response 就已经 ABORT interchangeable / 就已经 REJECT_SNAPSHOT interchangeable」。不要另写怎样做增量验。499 offersnapusage unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样写 OfferSnapshot、怎样切块。
- OfferSnapshot Usage bootstrap accept/reject 正式三事 bundled。那是不变量 499。
- bootstrap accept/reject not OfferSnapshot bundled。那是不变量 499 item 1 余量 / 647。
- Upon accepting retrieve and apply not Offer 装完。那是不变量 499 item 2 余量 / 648。
- OfferSnapshot Result ABORT。那是不变量 400。
- ApplySnapshotChunk REJECT_SNAPSHOT。那是不变量 398。
- Offer 收下之后 bundled。那是不变量 401。
- Offer 收下就已经装完。那是不变量 321。
- Only AppHash trusted。那是不变量 483。
