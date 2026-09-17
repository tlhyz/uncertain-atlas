# 例：看见 UNKNOWN always wrong crash is not already four gates settled interchangeable / not already VerifyStatus UNKNOWN interchangeable / not already OfferSnapshot UNKNOWN abort interchangeable

**层次**：实现 / ProposalStatus UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProposalStatus UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事（376 余量）/ not 713 propstat-notunknown interchangeable / not 376 proposalstatus-vs-prevote bundled interchangeable」，不是 ProposalStatus 正式三事 bundled（376），也不是四门已经结算（33）或 VerifyStatus UNKNOWN（434）。不要另写怎样写 ProposalStatus。

## 官方三件事

1. **看见 `ProposalStatus` 用在 `ProcessProposal` 回包 / 回 `UNKNOWN` 一律是错 / CometBFT 会当应用坏了，然后崩 / UNKNOWN is not already 已经是四门已经结算 interchangeable / 33 fourgates interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 713 propstat-notunknown interchangeable / 714 propstat-notaccept interchangeable / 376 proposalstatus item 2 ACCEPT interchangeable，也不是已经 UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事 bundled（376 item 1 余量） interchangeable / 376 proposalstatus item 1 interchangeable。**  
   官方 Data Types 写：ProposalStatus 用在 ProcessProposal 回包。回 UNKNOWN 一律是错。CometBFT 会当应用坏了，然后崩。看见回了 UNKNOWN 会崩，不是已经四门齐了 interchangeable——本页从 376 item 1 侧钉 not four gates 单句。376 proposalstatus vs prevote bundled unbundling 在本页 item 1 启动。

2. **看见回了 `UNKNOWN` / 看见崩了 / UNKNOWN is not already 已经 VerifyStatus 那种 UNKNOWN 一律是错、引擎当应用坏了会崩 interchangeable / 434 verifystatus interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 713 propstat-notunknown interchangeable / 376 proposalstatus item 3 REJECT interchangeable / 715 propstat-notreject interchangeable。**  
   官方把 ProposalStatus UNKNOWN 和 VerifyStatus UNKNOWN 分开——376 bundled 第一件事常与 434 混成「看见 UNKNOWN 就已经是扩展回包会崩 interchangeable」，本页钉 not VerifyStatus UNKNOWN 单句。

3. **看见回了 `UNKNOWN` / 看见 Usage 这句 / UNKNOWN is not already 已经 OfferSnapshot Result UNKNOWN 那种结果不明、中止全部装回（402） interchangeable / 402 offerunk interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 713 propstat-notunknown interchangeable / 714 propstat-notaccept interchangeable。**  
   官方把 Process 回包 UNKNOWN 会崩和 Offer UNKNOWN 中止装回分开。看见会崩，不是已经中止全部装回 interchangeable。376 proposalstatus vs prevote bundled unbundling 在本页 item 1 启动。

怎样写 `ProposalStatus`、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **UNKNOWN crash not four gates ≠ 33 interchangeable：** 官方把回 UNKNOWN 会崩和四门已经结算分开。
- **UNKNOWN crash not VerifyStatus UNKNOWN ≠ 434 interchangeable：** 官方把 ProposalStatus UNKNOWN 和 VerifyStatus UNKNOWN 分开。
- **UNKNOWN crash not OfferSnapshot UNKNOWN ≠ 402 interchangeable：** 官方把 Process 回包会崩和 Offer UNKNOWN 中止装回分开；376 proposalstatus vs prevote bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| UNKNOWN 一律是错、引擎当应用坏了会崩 | 不是已经是四门已经结算（33） | 不是 ACCEPT 会发 Prevote（714/376 item 2） |
| 看见回了 UNKNOWN | 不是 VerifyStatus UNKNOWN（434） | 不是 ProposalStatus bundled（376） |
| 看见崩了 | 不是 OfferSnapshot UNKNOWN 中止装回（402） | 不是 REJECT 会发 Prevote nil（715/376 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus UNKNOWN always wrong crash not four gates / not VerifyStatus UNKNOWN / not OfferSnapshot UNKNOWN 正式三事（376 余量），必须分开 UNKNOWN 是不是已经四门齐了 interchangeable / 33、是不是 VerifyStatus UNKNOWN interchangeable / 434、是不是 Offer UNKNOWN 中止装回 interchangeable / 402。可以跳过「看见回了 UNKNOWN 就已经是四门已经结算」。不要另写怎样写 ProposalStatus。376 proposalstatus vs prevote bundled unbundling 在本页 item 1 启动；续 [`worked-example-propstat-notaccept-vs-bundled.md`](worked-example-propstat-notaccept-vs-bundled.md)（不变量 714 item 2）。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- ProposalStatus 正式三事 bundled。那是不变量 376。
- ACCEPT 表示应用认为提案合法、共识会发 Prevote。那是不变量 376 item 2 余量 / 714。
- REJECT 表示应用认为提案非法、共识会发 Prevote nil。那是不变量 376 item 3 余量 / 715。
- 四门已经结算。那是不变量 33。
- VerifyStatus UNKNOWN。那是不变量 434。
- OfferSnapshot Result UNKNOWN。那是不变量 402。
