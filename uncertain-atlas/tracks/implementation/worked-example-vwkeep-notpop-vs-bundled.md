# 例：看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo不是已经 Verify When 正式流程 bundled；看见populate ExtendedCommitInfo in h+1 Prepare不是已经写进 last_commit；看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo不是已经 ExtendedCommitInfo 就已经进了块

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyKeep h+1-Prepare not already last_commit / not already in-block / not already same-path 正式三事（517 余量）/ not 1335 vwkeep-notpop interchangeable / not 517 verifywhen-keepdiscard-vs-bundled bundled interchangeable」，不是 verifywhen keepdiscard vs bundled bundled（517），也不是已经 ExtendedCommitInfo Notes 票序（441），也不是已经 Prepare ECI 就是 Process CommitInfo（443）。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方三件事

1. **看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo / 看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1335 vwkeep-notpop interchangeable / 1334 vwkeep-notkeep interchangeable，也不是已经 VerifyKeep h+1-Prepare not already last_commit / not already in-block / not already same-path 正式三事 bundled（517 item 2 余量） interchangeable / 517 vwkeep item 2 interchangeable。**  
   官方把用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo和已经 Verify When 正式流程 bundled写成两件。看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo，不是已经 Verify When 正式流程 bundled。

2. **看见populate ExtendedCommitInfo in h+1 Prepare / 看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1335 vwkeep-notpop interchangeable / 1336 vwkeep-notrej interchangeable，也不是已经 ExtendedCommitInfo Notes 票序 interchangeable / 441 ExtendedCommitInfo Notes 票序 interchangeable。**  
   官方把populate ExtendedCommitInfo in h+1 Prepare和已经写进 last_commit写成两件。看见populate ExtendedCommitInfo in h+1 Prepare，不是已经写进 last_commit。

3. **看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo / 看见populate ExtendedCommitInfo in h+1 Prepare / 这份对象 is not already 已经 ExtendedCommitInfo 就已经进了块 interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1335 vwkeep-notpop interchangeable / 1334 vwkeep-notkeep interchangeable，也不是已经 Prepare ECI 就是 Process CommitInfo interchangeable / 443 Prepare ECI 就是 Process CommitInfo interchangeable。**  
   官方把用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo和已经 ExtendedCommitInfo 就已经进了块写成两件。看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo，不是已经 ExtendedCommitInfo 就已经进了块。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方为什么这样拆

- **populate ExtendedCommitInfo in h+1 Prepare 不是已经写进 last_commit interchangeable：官方把 h+1 Prepare 用途单句和 last_commit 分开。**
- **看见 h+1 自己当提议者 不是已经写进 last_commit：本页钉留给下一高 Prepare，不是本高 last_commit。**
- **看见填 ExtendedCommitInfo 不是已经 ExtendedCommitInfo 就已经进了块：441/443 钉 Notes/Usage 异路，本页钉 When step 4 用途单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经ExtendedCommitInfo Notes 票序（441） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经Prepare ECI 就是 Process CommitInfo（443） |
| 已经 ExtendedCommitInfo 就已经进了块 | 不是已经 ExtendedCommitInfo 就已经进了块 | 不是已经1334 vwkeep-notkeep |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyKeep h+1-Prepare not already last_commit / not already in-block / not already same-path 正式三事（517 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经写进 last_commit、是不是已经 ExtendedCommitInfo 就已经进了块。可以跳过「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。517 VerifyVoteExtension When keepdiscard bundled unbundling 在本页 item 2 续；续 [`worked-example-vwkeep-notrej-vs-bundled.md`](worked-example-vwkeep-notrej-vs-bundled.md)（不变量 1336 item 3）。

## 本页不抄

- 怎样做写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
- 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
