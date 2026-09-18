# 例：看见 SHOULD Accept default strategy is not can't Reject / REJECT consensus rejects whole vote is not can't Reject / default Accept is not Verify det SHOULD Accept general rule 不是已经 Verify SHOULD Accept bundled interchangeable / 已经不能 Reject interchangeable / 已经 Verify 必须只依赖请求和上一份状态 SHOULD Accept 通则 interchangeable

**层次**：实现 / VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SHOULD Accept default strategy / REJECT rejects whole vote / not Verify det SHOULD Accept general rule 不是 Verify SHOULD Accept bundled interchangeable / 不是已经不能 Reject interchangeable / 不是已经 Verify 341 SHOULD Accept 通则 interchangeable」，不是 VerifyVoteExtension SHOULD Accept bundled（457），也不是 SHOULD always set ACCEPT（527），也不是 unless really know liveness implications（528）。不要另写怎样写默认 Accept 策略。

## 官方三件事

规范把 VerifyVoteExtension Usage 里 SHOULD Accept 默认策略不是已经不能 Reject 写成三件独立的实现事，不是「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable、已经 MUST Accept interchangeable、已经 Verify 341 SHOULD Accept 通则 interchangeable」一件事：

1. **看见 SHOULD Accept default strategy is not can't Reject / 看见 SHOULD Accept 默认策略不是已经不能 Reject 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经不能 Reject interchangeable / 已经 MUST Accept interchangeable，也不是已经 SHOULD always set ACCEPT bundled（457 第一件事 / 527） interchangeable / 已经 correct process must Accept interchangeable，也不是已经 unless really know liveness implications bundled（457 第二件事 / 528） interchangeable / 已经 REJECT 没有代价 interchangeable / 已经 REJECT 是免费过滤 interchangeable，也不是已经 VerifyVoteExtensionResponse.status is REJECT bundled（433） interchangeable / 已经 consensus rejects whole vote interchangeable / 已经 status 必须只依赖 interchangeable。**  
   官方 VerifyVoteExtension Usage 写：If VerifyVoteExtensionResponse.status is REJECT, the consensus algorithm will reject the whole received vote。看见 REJECT 拒整张票，不是已经不能 Reject interchangeable——457 bundled 常与 433 bundled 混成「SHOULD Accept = 已经不能 Reject」，本页钉 default strategy not can't Reject 单句。看见 SHOULD Accept 默认策略，不是已经 SHOULD always set ACCEPT（527） interchangeable——527 钉 SHOULD always set，本页钉 default strategy 不是 can't Reject。看见 can still Reject，不是已经 unless really know liveness（528） interchangeable——528 钉 unless 条件，本页钉 default strategy 边界。
2. **看见 REJECT consensus rejects whole vote is not can't Reject / 看见 REJECT 时共识拒整张票不是已经不能 Reject 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经不能 Reject interchangeable，也不是已经 VerifyVoteExtensionResponse.status bundled（433） interchangeable / 已经 REJECT 拒整张票 interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable，也不是已经 Verify When step 3 REJECT discard bundled（517） interchangeable / 已经丢掉 Precommit interchangeable / 已经 Accept keep for h+1 Prepare interchangeable，也不是已经验签拒收整张 Precommit bundled（34） interchangeable / 已经当成块非法 interchangeable。**  
   官方 VerifyVoteExtension Usage 把 REJECT 拒整张票和 can't Reject 分开——433 bundled 钉 REJECT 时共识拒整张票，本页钉 REJECT path 存在不是 can't Reject 单句。看见 consensus rejects whole vote，不是已经 Verify When REJECT discard（517） interchangeable——517 钉 When step 3b REJECT discard，本页钉 Usage 侧 REJECT 路径存在。看见 not can't Reject，不是已经验签拒收整张 Precommit（34） interchangeable——34 钉整张 Precommit 非法，本页钉 Usage SHOULD Accept 默认策略边界。
3. **看见 default Accept is not Verify det SHOULD Accept general rule / 看见默认 Accept 不是已经 Verify 必须只依赖请求和上一份状态那种 SHOULD Accept 通则 interchangeable 不是已经 Verify SHOULD Accept bundled（457） interchangeable / 已经 Verify 341 SHOULD Accept 通则 interchangeable / 已经丢了安全性 interchangeable，也不是已经 Verify 非确定 bug 会伤活性 bundled（341） interchangeable / 已经活性会被伤 interchangeable / 已经 MUST Accept interchangeable，也不是已经 VerifyVoteExtensionResponse.status bundled（433） interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable，也不是已经 SHOULD always set ACCEPT bundled（527） interchangeable / 已经 Requirement 6 已经测过 interchangeable。**  
   官方 VerifyVoteExtension Usage 把 Usage SHOULD Accept 默认策略和 Verify 非确定 bug 伤活性那种 SHOULD Accept 通则（341）分开——341 钉 Req 7–8 / 非确定 bug 伤活性，本页钉 Usage default strategy 单句。看见 default Accept，不是已经 Verify 341 SHOULD Accept 通则 interchangeable——341 钉 determinism / liveness，本页钉 Usage default strategy 不是 341 通则。看见 SHOULD Accept 默认策略，不是已经 Verify SHOULD Accept bundled（457） interchangeable——457 bundled 三事常被写成「SHOULD Accept 默认策略 = 341 通则 = 433 MUST Accept」，本页钉 default strategy 单句。

怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价 是规范里的做法，本页不抄。VerifyVoteExtension SHOULD Accept bundled（457）、SHOULD always set ACCEPT（527）、unless really know liveness implications（528）是另外那套，本页不抄。

## 官方为什么这样拆

- **SHOULD Accept default strategy ≠ 已经不能 Reject interchangeable：** 官方把 SHOULD 默认 Accept 和 can't Reject 分开。
- **REJECT rejects whole vote ≠ can't Reject interchangeable：** 官方把 REJECT 路径存在和已经不能 Reject 分开。
- **default Accept ≠ Verify det SHOULD Accept general rule (341) interchangeable：** 官方把 Usage default strategy 和 341 通则分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| SHOULD Accept default strategy | 不是 can't Reject | 不是 SHOULD always set ACCEPT（527） |
| REJECT rejects whole vote | 不是 can't Reject | 不是 Verify When REJECT discard（517） |
| default Accept | 不是 Verify det general rule (341) | 不是 Verify response bundled（433） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage SHOULD Accept default strategy 正式三事，必须分开 SHOULD Accept default strategy 是不是已经 can't Reject interchangeable / 已经 MUST Accept interchangeable、REJECT rejects whole vote 是不是 can't Reject interchangeable、default Accept 是不是 Verify 341 SHOULD Accept 通则 interchangeable。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。529 VerifyVoteExtension Usage SHOULD Accept default bundled unbundling 完成（1337 item 1 / 1338 item 2 / 1339 item 3）；精读 [`worked-example-vacdef-notcant-vs-bundled.md`](worked-example-vacdef-notcant-vs-bundled.md)（不变量 1337 item 1）、[`worked-example-vacdef-notrej-vs-bundled.md`](worked-example-vacdef-notrej-vs-bundled.md)（不变量 1338 item 2）、[`worked-example-vacdef-not341-vs-bundled.md`](worked-example-vacdef-not341-vs-bundled.md)（不变量 1339 item 3）。不要另写怎样写默认 Accept 策略。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- SHOULD always set VerifyVoteExtensionResponse.status to ACCEPT。那是不变量 527（457 item 1）。
- unless they really know liveness implications of REJECT。那是不变量 528（457 item 2）。
- Verify 回包栏 bundled 三事。那是不变量 433。
