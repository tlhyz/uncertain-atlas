# 例：看见 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩 / UNKNOWN crash is not extension enabled / VerifyStatus UNKNOWN is not ProposalStatus UNKNOWN 不是已经 VerifyStatus bundled interchangeable / 已经验过扩展 interchangeable / 已经扩展启用 interchangeable

**层次**：实现 / VerifyStatus UNKNOWN always wrong 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatus UNKNOWN always wrong / UNKNOWN crash not extension enabled / VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 不是 VerifyStatus bundled interchangeable / 不是已经验过扩展 interchangeable / 不是已经扩展启用 interchangeable」，不是 VerifyStatus bundled（434），也不是 ProposalStatus 那种 UNKNOWN 一律是错就已经是四门已经结算（376），也不是 VerifyVoteExtensionResponse.status valid/invalid（539 余量）。不要另写怎样写 VerifyStatus。

## 官方三件事

规范把 VerifyStatus 的 UNKNOWN 一律是错、引擎当应用坏了会崩写成三件独立的实现事，不是「看见回了 VerifyStatus UNKNOWN 就已经验过扩展 interchangeable、已经扩展启用 interchangeable、已经 ProposalStatus UNKNOWN interchangeable」一件事：

1. **看见 VerifyStatus 的 `UNKNOWN` 一律是错、引擎当应用坏了会崩 / 看见回了 `UNKNOWN` 不是已经验过扩展，也不是已经 VerifyStatus bundled（434） interchangeable / 已经当成块非法 interchangeable / 已经 MUST Accept interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（539 余量） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 Verify When step 3 return status bundled（516） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 status must exclusively depend bundled（540 余量） interchangeable / 已经对任意扩展同一裁决 interchangeable。**  
   官方写：`VerifyStatus` 用在 `VerifyVoteExtension` 回包。若 `Status` 是 `UNKNOWN`，应用出了问题。CometBFT 会当应用坏了，然后崩。看见回了 `UNKNOWN`，不是已经验过扩展——434 bundled 常被写成「回了 UNKNOWN 就已经验过扩展」，本页钉 UNKNOWN always wrong not already verified 单句。看见应用出了问题，不是已经 Verify When return ACCEPT/REJECT（516） interchangeable——516 钉 When step 3 return，本页钉 VerifyStatus UNKNOWN 语义单句。看见会崩，不是已经 status valid/invalid（539 余量） interchangeable——539 钉 valid/invalid 判断，本页钉 UNKNOWN always wrong 单句。
2. **看见 UNKNOWN crash is not extension enabled / 看见崩了不是已经扩展启用 不是已经 VerifyStatus bundled（434） interchangeable / 已经扩展启用 interchangeable / 已经验过扩展 interchangeable，也不是已经 ExtendVote 只在非 nil Precommit 才叫 bundled（437） interchangeable / 已经扩展启用 interchangeable，也不是已经 vote extensions enable height bundled（339 余量） interchangeable / 已经启用 interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（539 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 ProposalStatus UNKNOWN bundled（376） interchangeable / 已经四门已经结算 interchangeable。**  
   官方 VerifyStatus 把回 UNKNOWN 会崩和扩展启用分开——434 bundled 常被写成「崩了 = 已经扩展启用」，本页钉 UNKNOWN crash not extension enabled 单句。看见 crash not enabled，不是已经 ExtendVote 只在非 nil Precommit 才叫（437） interchangeable——437 钉 precommit nil 不会叫 ExtendVote，本页钉 UNKNOWN crash 边界。看见 not extension enabled，不是已经 ProposalStatus UNKNOWN（376） interchangeable——376 钉 ProposalStatus UNKNOWN 一律是错，本页钉 VerifyStatus UNKNOWN 单句。
3. **看见 VerifyStatus UNKNOWN is not ProposalStatus UNKNOWN / 看见 VerifyStatus 的 UNKNOWN 不是 ProposalStatus 那种 UNKNOWN 一律是错就已经是四门已经结算 不是已经 VerifyStatus bundled（434） interchangeable / 已经 ProposalStatus UNKNOWN interchangeable / 已经四门已经结算 interchangeable，也不是已经 ProposalStatus ACCEPT 会发 Prevote bundled（376） interchangeable / 已经当成块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（539 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 status must exclusively depend bundled（540 余量） interchangeable / 已经和对任意扩展同一裁决 interchangeable。**  
   官方 Data Types 把 VerifyStatus 和 ProposalStatus 分开——434 bundled 常被写成「UNKNOWN = ProposalStatus UNKNOWN」，本页钉 VerifyStatus UNKNOWN not ProposalStatus UNKNOWN 单句。看见 not four gates settled，不是已经 ProposalStatus UNKNOWN（376） interchangeable——376 钉 ProposalStatus 那种 UNKNOWN 一律是错，本页钉 VerifyStatus UNKNOWN 边界。看见 not ProposalStatus semantics，不是已经 Verify 回包栏 bundled（433） interchangeable——433 钉 Response status 依赖，本页钉 VerifyStatus UNKNOWN 单句。

怎样做写 `VerifyStatus`、怎样挑枚举 是规范里的做法，本页不抄。VerifyStatus bundled（434）、VerifyStatus ACCEPT/REJECT（542/543 余量）、ProposalStatus UNKNOWN（376）是另外那套，本页不抄。

## 官方为什么这样拆

- **UNKNOWN always wrong not already verified ≠ VerifyStatus bundled interchangeable：** 官方把回 UNKNOWN 会崩和已经验过扩展分开。
- **UNKNOWN crash not extension enabled ≠ extension enabled interchangeable：** 官方把崩溃和扩展启用分开。
- **VerifyStatus UNKNOWN not ProposalStatus UNKNOWN ≠ four gates settled interchangeable：** 官方把 VerifyStatus UNKNOWN 和 ProposalStatus UNKNOWN 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| UNKNOWN always wrong | 不是 already verified | 不是 Verify When return ACCEPT/REJECT（516） |
| UNKNOWN crash | 不是 extension enabled | 不是 ExtendVote 只在非 nil Precommit 才叫（437） |
| VerifyStatus UNKNOWN | 不是 ProposalStatus UNKNOWN | 不是 ProposalStatus UNKNOWN 一律是错就已经是四门已经结算（376） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus UNKNOWN always wrong 正式三事，必须分开 UNKNOWN always wrong 是不是 already verified interchangeable / VerifyStatus bundled interchangeable、UNKNOWN crash 是不是 extension enabled interchangeable、VerifyStatus UNKNOWN 是不是 ProposalStatus UNKNOWN interchangeable / 376 four gates settled interchangeable。可以跳过「看见回了 VerifyStatus UNKNOWN 就已经验过扩展 interchangeable」。不要另写怎样写 VerifyStatus。

## 本页不抄

- 怎样做写 `VerifyStatus`、怎样挑枚举。
- VerifyStatus 的 ACCEPT 会收下这张票。那是不变量 542（434 item 2 余量）。
- VerifyStatus 的 REJECT 会拒掉整张票。那是不变量 543（434 item 3 余量）。
- ProposalStatus 那种 UNKNOWN 一律是错。那是不变量 376。
