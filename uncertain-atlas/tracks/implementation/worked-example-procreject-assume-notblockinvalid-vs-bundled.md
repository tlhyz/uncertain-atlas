# 例：看见 `ProcessProposalResponse.status` 是 `REJECT` 时共识假设收到的提案不合法 / consensus assumes not valid is not block invalid 不是已经 Process REJECT consensus assume bundled interchangeable / 已经当成块非法 interchangeable / 已经永久标成非法块 interchangeable

**层次**：实现 / ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「REJECT → consensus assumes not valid not block invalid 不是 Process REJECT consensus assume bundled interchangeable / 不是已经当成块非法 interchangeable / 不是已经永久标成非法块 interchangeable」，不是 Process REJECT consensus assume bundled（455），也不是 ProcessProposal Response status valid/invalid bundled（533），也不是 ProposalStatus 枚举语义（376）。不要另写怎样挑 ACCEPT/REJECT。

## 官方三件事

规范把 ProcessProposal REJECT 时共识假设收到的提案不合法写成三件独立的实现事，不是「看见 Process 回了 REJECT 就已经当成块非法 interchangeable、已经永久标成非法块 interchangeable、已经 ProposalStatus REJECT interchangeable」一件事：

1. **看见 `ProcessProposalResponse.status` 是 `REJECT` 时共识假设收到的提案不合法 / 看见 consensus assumes the proposal received is not valid 不是已经当成块非法，也不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 prevote nil interchangeable / 已经不能整块执行候选 interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（430 / 533 余量） interchangeable / 已经 block invalid interchangeable / 已经 MUST Accept interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经整张 Precommit 非法 interchangeable / 已经块非法 interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable，也不是已经 Process REJECT consensus assume bundled（455 第二件事 / 541 余量） interchangeable / 已经 Verify REJECT whole vote interchangeable。**  
   官方写：If `ProcessProposalResponse.status` is `REJECT`, consensus assumes the proposal received is not valid。看见 assumes not valid，不是已经验签拒收整张 Precommit 就已经是块非法那种已经当成块非法——455 bundled 常被写成「回了 REJECT 就已经块非法」，本页钉 consensus assumes not valid not block invalid 单句。看见假设不合法，不是已经 ProcessProposalResponse.status valid/invalid（533 余量） interchangeable——533 钉 Response status 语义 bundled，本页钉 Usage assumes not valid 单句。看见 REJECT，不是已经 Verify 433 REJECT whole vote interchangeable——433 钉拒整张 Precommit，本页钉 Process assumes not valid 边界。
2. **看见 consensus assumes not valid is not permanently blacklisted block / 看见假设不合法不是已经永久标成非法块 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经当成块非法 interchangeable / 已经 prevote nil interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（430 / 533 余量） interchangeable / 已经 block invalid interchangeable / 已经 status 必须只依赖 interchangeable，也不是已经 ProposalStatus REJECT bundled（376） interchangeable / 已经不能稍后改裁决 interchangeable / 已经当成块非法 interchangeable，也不是已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable / 已经 REJECT 是免费过滤 interchangeable，也不是已经 Process REJECT consensus assume bundled（455 第三件事 / 542 余量） interchangeable / 已经不能整块执行候选 interchangeable。**  
   官方把 consensus assumes not valid 和应用状态里永久拉黑块分开——455 bundled 常被写成「回了 REJECT 就已经永久标成非法块」，本页钉 assumes not valid not permanently blacklisted 单句。看见 not permanently blacklisted，不是已经 Process 回包栏 bundled（430） interchangeable——430 钉 bundled 三事，本页钉 Usage assumes not valid 单句。看见 assumes not valid，不是已经 ProposalStatus REJECT（376） interchangeable——376 钉 ProposalStatus 枚举，本页钉 Process REJECT Usage 边界。
3. **看见 REJECT assumes not valid is not ProposalStatus REJECT / 看见 Process REJECT 时共识 assumes not valid 不是 ProposalStatus 那种 REJECT 会发 Prevote nil 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 ProposalStatus REJECT interchangeable / 已经会发 Prevote nil interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（533 余量） interchangeable / 已经 prevote nil interchangeable / 已经 block invalid interchangeable，也不是已经 VerifyStatus REJECT bundled（539 余量） interchangeable / 已经 rejects whole vote interchangeable / 已经 Process prevote nil interchangeable，也不是已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable / 已经当成块非法 interchangeable，也不是已经 Process REJECT consensus assume bundled（455 第二件事 / 541 余量） interchangeable / 已经 Verify REJECT whole vote interchangeable。**  
   官方 Data Types 把 ProcessProposalResponse.status REJECT 和 ProposalStatus REJECT 分开——455 bundled 常与 376 混成「Process REJECT = ProposalStatus REJECT 会发 Prevote nil」，本页钉 assumes not valid not ProposalStatus REJECT 单句。看见 not sends Prevote nil via ProposalStatus path，不是已经 ProposalStatus REJECT（376） interchangeable——376 钉 ProposalStatus REJECT 会发 Prevote nil，本页钉 Process assumes not valid 边界。看见 not Verify rejects whole vote，不是已经 VerifyStatus REJECT（539 余量） interchangeable——539 钉 VerifyStatus REJECT，本页钉 Process assumes not valid 单句。

怎样挑 ACCEPT/REJECT、怎样写 Process 回包栏 是规范里的做法，本页不抄。Process REJECT consensus assume bundled（455）、ProcessProposal Response status valid/invalid（533）、ProposalStatus REJECT（376）是另外那套，本页不抄。

## 官方为什么这样拆

- **consensus assumes not valid not block invalid ≠ Process REJECT consensus assume bundled interchangeable：** 官方把 assumes not valid 和块非法、验签拒收整张 Precommit 分开。
- **assumes not valid not permanently blacklisted ≠ block invalid interchangeable：** 官方把共识假设不合法和应用状态永久拉黑分开。
- **assumes not valid not ProposalStatus REJECT ≠ sends Prevote nil interchangeable：** 官方把 Process REJECT Usage 和 ProposalStatus REJECT 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| consensus assumes not valid | 不是 block invalid | 不是 Verify REJECT whole vote（433） |
| assumes not valid | 不是 permanently blacklisted | 不是 Process resp status bundled（533） |
| Process REJECT assumes not valid | 不是 ProposalStatus REJECT | 不是 ProposalStatus REJECT 会发 Prevote nil（376） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assumes not valid not block invalid 正式三事，必须分开 consensus assumes not valid 是不是 block invalid interchangeable / 34 block invalid interchangeable、assumes not valid 是不是 permanently blacklisted interchangeable / 430 block invalid interchangeable、Process REJECT assumes not valid 是不是 ProposalStatus REJECT interchangeable / 376 sends Prevote nil interchangeable。可以跳过「看见 Process 回了 REJECT 就已经当成块非法 interchangeable」。不要另写怎样挑 ACCEPT/REJECT。

## 本页不抄

- 怎样做挑 ACCEPT/REJECT、怎样写 Process 回包栏。
- Process REJECT → prevote nil ≠ Verify REJECT whole vote。那是不变量 541（455 item 2 余量）。
- REJECT 共识假设 ≠ 已经不能整块执行候选。那是不变量 542（455 item 3 余量）。
- ProcessProposal Response status valid/invalid 正式三事 bundled。那是不变量 533。
