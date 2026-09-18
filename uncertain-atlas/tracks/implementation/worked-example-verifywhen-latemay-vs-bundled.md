# 例：看见 MAY add Precommit and extension to ExtendedCommitInfo without calling VerifyVoteExtension / round 0 height h CommitRound r height h-1 from q≠p / without calling VerifyVoteExtension to verify it 不是已经 Verify When 正式流程 interchangeable / 已经 Verify 过 interchangeable / 已经又叫了 Verify interchangeable

**层次**：实现 / VerifyVoteExtension When late-arriving MAY add without Verify 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When late-arriving MAY 段。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MAY add without Verify / round 0 h-1 Precommit / without calling VerifyVoteExtension 不是迟到扩展 bundled interchangeable / 不是已经 Verify 过 interchangeable / 不是已经又叫了 Verify interchangeable」，不是迟到扩展 bundled（352），也不是 Verify When 正式流程 steps 1–4（435 / 514–517）。不要另写怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。

## 官方三件事

规范把 VerifyVoteExtension When 迟到 MAY 段里 MAY 写入、round 0 / h-1 / CommitRound 前提、without calling VerifyVoteExtension 写成三件独立的实现事，不是「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经是引擎会再 Verify interchangeable、已经又叫了 Verify interchangeable」一件事：

1. **看见 _p_ MAY add the Precommit message and associated extension to ExtendedCommitInfo without calling `VerifyVoteExtension` to verify it / 看见 MAY 把票和扩展写进 ExtendedCommitInfo 不再叫 Verify 不是已经迟到扩展 bundled（352） interchangeable / 已经 Verify 过 interchangeable / 已经又叫了 Verify interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经 step 2 call bundled（515） interchangeable / 已经带有效签就会调 Verify interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info bundled（352 第一件事） interchangeable / 已经 Accept interchangeable，也不是已经 ACCEPT keep for h+1 Prepare bundled（517） interchangeable / 已经写进 last_commit interchangeable。**  
   官方 When 迟到 MAY 段写：_p_ MAY add the Precommit message and associated extension to ExtendedCommitInfo without calling VerifyVoteExtension to verify it。看见 MAY add without Verify，不是已经迟到扩展（352） interchangeable——352 钉 bundled 三事，本页钉 MAY add without Verify 单句。看见写进 ExtendedCommitInfo，不是已经 Verify 过 interchangeable——352 第一件事 bundled 常被写成「写进了就已经 Verify 过」，本页钉 MAY 路径可以不叫 Verify。看见 without calling VerifyVoteExtension，不是已经 Verify When 正式流程 step 2 call（515） interchangeable——515 钉正常 When call，本页钉迟到 MAY 不调 Verify。
2. **看见 When a node _p_ is in consensus round _0_, height _h_, and _p_ receives a Precommit message for CommitRound _r_, height _h-1_ from validator _q_ (_q_ ≠ _p_) / 看见 round 0 height h 收到上一高度 CommitRound r 的 Precommit 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经 round r height h interchangeable，也不是已经 step 2 call bundled（515） interchangeable / 已经收到他人 Precommit interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable，也不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable / 已经 Verify 过 interchangeable，也不是已经 +2/3 之后才进来的扩展 bundled（352） interchangeable / 已经 last_commit 里有扩展 interchangeable。**  
   官方 When 迟到 MAY 段前提写：When a node _p_ is in consensus round _0_, height _h_, and _p_ receives a Precommit message for CommitRound _r_, height _h-1_ from validator _q_ (_q_ ≠ _p_)。看见 round 0 height h，不是已经正常 When round _r_ height _h_（515） interchangeable——515 钉正常 When 前提，本页钉 round 0 / h-1 / CommitRound 前提。看见上一高度 Precommit，不是已经 Verify When 正式流程（435） interchangeable——435 钉正常 When 四步，本页钉迟到 MAY 前提。看见 _q_ ≠ _p_，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉本地 ExtendVote 路径，本页钉收到他人迟到 Precommit。
3. **看见 without calling `VerifyVoteExtension` to verify it / 看见不再叫 VerifyVoteExtension 不是已经 Verify 过 interchangeable / 已经 Accept interchangeable，也不是已经建议按 Verify 同款逻辑再看一遍 bundled（352 第二件事） interchangeable / 已经是引擎会再 Verify interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经 Application returns status bundled（516） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable / 已经 Req 6 已经测过 interchangeable。**  
   官方 When 迟到 MAY 段把 without calling VerifyVoteExtension 写在 MAY add 同句。看见 without calling Verify，不是已经 Verify 过 interchangeable——352 bundled 常被写成「写进了就已经 Verify 过」，本页钉可以不叫 Verify。看见不再叫，不是已经建议按 Verify 同款逻辑再看一遍（352 第二件事） interchangeable——352 钉 Prepare 侧建议再看，本页钉 When 侧 MAY 不调 Verify。看见 to verify it 省略，不是已经 Verify When step 2 call（515） interchangeable——515 钉正常 When 必须 call，本页钉迟到 MAY 不调。

怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、Verify When 正式流程（435 / 514–517）、到了 H 已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **MAY add without Verify ≠ 迟到扩展 bundled interchangeable：** 官方把 MAY add without Verify 单句和 +2/3 commit info / 建议再看 bundled 分开。
- **round 0 h-1 CommitRound ≠ 正常 When round r height h interchangeable：** 官方把迟到 MAY 前提和正常 When 前提分开。
- **without calling VerifyVoteExtension ≠ 已经 Verify 过 interchangeable：** 官方把 MAY 不调 Verify 和已经 Verify / 引擎会再 Verify 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MAY add without calling VerifyVoteExtension | 不是 352 bundled | 不是 normal When step 2 call（515） |
| round 0 height h / CommitRound r / height h-1 | 不是 normal When round r height h | 不是 ExtendVote When（438） |
| without calling VerifyVoteExtension | 不是 already verified | 不是 engine will re-Verify（352 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When late-arriving MAY add without Verify 正式三事，必须分开 MAY add without Verify 是不是迟到扩展 bundled interchangeable / 已经 Verify 过 interchangeable、round 0 h-1 CommitRound 是不是正常 When round r height h interchangeable、without calling VerifyVoteExtension 是不是已经又叫了 Verify interchangeable / 已经是引擎会再 Verify interchangeable。可以跳过「看见 last_commit 里有扩展就已经 Verify 过 interchangeable、已经又叫了 Verify interchangeable」。518 VerifyVoteExtension When latemay bundled unbundling 完成（1322 item 1 / 1323 item 2 / 1324 item 3）；精读 [`worked-example-latemay-notadd-vs-bundled.md`](worked-example-latemay-notadd-vs-bundled.md)（不变量 1322 item 1）、[`worked-example-latemay-notround-vs-bundled.md`](worked-example-latemay-notround-vs-bundled.md)（不变量 1323 item 2）、[`worked-example-latemay-notcall-vs-bundled.md`](worked-example-latemay-notcall-vs-bundled.md)（不变量 1324 item 3）。不要另写怎样再验迟到扩展。

## 本页不抄

- 怎样做再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- +2/3 之后才进来的扩展写进了 commit info / 建议按 Verify 同款逻辑再看一遍。那是不变量 352。
- Verify When 正式流程 / step 2 call / ACCEPT keep。那是不变量 435 / 515 / 517。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
