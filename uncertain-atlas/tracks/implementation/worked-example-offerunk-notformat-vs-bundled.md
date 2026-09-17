# 例：看见 OfferSnapshot Result REJECT is not already REJECT_FORMAT interchangeable / not already REJECT_SNAPSHOT interchangeable / not already complete interchangeable

**层次**：实现 / OfferSnapshot Result REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事（402 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Result REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事（402 余量）/ not 727 offerunk-notformat interchangeable / not 402 offerunk-vs-crash bundled interchangeable」，不是 OfferSnapshot 结果枚举余量 bundled（402），也不是 Offer REJECT_FORMAT（400）或 Apply REJECT_SNAPSHOT（398）。不要另写怎样写 OfferSnapshot UNKNOWN。

## 官方三件事

1. **看见 OfferSnapshot Result `REJECT` 是拒掉这份、换一份 / 看见回了 REJECT / REJECT is not already 已经 OfferSnapshot Result REJECT_FORMAT 那种拒掉这种 format、换一份 interchangeable / 400 / 722 offerfmt-notrejectsnap interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 727 offerunk-notformat interchangeable / 725 offerunk-notcrash interchangeable / 402 offerunk item 1 UNKNOWN interchangeable，也不是已经 REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事 bundled（402 item 3 余量） interchangeable / 402 offerunk item 3 interchangeable。**  
   官方 Data Types 写：REJECT 是拒掉这份，换一份。看见回了 REJECT，不是已经 REJECT_FORMAT 那种拒掉这种 format interchangeable——本页从 402 item 3 侧钉 not REJECT_FORMAT 单句。402 offerunk vs crash bundled unbundling 在本页 item 3 完成。

2. **看见回了 REJECT / 看见能换一份 / REJECT is not already 已经 ApplySnapshotChunk Result REJECT_SNAPSHOT 那种拒掉这份 interchangeable / 398 / 721 applyretry-notchunkresult interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 727 offerunk-notformat interchangeable / 402 offerunk item 2 ACCEPT interchangeable / 726 offerunk-notrestored interchangeable。**  
   官方把 Offer REJECT 拒掉这份和 Apply REJECT_SNAPSHOT 拒掉这份分开——402 bundled 第三件事常与 398 混成「看见 REJECT 就已经是 REJECT_SNAPSHOT interchangeable」，本页钉 not REJECT_SNAPSHOT 单句。

3. **看见回了 REJECT / 看见 Usage 这句 / REJECT is not already 已经齐 interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 727 offerunk-notformat interchangeable / 725 offerunk-notcrash interchangeable。**  
   官方把拒掉这份、换一份和已经齐分开。看见能换一份，不是已经齐 interchangeable。402 offerunk vs crash bundled unbundling 在本页 item 3 完成。

怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **REJECT not REJECT_FORMAT ≠ 400 / 722 interchangeable：** 官方把拒掉这份和拒掉这种 format 分开。
- **REJECT not REJECT_SNAPSHOT ≠ 398 / 721 interchangeable：** 官方把 Offer REJECT 和 Apply REJECT_SNAPSHOT 分开。
- **REJECT not already complete ≠ 已经齐 interchangeable：** 官方把能换一份和已经齐分开；402 offerunk vs crash bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT 是拒掉这份、换一份 | 不是已经拒掉这种 format（400 / 722） | 不是 UNKNOWN 中止全部装回（725/402 item 1） |
| 看见回了 REJECT | 不是已经 REJECT_SNAPSHOT（398 / 721） | 不是 OfferSnapshot 结果枚举余量 bundled（402） |
| 看见能换一份 | 不是已经齐 | 不是 ACCEPT 开始装块（726/402 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result REJECT not REJECT_FORMAT / not REJECT_SNAPSHOT / not already complete 正式三事（402 余量），必须分开 REJECT 是不是已经拒掉这种 format interchangeable / 400 / 722、是不是已经 REJECT_SNAPSHOT interchangeable / 398 / 721、是不是已经齐。可以跳过「看见回了 REJECT 就已经是拒掉这种 format」。不要另写怎样写 OfferSnapshot UNKNOWN。402 offerunk vs crash bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT。
- OfferSnapshot 结果枚举余量 bundled。那是不变量 402。
- UNKNOWN 中止全部装回。那是不变量 402 item 1 余量 / 725。
- ACCEPT 收下这份、开始装块。那是不变量 402 item 2 余量 / 726。
- OfferSnapshot Result REJECT_FORMAT。那是不变量 400。
- ApplySnapshotChunk Result REJECT_SNAPSHOT。那是不变量 398。
