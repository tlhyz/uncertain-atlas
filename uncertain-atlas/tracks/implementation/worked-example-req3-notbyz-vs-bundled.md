# 例：看见 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 is not already only liveness interchangeable / not already Process nondet interchangeable / not already settled interchangeable

**层次**：实现 / Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness / not already Process nondet / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness / not already Process nondet / not already settled 正式三事（347 余量）/ not 873 req3-notbyz interchangeable / not 347 req3-coherence-vs-accept bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是 Process 必须只依赖请求和上一份状态（340），也不是四门已经结算（33）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

1. **看见 Prepare 或 Process（或两边）里有确定 bug / 看见踩中的人严格算拜占庭 这份确定 is not already 已经只是活性问题 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 873 req3-notbyz interchangeable / 872 req3-notany interchangeable / 347 req3 item 1 必须 Accept interchangeable，也不是已经 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness / not already Process nondet / not already settled 正式三事 bundled（347 item 2 余量） interchangeable / 347 req3 item 2 interchangeable。**  
   官方写：反过来，若 `PrepareProposal` 或 `ProcessProposal`（或两边）里有确定 bug，严格说，踩中的进程都算拜占庭。看见有确定 bug，不是已经只伤活性 interchangeable——本页从 347 item 2 侧钉 not already only liveness 单句。347 req3 vs accept bundled unbundling 在本页 item 2 续。

2. **看见踩中的人严格算拜占庭 / 看见算拜占庭 / 这份确定 is not already 已经是 Process 非确定 bug interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 873 req3-notbyz interchangeable / 347 req3 item 3 测试目标 interchangeable / 874 req3-nottested interchangeable，也不是已经 Process 必须只依赖请求和上一份状态 interchangeable / 340 processdet interchangeable。**  
   官方把算拜占庭和已经是 340 那种 Accept/Reject 不再确定分开——347 bundled 第二件事常与 340 混成「看见算拜占庭就已经只是活性或已经是非确定 bug interchangeable」，本页钉 not already Process nondet 单句。

3. **看见踩中的人严格算拜占庭 / 看见 Prepare 也能踩中 / 这份确定 is not already 已经交差 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 873 req3-notbyz interchangeable / 872 req3-notany interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把 Prepare 也能踩中和已经只是 Process 的确定性 / 已经交差分开。看见 Prepare 也能踩中，不是已经只是 Process 的确定性 interchangeable。347 req3 vs accept bundled unbundling 在本页 item 2 续。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness ≠ 已经只是活性问题 interchangeable：** 官方把确定 bug 算拜占庭和只伤活性分开。
- **看见算拜占庭 not already Process nondet ≠ 已经是非确定 bug interchangeable：** 官方把算拜占庭和已经是非确定 bug 分开。
- **看见 Prepare 也能踩中 not already settled ≠ 已经交差 interchangeable：** 官方把 Prepare 也能踩中和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 | 不是已经只是活性问题 | 不是 Process 必须只依赖请求和上一份状态（340） |
| 看见算拜占庭 | 不是已经是非确定 bug | 不是四门已经结算（33） |
| 看见 Prepare 也能踩中 | 不是已经交差 | 不是必须 Accept 就已经任意块都会过（872） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only liveness / not already Process nondet / not already settled 正式三事（347 余量），必须分开是不是已经只是活性问题、是不是已经是非确定 bug、是不是已经交差。可以跳过「看见算拜占庭就已经只是活性问题」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 2 续；续 [`worked-example-req3-nottested-vs-bundled.md`](worked-example-req3-nottested-vs-bundled.md)（不变量 874 item 3）。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347 item 1 余量 / 872。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
- 四门已经结算。那是不变量 33。
