# 例：看见+2/3 之后扩展写进 commit info 没有被 Verify不是已经迟到扩展 bundled；看见写进了 commit info不是已经 Verify 过；看见+2/3 之后扩展写进 commit info 没有被 Verify不是已经 Verify When 正式流程 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateUnverified not-verified not already 352-bundled / not already verified / not already Verify-When 正式三事（519 余量）/ not 1319 whenlate-notver interchangeable / not 519 preparewhen-lateext-unverified-vs-bundled bundled interchangeable」，不是 preparewhen lateext unverified vs bundled bundled（519），也不是已经 迟到扩展（352），也不是已经 Verify When（435）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见+2/3 之后扩展写进 commit info 没有被 Verify / 看见+2/3 之后扩展写进 commit info 没有被 Verify 这份对象 is not already 已经迟到扩展 bundled interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1319 whenlate-notver interchangeable / 1320 whenlate-notuse interchangeable，也不是已经 LateUnverified not-verified not already 352-bundled / not already verified / not already Verify-When 正式三事 bundled（519 item 1 余量） interchangeable / 519 whenlate item 1 interchangeable。**  
   官方把+2/3 之后扩展写进 commit info 没有被 Verify和已经迟到扩展 bundled写成两件。看见+2/3 之后扩展写进 commit info 没有被 Verify，不是已经迟到扩展 bundled。

2. **看见写进了 commit info / 看见+2/3 之后扩展写进 commit info 没有被 Verify / 这份对象 is not already 已经 Verify 过 interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1319 whenlate-notver interchangeable / 1321 whenlate-notsug interchangeable，也不是已经 迟到扩展 interchangeable / 352 迟到扩展 interchangeable。**  
   官方把写进了 commit info和已经 Verify 过写成两件。看见写进了 commit info，不是已经 Verify 过。

3. **看见+2/3 之后扩展写进 commit info 没有被 Verify / 看见写进了 commit info / 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1319 whenlate-notver interchangeable / 1320 whenlate-notuse interchangeable，也不是已经 Verify When interchangeable / 435 Verify When interchangeable。**  
   官方把+2/3 之后扩展写进 commit info 没有被 Verify和已经 Verify When 正式流程 bundled写成两件。看见+2/3 之后扩展写进 commit info 没有被 Verify，不是已经 Verify When 正式流程 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **+2/3 commit info extensions not verified 不是迟到扩展 bundled interchangeable：官方把 not verified 单句和 MAY add without Verify / 建议再看 bundled 分开。**
- **看见写进了 commit info 不是已经 Verify 过：352 第一件事 bundled 常被写成写进了就已经 Verify 过，本页钉未 Verify 单句。**
- **看见 +2/3 之后 不是已经 Verify When 正式流程：正常 When 会 call Verify，本页钉这批没 Verify。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经迟到扩展 bundled | 不是已经迟到扩展 bundled | 不是已经迟到扩展（352） |
| 已经 Verify 过 | 不是已经 Verify 过 | 不是已经Verify When（435） |
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经1320 whenlate-notuse |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateUnverified not-verified not already 352-bundled / not already verified / not already Verify-When 正式三事（519 余量），必须分开是不是已经迟到扩展 bundled、是不是已经 Verify 过、是不是已经 Verify When 正式流程 bundled。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。519 PrepareProposal When lateext-unverified bundled unbundling 在本页 item 1 启动；续 [`worked-example-whenlate-notuse-vs-bundled.md`](worked-example-whenlate-notuse-vs-bundled.md)（不变量 1320 item 2）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
