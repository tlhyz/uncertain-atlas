# 例：看见 unable to retrieve next chunk / reject via OfferSnapshot / reset and accept or abort is not already refetch/reject_senders（378） interchangeable / REJECT_SNAPSHOT bundled（398） interchangeable / already matched LastBlockAppHash（332） interchangeable

**层次**：实现 / ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量）/ not 655 applysnapusage-notunable interchangeable / not 653 applysnapusage-notverify interchangeable / not 654 applysnapusage-notinfo interchangeable / not 485 applysnapusage bundled interchangeable」，不是 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485），也不是 ApplySnapshotChunk 再拉 refetch/reject_senders（378）。不要另写怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。

## 官方三件事

规范把 ApplySnapshotChunk Usage 里 If CometBFT is unable to retrieve the next chunk after some time … it will reject the snapshot and try a different one via `OfferSnapshot`. The application should be prepared to reset and accept it or abort as appropriate 和「已经是 refetch_chunks / reject_senders（378） interchangeable / 已经是 ApplySnapshotChunk Result REJECT_SNAPSHOT（398） bundled interchangeable / 已经是装完又对上 LastBlockAppHash（332） interchangeable」分开写成三件独立的实现事，不是「看见 unable to retrieve next chunk 就已经 refetch 就齐 interchangeable / 就已经 REJECT_SNAPSHOT 回包 interchangeable / 就已经 reset 就代表装完 interchangeable」一件事：

1. **看见 If CometBFT is unable to retrieve the next chunk after some time (e.g. because no suitable peers are available) … / 看见拉不到下一块 is not already 已经 refetch_chunks / reject_senders（378）那种再拉就齐 interchangeable / 378 applysnap interchangeable / 397 ApplySnapshotChunk chunk 栏 interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable / 已经 ApplySnapshotChunk 再拉 bundled interchangeable / 已经 refetch 不论 result 都再拉 interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 655 applysnapusage-notunable interchangeable / 485 applysnapusage interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable，也不是已经 unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事 bundled（485 item 3 余量） interchangeable / 485 applysnapusage item 3 interchangeable，也不是已经 ApplySnapshotChunk Result REFETCH / REJECT_SENDER bundled（398） interchangeable / 398 applysnap-result interchangeable / 649 offersnapusage-notreject interchangeable / 501 loadsnapusage-retrieve interchangeable。**  
   官方 Usage 写：If CometBFT is unable to retrieve the next chunk after some time (e.g. because no suitable peers are available), it will reject the snapshot and try a different one via `OfferSnapshot`。看见 unable to retrieve next chunk，不是已经 refetch_chunks 不论 result 都再拉 interchangeable——378 钉应用下指令再拉/封邻居，本页从 485 item 3 侧钉 not refetch/reject_senders 单句。看见 after some time / no suitable peers，不是已经 ApplySnapshotChunk 再拉 bundled（378） interchangeable——378 钉 refetch/reject_senders 应用指令，本页钉引擎拉不到下一块时的换快照路径。看见 reject the snapshot and try a different one via OfferSnapshot，不是已经 refetch 就齐 interchangeable——378 钉再拉，本页钉 item 3 第一件事。485 applysnapusage unbundling 在本页 item 3 完成。

2. **看见 reject the snapshot and try a different one via `OfferSnapshot` / 看见经 OfferSnapshot 换一份 is not already 已经 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份换一份（398） interchangeable / 398 applysnap-result interchangeable / 397 chunk 栏 interchangeable / 已经 ApplySnapshotChunk 回包 result 栏 interchangeable / 649 offersnapusage-notreject interchangeable / 649 offersnapusage-notreject item 2 not REJECT_SNAPSHOT interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 655 applysnapusage-notunable interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable / 485 applysnapusage item 1 verify each chunk interchangeable / 485 applysnapusage item 2 all chunks accepted 后 Info interchangeable，也不是已经 unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事 bundled（485 item 3 余量） interchangeable / 400 offerabort interchangeable / 376 offerfmt interchangeable / 401 offerafter interchangeable，也不是已经 OfferSnapshot Usage reject in chunk response bundled（499 item 3 余量 / 649） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 648 offersnapusage-notrestored interchangeable。**  
   官方把 Usage 引擎拉不到下一块换快照单句和 ApplySnapshotChunk Result REJECT_SNAPSHOT 枚举分开——485 bundled 第三件事常与 398 混成「看见 unable to retrieve next chunk 就已经 REJECT_SNAPSHOT 回包 interchangeable / 就已经 ApplySnapshotChunk 回包 result 栏 interchangeable」，本页钉 not REJECT_SNAPSHOT bundled 单句。看见 reject via OfferSnapshot，不是已经 ApplySnapshotChunk Result REJECT_SNAPSHOT（398） interchangeable——398 钉 Result 枚举，本页钉 Methods Usage 引擎换快照路径。看见 try a different one via OfferSnapshot，不是已经 OfferSnapshot Usage reject in chunk response bundled（649） interchangeable——649 另钉 chunk response reject not REJECT_SNAPSHOT，本页钉 unable to retrieve 引擎侧换份单句。

