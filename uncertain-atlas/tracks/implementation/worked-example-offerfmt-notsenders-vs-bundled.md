# 例：看见 OfferSnapshot Result REJECT_SENDER is not already reject_senders regardless interchangeable / not already can continue interchangeable / not already chunk-response reject interchangeable

**层次**：实现 / OfferSnapshot Result REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事（400 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Result REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事（400 余量）/ not 723 offerfmt-notsenders interchangeable / not 400 offerfmt-vs-rejectsnap bundled interchangeable」，不是 OfferSnapshot 结果枚举 bundled（400），也不是 reject_senders 不论 Result 都拒这些人就已经能接着装（378）或 Usage reject in chunk（499）。不要另写怎样写 OfferSnapshot 结果枚举。

## 官方三件事

1. **看见 OfferSnapshot Result `REJECT_SENDER` 是拒掉送来这份的所有人、换一份 / 看见回了 REJECT_SENDER / REJECT_SENDER is not already 已经 reject_senders 不论 Result 都拒这些人 interchangeable / 378 refetch interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 723 offerfmt-notsenders interchangeable / 722 offerfmt-notrejectsnap interchangeable / 400 offerfmt item 1 REJECT_FORMAT interchangeable，也不是已经 REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事 bundled（400 item 2 余量） interchangeable / 400 offerfmt item 2 interchangeable。**  
   官方 Data Types 写：REJECT_SENDER 是拒掉送来这份的所有人，换一份。看见回了 REJECT_SENDER，不是已经 reject_senders 不论 Result 都拒 interchangeable——本页从 400 item 2 侧钉 not reject_senders regardless 单句。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 2 续。

2. **看见回了 REJECT_SENDER / 看见能换一份 / REJECT_SENDER is not already 已经能接着装 interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 723 offerfmt-notsenders interchangeable / 400 offerfmt item 3 ABORT interchangeable / 724 offerfmt-notabort interchangeable。**  
   官方把拒掉送来这份的所有人和已经能接着装分开——400 bundled 第二件事常与「看见拒了人就已经能接着装 interchangeable」糊成一句，本页钉 not can continue 单句。

3. **看见回了 REJECT_SENDER / 看见 Usage 这句 / REJECT_SENDER is not already 已经 Offer Usage reject in chunk response（499） interchangeable / 499 / 649 offersnapusage-notreject interchangeable，也不是已经 OfferSnapshot 结果枚举 bundled（400） interchangeable / 723 offerfmt-notsenders interchangeable / 722 offerfmt-notrejectsnap interchangeable。**  
   官方把 Result REJECT_SENDER 和 Usage 在 chunk 回包里拒掉这份分开。看见能换一份，不是已经 499 交差 interchangeable。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 2 续。

怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **REJECT_SENDER not reject_senders regardless ≠ 378 interchangeable：** 官方把拒掉送来这份的所有人和不论 Result 都拒分开。
- **REJECT_SENDER not can continue ≠ 已经能接着装 interchangeable：** 官方把能换一份和已经能接着装分开。
- **REJECT_SENDER not chunk-response reject ≠ 499 interchangeable：** 官方把 Result REJECT_SENDER 和 Usage chunk 回包拒掉分开；400 offerfmt vs rejectsnap bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT_SENDER 是拒掉送来这份的所有人、换一份 | 不是已经 reject_senders 不论 Result（378） | 不是 REJECT_FORMAT 拒这种 format（722/400 item 1） |
| 看见回了 REJECT_SENDER | 不是已经能接着装 | 不是 OfferSnapshot 结果枚举 bundled（400） |
| 看见能换一份 | 不是 Usage reject in chunk（499） | 不是 ABORT 中止装回（724/400 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT_SENDER not reject_senders regardless / not can continue / not chunk-response reject 正式三事（400 余量），必须分开 REJECT_SENDER 是不是已经不论 Result 都拒 interchangeable / 378、是不是已经能接着装、是不是 Usage chunk 回包拒掉 interchangeable / 499。可以跳过「看见回了 REJECT_SENDER 就已经拒了人」。不要另写怎样写 OfferSnapshot 结果枚举。400 offerfmt vs rejectsnap bundled unbundling 在本页 item 2 续；完成 [`worked-example-offerfmt-notabort-vs-bundled.md`](worked-example-offerfmt-notabort-vs-bundled.md)（不变量 724 item 3）。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举、怎样挑 REJECT_FORMAT、怎样挑 REJECT_SENDER。
- OfferSnapshot 结果枚举 bundled。那是不变量 400。
- REJECT_FORMAT 拒掉这种 format。那是不变量 400 item 1 余量 / 722。
- ABORT 中止装回、不再试别份。那是不变量 400 item 3 余量 / 724。
- reject_senders 不论 Result 都拒这些人就已经能接着装。那是不变量 378。
- Offer Usage reject in chunk。那是不变量 499。
