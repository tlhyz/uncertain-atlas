# 例：看见正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept；看见 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题；看见 Req 3 是大量测试和自动验证的目标不是已经测过

**层次**：实现 / Prepare–Process 一致性。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept / Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 / Req 3 是大量测试和自动验证的目标不是已经测过」，不是四门已经结算，也不是 Process 必须只依赖请求和上一份状态。不要另写怎样写 Prepare 或 Process。

## 官方三件事

规范把 Prepare 和 Process 的一致性写成三件独立的实现事，不是「看见必须 Accept 就已经任意块都会过、已经只是活性、已经测过」一件事：

1. **看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 看见正确进程之间永远过 不是已经是任意块都会 Accept，也不是已经是 Process 默认 Accept。**  
   官方写：任意两个正确进程 *p*、*q*，若 *q* 的引擎对 *p* 交出的准备提案 *u<sub>p</sub>* 叫 `ProcessProposal`，*q* 的应用必须在 `ProcessProposalResponse` 里回 Accept。看见正确提议者交出来的必须过，不是任意块已经都会过。看见必须 Accept，不是已经写了默认 Accept。看见正确进程之间过，不是拜占庭提案已经也会过。
2. **看见 Prepare 或 Process（或两边）里有确定 bug / 看见踩中的人严格算拜占庭 不是已经只是活性问题，也不是已经是 Process 非确定 bug。**  
   官方写：反过来，若 `PrepareProposal` 或 `ProcessProposal`（或两边）里有**确定** bug，严格说，踩中的进程都算拜占庭。看见有确定 bug，不是已经只伤活性。看见算拜占庭，不是已经是 340 那种 Accept/Reject 不再确定。看见 Prepare 也能踩中，不是已经只是 Process 的确定性。
3. **看见同一份代码库很可能同时踩中、多数 prevote nil / 看见 Req 3 因此是大量测试和自动验证的目标 不是已经测过，也不是已经是引擎会帮你挡。**  
   官方写：实践里验证者常常跑同一份代码，所以很可能**同时**踩中。这会让多数（或全部）进程 prevote `nil`，严重伤 CometBFT 的活性。正因为关键，Requirement 3 是大量测试和自动验证的目标。看见同一份代码，不是已经测过。看见会 prevote nil，不是已经是引擎会帮你挡。看见写了测试目标，不是已经交差。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **正确提议者的准备提案必须被正确接收者 Accept ≠ 已经是任意块都会 Accept：** 官方把正确进程之间必须过和任意块都会过分开。
- **Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 ≠ 已经只是活性问题：** 官方把确定 bug 算拜占庭和只伤活性、非确定 bug 分开。
- **Req 3 是大量测试和自动验证的目标 ≠ 已经测过：** 官方把必须测和已经测过、引擎会挡分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 正确提议者的准备提案必须被正确接收者 Accept | 不是已经是任意块都会 Accept | 不是四门已经结算（33） |
| Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 | 不是已经只是活性问题 | 不是 Process 必须只依赖请求和上一份状态（340） |
| Req 3 是大量测试和自动验证的目标 | 不是已经测过 | 不是 Prepare 没有确定性要求（338） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见必须 Accept 就已经任意块都会过、已经只是活性、已经测过」，必须分开正确提议者的准备提案必须被正确接收者 Accept 是不是已经是任意块都会 Accept、Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭是不是已经只是活性问题、Req 3 是大量测试和自动验证的目标是不是已经测过。可以跳过「看见必须 Accept 就已经交差」。不要另写怎样写 Prepare 或 Process。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- 四门已经结算。那是不变量 33。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
- Prepare 没有确定性要求。那是不变量 338。
