# 例：看见step 3 在 keep 或 discard 之前不是已经 Verify When 正式流程 bundled；看见step 3 before keep/discard不是已经写进 last_commit；看见step 3 在 keep 或 discard 之前不是已经 ACCEPT 留给 h+1 Prepare bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatusWhen before-keep not already Verify-When / not already ACCEPT-keep / not already REJECT-discard 正式三事（516 余量）/ not 1333 vwstat-notkeep interchangeable / not 516 verifywhen-status-vs-bundled bundled interchangeable」，不是 verifywhen status vs bundled bundled（516），也不是已经 Verify When 正式流程（435），也不是已经 迟到扩展（352）。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见step 3 在 keep 或 discard 之前 / 看见step 3 在 keep 或 discard 之前 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1333 vwstat-notkeep interchangeable / 1331 vwstat-notret interchangeable，也不是已经 VerifyStatusWhen before-keep not already Verify-When / not already ACCEPT-keep / not already REJECT-discard 正式三事 bundled（516 item 3 余量） interchangeable / 516 vwstat item 3 interchangeable。**  
   官方把step 3 在 keep 或 discard 之前和已经 Verify When 正式流程 bundled写成两件。看见step 3 在 keep 或 discard 之前，不是已经 Verify When 正式流程 bundled。

2. **看见step 3 before keep/discard / 看见step 3 在 keep 或 discard 之前 / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1333 vwstat-notkeep interchangeable / 1332 vwstat-notafter interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把step 3 before keep/discard和已经写进 last_commit写成两件。看见step 3 before keep/discard，不是已经写进 last_commit。

3. **看见step 3 在 keep 或 discard 之前 / 看见step 3 before keep/discard / 这份对象 is not already 已经 ACCEPT 留给 h+1 Prepare bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1333 vwstat-notkeep interchangeable / 1331 vwstat-notret interchangeable，也不是已经 迟到扩展 interchangeable / 352 迟到扩展 interchangeable。**  
   官方把step 3 在 keep 或 discard 之前和已经 ACCEPT 留给 h+1 Prepare bundled写成两件。看见step 3 在 keep 或 discard 之前，不是已经 ACCEPT 留给 h+1 Prepare bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **step 3 before keep/discard 不是已经写进 last_commit interchangeable：官方把 step 3 return 和 step 4 ACCEPT/REJECT 后效分开。**
- **看见回了 status 不是已经 ACCEPT 留给 h+1 Prepare：435 钉 step 4 后效，本页钉 step 3 在 keep/discard 之前。**
- **看见 Application returns 不是已经 REJECT 丢掉 Precommit：435 钉 step 4 discard，本页钉 step 3 return 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经迟到扩展（352） |
| 已经 ACCEPT 留给 h+1 Prepare bundled | 不是已经 ACCEPT 留给 h+1 Prepare bundled | 不是已经1331 vwstat-notret |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatusWhen before-keep not already Verify-When / not already ACCEPT-keep / not already REJECT-discard 正式三事（516 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经写进 last_commit、是不是已经 ACCEPT 留给 h+1 Prepare bundled。可以跳过「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable」。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。516 VerifyVoteExtension When status bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
