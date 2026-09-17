# 例：看见 Verify ACCEPT 留给 h+1 Prepare is not already late-verified interchangeable / not already settled interchangeable / not already must-reverify interchangeable

**层次**：实现 / Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量）/ not 1033 extpre-notlate interchangeable / not 409 extreq-vs-precommit bundled interchangeable」，不是 ExtendVote 请求对应 bundled（409），也不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352），也不是空扩展仍会调 Verify 就已经跳过（353）。不要另写怎样写 ExtendVote 请求对应。

## 官方三件事

1. **看见 Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo / 看见收下了 这份对应 is not already 已经 Verify 过迟到扩展 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1033 extpre-notlate interchangeable / 1031 extpre-notcall interchangeable / 409 extreq item 1 对应 interchangeable，也不是已经 Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事 bundled（409 item 3 余量） interchangeable / 409 extreq item 3 interchangeable。**  
   官方写：应用回 ACCEPT 后，p 把收到的票和对应扩展留在内部结构，用来在高度 h+1、自己当提议者的那些轮里，给 PrepareProposal 填 ExtendedCommitInfo。看见收下了，不是已经 +2/3 之后才进来的扩展写进了 commit info 那种已经 Verify 过 interchangeable——本页从 409 item 3 侧钉 not already late-verified 单句。409 extreq vs precommit bundled unbundling 在本页 item 3 完成。

2. **看见留给下一高 / 看见收下了 / 这份对应 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1033 extpre-notlate interchangeable / 409 extreq item 2 丢掉 interchangeable / 1032 extpre-notskip interchangeable，也不是已经 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过 interchangeable / 352 lateext interchangeable。**  
   官方把留给下一高和已经交差分开。看见留给下一高，不是已经交差 interchangeable。本页钉 not already settled 单句。

3. **看见能填 / 看见收下了 / 这份对应 is not already 已经必须再 Verify interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1033 extpre-notlate interchangeable / 1031 extpre-notcall interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 interchangeable / 353 verifyusage interchangeable。**  
   官方把能填和已经必须再 Verify 分开。看见能填，不是已经必须再 Verify interchangeable。409 extreq vs precommit bundled unbundling 在本页 item 3 完成。

怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Verify ACCEPT 留给 h+1 Prepare not already late-verified ≠ 已经 Verify 过迟到扩展 interchangeable：** 官方把本高 ACCEPT 留下去和迟到扩展已经 Verify 过分开。
- **看见留给下一高 not already settled ≠ 已经交差 interchangeable：** 官方把留给下一高和已经交差分开。
- **看见能填 not already must-reverify ≠ 已经必须再 Verify interchangeable：** 官方把能填和已经必须再 Verify 分开；409 extreq vs precommit bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo | 不是已经 Verify 过迟到扩展 | 不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352） |
| 看见留给下一高 | 不是已经交差 | 不是空扩展仍会调 Verify 就已经跳过（353） |
| 看见能填 | 不是已经必须再 Verify | 不是请求对应就已经会调 ExtendVote（1031） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Verify ACCEPT 留给 h+1 Prepare not already late-verified / not already settled / not already must-reverify 正式三事（409 余量），必须分开是不是已经 Verify 过迟到扩展、是不是已经交差、是不是已经必须再 Verify。可以跳过「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 请求对应。409 extreq vs precommit bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare。
- ExtendVote 请求对应 bundled。那是不变量 409。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过。那是不变量 352。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
