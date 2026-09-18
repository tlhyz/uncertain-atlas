# 例：看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify不是已经迟到扩展 bundled；看见MAY add without Verify不是已经 Verify 过；看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify不是已经 Verify When 正式流程 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「LateMay MAY-add not already 352-bundled / not already verified / not already step-2-call 正式三事（518 余量）/ not 1322 latemay-notadd interchangeable / not 518 verifywhen-latemay-vs-bundled bundled interchangeable」，不是 verifywhen latemay vs bundled bundled（518），也不是已经 迟到扩展（352），也不是已经 Verify When step 2 call（515）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify / 看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify 这份对象 is not already 已经迟到扩展 bundled interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1322 latemay-notadd interchangeable / 1323 latemay-notround interchangeable，也不是已经 LateMay MAY-add not already 352-bundled / not already verified / not already step-2-call 正式三事 bundled（518 item 1 余量） interchangeable / 518 latemay item 1 interchangeable。**  
   官方把MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify和已经迟到扩展 bundled写成两件。看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify，不是已经迟到扩展 bundled。

2. **看见MAY add without Verify / 看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify / 这份对象 is not already 已经 Verify 过 interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1322 latemay-notadd interchangeable / 1324 latemay-notcall interchangeable，也不是已经 迟到扩展 interchangeable / 352 迟到扩展 interchangeable。**  
   官方把MAY add without Verify和已经 Verify 过写成两件。看见MAY add without Verify，不是已经 Verify 过。

3. **看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify / 看见MAY add without Verify / 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen latemay vs bundled bundled（518） interchangeable / 1322 latemay-notadd interchangeable / 1323 latemay-notround interchangeable，也不是已经 Verify When step 2 call interchangeable / 515 Verify When step 2 call interchangeable。**  
   官方把MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify和已经 Verify When 正式流程 bundled写成两件。看见MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify，不是已经 Verify When 正式流程 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **MAY add without Verify 不是迟到扩展 bundled interchangeable：官方把 MAY add 单句和 352 bundled 三事分开。**
- **看见写进 ExtendedCommitInfo 不是已经 Verify 过：352 第一件事 bundled 常被写成写进了就已经 Verify 过，本页钉 MAY 路径可以不叫 Verify。**
- **看见 without calling VerifyVoteExtension 不是已经 Verify When step 2 call：515 钉正常 When call，本页钉迟到 MAY 不调 Verify。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经迟到扩展 bundled | 不是已经迟到扩展 bundled | 不是已经迟到扩展（352） |
| 已经 Verify 过 | 不是已经 Verify 过 | 不是已经Verify When step 2 call（515） |
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经1323 latemay-notround |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 LateMay MAY-add not already 352-bundled / not already verified / not already step-2-call 正式三事（518 余量），必须分开是不是已经迟到扩展 bundled、是不是已经 Verify 过、是不是已经 Verify When 正式流程 bundled。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经又叫了 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。518 VerifyVoteExtension When latemay bundled unbundling 在本页 item 1 启动；续 [`worked-example-latemay-notround-vs-bundled.md`](worked-example-latemay-notround-vs-bundled.md)（不变量 1323 item 2）。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
