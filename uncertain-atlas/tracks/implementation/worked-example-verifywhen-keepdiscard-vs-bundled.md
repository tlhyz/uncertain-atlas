# 例：看见 ACCEPT keep vote and extension for h+1 Prepare ExtendedCommitInfo / REJECT deem Precommit invalid and discard / step 4 after Application returns status 不是已经 Verify When 正式流程 interchangeable / 已经写进 last_commit interchangeable / 已经 Verify 过迟到扩展 interchangeable

**层次**：实现 / VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ACCEPT keep for h+1 Prepare / REJECT discard Precommit / step 4 after status return 不是 Verify When 正式流程 interchangeable / 不是已经写进 last_commit interchangeable / 不是已经 Verify 过迟到扩展 interchangeable」，不是 Verify When 正式流程（435），也不是 step 3 return status（516），也不是迟到扩展 MAY 不加 Verify（352）。不要另写怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方三件事

规范把 VerifyVoteExtension When step 4 里 ACCEPT 留票留扩展给 h+1 Prepare、REJECT 丢掉 Precommit、接在 step 3 return 之后写成三件独立的实现事，不是「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable、已经 REJECT 丢掉 Precommit interchangeable」一件事：

1. **看见 If the Application returns `ACCEPT`, _p_ will keep the received vote, together with its corresponding vote extension in its internal data structures / 看见 ACCEPT 会把票和扩展留在内部结构 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经写进 last_commit interchangeable，也不是已经 ExtendedCommitInfo 就已经进了块 interchangeable / 已经交差 interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info（352） interchangeable / 已经 Verify 过 interchangeable，也不是已经 Prepare 里有 ExtendedCommitInfo 就已经应用验完（440） interchangeable / 已经 Verify 过扩展 interchangeable，也不是已经 Application returns status bundled（516） interchangeable / 已经 Accept interchangeable。**  
   官方 When step 4 ACCEPT 写：_p_ will keep the received vote, together with its corresponding vote extension in its internal data structures。看见 keep vote and extension，不是已经 Verify When 正式流程（435） interchangeable——435 钉 steps 1–4 bundled，本页钉 step 4 ACCEPT keep 单句。看见留在内部结构，不是已经写进 last_commit interchangeable——435 第三件事 bundled 常被写成「ACCEPT 就已经写进 last_commit」，本页钉 keep 在内部结构、给 h+1 Prepare 用。看见收下了，不是已经 +2/3 之后才进来的扩展写进了 commit info（352） interchangeable——352 钉迟到扩展 MAY 路径，本页钉正常 When step 4 ACCEPT keep。
2. **看见 It will be used to populate the ExtendedCommitInfo structure in calls to `PrepareProposal`, in rounds of height _h + 1_ where _p_ is the proposer / 看见用来在 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经写进 last_commit interchangeable，也不是已经 ExtendedCommitInfo 就已经进了块 interchangeable / 已经 Prepare 带了扩展 interchangeable，也不是已经 ExtendedCommitInfo Notes 票序 bundled（441） interchangeable / 已经按投票权排好 interchangeable，也不是已经 Prepare 的 ExtendedCommitInfo 就是 Process 的 CommitInfo（443） interchangeable / 已经同一路 interchangeable，也不是已经 Application returns status bundled（516） interchangeable / 已经 Accept interchangeable。**  
   官方 When step 4 ACCEPT 续：It will be used to populate the ExtendedCommitInfo structure in calls to PrepareProposal, in rounds of height h+1 where p is the proposer。看见 populate ExtendedCommitInfo in h+1 Prepare，不是已经 Verify When 正式流程（435） interchangeable——435 钉 bundled 四步，本页钉 step 4 h+1 Prepare 用途单句。看见 h+1 自己当提议者，不是已经写进 last_commit interchangeable——本页钉留给下一高 Prepare，不是本高 last_commit。看见填 ExtendedCommitInfo，不是已经 ExtendedCommitInfo 就已经进了块 interchangeable——441/443 钉 Notes/Usage 异路，本页钉 When step 4 用途单句。
3. **看见 If the Application returns `REJECT`, _p_ will deem the Precommit message invalid and discard it / 看见 REJECT 会把 Precommit 当非法丢掉 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经 step 1 discard bundled（514） interchangeable / 已经跳过 Verify interchangeable，也不是已经 VerifyVoteExtensionResponse.status REJECT 就已经当成块非法 bundled（433） interchangeable / 已经 Process REJECT prevote nil interchangeable，也不是已经 step 3 return status bundled（516） interchangeable / 已经 Accept interchangeable，也不是已经验签拒收整张 Precommit 就已经是块非法（34） interchangeable / 已经不能收这张 Precommit interchangeable，也不是已经 step 4 after Application returns status bundled（435 step 3） interchangeable / 已经 REJECT 丢掉 Precommit bundled interchangeable。**  
   官方 When step 4 REJECT 写：_p_ will deem the Precommit message invalid and discard it。看见 REJECT discard Precommit，不是已经 Verify When 正式流程（435） interchangeable——435 钉 bundled 四步，本页钉 step 4 REJECT discard 单句。看见丢掉了，不是已经 step 1 discard（514） interchangeable——514 钉无有效签先丢掉，本页钉 Application REJECT 后丢掉。看见 deem invalid and discard，不是已经 Verify 回包栏（433） interchangeable——433 钉 status 语义，本页钉 When step 4 discard 单句。看见 step 4 在 return 之后，不是已经 Application returns status（516） interchangeable——516 钉 step 3 return，本页钉 step 4 后效单句。

怎样做写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit 是规范里的做法，本页不抄。Verify When 正式流程（435）、step 3 return status（516）、迟到扩展 MAY 不加 Verify（352）、Verify 回包栏（433）是另外那套，本页不抄。

## 官方为什么这样拆

- **ACCEPT keep for h+1 Prepare ≠ Verify When 正式流程 bundled interchangeable：** 官方把 step 4 ACCEPT keep 单句和 steps 1–3 bundled 分开。
- **populate ExtendedCommitInfo in h+1 Prepare ≠ 已经写进 last_commit interchangeable：** 官方把 h+1 Prepare 用途单句和 last_commit / 迟到扩展已经 Verify 过分开。
- **REJECT discard Precommit ≠ step 1 discard bundled interchangeable：** 官方把 Application REJECT 后丢掉和 step 1 无有效签先丢掉分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ACCEPT keep vote and extension | 不是 Verify When bundled（435） | 不是 already last_commit |
| populate ExtendedCommitInfo in h+1 Prepare | 不是 already in block | 不是 late extension MAY skip Verify（352） |
| REJECT discard Precommit | 不是 step 1 discard（514） | 不是 Verify response bar bundled（433） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When ACCEPT keep or REJECT discard 正式三事，必须分开 ACCEPT keep 是不是 Verify When 正式流程 bundled interchangeable / 已经写进 last_commit interchangeable、populate ExtendedCommitInfo in h+1 Prepare 是不是已经进了块 interchangeable / 已经 Prepare 带了扩展 interchangeable、REJECT discard 是不是 step 1 discard bundled interchangeable / 已经当成块非法 interchangeable。可以跳过「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」。不要另写怎样写 ExtendedCommitInfo。

## 本页不抄

- 怎样做写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
- Verify When 正式流程 / 带有效签就会调 Verify / Application returns status。那是不变量 435 / 515 / 516。
- step 1 discard invalid extension。那是不变量 514。
- VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法。那是不变量 433。
- 迟到扩展 MAY 不加 Verify 就已经 Verify 过。那是不变量 352。
