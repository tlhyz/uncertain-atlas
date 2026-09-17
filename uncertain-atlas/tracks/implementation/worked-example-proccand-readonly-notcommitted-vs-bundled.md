# 例：看见 Application checks/processes the proposed block, which is read-only / read-only checks/processes is not already mutate committed state 不是已经 ProcessProposal 候选执行 bundled interchangeable / 已经改了上一份已提交状态 interchangeable / 已经 async 了还能 Reject interchangeable

**层次**：实现 / ProcessProposal read-only checks/processes not mutate committed 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「read-only checks/processes not mutate committed 不是 ProcessProposal 候选执行 bundled interchangeable / 不是已经改了上一份已提交状态 interchangeable / 不是已经 async 了还能 Reject interchangeable」，不是 ProcessProposal 候选执行 bundled（452），也不是 Process 不得改已提交状态 bundled（349），也不是 Process 调用是同步的 / async 不能再 Reject bundled（354）。不要另写怎样实现 candidate 缓存。

## 官方三件事

规范把 ProcessProposal 里 read-only checks/processes、不得 mutate committed state、与 async 之后还能 Reject 分开写成三件独立的实现事，不是「看见 Process 处理了拟议块就已经改了上一份已提交状态 interchangeable、已经 Process 349 Req 9 interchangeable、已经 async 了还能 Reject interchangeable」一件事：

1. **看见 Application checks/processes the proposed block, which is read-only / 看见 read-only checks/processes is not already mutate committed state 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经改了上一份已提交状态 interchangeable / 已经改了 *s<sub>p,h-1</sub>* interchangeable，也不是已经 Process 不得改已提交状态 bundled（349 余量） interchangeable / 已经 Formal Requirement 9 已经测过 interchangeable / 已经 mutate committed state interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经改了已提交状态 interchangeable / 已经 candidate not committed interchangeable，也不是已经 Process MAY fully execute not already committed bundled（545 余量） interchangeable / 已经 immediate execution 交差 interchangeable / 已经是 ExecuteTxState interchangeable，也不是已经 Prepare/Process 立刻执行出候选 bundled（311 余量） interchangeable / 已经不得改 ExecuteTxState interchangeable。**  
   官方写：The Application checks/processes the proposed block, which is read-only, and returns `ACCEPT` or `REJECT`。看见 read-only，不是已经 Process 不得改已提交状态（349 余量） interchangeable——452 bundled 常与 349 混成「read-only = 已经 Req 9 测过 = 已经 mutate committed」，本页钉 read-only checks/processes not mutate committed 单句。看见 checks/processes，不是已经 candidate state must be kept（544 余量） interchangeable——544 钉 candidate not committed，本页钉 read-only 处理边界。看见 read-only，不是已经 Process MAY fully execute not committed（545 余量） interchangeable——545 钉 MAY execute not committed，本页钉 read-only checks/processes 单句。
2. **看见 read-only checks/processes is not immediate execution already committed / 看见 checks/processes 不是已经立刻执行就已经交差 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经立刻执行就已经交差 interchangeable / 已经 immediate execution 交差 interchangeable，也不是已经 Process MAY fully execute not already committed bundled（545 余量） interchangeable / 已经 MAY execute not committed interchangeable / 已经 Finalize + Commit interchangeable，也不是已经 ProcessProposalResponse.status is ACCEPT bundled（430 余量） interchangeable / 已经 prevote interchangeable / 已经已经交差 interchangeable，也不是已经 FinalizeBlock 套用候选 bundled（460 余量） interchangeable / 已经不用再在 Finalize 执行 interchangeable，也不是已经 candidate state must be kept bundled（544 余量） interchangeable / 已经 candidate not committed interchangeable / 已经 Process 回了 Accept 就换工作状态 interchangeable。**  
   官方把 read-only checks/processes 和 immediate execution 已经交差分开——452 bundled 常与 545 混成「处理了就已经 MAY execute 交差」，本页钉 read-only not immediate execution committed 单句。看见 checks/processes，不是已经 Process MAY fully execute not committed（545 余量） interchangeable——545 钉 Usage MAY execute，本页钉 read-only When/Usage 边界。看见 read-only，不是已经 FinalizeBlock 套用 candidate（460 余量） interchangeable——460 钉 Finalize 确定执行，本页钉 read-only checks/processes 单句。
