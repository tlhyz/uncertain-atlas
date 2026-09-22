# 例：看见 Prepare 或 Process 里有确定 bug / 看见踩中的人严格算拜占庭 / 看见 Prepare 也能踩中 is not already already only-liveness interchangeable / already process-nondet interchangeable / already settled interchangeable

**层次**：实现 / Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量）/ not 795 req3-notbyz interchangeable / not 347 req3coherence bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept（794 item 1 余量）或 Req 3 是大量测试和自动验证的目标不是已经测过（796 item 3 余量）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

规范把 Requirements 里 Prepare 或 Process（或两边）里有确定 bug、踩中的人严格算拜占庭 和「已经是有确定 bug 就已经只是活性问题 interchangeable / 已经是算拜占庭就已经是 Process 非确定 bug interchangeable / 已经是 Prepare 也能踩中就已经交差 interchangeable / 已经是 req3coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见算拜占庭就已经只是活性问题 interchangeable / 就已经是非确定 bug interchangeable / 就已经交差 interchangeable」一件事：

1. **看见 Prepare 或 Process（或两边）里有确定 bug / 看见踩中的人严格算拜占庭 / 看见有确定 bug is not already 已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable / 347 req3coherence bundled interchangeable / 340 processdet interchangeable / req3coherence-sold-as-accept interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 795 req3-notbyz interchangeable / 347 req3 item 2 interchangeable，也不是已经 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事 bundled（347 item 2 余量） interchangeable / 347 req3 item 2 interchangeable，也不是已经正确提议者的准备提案必须 Accept（794） interchangeable / 796 req3-nottested interchangeable / 33 four gates interchangeable，也不是已经 Process 必须只依赖请求和上一份状态（340） interchangeable。**  
   官方写：反过来，若 `PrepareProposal` 或 `ProcessProposal`（或两边）里有**确定** bug，严格说，踩中的进程都算拜占庭。看见有确定 bug，不是已经只伤活性。看见踩中的人严格算拜占庭，不是已经 only-liveness interchangeable——347 钉 bundled 三事，本页从 item 2 侧钉 not already only-liveness 单句。看见 Prepare 或 Process（或两边）里有确定 bug，不是已经 Prepare–Process 一致性 bundled（347） interchangeable——347 钉 bundled，本页钉 item 2 第一件事。看见有确定 bug，不是已经正确提议者的准备提案必须 Accept（794） interchangeable——794 另钉 item 1。347 req3 vs accept bundled unbundling 在本页 item 2 续。

2. **看见算拜占庭 / 看见踩中的人严格算拜占庭 / 看见确定 bug 让人算拜占庭 is not already 已经是 Process 非确定 bug interchangeable / 已经 process-nondet interchangeable / 已经非确定交差 interchangeable / 347 req3coherence bundled interchangeable / 340 processdet-sold-as-prepare interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 795 req3-notbyz interchangeable / 347 req3 item 1 必须 Accept interchangeable / 347 req3 item 3 测试目标 interchangeable，也不是已经 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事 bundled（347 item 2 余量） interchangeable / 347 req3 item 2 interchangeable，也不是已经只是活性问题（本页第一件事） interchangeable。**  
   官方写：看见算拜占庭，不是已经是 340 那种 Accept/Reject 不再确定。看见踩中的人严格算拜占庭，不是已经 process-nondet interchangeable——本页钉 not already process-nondet 单句。看见确定 bug 让人算拜占庭，不是已经只是活性问题（本页第一件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 2 续。

3. **看见 Prepare 也能踩中 / 看见 Prepare 或 Process 两边都能踩 / 看见不只是 Process 会踩 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经踩中交差 interchangeable / 347 req3coherence bundled interchangeable / 794 req3-notany interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 795 req3-notbyz interchangeable / 347 req3 item 1 / 347 req3 item 3，也不是已经 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事 bundled（347 item 2 余量） interchangeable / 347 req3 item 2 interchangeable，也不是已经只是活性问题（本页第一件事） interchangeable / 已经是 Process 非确定 bug（本页第二件事） interchangeable。**  
   官方写：看见 Prepare 也能踩中，不是已经只是 Process 的确定性，也不是已经交差。看见 Prepare 或 Process 两边都能踩，不是已经 settled interchangeable——本页钉 not already settled 单句。看见不只是 Process 会踩，不是已经是 Process 非确定 bug（本页第二件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 2 续。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。Prepare–Process 一致性 bundled（347）、正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept（347 item 1 余量 / 794）、Req 3 是大量测试和自动验证的目标不是已经测过（347 item 3 余量 / 796）、Process 必须只依赖请求和上一份状态（340）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only-liveness ≠ 347 / 340 interchangeable：** 官方把确定 bug 算拜占庭和只伤活性分开。
- **算拜占庭 not already process-nondet ≠ 已经是非确定 bug interchangeable：** 官方把算拜占庭和已经是非确定 bug 分开。
- **Prepare 也能踩中 not already settled ≠ 已经交差 interchangeable：** 官方把 Prepare 也能踩中和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 | 不是 already only-liveness | 不是 Process 必须只依赖请求和上一份状态 alone（340） |
| 算拜占庭 | 不是 already process-nondet | 不是四门已经结算 alone（33） |
| Prepare 也能踩中 | 不是 already settled | 不是必须 Accept 就已经任意块都会过 alone（794） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题 not already only-liveness / not already process-nondet / not already settled 正式三事（347 余量），必须分开 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 是不是 already only-liveness interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable、算拜占庭 是不是 already process-nondet interchangeable、Prepare 也能踩中 是不是 already settled interchangeable。可以跳过「看见算拜占庭就已经只是活性问题 interchangeable / 就已经是非确定 bug interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 2 续（794 + 795）；续 [`worked-example-req3-nottested-vs-bundled.md`](worked-example-req3-nottested-vs-bundled.md)（不变量 796 item 3）；完成见 796。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- 正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept。那是不变量 347 item 1 余量 / 794。
- Req 3 是大量测试和自动验证的目标不是已经测过。那是不变量 347 item 3 余量 / 796。
- Process 必须只依赖请求和上一份状态。那是不变量 340。
- 四门已经结算。那是不变量 33。
