# 例：看见正确提议者的准备提案必须被正确接收者 Accept / 看见正确进程之间永远过 / 看见必须 Accept is not already already any-block interchangeable / already default-accept interchangeable / already settled interchangeable

**层次**：实现 / 正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量）/ not 794 req3-notany interchangeable / not 347 req3coherence bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题（795 item 2 余量）或 Req 3 是大量测试和自动验证的目标不是已经测过（796 item 3 余量）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

规范把 Requirements 里正确进程交出的准备提案、正确接收者 Process 必须 Accept 和「已经是正确进程之间过就已经任意块都会 Accept interchangeable / 已经是必须 Accept 就已经写了默认 Accept interchangeable / 已经是正确进程之间过就已经交差 interchangeable / 已经是 req3coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见必须 Accept 就已经任意块都会过 interchangeable / 就已经写了默认 Accept interchangeable / 就已经交差 interchangeable」一件事：

1. **看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 看见正确进程之间永远过 / 看见正确提议者交出来的必须过 is not already 已经是任意块都会 Accept interchangeable / 已经 any-block interchangeable / 已经任意块过交差 interchangeable / 347 req3coherence bundled interchangeable / 33 four gates interchangeable / req3coherence-sold-as-accept interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 794 req3-notany interchangeable / 347 req3 item 1 interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事 bundled（347 item 1 余量） interchangeable / 347 req3 item 1 interchangeable，也不是已经 Prepare 或 Process 里有确定 bug（795） interchangeable / 796 req3-nottested interchangeable / 348 req6coherence interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：任意两个正确进程 *p*、*q*，若 *q* 的引擎对 *p* 交出的准备提案 *u<sub>p</sub>* 叫 `ProcessProposal`，*q* 的应用必须在 `ProcessProposalResponse` 里回 Accept。看见正确提议者交出来的必须过，不是任意块已经都会过。看见正确进程之间永远过，不是已经 any-block interchangeable——347 钉 bundled 三事，本页从 item 1 侧钉 not already any-block 单句。看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept，不是已经 Prepare–Process 一致性 bundled（347） interchangeable——347 钉 bundled，本页钉 item 1 第一件事。看见正确进程之间永远过，不是已经四门已经结算（33） interchangeable——33 另钉。347 req3 vs accept bundled unbundling 在本页 item 1 启动。

2. **看见必须 Accept / 看见正确接收者 Process 必须回 Accept / 看见正确进程之间永远过 is not already 已经写了默认 Accept interchangeable / 已经 default-accept interchangeable / 已经默认 Accept 交差 interchangeable / 347 req3coherence bundled interchangeable / 33 four gates interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 794 req3-notany interchangeable / 347 req3 item 2 确定 bug interchangeable / 347 req3 item 3 测试目标 interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事 bundled（347 item 1 余量） interchangeable / 347 req3 item 1 interchangeable，也不是已经是任意块都会 Accept（本页第一件事） interchangeable。**  
   官方写：看见必须 Accept，不是已经写了默认 Accept。看见正确接收者 Process 必须回 Accept，不是已经 default-accept interchangeable——本页钉 not already default-accept 单句。看见正确进程之间永远过，不是已经是任意块都会 Accept（本页第一件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 1 启动。

3. **看见正确进程之间过 / 看见正确提议者交出来的必须过 / 看见正确接收者必须 Accept is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经 Accept 交差 interchangeable / 347 req3coherence bundled interchangeable / 348 req6coherence interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 794 req3-notany interchangeable / 347 req3 item 2 / 347 req3 item 3，也不是已经正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事 bundled（347 item 1 余量） interchangeable / 347 req3 item 1 interchangeable，也不是已经是任意块都会 Accept（本页第一件事） interchangeable / 已经写了默认 Accept（本页第二件事） interchangeable。**  
   官方写：看见正确进程之间过，不是拜占庭提案已经也会过，也不是已经交差。看见正确提议者交出来的必须过，不是已经 settled interchangeable——本页钉 not already settled 单句。看见正确接收者必须 Accept，不是已经写了默认 Accept（本页第二件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 1 启动。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。Prepare–Process 一致性 bundled（347）、Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题（347 item 2 余量 / 795）、Req 3 是大量测试和自动验证的目标不是已经测过（347 item 3 余量 / 796）、四门已经结算（33）、Req 6 必须 Accept（348）、Process 必须只依赖请求和上一份状态（340）是另外那套，本页不抄。

## 官方为什么这样拆

- **正确提议者的准备提案必须被正确接收者 Accept not already any-block ≠ 347 / 33 interchangeable：** 官方把正确进程之间必须过和任意块都会过分开。
- **必须 Accept not already default-accept ≠ 已经写了默认 Accept interchangeable：** 官方把必须 Accept 和已经写了默认 Accept 分开。
- **正确进程之间过 not already settled ≠ 已经交差 interchangeable：** 官方把正确进程之间过和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确提议者的准备提案必须被正确接收者 Accept | 不是 already any-block | 不是四门已经结算 alone（33） |
| 必须 Accept | 不是 already default-accept | 不是 Req 6 必须 Accept alone（348） |
| 正确进程之间过 | 不是 already settled | 不是 Process 必须只依赖请求和上一份状态 alone（340） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept not already any-block / not already default-accept / not already settled 正式三事（347 余量），必须分开正确提议者的准备提案必须被正确接收者 Accept 是不是 already any-block interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable、必须 Accept 是不是 already default-accept interchangeable、正确进程之间过 是不是 already settled interchangeable。可以跳过「看见必须 Accept 就已经任意块都会过 interchangeable / 就已经写了默认 Accept interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 1 启动；续 [`worked-example-req3-notbyz-vs-bundled.md`](worked-example-req3-notbyz-vs-bundled.md)（不变量 795 item 2）；完成见 796。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题。那是不变量 347 item 2 余量 / 795。
- Req 3 是大量测试和自动验证的目标不是已经测过。那是不变量 347 item 3 余量 / 796。
- 四门已经结算。那是不变量 33。
- Req 6 必须 Accept。那是不变量 348。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
