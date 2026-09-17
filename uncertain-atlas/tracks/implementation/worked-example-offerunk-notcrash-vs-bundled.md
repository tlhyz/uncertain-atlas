# 例：看见 OfferSnapshot Result UNKNOWN is not already ProposalStatus crash interchangeable / not already ABORT interchangeable / not already settled interchangeable

**层次**：实现 / OfferSnapshot Result UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事（402 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Result UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事（402 余量）/ not 725 offerunk-notcrash interchangeable / not 402 offerunk-vs-crash bundled interchangeable」，不是 OfferSnapshot 结果枚举余量 bundled（402），也不是 ProposalStatus UNKNOWN 会崩（376）或 Offer ABORT（400）。不要另写怎样写 OfferSnapshot UNKNOWN。

## 官方三件事

1. **看见 OfferSnapshot Result `UNKNOWN` 是结果不明、中止全部装回 / 看见回了 UNKNOWN / UNKNOWN is not already 已经 ProposalStatus 那种 UNKNOWN 一律是错、引擎当应用坏了会崩 interchangeable / 376 / 713 propstat-notunknown interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 725 offerunk-notcrash interchangeable / 726 offerunk-notrestored interchangeable / 402 offerunk item 2 ACCEPT interchangeable，也不是已经 UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事 bundled（402 item 1 余量） interchangeable / 402 offerunk item 1 interchangeable。**  
   官方 Data Types 写：UNKNOWN 是结果不明，中止全部装回。看见回了 UNKNOWN，不是已经 ProposalStatus 那种会崩 interchangeable——本页从 402 item 1 侧钉 not ProposalStatus crash 单句。402 offerunk vs crash bundled unbundling 在本页 item 1 启动。

2. **看见回了 UNKNOWN / 看见能中止全部装回 / UNKNOWN is not already 已经 OfferSnapshot Result ABORT 那种中止装回、不再试别份 interchangeable / 400 / 724 offerfmt-notabort interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 725 offerunk-notcrash interchangeable / 402 offerunk item 3 REJECT interchangeable / 727 offerunk-notformat interchangeable。**  
   官方把 UNKNOWN 中止全部装回和 ABORT 不再试别份分开——402 bundled 第一件事常与 400 混成「看见 UNKNOWN 就已经是 ABORT interchangeable」，本页钉 not ABORT 单句。

3. **看见回了 UNKNOWN / 看见 Usage 这句 / UNKNOWN is not already 已经交差 interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 725 offerunk-notcrash interchangeable / 726 offerunk-notrestored interchangeable。**  
   官方把结果不明、中止全部装回和已经交差分开。看见能回 UNKNOWN，不是已经交差 interchangeable。402 offerunk vs crash bundled unbundling 在本页 item 1 启动。

怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **UNKNOWN not ProposalStatus crash ≠ 376 / 713 interchangeable：** 官方把中止全部装回和引擎当应用坏了会崩分开。
- **UNKNOWN not ABORT ≠ 400 / 724 interchangeable：** 官方把中止全部装回和 ABORT 不再试别份分开。
- **UNKNOWN not settled ≠ 已经交差 interchangeable：** 官方把能回 UNKNOWN 和已经交差分开；402 offerunk vs crash bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| UNKNOWN 是结果不明、中止全部装回 | 不是已经 ProposalStatus 会崩（376 / 713） | 不是 ACCEPT 开始装块（726/402 item 2） |
| 看见回了 UNKNOWN | 不是已经 ABORT（400 / 724） | 不是 OfferSnapshot 结果枚举余量 bundled（402） |
| 看见能中止全部装回 | 不是已经交差 | 不是 REJECT 拒掉这份（727/402 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result UNKNOWN not ProposalStatus crash / not ABORT / not settled 正式三事（402 余量），必须分开 UNKNOWN 是不是已经会崩 interchangeable / 376 / 713、是不是已经 ABORT interchangeable / 400 / 724、是不是已经交差。可以跳过「看见回了 UNKNOWN 就已经崩」。不要另写怎样写 OfferSnapshot UNKNOWN。402 offerunk vs crash bundled unbundling 在本页 item 1 启动；续 [`worked-example-offerunk-notrestored-vs-bundled.md`](worked-example-offerunk-notrestored-vs-bundled.md)（不变量 726 item 2）。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT。
- OfferSnapshot 结果枚举余量 bundled。那是不变量 402。
- ACCEPT 收下这份、开始装块。那是不变量 402 item 2 余量 / 726。
- REJECT 拒掉这份、换一份。那是不变量 402 item 3 余量 / 727。
- ProposalStatus UNKNOWN 会崩。那是不变量 376。
- OfferSnapshot Result ABORT。那是不变量 400。
