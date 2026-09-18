# 例：看见step 2 在应用回 status 之前不是已经 Verify When 正式流程 bundled；看见step 2 before status return不是已经写进 last_commit；看见step 2 在应用回 status 之前不是已经 VerifyVoteExtensionResponse.status bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量）/ not 1330 vwcall-notbefore interchangeable / not 515 verifywhen-call-vs-bundled bundled interchangeable」，不是 verifywhen call vs bundled bundled（515），也不是已经 Verify When 正式流程（435），也不是已经 Verify 回包 status（433）。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方三件事

1. **看见step 2 在应用回 status 之前 / 看见step 2 在应用回 status 之前 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1330 vwcall-notbefore interchangeable / 1328 vwcall-notcall interchangeable，也不是已经 VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事 bundled（515 item 3 余量） interchangeable / 515 vwcall item 3 interchangeable。**  
   官方把step 2 在应用回 status 之前和已经 Verify When 正式流程 bundled写成两件。看见step 2 在应用回 status 之前，不是已经 Verify When 正式流程 bundled。

2. **看见step 2 before status return / 看见step 2 在应用回 status 之前 / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1330 vwcall-notbefore interchangeable / 1329 vwcall-notrecv interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把step 2 before status return和已经写进 last_commit写成两件。看见step 2 before status return，不是已经写进 last_commit。

3. **看见step 2 在应用回 status 之前 / 看见step 2 before status return / 这份对象 is not already 已经 VerifyVoteExtensionResponse.status bundled interchangeable，也不是已经 verifywhen call vs bundled bundled（515） interchangeable / 1330 vwcall-notbefore interchangeable / 1328 vwcall-notcall interchangeable，也不是已经 Verify 回包 status interchangeable / 433 Verify 回包 status interchangeable。**  
   官方把step 2 在应用回 status 之前和已经 VerifyVoteExtensionResponse.status bundled写成两件。看见step 2 在应用回 status 之前，不是已经 VerifyVoteExtensionResponse.status bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。

## 官方为什么这样拆

- **step 2 before status return 不是已经验过扩展 interchangeable：官方把 step 2 call 和 step 3 ACCEPT/REJECT return 分开。**
- **看见 CometBFT 会调 不是已经 Application returns ACCEPT/REJECT：435 钉 step 3–4 后效，本页钉 step 2 在 return 之前。**
- **看见 call 了 不是已经 VerifyVoteExtensionResponse.status：433 钉回包栏，本页钉 When step 2 call 单句。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经Verify 回包 status（433） |
| 已经 VerifyVoteExtensionResponse.status bundled | 不是已经 VerifyVoteExtensionResponse.status bundled | 不是已经1328 vwcall-notcall |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyCall before-status not already Verify-When / not already status-column / not already ACCEPT-keep 正式三事（515 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经写进 last_commit、是不是已经 VerifyVoteExtensionResponse.status bundled。可以跳过「看见带有效签就会调 VerifyVoteExtension 就已经验过扩展 interchangeable、已经 Accept interchangeable」。不要另写 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。515 VerifyVoteExtension When call bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
- 怎样填 VerifyVoteExtensionRequest、怎样写 ExtendedCommitInfo、怎样在 h+1 Prepare 填 ExtendedCommitInfo。
