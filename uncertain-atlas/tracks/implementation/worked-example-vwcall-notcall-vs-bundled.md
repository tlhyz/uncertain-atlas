# 例：看见带有效签就会调 VerifyVoteExtension不是已经 Verify When 正式流程 bundled；看见calls VerifyVoteExtension不是已经验过扩展；看见带有效签就会调 VerifyVoteExtension不是已经 Accept

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyCall call not already Verify-When / not already verified / not already Accept 正式三事（515 余量）/ not 1328 vwcall-notcall interchangeable / not 515 verifywhen-call-vs-bundled bundled interchangeable」，不是 verifywhen call vs bundled bundled（515），也不是已经 Verify When 正式流程（435），也不是已经 step 1 discard（514）。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见带有效签就会调 VerifyVoteExtension / 看见带有效签就会调 VerifyVoteExtension 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1328 vwcall-notcall interchangeable / 1329 vwcall-notrecv interchangeable，也不是已经 VerifyCall call not already Verify-When / not already verified / not already Accept 正式三事 bundled（515 item 1 余量） interchangeable / 515 vwcall item 1 interchangeable。**  
   官方把带有效签就会调 VerifyVoteExtension和已经 Verify When 正式流程 bundled写成两件。看见带有效签就会调 VerifyVoteExtension，不是已经 Verify When 正式流程 bundled。

2. **看见calls VerifyVoteExtension / 看见带有效签就会调 VerifyVoteExtension / 这份对象 is not already 已经验过扩展 interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1328 vwcall-notcall interchangeable / 1330 vwcall-notbefore interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把calls VerifyVoteExtension和已经验过扩展写成两件。看见calls VerifyVoteExtension，不是已经验过扩展。

3. **看见带有效签就会调 VerifyVoteExtension / 看见calls VerifyVoteExtension / 这份对象 is not already 已经 Accept interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1328 vwcall-notcall interchangeable / 1329 vwcall-notrecv interchangeable，也不是已经 step 1 discard interchangeable / 514 step 1 discard interchangeable。**  
   官方把带有效签就会调 VerifyVoteExtension和已经 Accept写成两件。看见带有效签就会调 VerifyVoteExtension，不是已经 Accept。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **calls VerifyVoteExtension 不是 Verify When 正式流程 bundled interchangeable：官方把 step 2 call 单句和 steps 1/3/4 bundled 分开。**
- **看见 CometBFT 会调 不是已经验过扩展：435 第二件事 bundled 常被写成会叫就是已经验过，本页钉 step 2 只是 call。**
- **看见 Else 不是已经 step 1 discard：514 钉 step 1 无有效签先丢掉，本页钉 step 1 通过后才会 call。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经验过扩展 | 不是已经验过扩展 | 不是已经step 1 discard（514） |
| 已经 Accept | 不是已经 Accept | 不是已经1329 vwcall-notrecv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyCall call not already Verify-When / not already verified / not already Accept 正式三事（515 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经验过扩展、是不是已经 Accept。可以跳过「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable」。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。515 VerifyVoteExtension When call bundled unbundling 在本页 item 1 启动；续 [`worked-example-vwcall-notrecv-vs-bundled.md`](worked-example-vwcall-notrecv-vs-bundled.md)（不变量 1329 item 2）。

## 本页不抄

- 怎样做填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
