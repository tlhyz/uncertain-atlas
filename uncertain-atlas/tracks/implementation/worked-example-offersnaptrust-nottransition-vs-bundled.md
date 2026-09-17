# 例：看见 verified AppHash automatically checked at end is not already Info during load（332） interchangeable / Transition to Consensus bundled（323） interchangeable / Offer 装完 / Offer 收下之后 bundled（321 / 401） interchangeable

**层次**：实现 / OfferSnapshot Usage verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事（483 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Usage verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事（483 余量）/ not 652 offersnaptrust-nottransition interchangeable / not 650 offersnaptrust-notmetadata interchangeable / not 651 offersnaptrust-notverify interchangeable / not 38 apphash trust interchangeable」，不是 OfferSnapshot Usage trust 正式三事 bundled（483），也不是 Transition to Consensus Info 核对（323）。不要另写怎样做增量验、怎样封邻居、怎样配轻客户端 RPC。

## 官方三件事

规范把 OfferSnapshot Usage 里 The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration 和「已经是装 chunk 过程中 Info 对了 interchangeable / 已经是 Transition to Consensus bundled interchangeable / 已经是 Offer 装完 / Offer 收下之后 bundled interchangeable」分开写成三件独立的实现事，不是「看见 verified AppHash automatically checked at end 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable / 就已经 Offer 装完 interchangeable」一件事：

1. **看见 The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration / 看见装回结束时引擎会自动核对 verified AppHash is not already 已经在装 chunk 过程中 Info 对了（332） interchangeable / 已经装块时就叫 Info 对 LastBlockAppHash interchangeable / 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable / 已经 Snapshot Verification 增量验 / checksum bundled interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 652 offersnaptrust-nottransition interchangeable / 483 offersnaptrust interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable，也不是已经 verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事 bundled（483 item 3 余量） interchangeable / 483 offersnaptrust item 3 interchangeable，也不是已经 Only AppHash can be trusted not OfferSnapshot app_hash bundled（483 item 1 余量 / 650） interchangeable / 396 offersnap interchangeable / 38 apphash-trust interchangeable / 499 offersnapusage bundled interchangeable。**  
   官方 Usage 写：The verified `AppHash` is automatically checked against the restored application at the end of snapshot restoration。看见 automatically checked at the end，不是已经在装块时就叫 Info 对 LastBlockAppHash interchangeable——332 钉 app requirements 装过程中 Info，本页从 483 item 3 侧钉 not Info during load 单句。看见 against the restored application，不是已经 Snapshot Verification 增量验 bundled（332） interchangeable——651 另钉 not Snapshot Verification bundled on employ additional verification 单句，本页钉 at end 单句。看见 at the end of restoration，不是已经 Only AppHash can be trusted 就代表已经验完 interchangeable——650 另钉 not OfferSnapshot app_hash on Only AppHash 单句，本页钉 item 3 第一件事。483 offersnaptrust unbundling 在本页 item 3 完成。

2. **看见 automatically checked at the end / at the end of snapshot restoration is not already 已经 Transition to Consensus 那套 ChainID / 版本核对 bundled（323） interchangeable / 323 transition interchangeable / 已经切进共识就有完整历史 interchangeable / snapshotswitch-sold-as-full-history interchangeable / 已经装完就有 ChainID interchangeable / 370 infover interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 652 offersnaptrust-nottransition interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable / 483 offersnaptrust item 1 Only AppHash can be trusted interchangeable，也不是已经 verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事 bundled（483 item 3 余量） interchangeable / 321 offerrestored interchangeable / 322 listsnap interchangeable / 648 offersnapusage-notrestored interchangeable，也不是已经 Any other data can be spoofed not Snapshot Verification bundled bundled（483 item 2 余量 / 651） interchangeable / 332 snapshotverify interchangeable / 378 applysnap bundled interchangeable。**  
   官方把 Usage at end automatically checked 单句和 Transition to Consensus Info 核对 bundled 分开——483 bundled 第三件事常与 323 混成「看见 verified AppHash at end 就已经切进共识 interchangeable / 就已经 ChainID 对了 interchangeable」，本页钉 not Transition to Consensus bundled 单句。看见 at the end of restoration，不是已经 Transition to Consensus bundled（323） interchangeable——323 钉装完后再凑 ChainID / Info 核对，本页钉 Methods Usage at end 单句。看见 against the restored application，不是已经 Snapshot Restoration 装回流程 bundled（321） interchangeable——321 钉 Offer 装完，本页钉 item 3 第二件事。

