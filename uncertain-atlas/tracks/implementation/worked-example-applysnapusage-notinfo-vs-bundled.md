# 例：看见 all chunks accepted 后 Info / AppVersion / switch is not already Info during load（332） interchangeable / Transition to Consensus bundled（323） interchangeable / verified AppHash automatically checked at end（483） interchangeable

**层次**：实现 / ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量）/ not 654 applysnapusage-notinfo interchangeable / not 653 applysnapusage-notverify interchangeable / not 655 applysnapusage-notunable interchangeable / not 485 applysnapusage bundled interchangeable」，不是 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485），也不是 Transition to Consensus Info 核对（323）。不要另写怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。

## 官方三件事

规范把 ApplySnapshotChunk Usage 里 When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values, and record the `AppVersion` in the node state. It then switches to block sync or consensus and joins the network 和「已经是装 chunk 过程中 Info 对了 interchangeable / 已经是 Transition to Consensus bundled interchangeable / 已经是 verified AppHash automatically checked at end of restoration interchangeable」分开写成三件独立的实现事，不是「看见 all chunks accepted 后 Info 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable / 就已经 verified AppHash at end interchangeable」一件事：

1. **看见 When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values / 看见全部 chunk 都 ACCEPT 后引擎会叫 Info 核对 LastBlockAppHash / LastBlockHeight is not already 已经在装 chunk 过程中 Info 对了（332） interchangeable / 332 snapshotverify interchangeable / 已经装块时就叫 Info 对 LastBlockAppHash interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 653 applysnapusage-notverify interchangeable / 已经 Snapshot Verification 增量验 chunk bundled interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 654 applysnapusage-notinfo interchangeable / 485 applysnapusage interchangeable / 655 applysnapusage-notunable interchangeable，也不是已经 all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事 bundled（485 item 2 余量） interchangeable / 485 applysnapusage item 2 interchangeable，也不是已经 verified AppHash at end not Info during load bundled（483 item 3 余量 / 652） interchangeable / 652 offersnaptrust-nottransition interchangeable / 370 infover interchangeable。**  
   官方 Usage 写：When all chunks have been accepted, CometBFT will make an ABCI `Info` call to verify that `LastBlockAppHash` and `LastBlockHeight` matches the expected values。看见 all chunks accepted 后才 Info，不是已经在装块时就叫 Info 对 LastBlockAppHash interchangeable——332 钉 app requirements 装过程中 Info，本页从 485 item 2 侧钉 not Info during load 单句。看见 matches expected values，不是已经 Snapshot Verification 增量验 bundled（332） interchangeable——653 另钉 not Snapshot Verification bundled on verify each chunk 单句，本页钉 all chunks accepted 后 Info 单句。看见 LastBlockAppHash / LastBlockHeight，不是已经 Info 握手对齐（370） interchangeable——370 钉 Info 请求版本，本页钉 item 2 第一件事。485 applysnapusage unbundling 在本页 item 2 续。

2. **看见 record the `AppVersion` in the node state / switches to block sync or consensus and joins the network is not already 已经 Transition to Consensus 那套 ChainID / 版本核对 bundled（323） interchangeable / 323 transition interchangeable / 370 infover interchangeable / 已经切进共识就有完整历史 interchangeable / snapshotswitch-sold-as-full-history interchangeable / 已经装完就有 ChainID interchangeable / 321 offerrestored interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 654 applysnapusage-notinfo interchangeable / 653 applysnapusage-notverify interchangeable / 655 applysnapusage-notunable interchangeable / 485 applysnapusage item 1 verify each chunk interchangeable / 485 applysnapusage item 3 unable to retrieve next chunk interchangeable，也不是已经 all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事 bundled（485 item 2 余量） interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 3 verified AppHash at end interchangeable，也不是已经 Offer 装完（321） interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。**  
   官方把 Usage all chunks accepted 后 Info + AppVersion + switch 单句和 Transition to Consensus Info 核对 bundled 分开——485 bundled 第二件事常与 323 混成「看见 all chunks accepted 后 Info 就已经切进共识 interchangeable / 就已经 ChainID 对了 interchangeable」，本页钉 not Transition to Consensus bundled 单句。看见 record AppVersion + switches to sync/consensus，不是已经 Transition to Consensus bundled（323） interchangeable——323 钉装完后再凑 ChainID / Info 核对，本页钉 Methods Usage all chunks accepted 后 Info 单句。看见 joins the network，不是已经 Snapshot Restoration 装回流程 bundled（321） interchangeable——321 钉 Offer 装完，本页钉 item 2 第二件事。

