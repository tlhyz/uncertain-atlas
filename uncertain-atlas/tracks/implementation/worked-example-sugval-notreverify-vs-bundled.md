# 例：看见建议自验不是引擎会再 Verify不是已经是引擎会再 Verify；看见not calling VerifyVoteExtension again不是已经又叫了 Verify；看见建议自验不是引擎会再 Verify不是已经 Verify 过

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When step 3 建议自验句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SuggestValidate not-reverify not already verified / not already called-again / not already MAY-add-without-Verify 正式三事（520 余量）/ not 1318 sugval-notreverify interchangeable / not 520 preparewhen-suggestvalidate-vs-bundled bundled interchangeable」，不是 preparewhen suggestvalidate vs bundled bundled（520），也不是已经 +2/3 未 Verify（519），也不是已经 MAY add without Verify（518）。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

1. **看见建议自验不是引擎会再 Verify / 看见建议自验不是引擎会再 Verify 这份对象 is not already 已经是引擎会再 Verify interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1318 sugval-notreverify interchangeable / 1316 sugval-notmust interchangeable，也不是已经 SuggestValidate not-reverify not already verified / not already called-again / not already MAY-add-without-Verify 正式三事 bundled（520 item 3 余量） interchangeable / 520 sugval item 3 interchangeable。**  
   官方把建议自验不是引擎会再 Verify和已经是引擎会再 Verify写成两件。看见建议自验不是引擎会再 Verify，不是已经是引擎会再 Verify。

2. **看见not calling VerifyVoteExtension again / 看见建议自验不是引擎会再 Verify / 这份对象 is not already 已经又叫了 Verify interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1318 sugval-notreverify interchangeable / 1317 sugval-notcall interchangeable，也不是已经 +2/3 未 Verify interchangeable / 519 +2/3 未 Verify interchangeable。**  
   官方把not calling VerifyVoteExtension again和已经又叫了 Verify写成两件。看见not calling VerifyVoteExtension again，不是已经又叫了 Verify。

3. **看见建议自验不是引擎会再 Verify / 看见not calling VerifyVoteExtension again / 这份对象 is not already 已经 Verify 过 interchangeable，也不是已经 preparewhen suggestvalidate vs bundled bundled（520） interchangeable / 1318 sugval-notreverify interchangeable / 1316 sugval-notmust interchangeable，也不是已经 MAY add without Verify interchangeable / 518 MAY add without Verify interchangeable。**  
   官方把建议自验不是引擎会再 Verify和已经 Verify 过写成两件。看见建议自验不是引擎会再 Verify，不是已经 Verify 过。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方为什么这样拆

- **not engine re-Verify 不是已经 Verify 过 interchangeable：官方把建议自验和引擎再 call Verify 分开。**
- **看见不是引擎会再 Verify 不是已经又叫了 Verify：515 钉 Else CometBFT calls VerifyVoteExtension，本页钉 Prepare 侧 suggested 不是 call。**
- **看见建议自验路径 不是已经 MAY add without calling Verify：那是不变量 518。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是引擎会再 Verify | 不是已经是引擎会再 Verify | 不是已经+2/3 未 Verify（519） |
| 已经又叫了 Verify | 不是已经又叫了 Verify | 不是已经MAY add without Verify（518） |
| 已经 Verify 过 | 不是已经 Verify 过 | 不是已经1316 sugval-notmust |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 SuggestValidate not-reverify not already verified / not already called-again / not already MAY-add-without-Verify 正式三事（520 余量），必须分开是不是已经是引擎会再 Verify、是不是已经又叫了 Verify、是不是已经 Verify 过。可以跳过「看见建议按 Verify 同款逻辑再看一遍就已经是引擎会再 Verify interchangeable」。不要另写 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。520 PrepareProposal When suggestvalidate bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
