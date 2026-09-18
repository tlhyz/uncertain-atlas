# 例：看见REJECT 会把 Precommit 当非法丢掉不是已经 Verify When 正式流程 bundled；看见REJECT discard Precommit不是已经 step 1 discard bundled；看见REJECT 会把 Precommit 当非法丢掉不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量）/ not 1336 vwkeep-notrej interchangeable / not 517 verifywhen-keepdiscard-vs-bundled bundled interchangeable」，不是 verifywhen keepdiscard vs bundled bundled（517），也不是已经 step 1 discard（514），也不是已经 Verify 回包栏（433）。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方三件事

1. **看见REJECT 会把 Precommit 当非法丢掉 / 看见REJECT 会把 Precommit 当非法丢掉 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1336 vwkeep-notrej interchangeable / 1334 vwkeep-notkeep interchangeable，也不是已经 VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事 bundled（517 item 3 余量） interchangeable / 517 vwkeep item 3 interchangeable。**  
   官方把REJECT 会把 Precommit 当非法丢掉和已经 Verify When 正式流程 bundled写成两件。看见REJECT 会把 Precommit 当非法丢掉，不是已经 Verify When 正式流程 bundled。

2. **看见REJECT discard Precommit / 看见REJECT 会把 Precommit 当非法丢掉 / 这份对象 is not already 已经 step 1 discard bundled interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1336 vwkeep-notrej interchangeable / 1335 vwkeep-notpop interchangeable，也不是已经 step 1 discard interchangeable / 514 step 1 discard interchangeable。**  
   官方把REJECT discard Precommit和已经 step 1 discard bundled写成两件。看见REJECT discard Precommit，不是已经 step 1 discard bundled。

3. **看见REJECT 会把 Precommit 当非法丢掉 / 看见REJECT discard Precommit / 这份对象 is not already 已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1336 vwkeep-notrej interchangeable / 1334 vwkeep-notkeep interchangeable，也不是已经 Verify 回包栏 interchangeable / 433 Verify 回包栏 interchangeable。**  
   官方把REJECT 会把 Precommit 当非法丢掉和已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法写成两件。看见REJECT 会把 Precommit 当非法丢掉，不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方为什么这样拆

- **REJECT discard Precommit 不是 step 1 discard bundled interchangeable：官方把 Application REJECT 后丢掉和 step 1 无有效签先丢掉分开。**
- **看见丢掉了 不是已经 Verify 回包栏：433 钉 status 语义，本页钉 When step 4 discard 单句。**
- **看见 step 4 在 return 之后 不是已经 Application returns status：516 钉 step 3 return，本页钉 step 4 后效单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经step 1 discard（514） |
| 已经 step 1 discard bundled | 不是已经 step 1 discard bundled | 不是已经Verify 回包栏（433） |
| 已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 | 不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 | 不是已经1334 vwkeep-notkeep |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyKeep REJECT-discard not already Verify-When / not already step-1-discard / not already block-invalid 正式三事（517 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经 step 1 discard bundled、是不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法。可以跳过「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。517 VerifyVoteExtension When keepdiscard bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
- 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