3. **看见 all chunks accepted 后 Info / matches expected values / record AppVersion / switch is not already 已经 verified AppHash automatically checked at end of restoration（483） interchangeable / 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust item 3 verified AppHash at end interchangeable / 651 offersnaptrust-notverify interchangeable / 650 offersnaptrust-notmetadata interchangeable / 38 apphash-trust interchangeable，也不是已经 ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485） interchangeable / 654 applysnapusage-notinfo interchangeable / 653 applysnapusage-notverify interchangeable / 655 applysnapusage-notunable interchangeable / 485 applysnapusage item 1 verify each chunk interchangeable / 485 applysnapusage item 3 unable to retrieve next chunk interchangeable，也不是已经 all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事 bundled（485 item 2 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable / 649 offersnapusage-notreject interchangeable，也不是已经 Offer 收下就已经装完（321） interchangeable / 401 offerafter interchangeable / 378 applysnap bundled interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable。**  
   官方把 Usage all chunks accepted 后 Info 单句和 OfferSnapshot Usage verified AppHash at end bundled 分开——485 bundled 第二件事常与 483 混成「看见 all chunks accepted 后 Info 就已经 verified AppHash at end interchangeable / 就已经 Only AppHash 可信任就交差 interchangeable」，本页钉 not verified AppHash at end 单句。看见 matches expected values，不是已经 verified AppHash automatically checked at end（483 item 3 余量 / 652） interchangeable——652 另钉 at end not Info during load on OfferSnapshot Usage，本页钉 ApplySnapshotChunk Usage item 2 第三件事。看见 all chunks accepted 后 Info，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装，本页钉 item 2 第三件事。

怎样做增量验、怎样写 Metadata chunk hash、怎样 reset 是规范里的做法，本页不抄。ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled（485）、verify each chunk not Only AppHash can be trusted（485 item 1 余量 / 653）、unable to retrieve next chunk not refetch/reject_senders（485 item 3 余量 / 655）、Snapshot Verification app requirements（332）、Transition to Consensus Info 核对（323）、OfferSnapshot Usage trust 正式三事 bundled（483）、OfferSnapshot Usage verified AppHash at end not Info during load（483 item 3 余量 / 652）、Offer 装完（321）、Offer 收下之后拉块并装（401）是另外那套，本页不抄。

## 官方为什么这样拆

- **all chunks accepted 后 Info not Info during load ≠ 332 snapshotverify interchangeable：** 官方把全部 ACCEPT 后的 Info 核对和装过程中 Info 核对分开。
- **all chunks accepted 后 Info not Transition to Consensus bundled ≠ 323 transition interchangeable：** 官方把 Usage all chunks accepted 后 Info + AppVersion + switch 单句和 Transition to Consensus ChainID / Info 核对分开。
- **all chunks accepted 后 Info not verified AppHash at end ≠ 483 offersnaptrust / 652 offersnaptrust-nottransition interchangeable：** 官方把 ApplySnapshotChunk Usage all chunks accepted 后 Info 单句和 OfferSnapshot Usage verified AppHash at end bundled 分开；485 applysnapusage unbundling 续（654 item 2）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| all chunks accepted 后 Info | 不是 Info during load（332） | 不是 verify each chunk Only AppHash trusted（653） |
| all chunks accepted 后 Info / AppVersion / switch | 不是 Transition to Consensus bundled（323） | 不是 Offer 装完（321） |
| all chunks accepted 后 Info | 不是 verified AppHash at end（483/652） | 不是 Offer 收下之后（401） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage all chunks accepted 后 Info not Info during load / not Transition to Consensus bundled / not verified AppHash at end 正式三事（485 余量），必须分开 all chunks accepted 后 Info 是不是 Info during load interchangeable / 332 snapshotverify interchangeable / 653 applysnapusage-notverify interchangeable、all chunks accepted 后 Info 是不是 Transition to Consensus bundled interchangeable / 323 transition interchangeable / 370 infover interchangeable / 321 offerrestored interchangeable、all chunks accepted 后 Info 是不是 verified AppHash at end interchangeable / 483 offersnaptrust interchangeable / 652 offersnaptrust-nottransition interchangeable / 401 offerafter interchangeable。可以跳过「看见 all chunks accepted 后 Info 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable」。不要另写怎样做增量验。485 applysnapusage unbundling 在本页 item 2 续。

## 本页不抄

- 怎样做增量验、怎样写 Metadata chunk hash、怎样 reset。
- ApplySnapshotChunk Usage verify/Info/unable 正式三事 bundled。那是不变量 485。
- verify each chunk not Only AppHash can be trusted。那是不变量 485 item 1 余量 / 653。
- unable to retrieve next chunk not refetch/reject_senders。那是不变量 485 item 3 余量 / 655。
- Snapshot Verification app requirements。那是不变量 332。
- Transition to Consensus Info 核对。那是不变量 323。
- OfferSnapshot Usage trust 正式三事 bundled。那是不变量 483。
- OfferSnapshot Usage verified AppHash at end not Info during load。那是不变量 483 item 3 余量 / 652。
- Offer 装完。那是不变量 321。
- Offer 收下之后拉块并装。那是不变量 401。
