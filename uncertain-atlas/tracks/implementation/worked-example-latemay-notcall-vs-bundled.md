# 例：看见不再叫 VerifyVoteExtension不是已经 Verify 过；看见without calling VerifyVoteExtension不是已经建议按 Verify 同款逻辑再看一遍；看见不再叫 VerifyVoteExtension不是已经 Verify When step 2 call bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateMay without-call not already verified / not already suggested-recheck / not already step-2-call 正式三事（518 余量）/ not 1324 latemay-notcall interchangeable / not 518 verifywhen-latemay-vs-bundled bundled interchangeable」，不是 verifywhen latemay vs bundled bundled（518），也不是已经 +2/3 未 Verify（519），也不是已经 Req 6 must Accept（348）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见不再叫 VerifyVoteExtension / 看见不再叫 VerifyVoteExtension 这份对象 is not already 已经 Verify 过 interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1324 latemay-notcall interchangeable / 1322 latemay-notadd interchangeable，也不是已经 LateMay without-call not already verified / not already suggested-recheck / not already step-2-call 正式三事 bundled（518 item 3 余量） interchangeable / 518 latemay item 3 interchangeable。**  
   官方把不再叫 VerifyVoteExtension和已经 Verify 过写成两件。看见不再叫 VerifyVoteExtension，不是已经 Verify 过。

2. **看见without calling VerifyVoteExtension / 看见不再叫 VerifyVoteExtension / 这份对象 is not already 已经建议按 Verify 同款逻辑再看一遍 interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1324 latemay-notcall interchangeable / 1323 latemay-notround interchangeable，也不是已经 +2/3 未 Verify interchangeable / 519 +2/3 未 Verify interchangeable。**  
   官方把without calling VerifyVoteExtension和已经建议按 Verify 同款逻辑再看一遍写成两件。看见without calling VerifyVoteExtension，不是已经建议按 Verify 同款逻辑再看一遍。

3. **看见不再叫 VerifyVoteExtension / 看见without calling VerifyVoteExtension / 这份对象 is not already 已经 Verify When step 2 call bundled interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1324 latemay-notcall interchangeable / 1322 latemay-notadd interchangeable，也不是已经 Req 6 must Accept interchangeable / 348 Req 6 must Accept interchangeable。**  
   官方把不再叫 VerifyVoteExtension和已经 Verify When step 2 call bundled写成两件。看见不再叫 VerifyVoteExtension，不是已经 Verify When step 2 call bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **without calling Verify 不是已经 Verify 过 interchangeable：官方把可以不叫 Verify 和已经 Verify 分开。**
- **看见不再叫 不是已经建议按 Verify 同款逻辑再看一遍：352 钉 Prepare 侧建议再看，本页钉 When 侧 MAY 不调 Verify。**
- **看见省略 to verify it 不是已经 Verify When step 2 call：515 钉正常 When 必须 call，本页钉迟到 MAY 不调。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify 过 | 不是已经 Verify 过 | 不是已经+2/3 未 Verify（519） |
| 已经建议按 Verify 同款逻辑再看一遍 | 不是已经建议按 Verify 同款逻辑再看一遍 | 不是已经Req 6 must Accept（348） |
| 已经 Verify When step 2 call bundled | 不是已经 Verify When step 2 call bundled | 不是已经1322 latemay-notadd |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateMay without-call not already verified / not already suggested-recheck / not already step-2-call 正式三事（518 余量），必须分开是不是已经 Verify 过、是不是已经建议按 Verify 同款逻辑再看一遍、是不是已经 Verify When step 2 call bundled。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经又叫了 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。518 VerifyVoteExtension When latemay bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
