# 例：看见 OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回不是已经崩；看见 OfferSnapshot Result ACCEPT 是收下这份、开始装块不是已经装完；看见 OfferSnapshot Result REJECT 是拒掉这份、换一份不是已经是拒掉这种 format

**层次**：实现 / OfferSnapshot 结果枚举余量。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回不是已经崩 / OfferSnapshot Result ACCEPT 是收下这份、开始装块不是已经装完 / OfferSnapshot Result REJECT 是拒掉这份、换一份不是已经是拒掉这种 format」，不是 UNKNOWN 一律是错、引擎当应用坏了会崩，也不是 Offer 收下之后才去拉块并装就已经装完。不要另写怎样写 OfferSnapshot UNKNOWN。

## 官方三件事

规范把 OfferSnapshot Result `UNKNOWN` 是结果不明、中止全部装回、`ACCEPT` 是收下这份、开始装块、`REJECT` 是拒掉这份、换一份写成三件独立的实现事，不是「看见回了 OfferSnapshot 结果枚举余量就已经崩、已经装完、已经是拒掉这种 format」一件事：

1. **看见 OfferSnapshot Result `UNKNOWN` 是结果不明、中止全部装回 / 看见回了 UNKNOWN 不是已经崩，也不是已经是中止装回、不再试别份。**  
   官方写：`UNKNOWN` 是结果不明，中止全部装回。看见回了 UNKNOWN，不是已经 `ProposalStatus` 那种 UNKNOWN 一律是错、引擎当应用坏了会崩。看见能中止全部装回，不是已经 OfferSnapshot Result `ABORT` 那种中止装回、不再试别份。看见能回，不是已经交差。
2. **看见 OfferSnapshot Result `ACCEPT` 是收下这份、开始装块 / 看见回了 ACCEPT 不是已经装完，也不是已经齐。**  
   官方写：`ACCEPT` 是收下这份，开始装块。看见回了 ACCEPT，不是已经 Offer 收下之后才去拉块并装就已经装完。看见开始装块，不是已经一块 chunk 收下就已经齐。看见能收，不是已经交差。
3. **看见 OfferSnapshot Result `REJECT` 是拒掉这份、换一份 / 看见回了 REJECT 不是已经是拒掉这种 format，也不是已经是拒掉这份。**  
   官方写：`REJECT` 是拒掉这份，换一份。看见回了 REJECT，不是已经 OfferSnapshot Result `REJECT_FORMAT` 那种拒掉这种 format、换一份。看见能换一份，不是已经 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份。看见能回，不是已经交差。

怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT 是规范里的做法，本页不抄。UNKNOWN 一律是错、引擎当应用坏了会崩是不变量 376，本页不抄。

## 官方为什么这样拆

- **OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回 ≠ 已经崩：** 官方把结果不明、中止全部装回和引擎当应用坏了会崩分开。
- **OfferSnapshot Result ACCEPT 是收下这份、开始装块 ≠ 已经装完：** 官方把收下这份、开始装块和已经装完分开。
- **OfferSnapshot Result REJECT 是拒掉这份、换一份 ≠ 已经是拒掉这种 format：** 官方把拒掉这份和拒掉这种 format 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回 | 不是已经崩 | 不是 UNKNOWN 一律是错、引擎当应用坏了会崩（376） |
| OfferSnapshot Result ACCEPT 是收下这份、开始装块 | 不是已经装完 | 不是 Offer 收下之后才去拉块并装就已经装完（401） |
| OfferSnapshot Result REJECT 是拒掉这份、换一份 | 不是已经是拒掉这种 format | 不是 OfferSnapshot Result REJECT_FORMAT 就已经是拒掉这种 format（400） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 OfferSnapshot 结果枚举余量就已经崩、已经装完、已经是拒掉这种 format」，必须分开 OfferSnapshot Result UNKNOWN 是结果不明、中止全部装回是不是已经崩、OfferSnapshot Result ACCEPT 是收下这份、开始装块是不是已经装完、OfferSnapshot Result REJECT 是拒掉这份、换一份是不是已经是拒掉这种 format。可以跳过「看见回了 OfferSnapshot 结果枚举余量就已经崩」。不要另写怎样写 OfferSnapshot UNKNOWN。402 offerunk vs crash bundled unbundling 完成（725 item 1 / 726 item 2 / 727 item 3）；精读 [`worked-example-offerunk-notcrash-vs-bundled.md`](worked-example-offerunk-notcrash-vs-bundled.md)（不变量 725 item 1）。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT。
- UNKNOWN 一律是错、引擎当应用坏了会崩。那是不变量 376。
- Offer 收下之后才去拉块并装就已经装完。那是不变量 401。
- OfferSnapshot Result REJECT_FORMAT 就已经是拒掉这种 format。那是不变量 400。
