# 例：看见 ACCEPT means app considers proposal valid consensus prevotes is not already settled interchangeable / not already honest proposal must Accept interchangeable / not already four gates interchangeable

**层次**：实现 / ProposalStatus ACCEPT prevote not settled / not must Accept / not four gates 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProposalStatus ACCEPT prevote not settled / not must Accept / not four gates 正式三事（376 余量）/ not 714 propstat-notaccept interchangeable / not 376 proposalstatus-vs-prevote bundled interchangeable」，不是 ProposalStatus 正式三事 bundled（376），也不是正确提议者的准备提案必须被正确接收者 Accept（347）或四门已经结算（33）。不要另写怎样写 ProposalStatus。

## 官方三件事

1. **看见 `ACCEPT` 表示应用认为这份提案合法 / 共识算法收下这份提案，并给它发 Prevote / ACCEPT is not already 已经交差 interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 714 propstat-notaccept interchangeable / 713 propstat-notunknown interchangeable / 376 proposalstatus item 1 UNKNOWN interchangeable，也不是已经 ACCEPT prevote not settled / not must Accept / not four gates 正式三事 bundled（376 item 2 余量） interchangeable / 376 proposalstatus item 2 interchangeable。**  
   官方 Data Types 写：ACCEPT 表示应用认为这份提案合法。共识算法收下这份提案，并给它发 Prevote。看见会发 Prevote，不是已经交差 interchangeable——本页从 376 item 2 侧钉 not settled 单句。376 proposalstatus vs prevote bundled unbundling 在本页 item 2 续。

2. **看见回了 `ACCEPT` / 看见会发 Prevote / ACCEPT is not already 已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable / 347 mustaccept interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 714 propstat-notaccept interchangeable / 376 proposalstatus item 3 REJECT interchangeable / 715 propstat-notreject interchangeable。**  
   官方把 ACCEPT 会发 Prevote 和 Req 3 必须 Accept 分开——376 bundled 第二件事常与 347 混成「看见 ACCEPT 就已经是 honest proposal 必须 Accept interchangeable」，本页钉 not must Accept 单句。

3. **看见回了 `ACCEPT` / 看见 Usage 这句 / ACCEPT is not already 已经四门已经结算（33） interchangeable / 33 fourgates interchangeable / 已经 VerifyStatus ACCEPT 收下这张票 interchangeable / 434 verifystatus interchangeable，也不是已经 ProposalStatus 正式三事 bundled（376） interchangeable / 714 propstat-notaccept interchangeable / 713 propstat-notunknown interchangeable。**  
   官方把 Process ACCEPT 会发 Prevote 和四门齐了 / Verify ACCEPT 收下票分开。看见会发 Prevote，不是已经四门交差 interchangeable。376 proposalstatus vs prevote bundled unbundling 在本页 item 2 续。

怎样写 `ProposalStatus`、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ACCEPT prevote not settled ≠ 已经交差 interchangeable：** 官方把发 Prevote 和已经交差分开。
- **ACCEPT prevote not must Accept ≠ 347 interchangeable：** 官方把 ACCEPT 会发 Prevote 和 Req 3 必须 Accept 分开。
- **ACCEPT prevote not four gates ≠ 33 / 434 interchangeable：** 官方把 Process ACCEPT 和四门齐了 / Verify ACCEPT 分开；376 proposalstatus vs prevote bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ACCEPT 表示应用认为提案合法、共识会发 Prevote | 不是已经交差 | 不是 UNKNOWN 会崩（713/376 item 1） |
| 看见回了 ACCEPT | 不是 honest proposal 必须 Accept（347） | 不是 ProposalStatus bundled（376） |
| 看见会发 Prevote | 不是四门已经结算（33） / VerifyStatus ACCEPT（434） | 不是 REJECT 会发 Prevote nil（715/376 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProposalStatus ACCEPT prevote not settled / not must Accept / not four gates 正式三事（376 余量），必须分开 ACCEPT 是不是已经交差、是不是 Req 3 必须 Accept interchangeable / 347、是不是四门齐了 interchangeable / 33。可以跳过「看见回了 ACCEPT 就已经交差」。不要另写怎样写 ProposalStatus。376 proposalstatus vs prevote bundled unbundling 在本页 item 2 续；完成 [`worked-example-propstat-notreject-vs-bundled.md`](worked-example-propstat-notreject-vs-bundled.md)（不变量 715 item 3）。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- ProposalStatus 正式三事 bundled。那是不变量 376。
- UNKNOWN 一律是错、引擎当应用坏了会崩。那是不变量 376 item 1 余量 / 713。
- REJECT 表示应用认为提案非法、共识会发 Prevote nil。那是不变量 376 item 3 余量 / 715。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- 四门已经结算。那是不变量 33。
- VerifyStatus ACCEPT。那是不变量 434。
