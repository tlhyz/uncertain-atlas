# 例：看见 OfferSnapshot Result ACCEPT is not already restored interchangeable / not already complete interchangeable / not already ProposalStatus ACCEPT interchangeable

**层次**：实现 / OfferSnapshot Result ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事（402 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「OfferSnapshot Result ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事（402 余量）/ not 726 offerunk-notrestored interchangeable / not 402 offerunk-vs-crash bundled interchangeable」，不是 OfferSnapshot 结果枚举余量 bundled（402），也不是 Offer 收下之后才去拉块并装就已经装完（401）或 ProposalStatus ACCEPT（376）。不要另写怎样写 OfferSnapshot UNKNOWN。

## 官方三件事

1. **看见 OfferSnapshot Result `ACCEPT` 是收下这份、开始装块 / 看见回了 ACCEPT / ACCEPT is not already 已经 Offer 收下之后才去拉块并装就已经装完 interchangeable / 401 offerafter interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 726 offerunk-notrestored interchangeable / 725 offerunk-notcrash interchangeable / 402 offerunk item 1 UNKNOWN interchangeable，也不是已经 ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事 bundled（402 item 2 余量） interchangeable / 402 offerunk item 2 interchangeable。**  
   官方 Data Types 写：ACCEPT 是收下这份，开始装块。看见回了 ACCEPT，不是已经装完 interchangeable——本页从 402 item 2 侧钉 not restored 单句。402 offerunk vs crash bundled unbundling 在本页 item 2 续。

2. **看见回了 ACCEPT / 看见开始装块 / ACCEPT is not already 已经一块 chunk 收下就已经齐 interchangeable / 321 offerrestored interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 726 offerunk-notrestored interchangeable / 402 offerunk item 3 REJECT interchangeable / 727 offerunk-notformat interchangeable。**  
   官方把开始装块和已经齐分开——402 bundled 第二件事常与「看见开始装就已经齐 interchangeable」糊成一句，本页钉 not already complete 单句。

3. **看见回了 ACCEPT / 看见 Usage 这句 / ACCEPT is not already 已经 ProposalStatus ACCEPT 会发 Prevote（376） interchangeable / 376 / 714 propstat-notaccept interchangeable，也不是已经 OfferSnapshot 结果枚举余量 bundled（402） interchangeable / 726 offerunk-notrestored interchangeable / 725 offerunk-notcrash interchangeable。**  
   官方把 Offer ACCEPT 开始装块和 Process ACCEPT 发 Prevote 分开。看见能收，不是已经 376 交差 interchangeable。402 offerunk vs crash bundled unbundling 在本页 item 2 续。

怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ACCEPT not restored ≠ 401 interchangeable：** 官方把收下这份、开始装块和已经装完分开。
- **ACCEPT not already complete ≠ 321 interchangeable：** 官方把开始装块和一块 chunk 收下就已经齐分开。
- **ACCEPT not ProposalStatus ACCEPT ≠ 376 / 714 interchangeable：** 官方把 Offer ACCEPT 和 Process ACCEPT 发 Prevote 分开；402 offerunk vs crash bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ACCEPT 是收下这份、开始装块 | 不是已经装完（401） | 不是 UNKNOWN 中止全部装回（725/402 item 1） |
| 看见回了 ACCEPT | 不是已经一块 chunk 齐了（321） | 不是 OfferSnapshot 结果枚举余量 bundled（402） |
| 看见开始装块 | 不是 ProposalStatus ACCEPT（376 / 714） | 不是 REJECT 拒掉这份（727/402 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 OfferSnapshot Result ACCEPT not restored / not already complete / not ProposalStatus ACCEPT 正式三事（402 余量），必须分开 ACCEPT 是不是已经装完 interchangeable / 401、是不是已经齐 interchangeable / 321、是不是 Process ACCEPT interchangeable / 376 / 714。可以跳过「看见回了 ACCEPT 就已经装完」。不要另写怎样写 OfferSnapshot UNKNOWN。402 offerunk vs crash bundled unbundling 在本页 item 2 续；完成 [`worked-example-offerunk-notformat-vs-bundled.md`](worked-example-offerunk-notformat-vs-bundled.md)（不变量 727 item 3）。

## 本页不抄

- 怎样写 OfferSnapshot 结果枚举余量、怎样挑 UNKNOWN、怎样挑 ACCEPT。
- OfferSnapshot 结果枚举余量 bundled。那是不变量 402。
- UNKNOWN 中止全部装回。那是不变量 402 item 1 余量 / 725。
- REJECT 拒掉这份、换一份。那是不变量 402 item 3 余量 / 727。
- Offer 收下之后才去拉块并装就已经装完。那是不变量 401。
- ProposalStatus ACCEPT。那是不变量 376。
