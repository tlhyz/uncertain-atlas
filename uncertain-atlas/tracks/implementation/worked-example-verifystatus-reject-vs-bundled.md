# 例：看见 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票 / REJECT rejects whole vote is not Process prevote nil / REJECT rejects whole vote is not block invalid 不是已经 VerifyStatus bundled interchangeable / 已经会发 Prevote nil interchangeable / 已经当成块非法 interchangeable

**层次**：实现 / VerifyStatus REJECT rejects whole vote 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatus REJECT rejects whole vote / not Process prevote nil / not block invalid 不是 VerifyStatus bundled interchangeable / 不是已经会发 Prevote nil interchangeable / 不是已经当成块非法 interchangeable」，不是 VerifyStatus bundled（434），也不是 ProposalStatus 那种 REJECT 会发 Prevote nil（376），也不是 ProcessProposalResponse.status is REJECT prevote nil（430/533）。不要另写怎样写 VerifyStatus。

## 官方三件事

规范把 VerifyStatus 的 REJECT 表示应用认为扩展非法、共识会拒掉整张票写成三件独立的实现事，不是「看见回了 VerifyStatus REJECT 就已经会发 Prevote nil interchangeable、已经当成块非法 interchangeable、已经 Process prevote nil interchangeable」一件事：

1. **看见 VerifyStatus 的 `REJECT` 表示应用认为扩展非法、共识会拒掉整张票 / 看见回了 `REJECT` 不是已经会发 Prevote nil，也不是已经 VerifyStatus bundled（434） interchangeable / 已经验过扩展 interchangeable / 已经 MUST Accept interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 / 533 余量） interchangeable / 已经 prevote nil interchangeable / 已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable，也不是已经 ProposalStatus REJECT 会发 Prevote nil bundled（376） interchangeable / 已经当成块非法 interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经丢掉 Precommit interchangeable，也不是已经 VerifyStatus ACCEPT bundled（538 余量） interchangeable / 已经收下这张票 interchangeable。**  
   官方写：若 `Status` 是 `REJECT`，共识算法会拒掉整张票，当成非法。Usage 也写：*p* 会把这张 Precommit 当非法丢掉。看见回了 `REJECT`，不是已经 ProposalStatus 那种 REJECT 会发 Prevote nil——434 bundled 常被写成「回了 REJECT 就已经会发 Prevote nil」，本页钉 REJECT rejects whole vote not Process prevote nil 单句。看见拒掉整张票，不是已经 ProcessProposalResponse.status is REJECT（430/533） interchangeable——533 钉 Process prevote nil，本页钉 VerifyStatus REJECT 语义单句。看见丢掉 Precommit，不是已经 Verify When REJECT discard（517） interchangeable——517 钉 When step 3 discard，本页钉 VerifyStatus REJECT 单句。
2. **看见 REJECT rejects whole vote is not block invalid / 看见拒掉整张票不是已经当成块非法 不是已经 VerifyStatus bundled（434） interchangeable / 已经当成块非法 interchangeable / 已经验签拒收整张 Precommit bundled（34） interchangeable / 已经整张 Precommit 非法 interchangeable / 已经块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（535 余量） interchangeable / 已经 block invalid interchangeable / 已经 REJECT rejects whole vote not block invalid interchangeable，也不是已经 ProcessProposalResponse.status is REJECT assumes not valid bundled（533 余量） interchangeable / 已经 prevote nil interchangeable，也不是已经 VerifyStatus ACCEPT bundled（538 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 Process REJECT consensus assume bundled（455 余量） interchangeable / 已经 prevote nil interchangeable。**  
   官方 VerifyStatus 把拒整张票和块非法分开——434 bundled 常被写成「回了 REJECT 就已经块非法」，本页钉 REJECT rejects whole vote not block invalid 单句。看见 not block invalid，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉整张 Precommit 非法，本页钉 VerifyStatus REJECT 边界。看见 rejects whole vote，不是已经 VerifyVoteExtensionResponse.status valid/invalid（535 余量） interchangeable——535 钉 Response status REJECT 语义，本页钉 VerifyStatus REJECT 单句。
