# 例：看见 VerifyVoteExtensionResponse.status is not already block-invalid interchangeable / not already no-precommit interchangeable / not already process-reject interchangeable

**层次**：实现 / VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量）/ not 1076 vresp-notinvalid interchangeable / not 433 verifyresp-vs-status bundled interchangeable」，不是 Verify 回包栏 bundled（433），也不是验签拒收整张 Precommit 就已经是块非法（34），也不是 ProcessProposalResponse.status REJECT 就已经 prevote nil（430）。不要另写怎样写 Verify 回包栏。

## 官方三件事

1. **看见 VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 / 看见回了 REJECT 这份栏 is not already 已经当成块非法 interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1076 vresp-notinvalid interchangeable / 1077 vresp-notext interchangeable / 433 verifyresp item 2 exclusive interchangeable，也不是已经 VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事 bundled（433 item 1 余量） interchangeable / 433 verifyresp item 1 interchangeable。**  
   官方写：若 VerifyVoteExtensionResponse.status 是 REJECT，共识算法会拒掉整张收到的票。看见回了 REJECT，不是已经当成块非法 interchangeable——本页从 433 item 1 侧钉 not already block-invalid 单句。433 verifyresp vs status bundled unbundling 在本页 item 1 启动。

2. **看见拒掉整张票 / 看见回了 REJECT / 这份栏 is not already 已经不能收这张 Precommit interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1076 vresp-notinvalid interchangeable / 433 verifyresp item 3 should-accept interchangeable / 1078 vresp-nothonest interchangeable，也不是已经验签拒收整张 Precommit 就已经是块非法 interchangeable / 34 verify interchangeable。**  
   官方把拒掉整张票和已经不能收这张 Precommit 分开。看见拒掉整张票，不是已经不能收这张 Precommit interchangeable。本页钉 not already no-precommit 单句。

3. **看见 Precommit 被丢掉 / 看见回了 REJECT / 这份栏 is not already 已经是 Process REJECT 那种 prevote nil interchangeable，也不是已经 Verify 回包栏 bundled（433） interchangeable / 1076 vresp-notinvalid interchangeable / 1077 vresp-notext interchangeable，也不是已经 ProcessProposalResponse.status REJECT 就已经 prevote nil interchangeable / 430 procresp interchangeable。**  
   官方把 Precommit 被丢掉和已经是 Process REJECT 那种 prevote nil 分开。看见 Precommit 被丢掉，不是已经是 Process REJECT 那种 prevote nil interchangeable。433 verifyresp vs status bundled unbundling 在本页 item 1 启动。

怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **VerifyVoteExtensionResponse.status not already block-invalid ≠ 已经当成块非法 interchangeable：** 官方把应用认为扩展非法和已经当成块非法分开。
- **看见拒掉整张票 not already no-precommit ≠ 已经不能收这张 Precommit interchangeable：** 官方把拒掉整张票和已经不能收这张 Precommit 分开。
- **看见 Precommit 被丢掉 not already process-reject ≠ 已经是 Process REJECT 那种 prevote nil interchangeable：** 官方把 Precommit 被丢掉和已经是 Process REJECT 那种 prevote nil 分开；433 verifyresp vs status bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法 | 不是已经当成块非法 | 不是验签拒收整张 Precommit 就已经是块非法（34） |
| 看见拒掉整张票 | 不是已经不能收这张 Precommit | 不是 ProcessProposalResponse.status REJECT 就已经 prevote nil（430） |
| 看见 Precommit 被丢掉 | 不是已经是 Process REJECT 那种 prevote nil | 不是 exclusive dependence 就已经可以像 ExtendVote 那样（1077） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtensionResponse.status not already block-invalid / not already no-precommit / not already process-reject 正式三事（433 余量），必须分开是不是已经当成块非法、是不是已经不能收这张 Precommit、是不是已经是 Process REJECT 那种 prevote nil。可以跳过「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法」。不要另写怎样写 Verify 回包栏。433 verifyresp vs status bundled unbundling 在本页 item 1 启动；续 [`worked-example-vresp-notext-vs-bundled.md`](worked-example-vresp-notext-vs-bundled.md)（不变量 1077 item 2）。

## 本页不抄

- 怎样写 Verify 回包栏、怎样挑 ACCEPT/REJECT、怎样拒整张 Precommit。
- Verify 回包栏 bundled。那是不变量 433。
- 验签拒收整张 Precommit 就已经是块非法。那是不变量 34。
- ProcessProposalResponse.status REJECT 就已经 prevote nil。那是不变量 430。
