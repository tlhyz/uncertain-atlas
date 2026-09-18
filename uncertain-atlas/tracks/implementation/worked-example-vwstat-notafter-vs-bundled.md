# 例：看见step 3 在 call VerifyVoteExtension 之后不是已经 step 2 call bundled；看见step 3 after call不是已经 CometBFT 会叫；看见step 3 在 call VerifyVoteExtension 之后不是已经 step 1 discard bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 3。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyStatusWhen after-call not already step-2-call / not already step-1-discard / not already late-MAY 正式三事（516 余量）/ not 1332 vwstat-notafter interchangeable / not 516 verifywhen-status-vs-bundled bundled interchangeable」，不是 verifywhen status vs bundled bundled（516），也不是已经 step 2 call（515），也不是已经 step 1 discard（514）。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见step 3 在 call VerifyVoteExtension 之后 / 看见step 3 在 call VerifyVoteExtension 之后 这份对象 is not already 已经 step 2 call bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1332 vwstat-notafter interchangeable / 1331 vwstat-notret interchangeable，也不是已经 VerifyStatusWhen after-call not already step-2-call / not already step-1-discard / not already late-MAY 正式三事 bundled（516 item 2 余量） interchangeable / 516 vwstat item 2 interchangeable。**  
   官方把step 3 在 call VerifyVoteExtension 之后和已经 step 2 call bundled写成两件。看见step 3 在 call VerifyVoteExtension 之后，不是已经 step 2 call bundled。

2. **看见step 3 after call / 看见step 3 在 call VerifyVoteExtension 之后 / 这份对象 is not already 已经 CometBFT 会叫 interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1332 vwstat-notafter interchangeable / 1333 vwstat-notkeep interchangeable，也不是已经 step 2 call interchangeable / 515 step 2 call interchangeable。**  
   官方把step 3 after call和已经 CometBFT 会叫写成两件。看见step 3 after call，不是已经 CometBFT 会叫。

3. **看见step 3 在 call VerifyVoteExtension 之后 / 看见step 3 after call / 这份对象 is not already 已经 step 1 discard bundled interchangeable，也不是已经 verifywhen status vs bundled bundled（516） interchangeable / 1332 vwstat-notafter interchangeable / 1331 vwstat-notret interchangeable，也不是已经 step 1 discard interchangeable / 514 step 1 discard interchangeable。**  
   官方把step 3 在 call VerifyVoteExtension 之后和已经 step 1 discard bundled写成两件。看见step 3 在 call VerifyVoteExtension 之后，不是已经 step 1 discard bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **step 3 after call 不是 step 2 call bundled interchangeable：官方把 step 3 return 和 step 2 call 分开。**
- **看见 Application returns 不是已经 step 1 discard：514 钉 step 1 无有效签先丢掉，本页钉 step 3 在 call 之后 return。**
- **看见回了 status 不是已经迟到扩展 MAY 不加 Verify：352 钉迟到 MAY，本页钉正常 When step 3 return。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 step 2 call bundled | 不是已经 step 2 call bundled | 不是已经step 2 call（515） |
| 已经 CometBFT 会叫 | 不是已经 CometBFT 会叫 | 不是已经step 1 discard（514） |
| 已经 step 1 discard bundled | 不是已经 step 1 discard bundled | 不是已经1331 vwstat-notret |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyStatusWhen after-call not already step-2-call / not already step-1-discard / not already late-MAY 正式三事（516 余量），必须分开是不是已经 step 2 call bundled、是不是已经 CometBFT 会叫、是不是已经 step 1 discard bundled。可以跳过「看见 CometBFT 会叫 VerifyVoteExtension 就已经 Accept interchangeable、已经 REJECT 丢掉 Precommit interchangeable」。不要另写 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。516 VerifyVoteExtension When status bundled unbundling 在本页 item 2 续；续 [`worked-example-vwstat-notkeep-vs-bundled.md`](worked-example-vwstat-notkeep-vs-bundled.md)（不变量 1333 item 3）。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样写 Verify 回包栏、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
