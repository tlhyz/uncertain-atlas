# 例：看见 ACCEPT keep / REJECT discard is not already last-commit interchangeable / not already late-verified interchangeable / not already block-invalid interchangeable

**层次**：实现 / ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量）/ not 1087 vfwhen-notcommit interchangeable / not 435 verify-formal-when-vs-flow bundled interchangeable」，不是 Verify When 正式流程 bundled（435），也不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352），也不是 ExtendVote ACCEPT 就已经 Verify 过迟到扩展（409）。不要另写怎样写 Verify When 正式流程。

## 官方三件事

1. **看见 ACCEPT 会把票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo / 看见 REJECT 会把 Precommit 当非法丢掉 这份栏 is not already 已经写进 last_commit interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1087 vfwhen-notcommit interchangeable / 1085 vfwhen-notskip interchangeable / 435 verify-formal-when item 1 discard interchangeable，也不是已经 ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事 bundled（435 item 3 余量） interchangeable / 435 verify-formal-when item 3 interchangeable。**  
   官方写：若应用回 ACCEPT，p 会把收到的票和对应扩展留在内部结构，用来在高度 h+1、自己当提议者的那些轮里，给 PrepareProposal 填 ExtendedCommitInfo。若应用回 REJECT，p 会把 Precommit 当非法丢掉。看见收下了，不是已经写进 last_commit interchangeable——本页从 435 item 3 侧钉 not already last-commit 单句。435 verify-formal-when vs flow bundled unbundling 在本页 item 3 完成。

2. **看见留给下一高 / 看见收下了 / 这份栏 is not already 已经 Verify 过迟到扩展 interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1087 vfwhen-notcommit interchangeable / 435 verify-formal-when item 2 call interchangeable / 1086 vfwhen-notverif interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过 interchangeable / 352 lateext interchangeable。**  
   官方把留给下一高和已经 Verify 过迟到扩展分开。看见留给下一高，不是已经 Verify 过迟到扩展 interchangeable。本页钉 not already late-verified 单句。

3. **看见丢掉了 / 看见 REJECT / 这份栏 is not already 已经当成块非法 interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1087 vfwhen-notcommit interchangeable / 1085 vfwhen-notskip interchangeable，也不是已经 ExtendVote ACCEPT 就已经 Verify 过迟到扩展 interchangeable / 409 extpre interchangeable。**  
   官方把 REJECT 丢掉和已经当成块非法分开。看见丢掉了，不是已经当成块非法 interchangeable。435 verify-formal-when vs flow bundled unbundling 在本页 item 3 完成。

怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ACCEPT keep / REJECT discard not already last-commit ≠ 已经写进 last_commit interchangeable：** 官方把本高 ACCEPT 留下去和已经写进 last_commit 分开。
- **看见留给下一高 not already late-verified ≠ 已经 Verify 过迟到扩展 interchangeable：** 官方把留给下一高和已经 Verify 过迟到扩展分开。
- **看见丢掉了 not already block-invalid ≠ 已经当成块非法 interchangeable：** 官方把 REJECT 丢掉和已经当成块非法分开；435 verify-formal-when vs flow bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit | 不是已经写进 last_commit | 不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352） |
| 看见留给下一高 | 不是已经 Verify 过迟到扩展 | 不是 ExtendVote ACCEPT 就已经 Verify 过迟到扩展（409） |
| 看见丢掉了 | 不是已经当成块非法 | 不是 unsigned discard 就已经跳过 Verify（1085） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT keep / REJECT discard not already last-commit / not already late-verified / not already block-invalid 正式三事（435 余量），必须分开是不是已经写进 last_commit、是不是已经 Verify 过迟到扩展、是不是已经当成块非法。可以跳过「看见收到 Precommit 就已经验过扩展」。不要另写怎样写 Verify When 正式流程。435 verify-formal-when vs flow bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare。
- Verify When 正式流程 bundled。那是不变量 435。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过。那是不变量 352。
- ExtendVote ACCEPT 就已经 Verify 过迟到扩展。那是不变量 409。
