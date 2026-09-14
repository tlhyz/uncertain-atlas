# 例：看见 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票 / ACCEPT accepts vote is not block invalid / ACCEPT is not Requirement 6 must Accept 不是已经 VerifyStatus bundled interchangeable / 已经当成块非法 interchangeable / 已经正确进程交出的扩展必须 Accept interchangeable

**层次**：实现 / VerifyStatus ACCEPT accepts vote 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VerifyStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatus ACCEPT accepts vote / not block invalid / not Req 6 must Accept 不是 VerifyStatus bundled interchangeable / 不是已经当成块非法 interchangeable / 不是已经 correct process must Accept interchangeable」，不是 VerifyStatus bundled（434），也不是 ProposalStatus 那种 ACCEPT 会发 Prevote（376），也不是 Extend–Verify 一致性 Req 6 must Accept（348）。不要另写怎样写 VerifyStatus。

## 官方三件事

规范把 VerifyStatus 的 ACCEPT 表示应用认为扩展合法、共识会收下这张票写成三件独立的实现事，不是「看见回了 VerifyStatus ACCEPT 就已经当成块非法 interchangeable、已经 correct process must Accept interchangeable、已经 ProposalStatus ACCEPT interchangeable」一件事：

1. **看见 VerifyStatus 的 `ACCEPT` 表示应用认为扩展合法、共识会收下这张票 / 看见回了 `ACCEPT` 不是已经当成块非法，也不是已经 VerifyStatus bundled（434） interchangeable / 已经验过扩展 interchangeable / 已经 MUST Accept interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经整张 Precommit 非法 interchangeable / 已经块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（535 余量） interchangeable / 已经 block invalid interchangeable，也不是已经 Verify When step 3 return ACCEPT bundled（516） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 VerifyStatus UNKNOWN bundled（537 余量） interchangeable / 已经验过扩展 interchangeable。**  
   官方写：若 `Status` 是 `ACCEPT`，共识算法会收下这张票，当成合法。Usage 也写：*p* 会把收到的票和对应扩展留在内部结构。看见回了 `ACCEPT`，不是已经当成块非法——434 bundled 常被写成「回了 ACCEPT 就已经块非法」，本页钉 ACCEPT accepts vote not block invalid 单句。看见会收下这张票，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉整张 Precommit 非法，本页钉 VerifyStatus ACCEPT 语义单句。看见合法，不是已经 status valid/invalid（535 余量） interchangeable——535 钉 Response status valid/invalid，本页钉 VerifyStatus ACCEPT 单句。
2. **看见 ACCEPT accepts vote is not Requirement 6 must Accept / correct process extension must Accept / 看见会收下这张票不是已经正确进程交出的扩展必须 Accept 不是已经 VerifyStatus bundled（434） interchangeable / 已经 correct process must Accept interchangeable / 已经 Requirement 6 已经测过 interchangeable，也不是已经 Extend–Verify consistency bundled（348） interchangeable / 已经 correct process must Accept interchangeable / 已经 Req 6 是测试目标 interchangeable，也不是已经 VerifyVoteExtension Usage SHOULD always set ACCEPT bundled（527） interchangeable / 已经 MUST Accept interchangeable / 已经不能 Reject interchangeable，也不是已经 VerifyVoteExtensionResponse.status must exclusively depend bundled（536 余量） interchangeable / 已经和对任意扩展同一裁决 interchangeable，也不是已经 Verify SHOULD Accept default strategy bundled（529 余量） interchangeable / 已经 can't Reject interchangeable。**  
   官方 VerifyStatus 把收下这张票和 Requirement 6 must Accept 分开——434 bundled 常被写成「回了 ACCEPT = 已经 correct process must Accept」，本页钉 ACCEPT not Req 6 must Accept 单句。看见 not correct process must Accept，不是已经 Extend–Verify consistency（348） interchangeable——348 钉 Req 6 must Accept，本页钉 VerifyStatus ACCEPT 边界。看见 accepts vote，不是已经 Verify SHOULD always set ACCEPT（527） interchangeable——527 钉 Usage SHOULD，本页钉 VerifyStatus ACCEPT 单句。
