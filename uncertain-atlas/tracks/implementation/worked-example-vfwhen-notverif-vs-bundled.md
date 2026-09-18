# 例：看见 signed Precommit calls Verify is not already verified interchangeable / not already accept interchangeable / not already local-skip interchangeable

**层次**：实现 / signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量）/ not 1086 vfwhen-notverif interchangeable / not 435 verify-formal-when-vs-flow bundled interchangeable」，不是 Verify When 正式流程 bundled（435），也不是 VerifyStatus ACCEPT 就已经验过扩展（434），也不是 Verify 回包 status 就已经当成块非法（433）。不要另写怎样写 Verify When 正式流程。

## 官方三件事

1. **看见带有效签就会调 VerifyVoteExtension / 看见 CometBFT 会叫 这份栏 is not already 已经验过扩展 interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1086 vfwhen-notverif interchangeable / 1085 vfwhen-notskip interchangeable / 435 verify-formal-when item 1 discard interchangeable，也不是已经 signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事 bundled（435 item 2 余量） interchangeable / 435 verify-formal-when item 2 interchangeable。**  
   官方写：节点 p 在一轮 r、高度 h，收到验证者 q（q ≠ p）的 Precommit，且扩展带有效签，p 的 CometBFT 会调 VerifyVoteExtension。看见叫了，不是已经验过扩展 interchangeable——本页从 435 item 2 侧钉 not already verified 单句。435 verify-formal-when vs flow bundled unbundling 在本页 item 2 续。

2. **看见会调 / 看见 CometBFT 会叫 / 这份栏 is not already 已经 Accept interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1086 vfwhen-notverif interchangeable / 435 verify-formal-when item 3 accept-reject interchangeable / 1087 vfwhen-notcommit interchangeable，也不是已经 VerifyStatus ACCEPT 就已经验过扩展 interchangeable / 434 verifystatus interchangeable。**  
   官方把会调和已经 Accept 分开。看见会调，不是已经 Accept interchangeable。本页钉 not already accept 单句。

3. **看见收到他人票 / 看见 CometBFT 会叫 / 这份栏 is not already 已经不对本进程自己发出的 Precommit 调用 interchangeable，也不是已经 Verify When 正式流程 bundled（435） interchangeable / 1086 vfwhen-notverif interchangeable / 1085 vfwhen-notskip interchangeable，也不是已经 Verify 回包 status 就已经当成块非法 interchangeable / 433 verifyresp interchangeable。**  
   官方把收到他人票和已经不对本进程自己发出的 Precommit 调用分开。看见收到他人票，不是已经不对本进程自己发出的 Precommit 调用 interchangeable。435 verify-formal-when vs flow bundled unbundling 在本页 item 2 续。

怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **signed Precommit calls Verify not already verified ≠ 已经验过扩展 interchangeable：** 官方把会叫 Verify 和已经验过扩展分开。
- **看见会调 not already accept ≠ 已经 Accept interchangeable：** 官方把会调和已经 Accept 分开。
- **看见收到他人票 not already local-skip ≠ 已经不对本进程自己发出的 Precommit 调用 interchangeable：** 官方把收到他人票和已经本地票分开；435 verify-formal-when vs flow bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 带有效签就会调 VerifyVoteExtension | 不是已经验过扩展 | 不是 VerifyStatus ACCEPT 就已经验过扩展（434） |
| 看见会调 | 不是已经 Accept | 不是 Verify 回包 status 就已经当成块非法（433） |
| 看见收到他人票 | 不是已经不对本进程自己发出的 Precommit 调用 | 不是 ACCEPT/REJECT 就已经写进 last_commit（1087） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 signed Precommit calls Verify not already verified / not already accept / not already local-skip 正式三事（435 余量），必须分开是不是已经验过扩展、是不是已经 Accept、是不是已经不对本进程自己发出的 Precommit 调用。可以跳过「看见收到 Precommit 就已经验过扩展」。不要另写怎样写 Verify When 正式流程。435 verify-formal-when vs flow bundled unbundling 在本页 item 2 续；续 [`worked-example-vfwhen-notcommit-vs-bundled.md`](worked-example-vfwhen-notcommit-vs-bundled.md)（不变量 1087 item 3）。

## 本页不抄

- 怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare。
- Verify When 正式流程 bundled。那是不变量 435。
- VerifyStatus ACCEPT 就已经验过扩展。那是不变量 434。
- Verify 回包 status 就已经当成块非法。那是不变量 433。
