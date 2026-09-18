# 例：看见建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify；看见suggested validate like Verify不是已经 Verify When step 2 call bundled；看见建议按 Verify 同款逻辑再看一遍不是已经正确进程必须 Verify Accept

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateUnverified suggested not already engine-re-Verify / not already step-2-call / not already Req-6 正式三事（519 余量）/ not 1321 whenlate-notsug interchangeable / not 519 preparewhen-lateext-unverified-vs-bundled bundled interchangeable」，不是 preparewhen lateext unverified vs bundled bundled（519），也不是已经 Verify When step 2 call（515），也不是已经 Req 6 must Accept（348）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见建议按 Verify 同款逻辑再看一遍 / 看见建议按 Verify 同款逻辑再看一遍 这份对象 is not already 已经是引擎会再 Verify interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1321 whenlate-notsug interchangeable / 1319 whenlate-notver interchangeable，也不是已经 LateUnverified suggested not already engine-re-Verify / not already step-2-call / not already Req-6 正式三事 bundled（519 item 3 余量） interchangeable / 519 whenlate item 3 interchangeable。**  
   官方把建议按 Verify 同款逻辑再看一遍和已经是引擎会再 Verify写成两件。看见建议按 Verify 同款逻辑再看一遍，不是已经是引擎会再 Verify。

2. **看见suggested validate like Verify / 看见建议按 Verify 同款逻辑再看一遍 / 这份对象 is not already 已经 Verify When step 2 call bundled interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1321 whenlate-notsug interchangeable / 1320 whenlate-notuse interchangeable，也不是已经 Verify When step 2 call interchangeable / 515 Verify When step 2 call interchangeable。**  
   官方把suggested validate like Verify和已经 Verify When step 2 call bundled写成两件。看见suggested validate like Verify，不是已经 Verify When step 2 call bundled。

3. **看见建议按 Verify 同款逻辑再看一遍 / 看见suggested validate like Verify / 这份对象 is not already 已经正确进程必须 Verify Accept interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1321 whenlate-notsug interchangeable / 1319 whenlate-notver interchangeable，也不是已经 Req 6 must Accept interchangeable / 348 Req 6 must Accept interchangeable。**  
   官方把建议按 Verify 同款逻辑再看一遍和已经正确进程必须 Verify Accept写成两件。看见建议按 Verify 同款逻辑再看一遍，不是已经正确进程必须 Verify Accept。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **suggested validate like Verify 不是已经是引擎会再 Verify interchangeable：官方把应用建议自验和引擎会再 call Verify 分开。**
- **看见建议再看 不是已经 Verify When step 2 call：515 钉引擎会 call Verify，本页钉 Prepare 侧应用建议自验。**
- **看见 same manner 不是已经 Req 6 必须 Accept：那是不变量 348。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是引擎会再 Verify | 不是已经是引擎会再 Verify | 不是已经Verify When step 2 call（515） |
| 已经 Verify When step 2 call bundled | 不是已经 Verify When step 2 call bundled | 不是已经Req 6 must Accept（348） |
| 已经正确进程必须 Verify Accept | 不是已经正确进程必须 Verify Accept | 不是已经1319 whenlate-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateUnverified suggested not already engine-re-Verify / not already step-2-call / not already Req-6 正式三事（519 余量），必须分开是不是已经是引擎会再 Verify、是不是已经 Verify When step 2 call bundled、是不是已经正确进程必须 Verify Accept。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。519 PrepareProposal When lateext-unverified bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