3. **看见 VerifyStatus ACCEPT is not ProposalStatus ACCEPT / 看见 VerifyStatus 的 ACCEPT 不是 ProposalStatus 那种 ACCEPT 会发 Prevote 不是已经 VerifyStatus bundled（434） interchangeable / 已经 ProposalStatus ACCEPT interchangeable / 已经会发 Prevote interchangeable，也不是已经 ProposalStatus REJECT 会发 Prevote nil bundled（376） interchangeable / 已经当成块非法 interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable，也不是已经 VerifyVoteExtensionResponse.status valid/invalid bundled（535 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 VerifyStatus UNKNOWN bundled（537 余量） interchangeable / 已经 ProposalStatus UNKNOWN interchangeable。**  
   官方 Data Types 把 VerifyStatus 和 ProposalStatus 分开——434 bundled 常被写成「ACCEPT = ProposalStatus ACCEPT 会发 Prevote」，本页钉 VerifyStatus ACCEPT not ProposalStatus ACCEPT 单句。看见 not sends Prevote，不是已经 ProposalStatus ACCEPT（376） interchangeable——376 钉 ProposalStatus ACCEPT 会发 Prevote，本页钉 VerifyStatus ACCEPT 边界。看见 not Process prevote，不是已经 ProcessProposalResponse.status ACCEPT（430 余量） interchangeable——430 钉 Process 回包栏，本页钉 VerifyStatus ACCEPT 单句。

怎样做写 `VerifyStatus`、怎样留票和扩展 是规范里的做法，本页不抄。VerifyStatus bundled（434）、VerifyStatus REJECT（539 余量）、ProposalStatus ACCEPT（376）、Req 6 must Accept（348）是另外那套，本页不抄。

## 官方为什么这样拆

- **ACCEPT accepts vote not block invalid ≠ VerifyStatus bundled interchangeable：** 官方把收下这张票和块非法分开。
- **ACCEPT not Req 6 must Accept ≠ correct process must Accept interchangeable：** 官方把 VerifyStatus ACCEPT 和 Extend–Verify 一致性 Req 6 分开。
- **VerifyStatus ACCEPT not ProposalStatus ACCEPT ≠ sends Prevote interchangeable：** 官方把 VerifyStatus ACCEPT 和 ProposalStatus ACCEPT 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ACCEPT accepts vote | 不是 block invalid | 不是验签拒收整张 Precommit 就已经是块非法（34） |
| ACCEPT not Req 6 must Accept | 不是 correct process must Accept | 不是 Extend–Verify consistency Req 6 must Accept（348） |
| VerifyStatus ACCEPT | 不是 ProposalStatus ACCEPT | 不是 ProposalStatus ACCEPT 会发 Prevote（376） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatus ACCEPT accepts vote 正式三事，必须分开 ACCEPT accepts vote 是不是 block invalid interchangeable / VerifyStatus bundled interchangeable、ACCEPT 是不是 Req 6 must Accept interchangeable / 348 correct process must Accept interchangeable、VerifyStatus ACCEPT 是不是 ProposalStatus ACCEPT interchangeable / 376 sends Prevote interchangeable。可以跳过「看见回了 VerifyStatus ACCEPT 就已经当成块非法 interchangeable」。不要另写怎样写 VerifyStatus。

## 本页不抄

- 怎样做写 `VerifyStatus`、怎样留票和扩展。
- VerifyStatus 的 REJECT 会拒掉整张票。那是不变量 539（434 item 3 余量）。
- VerifyStatus 的 UNKNOWN 一律是错。那是不变量 537（434 item 1 余量）。
- ProposalStatus 那种 ACCEPT 会发 Prevote。那是不变量 376。
