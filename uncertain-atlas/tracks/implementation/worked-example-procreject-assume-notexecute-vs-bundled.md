# 例：看见 REJECT 共识假设不是已经不能整块执行候选 / REJECT not can't execute candidate / MAY fully execute candidate state is not already committed 不是已经 Process REJECT consensus assume bundled interchangeable / 已经不能整块执行候选 interchangeable / 已经改了已提交状态 interchangeable

**层次**：实现 / ProcessProposal REJECT consensus assume not can't execute candidate 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「REJECT not can't execute candidate / MAY fully execute candidate state not committed 不是 Process REJECT consensus assume bundled interchangeable / 不是已经不能整块执行候选 interchangeable / 不是已经改了已提交状态 interchangeable」，不是 Process REJECT consensus assume bundled（455），也不是 ProcessProposal MAY fully execute bundled（452），也不是 ProcessProposal Response status valid/invalid bundled（533）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 ProcessProposal REJECT 与 MAY 整块执行候选、candidate state、已提交状态分开写成三件独立的实现事，不是「看见 Process 回了 REJECT 就已经不能整块执行候选 interchangeable、已经改了已提交状态 interchangeable、已经 Finalize + Commit 交差 interchangeable」一件事：

1. **看见 REJECT 共识假设不是已经不能整块执行候选 / 看见 REJECT not can't execute candidate / 看见回了 `REJECT` 不是已经不能 MAY 像 Finalize 那样整块执行 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经不能整块执行候选 interchangeable / 已经 assumes not valid interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（533 余量） interchangeable / 已经 REJECT not can't execute candidate interchangeable / 已经 block invalid interchangeable，也不是已经 ProcessProposal MAY fully execute bundled（452） interchangeable / 已经交差 interchangeable / 已经改了已提交状态 interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经当成块非法 interchangeable，也不是已经 Process REJECT prevote nil not Verify whole vote bundled（541 余量） interchangeable / 已经 Verify REJECT whole vote interchangeable。**  
   官方 Usage 写：The Application MAY fully execute the block (immediate execution)。However, any resulting state changes must be kept as _candidate state_。看见 MAY fully execute，不是已经 REJECT 就不能执行 interchangeable——455 bundled 常被写成「回了 REJECT 就已经不能整块执行候选」，本页钉 REJECT not can't execute candidate 单句。看见 immediate execution，不是已经 ProcessProposal MAY fully execute（452） interchangeable——452 钉 MAY execute not committed，本页钉 REJECT 与 MAY execute 可并存单句。看见 REJECT，不是已经 ProcessProposalResponse.status valid/invalid（533 余量） interchangeable——533 钉 Response status REJECT 语义 bundled，本页钉 Usage REJECT 与 candidate 可并存单句。
2. **看见 MAY fully execute candidate state is not already committed / 看见任何状态改动必须留作 candidate state 不是已经改了已提交状态 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经改了已提交状态 interchangeable / 已经 ExecuteTxState interchangeable，也不是已经 ProcessProposal MAY fully execute bundled（452） interchangeable / 已经交差 interchangeable / 已经 Process 回了 Accept 就已经换工作状态 interchangeable，也不是已经 ProcessProposalResponse.status valid/invalid bundled（533 余量） interchangeable / 已经 REJECT not can't execute candidate interchangeable / 已经 block invalid interchangeable，也不是已经 Prepare/Process 立刻执行出候选 bundled（311 余量） interchangeable / 已经 candidate 就不需要 Commit interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经 permanently blacklisted interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable。**  
   官方把 REJECT 后 candidate state 和已提交状态分开——455 bundled 常与 452 混成「回了 REJECT 就已经改了已提交状态」，本页钉 candidate state not already committed 单句。看见 candidate state，不是已经 ProcessProposal MAY fully execute（452） interchangeable——452 钉 MAY execute / candidate / read-only，本页钉 REJECT 与 candidate 可并存单句。看见 must be kept as candidate，不是已经 Finalize + Commit 那种已经交差 interchangeable——本页钉 REJECT 后仍须留候选、不是已经 committed。
3. **看见 REJECT consensus assume is not Finalize + Commit already settled / 看见 assumes not valid 不是已经 Process 跑过就意味着已经交差 不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 Finalize + Commit interchangeable / 已经 Process MAY 整块执行就意味着已经交差 interchangeable，也不是已经 ProcessProposal MAY fully execute bundled（452） interchangeable / 已经交差 interchangeable / 已经改了已提交状态 interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 Process REJECT consensus assume not block invalid bundled（540 余量） interchangeable / 已经 block invalid interchangeable，也不是已经 Process REJECT prevote nil not Verify whole vote bundled（541 余量） interchangeable / 已经 prevote nil interchangeable，也不是已经 Process 不得改已提交状态 bundled（349 余量） interchangeable / 已经 Formal Requirement 9 已经测过 interchangeable。**  
   官方把 REJECT 共识假设和 Finalize + Commit 交差分开——455 bundled 第三件事常被写成「assumes not valid = 已经不能整块执行 = 已经交差」，本页钉 REJECT assume not already settled 单句。看见 assumes not valid，不是已经 Process 跑过就意味着已经改了已提交状态（452） interchangeable——452 钉 MAY execute not committed，本页钉 REJECT Usage 边界。看见 REJECT，不是已经 Process 回了 ACCEPT 就已经交差 interchangeable——430 钉 Response status ACCEPT 后效，本页钉 REJECT 与 candidate 可并存单句。

怎样做实现 candidate 缓存、怎样在 Finalize 套用 是规范里的做法，本页不抄。Process REJECT consensus assume bundled（455）、ProcessProposal MAY fully execute（452）、ProcessProposal Response status valid/invalid（533）是另外那套，本页不抄。

## 官方为什么这样拆

- **REJECT not can't execute candidate ≠ Process REJECT consensus assume bundled interchangeable：** 官方把 REJECT 与 MAY fully execute / candidate state 分开。
- **candidate state not already committed ≠ Process MAY execute committed interchangeable：** 官方把 REJECT 后 candidate 和已提交状态分开。
- **REJECT assume not already settled ≠ Finalize + Commit interchangeable：** 官方把 assumes not valid 和已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| REJECT not can't execute candidate | 不是 can't execute | 不是 Process MAY execute committed（452） |
| candidate state | 不是 already committed | 不是 Finalize + Commit 交差 |
| REJECT consensus assume | 不是 already settled | 不是 Process resp status bundled（533） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT consensus assume not can't execute candidate 正式三事，必须分开 REJECT not can't execute candidate 是不是已经 can't execute interchangeable / 452 already committed interchangeable、candidate state 是不是 already committed interchangeable / 452 MAY execute interchangeable、REJECT assume 是不是 Finalize + Commit already settled interchangeable / 430 ACCEPT already settled interchangeable。可以跳过「看见 Process 回了 REJECT 就已经不能整块执行候选 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样做实现 candidate 缓存、怎样在 Finalize 套用。
- REJECT → consensus assumes not valid ≠ block invalid。那是不变量 540（455 item 1 余量）。
- REJECT → prevote nil ≠ Verify REJECT whole vote。那是不变量 541（455 item 2 余量）。
- ProcessProposal MAY fully execute 正式三事 bundled。那是不变量 452。