3. **看见 VerifyStatus REJECT is not ProposalStatus REJECT / 看见 VerifyStatus 的 REJECT 不是 ProposalStatus 那种 REJECT 会发 Prevote nil 不是已经 VerifyStatus bundled（434） interchangeable / 已经 ProposalStatus REJECT interchangeable / 已经会发 Prevote nil interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 余量） interchangeable / 已经 prevote nil interchangeable / 已经 Process REJECT = prevote nil interchangeable，也不是已经 ProposalStatus ACCEPT 会发 Prevote bundled（376） interchangeable / 已经当成块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（535 余量） interchangeable / 已经 block invalid interchangeable，也不是已经 VerifyStatus ACCEPT bundled（538 余量） interchangeable / 已经 ProposalStatus ACCEPT interchangeable。**  
   官方 Data Types 把 VerifyStatus 和 ProposalStatus 分开——434 bundled 常被写成「REJECT = ProposalStatus REJECT 会发 Prevote nil」，本页钉 VerifyStatus REJECT not ProposalStatus REJECT 单句。看见 not sends Prevote nil，不是已经 ProposalStatus REJECT（376） interchangeable——376 钉 ProposalStatus REJECT 会发 Prevote nil，本页钉 VerifyStatus REJECT 边界。看见 not Process prevote nil path，不是已经 ProcessProposalResponse.status REJECT（430 余量） interchangeable——430 钉 Process 回包栏，本页钉 VerifyStatus REJECT 单句。

怎样做写 `VerifyStatus`、怎样拒整张 Precommit 是规范里的做法，本页不抄。VerifyStatus bundled（434）、VerifyStatus UNKNOWN/ACCEPT（537/538 余量）、ProposalStatus REJECT（376）、Process REJECT prevote nil（430/533）是另外那套，本页不抄。

## 官方为什么这样拆

- **REJECT rejects whole vote not Process prevote nil ≠ VerifyStatus bundled interchangeable：** 官方把拒整张 Precommit 和 Process/Proposal prevote nil 分开。
- **REJECT rejects whole vote not block invalid ≠ block invalid interchangeable：** 官方把 VerifyStatus REJECT 和验签拒收整张 Precommit 块非法分开。
- **VerifyStatus REJECT not ProposalStatus REJECT ≠ sends Prevote nil interchangeable：** 官方把 VerifyStatus REJECT 和 ProposalStatus REJECT 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT rejects whole vote | 不是 Process prevote nil | 不是 ProcessProposalResponse.status is REJECT prevote nil（430/533） |
| REJECT rejects whole vote | 不是 block invalid | 不是验签拒收整张 Precommit 就已经是块非法（34） |
| VerifyStatus REJECT | 不是 ProposalStatus REJECT | 不是 ProposalStatus REJECT 会发 Prevote nil（376） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus REJECT rejects whole vote 正式三事，必须分开 REJECT rejects whole vote 是不是 Process prevote nil interchangeable / VerifyStatus bundled interchangeable、REJECT rejects whole vote 是不是 block invalid interchangeable / 34 block invalid interchangeable、VerifyStatus REJECT 是不是 ProposalStatus REJECT interchangeable / 376 sends Prevote nil interchangeable。可以跳过「看见回了 VerifyStatus REJECT 就已经会发 Prevote nil interchangeable」。不要另写怎样写 VerifyStatus。

## 本页不抄

- 怎样做写 `VerifyStatus`、怎样拒整张 Precommit。
- VerifyStatus 的 UNKNOWN 一律是错。那是不变量 537（434 item 1 余量）。
- VerifyStatus 的 ACCEPT 会收下这张票。那是不变量 538（434 item 2 余量）。
- VerifyVoteExtensionResponse.status REJECT rejects whole vote not block invalid。那是不变量 535（433 item 1 余量）。
