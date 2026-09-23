# 例：看见写进去了 / 看见规范允许 / 看见是上一高度 is not already already called-again interchangeable / already must-recall interchangeable / already this-round-verify interchangeable

**层次**：实现 / 下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量）/ not 811 lateext-notrecall interchangeable / not 352 lateext bundled interchangeable」，不是迟到扩展 bundled（352），也不是 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过（809 item 1 余量）或建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify（810 item 2 余量）。不要另写怎样再验迟到扩展。

## 官方三件事

规范把 Methods 里节点在高度 *h*、round 0 收到上一高度 Precommit 时 MAY 写进 `ExtendedCommitInfo` 而不再叫 `VerifyVoteExtension` 和「已经是写进去了就已经又叫了 Verify interchangeable / 已经是规范允许就已经必须再叫 interchangeable / 已经是上一高度就已经是本轮那次 Verify interchangeable / 已经是 lateext bundled interchangeable」分开写成三件独立的实现事，不是「看见写进去了就已经又叫了 Verify interchangeable / 就已经必须再叫 interchangeable / 就已经是本轮那次 Verify interchangeable」一件事：

1. **看见下一高度 round 0 收到上一高度 `CommitRound` 的 Precommit / 看见写进 `ExtendedCommitInfo` / 看见写进去了 is not already 已经又叫了 Verify interchangeable / 已经 called-again interchangeable / 已经又 Verify 交差 interchangeable / 352 lateext bundled interchangeable / 330 veheight interchangeable / lateext-sold-as-verified interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 811 lateext-notrecall interchangeable / 352 lateext item 3 interchangeable，也不是已经下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事 bundled（352 item 3 余量） interchangeable / 352 lateext item 3 interchangeable，也不是已经 Verify 过（809） interchangeable / 810 lateext-notreverify interchangeable / 34 vote-extension-block interchangeable，也不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable。**  
   官方写：MAY 把这张票和扩展写进 `ExtendedCommitInfo`，**不**再叫 `VerifyVoteExtension`。看见写进去了，不是已经又 Verify。看见写进去了，不是已经 called-again interchangeable——352 钉 bundled 三事，本页从 item 3 侧钉 not already called-again 单句。看见下一高度 round 0 写进 ExtendedCommitInfo，不是已经迟到扩展 bundled（352） interchangeable——352 钉 bundled，本页钉 item 3 第一件事。看见写进去了，不是已经 Verify 过（809） interchangeable——809 另钉 item 1。看见写进去了，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。352 lateext vs verified bundled unbundling 在本页 item 3 完成。

2. **看见规范允许 / 看见 MAY 写进 / 看见可以不叫 is not already 已经必须再叫 interchangeable / 已经 must-recall interchangeable / 已经必须再 Verify 交差 interchangeable / 352 lateext bundled interchangeable / 348 req6coherence interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 811 lateext-notrecall interchangeable / 352 lateext item 1 写进 interchangeable / 352 lateext item 2 建议再看 interchangeable，也不是已经下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事 bundled（352 item 3 余量） interchangeable / 352 lateext item 3 interchangeable，也不是已经又叫了 Verify（本页第一件事） interchangeable。**  
   官方写：看见规范允许，不是已经必须再叫。看见 MAY 写进，不是已经 must-recall interchangeable——本页钉 not already must-recall 单句。看见可以不叫，不是已经又叫了 Verify（本页第一件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 3 完成。

3. **看见是上一高度 / 看见 *h-1* / 看见上一高度 `CommitRound` *r* is not already 已经是本轮那次 Verify interchangeable / 已经 this-round-verify interchangeable / 已经本轮 Verify 交差 interchangeable / 352 lateext bundled interchangeable / 810 lateext-notreverify interchangeable，也不是已经迟到扩展 bundled（352） interchangeable / 811 lateext-notrecall interchangeable / 352 lateext item 1 / 352 lateext item 2，也不是已经下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事 bundled（352 item 3 余量） interchangeable / 352 lateext item 3 interchangeable，也不是已经又叫了 Verify（本页第一件事） interchangeable / 已经必须再叫（本页第二件事） interchangeable。**  
   官方写：看见是上一高度，不是已经是本轮那次 Verify。看见 *h-1*，不是已经 this-round-verify interchangeable——本页钉 not already this-round-verify 单句。看见上一高度 `CommitRound` *r*，不是已经必须再叫（本页第二件事） interchangeable——三件事分开钉。352 lateext vs verified bundled unbundling 在本页 item 3 完成。

怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。迟到扩展 bundled（352）、+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过（352 item 1 余量 / 809）、建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify（352 item 2 余量 / 810）、验签拒收整张预提交就已经是块非法（34）、正确进程交出的扩展必须被正确接收者 Verify Accept（348）、到了 H 已经 Prepare 带了扩展（330）是另外那套，本页不抄。

## 官方为什么这样拆

- **写进去了 not already called-again ≠ 352 / 330 interchangeable：** 官方把可以写入和已经又叫了 Verify 分开。
- **规范允许 not already must-recall ≠ 已经必须再叫 interchangeable：** 官方把规范允许和已经必须再叫分开。
- **是上一高度 not already this-round-verify ≠ 已经是本轮那次 Verify interchangeable：** 官方把是上一高度和已经是本轮那次 Verify 分开；352 lateext vs verified bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写进去了 | 不是 already called-again | 不是到了 H 已经 Prepare 带了扩展 alone（330） |
| 规范允许 | 不是 already must-recall | 不是建议再看 already engine-reverify alone（810） |
| 是上一高度 | 不是 already this-round-verify | 不是写进了 last_commit already verified alone（809） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify not already called-again / not already must-recall / not already this-round-verify 正式三事（352 余量），必须分开写进去了 是不是 already called-again interchangeable / 352 lateext bundled interchangeable / lateext-sold-as-verified interchangeable、规范允许 是不是 already must-recall interchangeable、是上一高度 是不是 already this-round-verify interchangeable。可以跳过「看见写进去了就已经又叫了 Verify interchangeable / 就已经必须再叫 interchangeable / 就已经是本轮那次 Verify interchangeable」。不要另写怎样再验迟到扩展。352 lateext vs verified bundled unbundling 在本页 item 3 完成（809 + 810 + 811）。

## 本页不抄

- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 迟到扩展 bundled。那是不变量 352。
- +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过。那是不变量 352 item 1 余量 / 809。
- 建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify。那是不变量 352 item 2 余量 / 810。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
