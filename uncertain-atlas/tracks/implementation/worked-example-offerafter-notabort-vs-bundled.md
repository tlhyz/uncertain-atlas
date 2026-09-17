# 例：看见在装这块的回包里拒掉这份、还要再收 Offer is not already ABORT interchangeable / not already REJECT_SNAPSHOT interchangeable / not already Usage chunk-response reject interchangeable

**层次**：实现 / 在装这块的回包里拒掉这份、还要再收 Offer not ABORT / not REJECT_SNAPSHOT / not Usage reject 正式三事（401 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「在装这块的回包里拒掉这份、还要再收 Offer not ABORT / not REJECT_SNAPSHOT / not Usage reject 正式三事（401 余量）/ not 729 offerafter-notabort interchangeable / not 401 offeraccept-vs-restored bundled interchangeable」，不是 Offer 收下之后 bundled（401），也不是 OfferSnapshot Result ABORT（400）或 Apply REJECT_SNAPSHOT（398）或 Usage reject in chunk（499 / 649）。不要另写怎样写 Offer 收下之后。

## 官方三件事

1. **看见在装这块的回包里也能拒掉这份、还要准备再收 Offer / 看见在装这块时拒了 / 回包拒还要再收 Offer is not already 已经 OfferSnapshot Result `ABORT` 那种中止装回、不再试别份 interchangeable / 400 / 724 offerfmt-notabort interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 729 offerafter-notabort interchangeable / 728 offerafter-notrestored interchangeable / 401 offeraccept item 1 收下之后才去拉装 interchangeable，也不是已经回包拒还要再收 Offer not ABORT / not REJECT_SNAPSHOT / not Usage reject 正式三事 bundled（401 item 2 余量） interchangeable / 401 offeraccept item 2 interchangeable。**  
   官方 Usage 写：应用也可以在装这块的回包里拒掉这份；这时还要准备再收 `OfferSnapshot`。看见在装这块时拒了，不是已经 ABORT 那种中止装回、不再试别份 interchangeable——本页从 401 item 2 侧钉 not ABORT 单句。401 offeraccept vs restored bundled unbundling 在本页 item 2 续。

2. **看见在装这块时拒了 / 看见还能再收 Offer / 回包拒还要再收 Offer is not already 已经 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份 interchangeable / 398 / 721 applyretry-notchunkresult interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 729 offerafter-notabort interchangeable / 401 offeraccept item 3 Apply ACCEPT interchangeable / 730 offerafter-notcomplete interchangeable。**  
   官方把还能再收 Offer 和 REJECT_SNAPSHOT 拒掉这份分开——401 bundled 第二件事常与 398 混成「看见在装这块时拒了就已经是 REJECT_SNAPSHOT interchangeable」，本页钉 not REJECT_SNAPSHOT 单句。

3. **看见在装这块时拒了 / 看见 Usage 这句 / 回包拒还要再收 Offer is not already 已经 OfferSnapshot Usage reject in chunk response interchangeable / 499 / 649 offersnapusage-notreject interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 729 offerafter-notabort interchangeable / 728 offerafter-notrestored interchangeable。**  
   官方把 401 侧「还能再收 Offer」和 499 Usage reject in chunk 分开。看见能回，不是已经 649 interchangeable。401 offeraccept vs restored bundled unbundling 在本页 item 2 续。

怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **回包拒还要再收 Offer not ABORT ≠ 400 / 724 interchangeable：** 官方把还能再收 Offer 和中止装回、不再试别份分开。
- **回包拒还要再收 Offer not REJECT_SNAPSHOT ≠ 398 / 721 interchangeable：** 官方把还能再收 Offer 和 REJECT_SNAPSHOT 拒掉这份分开。
- **回包拒还要再收 Offer not Usage reject ≠ 499 / 649 interchangeable：** 官方把 401 侧还能再收和 499 Usage reject in chunk 分开；401 offeraccept vs restored bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 在装这块的回包里拒掉这份、还要再收 Offer | 不是已经 ABORT（400 / 724） | 不是收下之后才去拉装（728/401 item 1） |
| 看见在装这块时拒了 | 不是已经 REJECT_SNAPSHOT（398 / 721） | 不是 Offer 收下之后 bundled（401） |
| 看见还能再收 Offer | 不是已经 Usage reject（499 / 649） | 不是 Apply ACCEPT 这块收下了（730/401 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看在装这块的回包里拒掉这份、还要再收 Offer not ABORT / not REJECT_SNAPSHOT / not Usage reject 正式三事（401 余量），必须分开回包拒是不是已经 ABORT interchangeable / 400 / 724、是不是已经 REJECT_SNAPSHOT interchangeable / 398 / 721、是不是已经 Usage reject interchangeable / 499 / 649。可以跳过「看见在装这块时拒了就已经中止」。不要另写怎样写 Offer 收下之后。401 offeraccept vs restored bundled unbundling 在本页 item 2 续；完成 [`worked-example-offerafter-notcomplete-vs-bundled.md`](worked-example-offerafter-notcomplete-vs-bundled.md)（不变量 730 item 3）。

## 本页不抄

- 怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT。
- Offer 收下之后 bundled。那是不变量 401。
- Offer 收下之后才去拉块并装。那是不变量 401 item 1 余量 / 728。
- ApplySnapshotChunk Result ACCEPT 是这块收下了。那是不变量 401 item 3 余量 / 730。
- OfferSnapshot Result ABORT。那是不变量 400。
- ApplySnapshotChunk Result REJECT_SNAPSHOT。那是不变量 398。
- OfferSnapshot Usage reject in chunk response。那是不变量 499 / 649。
