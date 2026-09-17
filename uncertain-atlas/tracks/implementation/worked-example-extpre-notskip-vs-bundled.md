# 例：看见 Precommit 丢掉无有效签扩展 is not already skip-verify interchangeable / not already unsigned interchangeable / not already self-verified interchangeable

**层次**：实现 / Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量）/ not 1032 extpre-notskip interchangeable / not 409 extreq-vs-precommit bundled interchangeable」，不是 ExtendVote 请求对应 bundled（409），也不是空扩展仍会调 Verify 就已经跳过 Verify（353），也不是迟到扩展就已经 Verify（352）。不要另写怎样写 ExtendVote 请求对应。

## 官方三件事

1. **看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见空扩展 这份对应 is not already 已经跳过 Verify interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1032 extpre-notskip interchangeable / 1031 extpre-notcall interchangeable / 409 extreq item 1 对应 interchangeable，也不是已经 Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事 bundled（409 item 2 余量） interchangeable / 409 extreq item 2 interchangeable。**  
   官方写：若 Precommit 没有带有效签的扩展，p 把这张 Precommit 当非法丢掉。0 长度扩展只要伴随签名也合法，就算有效。看见丢掉了，不是已经空扩展仍会调 Verify 那种已经跳过 interchangeable——本页从 409 item 2 侧钉 not already skip-verify 单句。409 extreq vs precommit bundled unbundling 在本页 item 2 续。

2. **看见空扩展 / 看见丢掉了 / 这份对应 is not already 已经没有签 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1032 extpre-notskip interchangeable / 409 extreq item 3 ACCEPT interchangeable / 1033 extpre-notlate interchangeable，也不是已经空扩展仍会调 Verify 就已经跳过 Verify interchangeable / 353 verifyusage interchangeable。**  
   官方把空扩展和已经没有签分开。看见空扩展，不是已经没有签 interchangeable。本页钉 not already unsigned 单句。

3. **看见没调 Verify / 看见丢掉了 / 这份对应 is not already 已经自己验过 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1032 extpre-notskip interchangeable / 1031 extpre-notcall interchangeable，也不是已经迟到扩展就已经 Verify interchangeable / 352 lateext interchangeable。**  
   官方把没调 Verify 和已经自己验过分开。看见没调 Verify，不是已经自己验过 interchangeable。409 extreq vs precommit bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Precommit 丢掉无有效签扩展 not already skip-verify ≠ 已经跳过 Verify interchangeable：** 官方把签先丢掉和空扩展仍会调分开。
- **看见空扩展 not already unsigned ≠ 已经没有签 interchangeable：** 官方把空扩展和已经没有签分开。
- **看见没调 Verify not already self-verified ≠ 已经自己验过 interchangeable：** 官方把没调 Verify 和已经自己验过分开；409 extreq vs precommit bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 看见空扩展 | 不是已经没有签 | 不是迟到扩展就已经 Verify（352） |
| 看见没调 Verify | 不是已经自己验过 | 不是 ACCEPT 就已经 Verify 过迟到扩展（1033） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Precommit 丢掉无有效签扩展 not already skip-verify / not already unsigned / not already self-verified 正式三事（409 余量），必须分开是不是已经跳过 Verify、是不是已经没有签、是不是已经自己验过。可以跳过「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 请求对应。409 extreq vs precommit bundled unbundling 在本页 item 2 续；续 [`worked-example-extpre-notlate-vs-bundled.md`](worked-example-extpre-notlate-vs-bundled.md)（不变量 1033 item 3）。

## 本页不抄

- 怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare。
- ExtendVote 请求对应 bundled。那是不变量 409。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- 迟到扩展就已经 Verify。那是不变量 352。