3. **看见 The application should be prepared to reset and accept it or abort as appropriate / 看见 reset and accept or abort is not already 已经装完又对上 LastBlockAppHash（332） interchangeable / 332 snapshotverify interchangeable / 已经 Snapshot Verification 装完又对上 LastBlockAppHash bundled interchangeable / 654 applysnapusage-notinfo interchangeable / 654 applysnapusage-notinfo item 1 not Info during load interchangeable / 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 655 applysnapusage-notunable interchangeable / 653 applysnapusage-notverify interchangeable / 654 applysnapusage-notinfo interchangeable / 485 applysnapusage item 1 verify each chunk interchangeable / 485 applysnapusage item 2 all chunks accepted 后 Info interchangeable，也不是已经 unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事 bundled（485 item 3 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 649 offersnapusage-notreject interchangeable / 400 offerabort interchangeable，也不是已经 Offer 装完（321） interchangeable / 323 transition interchangeable / 370 infover interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable。**  
   官方把 Usage reset and accept or abort 单句和 Snapshot Verification 装完又对上 LastBlockAppHash bundled 分开——485 bundled 第三件事常与 332 混成「看见 reset and accept or abort 就已经装完 interchangeable / 就已经 LastBlockAppHash 对了 interchangeable」，本页钉 not already matched LastBlockAppHash 单句。看见 reset and accept it or abort as appropriate，不是已经装完又对上 LastBlockAppHash（332） interchangeable——332 钉 app requirements 装完核对，本页钉 Methods Usage unable to retrieve 单句。看见 prepared to reset，不是已经 Offer 装完（321） interchangeable——321 钉 Offer 装完，本页钉 item 3 第三件事。

怎样做增量验、怎样写 Metadata chunk hash、怎样 reset 是规范里的做法，本页不抄。ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485）、verify each chunk not Only AppHash can be trusted（485 item 1 余量 / 653）、all chunks accepted 后 Info not Info during load（485 item 2 余量 / 654）、ApplySnapshotChunk 再拉 refetch/reject_senders（378）、ApplySnapshotChunk Result REJECT_SNAPSHOT（398）、OfferSnapshot Usage reject in chunk response（499 item 3 余量 / 649）、Snapshot Verification app requirements（332）、Offer 装完（321）、Offer 收下之后拉块并装（401）是另外那套，本页不抄。

## 官方为什么这样拆

- **unable to retrieve next chunk not refetch/reject_senders ≠ 378 applysnap interchangeable：** 官方把引擎拉不到下一块换快照和应用下指令再拉分开。
- **unable to retrieve next chunk not REJECT_SNAPSHOT bundled ≠ 398 applysnap-result interchangeable：** 官方把 Usage 引擎换快照路径和 ApplySnapshotChunk Result 枚举分开。
- **unable to retrieve next chunk not already matched LastBlockAppHash ≠ 332 snapshotverify interchangeable：** 官方把 reset and accept or abort 单句和装完又对上 LastBlockAppHash bundled 分开；485 applysnapusage unbundling 完成（655 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| unable to retrieve next chunk | 不是 refetch/reject_senders（378） | 不是 LoadSnapshotChunk 齐（375） |
| reject via OfferSnapshot | 不是 REJECT_SNAPSHOT（398） | 不是 reject in chunk response（649） |
| reset and accept or abort | 不是 already matched LastBlockAppHash（332） | 不是 Offer 装完（321） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage unable to retrieve next chunk not refetch/reject_senders / not REJECT_SNAPSHOT bundled / not already matched LastBlockAppHash 正式三事（485 余量），必须分开 unable to retrieve next chunk 是不是 refetch/reject_senders interchangeable / 378 applysnap interchangeable / 397 chunk 栏 interchangeable / 375 LoadSnapshotChunk interchangeable、reject via OfferSnapshot 是不是 REJECT_SNAPSHOT bundled interchangeable / 398 applysnap-result interchangeable / 649 offersnapusage-notreject interchangeable / 400 offerabort interchangeable、reset and accept or abort 是不是 already matched LastBlockAppHash interchangeable / 332 snapshotverify interchangeable / 654 applysnapusage-notinfo interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。可以跳过「看见 unable to retrieve next chunk 就已经 refetch 就齐 interchangeable / 就已经 REJECT_SNAPSHOT 回包 interchangeable」。不要另写怎样做增量验。485 applysnapusage unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。
- ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled。那是不变量 485。
- verify each chunk not Only AppHash can be trusted。那是不变量 485 item 1 余量 / 653。
- all chunks accepted 后 Info not Info during load。那是不变量 485 item 2 余量 / 654。
- ApplySnapshotChunk 再拉 refetch/reject_senders。那是不变量 378。
- ApplySnapshotChunk Result REJECT_SNAPSHOT。那是不变量 398。
- OfferSnapshot Usage reject in chunk response。那是不变量 499 item 3 余量 / 649。
- Snapshot Verification app requirements。那是不变量 332。
- Offer 装完。那是不变量 321。
- Offer 收下之后拉块并装。那是不变量 401。
