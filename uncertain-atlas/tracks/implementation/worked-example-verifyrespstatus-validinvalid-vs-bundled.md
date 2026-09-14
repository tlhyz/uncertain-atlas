# 例：看见 VerifyVoteExtensionResponse.status is application considers extension valid or invalid / REJECT rejects whole vote is not block invalid / REJECT not can't receive precommit 不是已经 Verify 回包栏 bundled interchangeable / 已经当成块非法 interchangeable / 已经不能收这张 Precommit interchangeable

**层次**：实现 / VerifyVoteExtension Response status valid/invalid 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Response status 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「status is application considers valid/invalid / REJECT rejects whole vote not block invalid / REJECT not can't receive precommit 不是 Verify 回包栏 bundled interchangeable / 不是已经当成块非法 interchangeable / 不是已经不能收这张 Precommit interchangeable」，不是 VerifyVoteExtension Response bundled（433），也不是验签拒收整张 Precommit 就已经是块非法（34），也不是 Verify When REJECT discard bundled（517）。不要另写怎样写 Verify 回包栏。

## 官方三件事

规范把 VerifyVoteExtension Response 表上 status 是应用认为这份扩展合法还是非法写成三件独立的实现事，不是「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法 interchangeable、已经不能收这张 Precommit interchangeable、已经 Process prevote nil interchangeable」一件事：

1. **看见 `VerifyVoteExtensionResponse.status` is application considers extension valid or invalid / 看见 status 是应用认为这份扩展合法还是非法 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经当成块非法 interchangeable / 已经 MUST Accept interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 / 533 余量） interchangeable / 已经 prevote nil interchangeable，也不是已经 Verify When step 3 return status bundled（516） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 status must exclusively depend bundled（433 第二件事 / 536 余量） interchangeable / 已经可以像 ExtendVote 那样依赖其它值 interchangeable。**  
   官方 VerifyVoteExtension Response 写：`status` indicates whether the Application considers the vote extension valid or invalid。看见 status 是合法/非法判断，不是已经 Verify 回包栏 bundled（433） interchangeable——433 钉 bundled 三事，本页钉 status valid/invalid 单句。看见 application considers valid or invalid，不是已经 Process 533 REJECT assumes not valid（533） interchangeable——533 钉 Process prevote nil，本页钉 Verify Response 表 status 语义单句。看见回了 status，不是已经 Verify When return ACCEPT/REJECT（516） interchangeable——516 钉 When step 3 return，本页钉 Response 表 status 语义单句。
2. **看见 REJECT rejects whole vote is not block invalid / 看见 REJECT 时共识拒整张票不是已经当成块非法 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经当成块非法 interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430 / 533 余量） interchangeable / 已经 prevote nil interchangeable / 已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经整张 Precommit 非法 interchangeable / 已经 Verify REJECT = 块非法 interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经丢掉 Precommit interchangeable。**  
   官方 VerifyVoteExtension Response/Usage 写：若 `VerifyVoteExtensionResponse.status` 是 `REJECT`，共识算法会拒掉整张收到的票。Usage 也写：*p* 会把这张 Precommit 当非法丢掉。看见 rejects whole vote，不是已经当成块非法 interchangeable——433 bundled 常被写成「回了 REJECT 就已经块非法」，本页钉 rejects whole vote not block invalid 单句。看见 not Process prevote nil，不是已经 Process 533 REJECT assumes not valid（533） interchangeable——533 钉 Process prevote nil 路径，本页钉 Verify 拒整张票单句。看见 not block invalid，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉整张 Precommit 非法，本页钉 Response status REJECT 语义边界。
3. **看见 REJECT not can't receive precommit / discard whole vote is not can't receive / 看见 REJECT 不是已经不能收这张 Precommit 不是已经 Verify 回包栏 bundled（433） interchangeable / 已经不能收这张 Precommit interchangeable / 已经当成块非法 interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经 REJECT 丢掉 Precommit interchangeable / 已经 Accept keep for h+1 Prepare interchangeable，也不是已经 VerifyVoteExtension Usage SHOULD Accept default strategy bundled（529 余量） interchangeable / 已经 can't Reject interchangeable，也不是已经 status must exclusively depend bundled（536 余量） interchangeable / 已经和对任意扩展同一裁决 interchangeable。**  
   官方 VerifyVoteExtension Response/Usage 把 REJECT 拒整张票和「不能收这张 Precommit」分开——433 bundled 常被写成「回了 REJECT 就已经不能收」，本页钉 REJECT not can't receive precommit 单句。看见 discard whole vote，不是已经 Verify When REJECT discard（517） interchangeable——517 钉 When step 3b REJECT discard，本页钉 Response status REJECT 与仍可收票路径边界。看见 not can't receive，不是已经 Verify SHOULD Accept default strategy（529 余量） interchangeable——529 钉 default strategy not can't Reject，本页钉 Response status REJECT 单句。

怎样做写 Verify 回包栏、怎样拒整张 Precommit 是规范里的做法，本页不抄。Verify 回包栏 bundled（433）、status must exclusively depend（536 余量）、Verify When REJECT discard（517）是另外那套，本页不抄。

## 官方为什么这样拆

- **status is valid/invalid judgment ≠ 已经当成块非法 interchangeable：** 官方把 Response status 语义和块非法分开。
- **REJECT rejects whole vote not block invalid ≠ Process prevote nil interchangeable：** 官方把 Verify 拒整张票和 Process prevote nil、验签拒收整张 Precommit 块非法分开。
- **REJECT not can't receive precommit ≠ Verify When REJECT discard bundled interchangeable：** 官方把 Response status REJECT 和 When step 3 discard、can't Reject 默认策略分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| status valid/invalid | 不是 block invalid | 不是验签拒收整张 Precommit 就已经是块非法（34） |
| REJECT rejects whole vote | 不是 block invalid | 不是 Process REJECT assumes not valid prevote nil（533） |
| REJECT not can't receive precommit | 不是 can't receive | 不是 Verify When REJECT discard（517） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Response status valid/invalid 正式三事，必须分开 status is valid/invalid 是不是已经 block invalid interchangeable / 已经 MUST Accept interchangeable、REJECT rejects whole vote 是不是 block invalid interchangeable / Process prevote nil interchangeable、REJECT not can't receive precommit 是不是已经 can't receive interchangeable / 517 When REJECT discard interchangeable。可以跳过「看见回了 VerifyVoteExtensionResponse.status 就已经当成块非法 interchangeable」。不要另写怎样写 Verify 回包栏。

## 本页不抄

- 怎样做写 Verify 回包栏、怎样拒整张 Precommit。
- VerifyVoteExtensionResponse.status must exclusively depend。那是不变量 536（433 item 2 余量）。
- 应用 SHOULD always set ACCEPT。那是不变量 527（457 item 1 / 433 Usage 余量）。
- Verify When step 3 REJECT discard 正式三事 bundled。那是不变量 517。
