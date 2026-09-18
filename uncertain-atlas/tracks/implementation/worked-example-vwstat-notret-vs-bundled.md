# 例：看见应用回 status不是已经 Verify When 正式流程 bundled；看见returns ACCEPT or REJECT不是已经验过扩展；看见应用回 status不是已经 VerifyVoteExtensionResponse.status bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量）/ not 1331 vwstat-notret interchangeable / not 516 verifywhen-status-vs-bundled bundled interchangeable」，不是 verifywhen status vs bundled bundled（516），也不是已经 Verify When 正式流程（435），也不是已经 Verify 回包栏（433）。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见应用回 status / 看见应用回 status 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1331 vwstat-notret interchangeable / 1332 vwstat-notafter interchangeable，也不是已经 VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事 bundled（516 item 1 余量） interchangeable / 516 vwstat item 1 interchangeable。**  
   官方把应用回 status和已经 Verify When 正式流程 bundled写成两件。看见应用回 status，不是已经 Verify When 正式流程 bundled。

2. **看见returns ACCEPT or REJECT / 看见应用回 status / 这份对象 is not already 已经验过扩展 interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1331 vwstat-notret interchangeable / 1333 vwstat-notkeep interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把returns ACCEPT or REJECT和已经验过扩展写成两件。看见returns ACCEPT or REJECT，不是已经验过扩展。

3. **看见应用回 status / 看见returns ACCEPT or REJECT / 这份对象 is not already 已经 VerifyVoteExtensionResponse.status bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1331 vwstat-notret interchangeable / 1332 vwstat-notafter interchangeable，也不是已经 Verify 回包栏 interchangeable / 433 Verify 回包栏 interchangeable。**  
   官方把应用回 status和已经 VerifyVoteExtensionResponse.status bundled写成两件。看见应用回 status，不是已经 VerifyVoteExtensionResponse.status bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **Application returns ACCEPT/REJECT 不是 Verify When 正式流程 bundled interchangeable：官方把 step 3 return 单句和 steps 1/2/4 bundled 分开。**
- **看见回了 ACCEPT/REJECT 不是已经验过扩展：515 钉 step 2 call 在 return 之前，本页钉 step 3 return 单句。**
- **看见 Application returns 不是已经 Verify 回包栏：433 钉 Response 表语义，本页钉 When step 3 return 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经验过扩展 | 不是已经验过扩展 | 不是已经Verify 回包栏（433） |
| 已经 VerifyVoteExtensionResponse.status bundled | 不是已经 VerifyVoteExtensionResponse.status bundled | 不是已经1332 vwstat-notafter |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatusWhen return not already Verify-When / not already verified / not already status-column 正式三事（516 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经验过扩展、是不是已经 VerifyVoteExtensionResponse.status bundled。可以跳过「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable」。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。516 VerifyVoteExtension When status bundled unbundling 在本页 item 1 启动；续 [`worked-example-vwstat-notafter-vs-bundled.md`](worked-example-vwstat-notafter-vs-bundled.md)（不变量 1332 item 2）。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
