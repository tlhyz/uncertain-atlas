# 例：看见 SHOULD Accept default strategy is not can't Reject / REJECT assumes not valid is not can't Reject / default Accept is not Process det SHOULD Accept general rule 不是已经 Process SHOULD Accept bundled interchangeable / 已经不能 Reject interchangeable / 已经 Process 340 SHOULD Accept 通则 interchangeable

**层次**：实现 / ProcessProposal Usage SHOULD Accept default strategy 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD Accept default strategy 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SHOULD Accept default strategy / REJECT assumes not valid / not Process det SHOULD Accept general rule 不是 Process SHOULD Accept bundled interchangeable / 不是已经不能 Reject interchangeable / 不是已经 Process 340 SHOULD Accept 通则 interchangeable」，不是 ProcessProposal SHOULD Accept bundled（456），也不是 SHOULD always set ACCEPT（530），也不是 unless really know liveness implications（531）。不要另写怎样写默认 Accept 策略。

## 官方三件事

规范把 ProcessProposal Usage 里 SHOULD Accept 默认策略不是已经不能 Reject 写成三件独立的实现事，不是「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable、已经 MUST Accept interchangeable、已经 Process 340 SHOULD Accept 通则 interchangeable」一件事：

1. **看见 SHOULD Accept default strategy is not can't Reject / 看见 SHOULD Accept 默认策略不是已经不能 Reject 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经不能 Reject interchangeable / 已经 MUST Accept interchangeable，也不是已经 SHOULD always set ACCEPT bundled（456 第一件事 / 530） interchangeable / 已经 honest proposal 必须 Accept interchangeable，也不是已经 unless really know liveness implications bundled（456 第二件事 / 531） interchangeable / 已经 REJECT 没有代价 interchangeable / 已经 REJECT 是免费过滤 interchangeable，也不是已经 ProcessProposalResponse.status is REJECT bundled（430） interchangeable / 已经 consensus assumes not valid interchangeable / 已经 status 必须只依赖 interchangeable。**  
   官方 ProcessProposal Usage 写：If ProcessProposalResponse.status is REJECT, consensus assumes the proposal received is not valid。看见 REJECT assumes not valid，不是已经不能 Reject interchangeable——456 bundled 常与 430 bundled 混成「SHOULD Accept = 已经不能 Reject」，本页钉 default strategy not can't Reject 单句。看见 SHOULD Accept 默认策略，不是已经 SHOULD always set ACCEPT（530） interchangeable——530 钉 SHOULD always set，本页钉 default strategy 不是 can't Reject。看见 can still Reject，不是已经 unless really know liveness（531） interchangeable——531 钉 unless 条件，本页钉 default strategy 边界。
2. **看见 REJECT assumes not valid is not can't Reject / 看见 REJECT 时共识 assumes not valid 不是已经不能 Reject 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经不能 Reject interchangeable，也不是已经 ProcessProposalResponse.status bundled（430） interchangeable / 已经 REJECT assumes not valid interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable，也不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 prevote nil interchangeable / 已经 Process REJECT = prevote nil 不是免费过滤 bundled（33） interchangeable / 已经当成块非法 interchangeable。**  
   官方 ProcessProposal Usage 把 REJECT assumes not valid 和 can't Reject 分开——430 bundled 钉 REJECT 时共识 assumes not valid，本页钉 REJECT path 存在不是 can't Reject 单句。看见 consensus assumes not valid，不是已经 Process REJECT consensus assume（455） interchangeable——455 钉 assumes not valid / prevote nil bundled，本页钉 Usage 侧 REJECT 路径存在。看见 not can't Reject，不是已经 Process REJECT = prevote nil 不是免费过滤（33） interchangeable——33 钉 prevote nil 路径，本页钉 Usage SHOULD Accept 默认策略边界。
3. **看见 default Accept is not Process det SHOULD Accept general rule / 看见默认 Accept 不是已经 Process 必须只依赖请求和上一份状态那种 SHOULD Accept 通则 interchangeable 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经 Process 340 SHOULD Accept 通则 interchangeable / 已经丢了安全性 interchangeable，也不是已经 Process 非确定 bug 会伤活性 bundled（340） interchangeable / 已经活性会被伤 interchangeable / 已经 MUST Accept interchangeable，也不是已经 ProcessProposalResponse.status bundled（430） interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable，也不是已经 SHOULD always set ACCEPT bundled（530） interchangeable / 已经 Requirement 3 已经测过 interchangeable。**  
   官方 ProcessProposal Usage 把 Usage SHOULD Accept 默认策略和 Process 非确定 bug 伤活性那种 SHOULD Accept 通则（340）分开——340 钉 Req 4–5 / 非确定 bug 伤活性，本页钉 Usage default strategy 单句。看见 default Accept，不是已经 Process 340 SHOULD Accept 通则 interchangeable——340 钉 determinism / liveness，本页钉 Usage default strategy 不是 340 通则。看见 SHOULD Accept 默认策略，不是已经 Process SHOULD Accept bundled（456） interchangeable——456 bundled 三事常被写成「SHOULD Accept 默认策略 = 340 通则 = 430 MUST Accept」，本页钉 default strategy 单句。

怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价 是规范里的做法，本页不抄。ProcessProposal SHOULD Accept bundled（456）、SHOULD always set ACCEPT（530）、unless really know liveness implications（531）是另外那套，本页不抄。

## 官方为什么这样拆

- **SHOULD Accept default strategy ≠ 已经不能 Reject interchangeable：** 官方把 SHOULD 默认 Accept 和 can't Reject 分开。
- **REJECT assumes not valid ≠ can't Reject interchangeable：** 官方把 REJECT 路径存在和已经不能 Reject 分开。
- **default Accept ≠ Process det SHOULD Accept general rule (340) interchangeable：** 官方把 Usage default strategy 和 340 通则分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| SHOULD Accept default strategy | 不是 can't Reject | 不是 SHOULD always set ACCEPT（530） |
| REJECT assumes not valid | 不是 can't Reject | 不是 Process REJECT consensus assume（455） |
| default Accept | 不是 Process det general rule (340) | 不是 Process response bundled（430） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD Accept default strategy 正式三事，必须分开 SHOULD Accept default strategy 是不是已经 can't Reject interchangeable / 已经 MUST Accept interchangeable、REJECT assumes not valid 是不是 can't Reject interchangeable、default Accept 是不是 Process 340 SHOULD Accept 通则 interchangeable。可以跳过「看见 SHOULD Accept 默认策略 就已经不能 Reject interchangeable」。不要另写怎样写默认 Accept 策略。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- SHOULD always set ProcessProposalResponse.status to ACCEPT。那是不变量 530（456 item 1）。
- unless they really know liveness implications of REJECT。那是不变量 531（456 item 2）。
- Process 回包栏 bundled 三事。那是不变量 430。