3. **看见 automatically checked at the end is not already 已经 Offer 收下就已经装完（321） interchangeable / 已经 Offer 收下之后 bundled（401） interchangeable / 401 offerafter interchangeable / 已经 ApplySnapshotChunk Result ACCEPT 是这块收下了就代表已经齐 interchangeable / 321 offerrestored interchangeable / 648 offersnapusage-notrestored interchangeable / 649 offersnapusage-notreject interchangeable / 375 LoadSnapshotChunk 已经齐 interchangeable，也不是已经 OfferSnapshot Usage trust 正式三事 bundled（483） interchangeable / 652 offersnaptrust-nottransition interchangeable / 650 offersnaptrust-notmetadata interchangeable / 651 offersnaptrust-notverify interchangeable / 483 offersnaptrust item 2 Any other data can be spoofed interchangeable，也不是已经 verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事 bundled（483 item 3 余量） interchangeable / 499 offersnapusage bundled interchangeable / 647 offersnapusage-notlisted interchangeable，也不是已经 OfferSnapshot Usage upon accepting retrieve and apply bundled（499 item 2 余量 / 648） interchangeable / 378 applysnap bundled interchangeable / 397 chunk 栏 interchangeable。**  
   官方把 Usage at end automatically checked 单句和 Offer 收下之后 bundled 分开——483 bundled 第三件事常与 401 混成「看见 verified AppHash at end 就已经 Offer 装完 interchangeable / 就已经 ApplySnapshotChunk Result ACCEPT 就代表已经齐 interchangeable」，本页钉 not Offer restored bundled 单句。看见 at the end of restoration，不是已经 Offer 收下就已经装完（321） interchangeable——321 钉 Snapshot Restoration 装回，本页钉 at end 单句。看见 automatically checked，不是已经 Offer 收下之后 bundled（401） interchangeable——401 钉 Accept 后拉块并装，本页钉 item 3 第三件事。

怎样做增量验、怎样封邻居、怎样配轻客户端 RPC 是规范里的做法，本页不抄。OfferSnapshot Usage trust 正式三事 bundled（483）、Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash（483 item 1 余量 / 650）、Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS（483 item 2 余量 / 651）、Snapshot Verification app requirements（332）、Transition to Consensus Info 核对（323）、Offer 收下之后拉块并装（401）、Offer 装完（321）是另外那套，本页不抄。

## 官方为什么这样拆

- **verified AppHash at end not Info during load ≠ 332 snapshotverify interchangeable：** 官方把装回结束时自动核对和装过程中 Info 核对 分开。
- **verified AppHash at end not Transition to Consensus bundled ≠ 323 transition interchangeable：** 官方把 Usage at end 单句和 Transition to Consensus ChainID / Info 核对 分开。
- **verified AppHash at end not Offer restored bundled ≠ 321 offerrestored / 401 offerafter interchangeable：** 官方把 Usage at end 单句和 Offer 装完 / Offer 收下之后 bundled 分开；483 offersnaptrust unbundling 完成（652 item 3）。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| verified AppHash at end | 不是 Info during load（332） | 不是 Only AppHash can be trusted（650） |
| verified AppHash at end | 不是 Transition to Consensus bundled（323） | 不是 Snapshot Verification bundled（651） |
| verified AppHash at end | 不是 Offer 装完 / Offer 收下之后（321/401） | 不是 upon accepting retrieve and apply（648） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Usage verified AppHash at end not Info during load / not Transition to Consensus bundled / not Offer restored bundled 正式三事（483 余量），必须分开 verified AppHash at end 是不是 Info during load interchangeable / 332 snapshotverify interchangeable / 485 applysnapusage verify/Info/unable interchangeable、verified AppHash at end 是不是 Transition to Consensus bundled interchangeable / 323 transition interchangeable / 370 infover interchangeable、verified AppHash at end 是不是 Offer 装完 / Offer 收下之后 bundled interchangeable / 321 offerrestored interchangeable / 401 offerafter interchangeable / 648 offersnapusage-notrestored interchangeable。可以跳过「看见 verified AppHash at end 就已经装块时就 Info 对了 interchangeable / 就已经切进共识 interchangeable」。不要另写怎样做增量验。483 offersnaptrust unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做增量验、怎样封邻居、怎样配轻客户端 RPC、怎样写 OfferSnapshot。
- OfferSnapshot Usage trust 正式三事 bundled。那是不变量 483。
- Only AppHash can be trusted not Snapshot metadata / not hash comparison / not OfferSnapshot app_hash。那是不变量 483 item 1 余量 / 650。
- Any other data can be spoofed not hash comparison enough / not Snapshot Verification bundled / not ApplySnapshotChunk reject refetch DoS。那是不变量 483 item 2 余量 / 651。
- Snapshot Verification app requirements。那是不变量 332。
- Transition to Consensus Info 核对。那是不变量 323。
- Offer 收下之后拉块并装。那是不变量 401。
- Offer 装完。那是不变量 321。
