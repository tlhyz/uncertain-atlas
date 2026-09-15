# 例：看见 application implementers SHOULD always set ProcessProposalResponse.status to ACCEPT / SHOULD always set ACCEPT is not honest proposal must Accept / not Requirement 3 already tested 不是已经 Process SHOULD Accept bundled interchangeable / 已经 honest proposal 必须 Accept interchangeable / 已经 Requirement 3 已经测过 interchangeable

**层次**：实现 / ProcessProposal Usage SHOULD always set ACCEPT 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage SHOULD always set ACCEPT 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「SHOULD always set ACCEPT / not honest proposal must Accept / not Req 3 already tested 不是 Process SHOULD Accept bundled interchangeable / 不是已经 honest proposal 必须 Accept interchangeable / 不是已经 Requirement 3 已经测过 interchangeable」，不是 ProcessProposal SHOULD Accept bundled（456），也不是 honest proposal must Accept at Req 3（347），也不是 unless really know liveness implications（531 余量）。不要另写怎样写默认 Accept 策略。

## 官方三件事

规范把 ProcessProposal Usage 里 application implementers SHOULD always set status to ACCEPT 写成三件独立的实现事，不是「看见写了默认 Accept 就已经 honest proposal 必须 Accept interchangeable、已经 Requirement 3 已经测过 interchangeable、已经 MUST Accept interchangeable」一件事：

1. **看见 application implementers SHOULD always set `ProcessProposalResponse.status` to `ACCEPT` / 看见 SHOULD always set to ACCEPT 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经 honest proposal 必须 Accept interchangeable / 已经 Requirement 3 已经测过 interchangeable，也不是已经 honest proposal must Accept at Req bundled（347） interchangeable / 已经 correct proposer must Accept interchangeable，也不是已经 ProcessProposalResponse.status bundled（430） interchangeable / 已经 MUST Accept interchangeable / 已经当成块非法 interchangeable，也不是已经 unless really know liveness implications bundled（456 第二件事 / 531 余量） interchangeable / 已经 REJECT 是免费过滤 interchangeable。**  
   官方 ProcessProposal Usage 写：Moreover, application implementers SHOULD always set ProcessProposalResponse.status to ACCEPT。看见 SHOULD always set to ACCEPT，不是已经 Process SHOULD Accept bundled（456） interchangeable——456 钉 bundled 三事，本页钉 SHOULD always set ACCEPT 单句。看见 SHOULD 总是 Accept，不是已经 honest proposal must Accept at Req（347） interchangeable——347 钉 Req 3 必须 Accept，本页钉 Usage 侧 SHOULD 建议单句。看见 application implementers SHOULD，不是已经 Process 回包栏（430） interchangeable——430 钉 Response 表 status 语义 bundled，本页钉 Usage SHOULD always set 单句。
2. **看见 SHOULD always set ACCEPT is not Requirement 3 is test target / already tested / 看见 SHOULD 不是已经 Requirement 3 已经测过 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经 Requirement 3 已经测过 interchangeable，也不是已经 honest proposal must Accept at Req bundled（347） interchangeable / 已经 Req 3 是大量测试和自动验证的目标 interchangeable / 已经 honest proposal 必须 Accept interchangeable，也不是已经 Process REJECT consensus assume bundled（455） interchangeable / 已经 prevote nil interchangeable / 已经 Process 必须只依赖请求和上一份状态 bundled（340） interchangeable / 已经 SHOULD Accept 通则 interchangeable。**  
   官方把 Usage SHOULD always Accept 和 Requirement 3 测试目标分开——456 bundled 常被写成「写了默认 Accept 就已经 Requirement 3 已经测过」，本页钉 not already Req 3 tested 单句。看见 SHOULD 不是 Req 3 test target，不是已经 honest proposal must Accept（347） interchangeable——347 钉 must Accept 是 Req 3，本页钉 SHOULD 不是 must。看见 not already tested，不是已经 Process REJECT assumes not valid（455） interchangeable——455 钉 REJECT 共识假设，本页钉 Usage SHOULD 与 Req 3 测试目标分开。
3. **看见 SHOULD is not MUST Accept any block / honest proposal must Accept / 看见 SHOULD 不是 MUST Accept 不是已经 Process SHOULD Accept bundled（456） interchangeable / 已经 MUST Accept interchangeable / 已经 honest proposal 必须 Accept interchangeable，也不是已经 honest proposal must Accept at Req bundled（347） interchangeable / 已经 correct proposer must Accept interchangeable，也不是已经 ProcessProposalResponse.status bundled（430） interchangeable / 已经 status 必须只依赖请求和上一份状态 interchangeable / 已经 SHOULD Accept 默认策略 bundled（456 第三件事 / 532 余量） interchangeable / 已经不能 Reject interchangeable，也不是已经 unless really know liveness implications bundled（531 余量） interchangeable / 已经 REJECT 是免费过滤 interchangeable。**  
   官方 ProcessProposal Usage 把 SHOULD 建议和 must Accept 分开——347 Req 3 钉 must Accept，本页钉 SHOULD is not must 单句。看见 SHOULD 不是 MUST，不是已经 Process SHOULD Accept bundled（456） interchangeable——456 bundled 三事常被写成「SHOULD 就已经 must Accept」，本页钉 SHOULD vs MUST 单句。看见 not honest proposal must Accept，不是已经 honest proposal must Accept at Req（347） interchangeable——347 钉 correct proposer 的 prepared proposal 必须被 correct receiver Accept，本页钉 Usage SHOULD 建议边界。

怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价 是规范里的做法，本页不抄。ProcessProposal SHOULD Accept bundled（456）、honest proposal must Accept at Req 3（347）、unless really know liveness implications（531 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **SHOULD always set ACCEPT ≠ 已经 honest proposal 必须 Accept interchangeable：** 官方把 Usage SHOULD 建议和 Req 3 must Accept 分开。
- **SHOULD not already Req 3 tested ≠ Process SHOULD Accept bundled interchangeable：** 官方把 SHOULD 建议和 Requirement 3 测试目标分开。
- **SHOULD is not MUST Accept ≠ honest proposal must Accept at Req interchangeable：** 官方把 SHOULD 建议和 must Accept 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| SHOULD always set ACCEPT | 不是 honest proposal must Accept | 不是 Req 3 must Accept（347） |
| not already Req 3 tested | 不是 Process SHOULD Accept bundled | 不是 Process REJECT assumes not valid（455） |
| SHOULD is not MUST Accept | 不是 must Accept any block | 不是 unless know liveness（531） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal Usage SHOULD always set ACCEPT 正式三事，必须分开 SHOULD always set ACCEPT 是不是已经 honest proposal must Accept interchangeable / 已经 Requirement 3 已经测过 interchangeable、not already Req 3 tested 是不是 Process SHOULD Accept bundled interchangeable、SHOULD is not MUST Accept 是不是 honest proposal must Accept at Req interchangeable。可以跳过「看见写了默认 Accept 就已经 honest proposal 必须 Accept interchangeable」。不要另写怎样写默认 Accept 策略。

## 本页不抄

- 怎样做写默认 Accept 策略、怎样评估 REJECT 活性代价。
- unless they really know liveness implications of REJECT。那是不变量 531（456 item 2 余量）。
- SHOULD Accept default strategy is not can't Reject。那是不变量 532（456 item 3 余量）。
- Process 回包栏 bundled 三事。那是不变量 430。
