# 例：看见 ExtendVoteRequest 对应即将发 Precommit is not already will-call interchangeable / not already non-nil-only interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量）/ not 1031 extpre-notcall interchangeable / not 409 extreq-vs-precommit bundled interchangeable」，不是 ExtendVote 请求对应 bundled（409），也不是一轮只能交出一份扩展就已经是每一高度一份（350），也不是 ExtendVoteRequest.hash 就已经跑过 Process（410）。不要另写怎样写 ExtendVote 请求对应。

## 官方三件事

1. **看见 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 / 看见填了请求 这份对应 is not already 已经会调 ExtendVote interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1031 extpre-notcall interchangeable / 1032 extpre-notskip interchangeable / 409 extreq item 2 丢掉 interchangeable，也不是已经 ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事 bundled（409 item 1 余量） interchangeable / 409 extreq item 1 interchangeable。**  
   官方写：ExtendVoteRequest 的内容对应共识算法即将发 Precommit 的那份拟议块。看见填了请求，不是已经到了 prevote 步就已经会调 interchangeable——本页从 409 item 1 侧钉 not already will-call 单句。409 extreq vs precommit bundled unbundling 在本页 item 1 启动。

2. **看见对上了拟议块 / 看见填了请求 / 这份对应 is not already 已经只在即将广播非 nil Precommit 时才叫 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1031 extpre-notcall interchangeable / 409 extreq item 3 ACCEPT interchangeable / 1033 extpre-notlate interchangeable，也不是已经一轮只能交出一份扩展就已经是每一高度一份 interchangeable / 350 extend-once interchangeable。**  
   官方把对上了拟议块和已经只在即将广播非 nil Precommit 时才叫分开。看见对上了拟议块，不是已经只在即将广播非 nil Precommit 时才叫 interchangeable。本页钉 not already non-nil-only 单句。

3. **看见有内容 / 看见填了请求 / 这份对应 is not already 已经交差 interchangeable，也不是已经 ExtendVote 请求对应 bundled（409） interchangeable / 1031 extpre-notcall interchangeable / 1032 extpre-notskip interchangeable，也不是已经 ExtendVoteRequest.hash 就已经跑过 Process interchangeable / 410 extreqhash interchangeable。**  
   官方把有内容和已经交差分开。看见有内容，不是已经交差 interchangeable。409 extreq vs precommit bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest 对应即将发 Precommit not already will-call ≠ 已经会调 ExtendVote interchangeable：** 官方把请求内容和已经会调分开。
- **看见对上了拟议块 not already non-nil-only ≠ 已经只在即将广播非 nil Precommit 时才叫 interchangeable：** 官方把对上了拟议块和已经只在即将广播非 nil Precommit 时才叫分开。
- **看见有内容 not already settled ≠ 已经交差 interchangeable：** 官方把有内容和已经交差分开；409 extreq vs precommit bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 | 不是已经会调 ExtendVote | 不是一轮只能交出一份扩展就已经是每一高度一份（350） |
| 看见对上了拟议块 | 不是已经只在即将广播非 nil Precommit 时才叫 | 不是 ExtendVoteRequest.hash 就已经跑过 Process（410） |
| 看见有内容 | 不是已经交差 | 不是丢掉就已经跳过 Verify（1032） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteRequest 对应即将发 Precommit not already will-call / not already non-nil-only / not already settled 正式三事（409 余量），必须分开是不是已经会调 ExtendVote、是不是已经只在即将广播非 nil Precommit 时才叫、是不是已经交差。可以跳过「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 请求对应。409 extreq vs precommit bundled unbundling 在本页 item 1 启动；续 [`worked-example-extpre-notskip-vs-bundled.md`](worked-example-extpre-notskip-vs-bundled.md)（不变量 1032 item 2）。

## 本页不抄

- 怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare。
- ExtendVote 请求对应 bundled。那是不变量 409。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- ExtendVoteRequest.hash 就已经跑过 Process。那是不变量 410。
