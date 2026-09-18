# 例：看见MAY 用 commit info 里的扩展改提案不是已经 Verify 过；看见未 Verify 前提下 MAY 使用不是已经 ExtendedCommitInfo 就已经进了块；看见MAY 用 commit info 里的扩展改提案不是已经 Prepare 改列表 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 迟到扩展脚注。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量）/ not 1320 whenlate-notuse interchangeable / not 519 preparewhen-lateext-unverified-vs-bundled bundled interchangeable」，不是 preparewhen lateext unverified vs bundled bundled（519），也不是已经 Prepare 改列表（355），也不是已经 到了 H 已经 Prepare 带了扩展（330）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见MAY 用 commit info 里的扩展改提案 / 看见MAY 用 commit info 里的扩展改提案 这份对象 is not already 已经 Verify 过 interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1320 whenlate-notuse interchangeable / 1319 whenlate-notver interchangeable，也不是已经 LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事 bundled（519 item 2 余量） interchangeable / 519 whenlate item 2 interchangeable。**  
   官方把MAY 用 commit info 里的扩展改提案和已经 Verify 过写成两件。看见MAY 用 commit info 里的扩展改提案，不是已经 Verify 过。

2. **看见未 Verify 前提下 MAY 使用 / 看见MAY 用 commit info 里的扩展改提案 / 这份对象 is not already 已经 ExtendedCommitInfo 就已经进了块 interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1320 whenlate-notuse interchangeable / 1321 whenlate-notsug interchangeable，也不是已经 Prepare 改列表 interchangeable / 355 Prepare 改列表 interchangeable。**  
   官方把未 Verify 前提下 MAY 使用和已经 ExtendedCommitInfo 就已经进了块写成两件。看见未 Verify 前提下 MAY 使用，不是已经 ExtendedCommitInfo 就已经进了块。

3. **看见MAY 用 commit info 里的扩展改提案 / 看见未 Verify 前提下 MAY 使用 / 这份对象 is not already 已经 Prepare 改列表 bundled interchangeable，也不是已经 preparewhen lateext unverified vs bundled bundled（519） interchangeable / 1320 whenlate-notuse interchangeable / 1319 whenlate-notver interchangeable，也不是已经 到了 H 已经 Prepare 带了扩展 interchangeable / 330 到了 H 已经 Prepare 带了扩展 interchangeable。**  
   官方把MAY 用 commit info 里的扩展改提案和已经 Prepare 改列表 bundled写成两件。看见MAY 用 commit info 里的扩展改提案，不是已经 Prepare 改列表 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **MAY use commit info extensions 不是已经 Verify 过 interchangeable：官方把 MAY 使用和已经 Verify 分开。**
- **看见改提案 不是已经 ExtendedCommitInfo 就已经进了块：359/441 钉 Notes/Usage 异路，本页钉 Prepare 侧 MAY 使用。**
- **看见 MAY 用扩展 不是已经 Prepare 改列表 bundled：那是不变量 355。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify 过 | 不是已经 Verify 过 | 不是已经Prepare 改列表（355） |
| 已经 ExtendedCommitInfo 就已经进了块 | 不是已经 ExtendedCommitInfo 就已经进了块 | 不是已经到了 H 已经 Prepare 带了扩展（330） |
| 已经 Prepare 改列表 bundled | 不是已经 Prepare 改列表 bundled | 不是已经1319 whenlate-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateUnverified MAY-use not already verified / not already in-block / not already Prepare-list 正式三事（519 余量），必须分开是不是已经 Verify 过、是不是已经 ExtendedCommitInfo 就已经进了块、是不是已经 Prepare 改列表 bundled。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。519 PrepareProposal When lateext-unverified bundled unbundling 在本页 item 2 续；续 [`worked-example-whenlate-notsug-vs-bundled.md`](worked-example-whenlate-notsug-vs-bundled.md)（不变量 1321 item 3）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
