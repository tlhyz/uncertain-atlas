# 例：看见收到他人 Precommit不是已经 Verify 不对 local process 调用 bundled；看见received from q≠p不是已经本地票也 Verify；看见收到他人 Precommit不是已经 round 0 height h MAY add without calling Verify

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量）/ not 1329 vwcall-notrecv interchangeable / not 515 verifywhen-call-vs-bundled bundled interchangeable」，不是 verifywhen call vs bundled bundled（515），也不是已经 Usage 本地票不调（353），也不是已经 迟到扩展 MAY（352）。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见收到他人 Precommit / 看见收到他人 Precommit 这份对象 is not already 已经 Verify 不对 local process 调用 bundled interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1329 vwcall-notrecv interchangeable / 1328 vwcall-notcall interchangeable，也不是已经 VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事 bundled（515 item 2 余量） interchangeable / 515 vwcall item 2 interchangeable。**  
   官方把收到他人 Precommit和已经 Verify 不对 local process 调用 bundled写成两件。看见收到他人 Precommit，不是已经 Verify 不对 local process 调用 bundled。

2. **看见received from q≠p / 看见收到他人 Precommit / 这份对象 is not already 已经本地票也 Verify interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1329 vwcall-notrecv interchangeable / 1330 vwcall-notbefore interchangeable，也不是已经 Usage 本地票不调 interchangeable / 353 Usage 本地票不调 interchangeable。**  
   官方把received from q≠p和已经本地票也 Verify写成两件。看见received from q≠p，不是已经本地票也 Verify。

3. **看见收到他人 Precommit / 看见received from q≠p / 这份对象 is not already 已经 round 0 height h MAY add without calling Verify interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1329 vwcall-notrecv interchangeable / 1328 vwcall-notcall interchangeable，也不是已经 迟到扩展 MAY interchangeable / 352 迟到扩展 MAY interchangeable。**  
   官方把收到他人 Precommit和已经 round 0 height h MAY add without calling Verify写成两件。看见收到他人 Precommit，不是已经 round 0 height h MAY add without calling Verify。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **received from q≠p 不是不对 local process 调用 bundled interchangeable：官方把 When step 2 收到侧 call 和 Usage 侧本地票不调分开。**
- **看见 q ≠ p 不是已经 ExtendVote When 正式流程：438 钉本地 ExtendVote，本页钉收到他人 Precommit 后 call Verify。**
- **看见 round r height h 不是已经迟到扩展 MAY 不加 Verify：352 钉迟到 MAY，本页钉正常 When step 2 call。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify 不对 local process 调用 bundled | 不是已经 Verify 不对 local process 调用 bundled | 不是已经Usage 本地票不调（353） |
| 已经本地票也 Verify | 不是已经本地票也 Verify | 不是已经迟到扩展 MAY（352） |
| 已经 round 0 height h MAY add without calling Verify | 不是已经 round 0 height h MAY add without calling Verify | 不是已经1328 vwcall-notcall |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyCall recv not already local-also-Verify / not already ExtendVote-When / not already late-MAY 正式三事（515 余量），必须分开是不是已经 Verify 不对 local process 调用 bundled、是不是已经本地票也 Verify、是不是已经 round 0 height h MAY add without calling Verify。可以跳过「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable」。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。515 VerifyVoteExtension When call bundled unbundling 在本页 item 2 续；续 [`worked-example-vwcall-notbefore-vs-bundled.md`](worked-example-vwcall-notbefore-vs-bundled.md)（不变量 1330 item 3）。

## 本页不抄

- 怎样做填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