3. **看见 read-only checks/processes is not async Process can still Reject / 看见 read-only 处理不是已经 async 了还能 Reject 不是已经 ProcessProposal 候选执行 bundled（452） interchangeable / 已经 async 了还能 Reject interchangeable / 已经 Process 调用是同步的 interchangeable，也不是已经 Process 调用是同步的 / async 不能再 Reject bundled（354 余量） interchangeable / 已经 async Process 之后还能 Reject interchangeable / 已经 Process 调用是同步的 interchangeable，也不是已经 Process REJECT prevote nil not async can still Reject bundled（535 余量） interchangeable / 已经 prevote nil interchangeable / 已经 REJECT 是免费过滤 interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 余量） interchangeable / 已经 prevote nil interchangeable / 已经 assumes not valid interchangeable，也不是已经 ProcessProposal When basic checks then async bundled（354 余量） interchangeable / 已经 will not be able to reject interchangeable。**  
   官方 When 写：after doing some basic checks, and process the block asynchronously … will not be able to reject the block。看见 read-only checks/processes，不是已经 async 了还能 Reject interchangeable——452 bundled 第三件事常与 354 混成「read-only = async = 还能 Reject」，本页钉 read-only not async can still Reject 单句。看见 checks/processes，不是已经 Process 调用是同步的 / async 不能再 Reject（354 余量） interchangeable——354 钉 When async path，本页钉 Usage read-only 单句。看见 read-only，不是已经 Process REJECT prevote nil not async（535 余量） interchangeable——535 钉 When prevote nil，本页钉 read-only checks/processes 边界。

怎样做实现 candidate 缓存、怎样在 Finalize 套用 是规范里的做法，本页不抄。ProcessProposal 候选执行 bundled（452）、Process MAY fully execute not committed（543）、Process 调用是同步的 / async 不能再 Reject（354）是另外那套，本页不抄。

## 官方为什么这样拆

- **read-only checks/processes not mutate committed ≠ ProcessProposal 候选执行 bundled interchangeable：** 官方把 read-only 处理和 mutate committed state 分开。
- **read-only not immediate execution committed ≠ MAY execute committed interchangeable：** 官方把 checks/processes read-only 和 immediate execution 交差分开。
- **read-only not async can still Reject ≠ Process async can Reject interchangeable：** 官方把 Usage read-only 和 When async 不能再 Reject 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| read-only checks/processes | 不是 mutate committed | 不是 Process 349 Req 9 bundled（349） |
| read-only processing | 不是 immediate execution committed | 不是 Process MAY execute（543） |
| read-only checks/processes | 不是 async can still Reject | 不是 Process async 不能再 Reject（354） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal read-only checks/processes not mutate committed 正式三事，必须分开 read-only checks/processes 是不是 mutate committed interchangeable / 349 Req 9 interchangeable、read-only 是不是 immediate execution committed interchangeable / 545 MAY execute interchangeable、read-only 是不是 async can still Reject interchangeable / 354 async can Reject interchangeable。可以跳过「看见 Process 处理了拟议块就已经改了上一份已提交状态 interchangeable」。不要另写怎样实现 candidate 缓存。

## 本页不抄

- 怎样做实现 candidate 缓存、怎样在 Finalize 套用。
- Process MAY fully execute not already committed。那是不变量 545（452 item 1 余量）。
- candidate state must be kept ≠ already changed committed state。那是不变量 544（452 item 2 余量）。
- Process 调用是同步的 / async 不能再 Reject。那是不变量 354。
