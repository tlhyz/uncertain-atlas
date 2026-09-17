# 例：看见正确提议者的准备提案必须被正确接收者 Accept is not already any block Accepts interchangeable / not already default Accept interchangeable / not already settled interchangeable

**层次**：实现 / 正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts / not already default Accept / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts / not already default Accept / not already settled 正式三事（347 余量）/ not 872 req3-notany interchangeable / not 347 req3-coherence-vs-accept bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是四门已经结算（33），也不是 Req 6 必须 Accept（348/869）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

1. **看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 看见正确进程之间永远过 这份必须 is not already 已经是任意块都会 Accept interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 872 req3-notany interchangeable / 873 req3-notbyz interchangeable / 347 req3 item 2 确定 bug interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts / not already default Accept / not already settled 正式三事 bundled（347 item 1 余量） interchangeable / 347 req3 item 1 interchangeable。**  
   官方写：任意两个正确进程 *p*、*q*，若 *q* 的引擎对 *p* 交出的准备提案叫 `ProcessProposal`，*q* 的应用必须在 `ProcessProposalResponse` 里回 Accept。看见正确提议者交出来的必须过，不是任意块已经都会过 interchangeable——本页从 347 item 1 侧钉 not already any block Accepts 单句。347 req3 vs accept bundled unbundling 在本页 item 1 启动。

2. **看见正确进程之间永远过 / 看见必须 Accept / 这份必须 is not already 已经写了默认 Accept interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 872 req3-notany interchangeable / 347 req3 item 3 测试目标 interchangeable / 874 req3-nottested interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把必须 Accept 和已经写了默认 Accept 分开——347 bundled 第一件事常与 33 混成「看见必须 Accept 就已经任意块都会过或已经是默认 Accept interchangeable」，本页钉 not already default Accept 单句。

3. **看见正确进程之间永远过 / 看见正确提议者交出来的必须过 / 这份必须 is not already 已经交差 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 872 req3-notany interchangeable / 873 req3-notbyz interchangeable，也不是已经 Req 6 必须 Accept interchangeable / 348 req6 / 869 req6-notany interchangeable。**  
   官方把正确进程之间过和拜占庭提案已经也会过 / 已经交差分开。看见正确进程之间过，不是拜占庭提案已经也会过 interchangeable。347 req3 vs accept bundled unbundling 在本页 item 1 启动。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts ≠ 已经是任意块都会 Accept interchangeable：** 官方把正确进程之间必须过和任意块都会过分开。
- **看见必须 Accept not already default Accept ≠ 已经写了默认 Accept interchangeable：** 官方把必须 Accept 和已经写了默认 Accept 分开。
- **看见正确进程之间过 not already settled ≠ 已经交差 interchangeable：** 官方把正确进程之间过和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确提议者的准备提案必须被正确接收者 Accept | 不是已经是任意块都会 Accept | 不是四门已经结算（33） |
| 看见必须 Accept | 不是已经写了默认 Accept | 不是 Req 6 必须 Accept（348/869） |
| 看见正确进程之间过 | 不是已经交差 | 不是 Process 必须只依赖请求和上一份状态（340） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确提议者的准备提案必须被正确接收者 Accept not already any block Accepts / not already default Accept / not already settled 正式三事（347 余量），必须分开是不是已经是任意块都会 Accept、是不是已经写了默认 Accept、是不是已经交差。可以跳过「看见必须 Accept 就已经交差」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 1 启动；续 [`worked-example-req3-notbyz-vs-bundled.md`](worked-example-req3-notbyz-vs-bundled.md)（不变量 873 item 2）。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- Prepare 或 Process 里有确定 bug。那是不变量 347 item 2 余量 / 873。
- 四门已经结算。那是不变量 33。
- Req 6 必须 Accept。那是不变量 348 / 869。
