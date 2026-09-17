# 例：看见 OfferSnapshot Result REJECT_FORMAT is not already REJECT_SNAPSHOT interchangeable / not already complete interchangeable / not already Offer REJECT interchangeable

**层次**：实现 / OfferSnapshot Result REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事（400 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Result REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事（400 余量）/ not 722 offerfmt-notrejectsnap interchangeable / not 400 offerfmt-vs-rejectsnap bundled interchangeable」，不是 OfferSnapshot 结果枚举 bundled（400），也不是 ApplySnapshotChunk Result REJECT_SNAPSHOT（398）或 OfferSnapshot Result REJECT（402）。不要另写怎样写 OfferSnapshot 结果枚举。

## 官方三件事

1. **看见 OfferSnapshot Result `REJECT_FORMAT` 是拒掉这种 format、换一份 / 看见回了 REJECT_FORMAT / REJECT_FORMAT is not already 已经 ApplySnapshotChunk Result REJECT_SNAPSHOT 那种拒掉这份、换一份 interchangeable / 398 / 721 applyretry-notchunkresult interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 722 offerfmt-notrejectsnap interchangeable / 723 offerfmt-notsenders interchangeable / 400 offerfmt item 2 REJECT_SENDER interchangeable，也不是已经 REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事 bundled（400 item 1 余量） interchangeable / 400 offerfmt item 1 interchangeable。**  
   官方 Data Types 写：REJECT_FORMAT 是拒掉这种 format，换一份。看见回了 REJECT_FORMAT，不是已经 REJECT_SNAPSHOT 那种拒掉这份 interchangeable——本页从 400 item 1 侧钉 not REJECT_SNAPSHOT 单句。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 1 启动。

2. **看见回了 REJECT_FORMAT / 看见能换一份 / REJECT_FORMAT is not already 已经齐 interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 722 offerfmt-notrejectsnap interchangeable / 400 offerfmt item 3 ABORT interchangeable / 724 offerfmt-notabort interchangeable。**  
   官方把拒掉这种 format 和已经齐分开——400 bundled 第一件事常与「看见能换一份就已经齐 interchangeable」糊成一句，本页钉 not already complete 单句。

3. **看见回了 REJECT_FORMAT / 看见 Usage 这句 / REJECT_FORMAT is not already 已经 OfferSnapshot Result REJECT 那种拒掉这份、换一份（402） interchangeable / 402 offerunk interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 722 offerfmt-notrejectsnap interchangeable / 723 offerfmt-notsenders interchangeable。**  
   官方把 REJECT_FORMAT 拒掉这种 format 和 402 REJECT 拒掉这份分开。看见能换一份，不是已经 402 交差 interchangeable。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 1 启动。

怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **REJECT_FORMAT not REJECT_SNAPSHOT ≠ 398 / 721 interchangeable：** 官方把拒掉这种 format 和拒掉这份分开。
- **REJECT_FORMAT not already complete ≠ 已经齐 interchangeable：** 官方把能换一份和已经齐分开。
- **REJECT_FORMAT not Offer REJECT ≠ 402 interchangeable：** 官方把 REJECT_FORMAT 和 Offer REJECT 拒掉这份分开；400 offerfmt vs rejectsnap bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT_FORMAT 是拒掉这种 format、换一份 | 不是已经是拒掉这份（398 / 721） | 不是 REJECT_SENDER 拒送来的人（723/400 item 2） |
| 看见回了 REJECT_FORMAT | 不是已经齐 | 不是 OfferSnapshot 结果枚举 bundled（400） |
| 看见能换一份 | 不是 Offer REJECT（402） | 不是 ABORT 中止装回（724/400 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_FORMAT not REJECT_SNAPSHOT / not already complete / not Offer REJECT 正式三事（400 余量），必须分开 REJECT_FORMAT 是不是已经拒掉这份 interchangeable / 398 / 721、是不是已经齐、是不是 Offer REJECT interchangeable / 402。可以跳过「看见回了 REJECT_FORMAT 就已经是拒掉这份」。不要另写怎样写 OfferSnapshot 结果枚举。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 1 启动；续 [`worked-example-offerfmt-notsenders-vs-bundled.md`](worked-example-offerfmt-notsenders-vs-bundled.md)（不变量 723 item 2）。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER。
- OfferSnapshot 结果枚举 bundled。那是不变量 400。
- REJECT_SENDER 拒掉送来这份的所有人。那是不变量 400 item 2 余量 / 723。
- ABORT 中止装回、不再试别份。那是不变量 400 item 3 余量 / 724。
- ApplySnapshotChunk Result REJECT_SNAPSHOT。那是不变量 398。
- OfferSnapshot Result REJECT。那是不变量 402。
