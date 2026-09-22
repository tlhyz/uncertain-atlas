# 例：看见 Req 3 是大量测试和自动验证的目标 / 看见会 prevote nil / 看见写了测试目标 is not already already tested interchangeable / already engine-blocks interchangeable / already settled interchangeable

**层次**：实现 / Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量）/ not 796 req3-nottested interchangeable / not 347 req3coherence bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept（794 item 1 余量）或 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题（795 item 2 余量）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

规范把 Requirements 里 Requirement 3 是大量测试和自动验证的目标 和「已经是写了测试目标就已经测过 interchangeable / 已经是会 prevote nil 就已经是引擎会帮你挡 interchangeable / 已经是写了测试目标就已经交差 interchangeable / 已经是 req3coherence bundled interchangeable」分开写成三件独立的实现事，不是「看见写了测试目标就已经测过 interchangeable / 就已经是引擎会帮你挡 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见同一份代码库很可能同时踩中、多数 prevote nil / 看见 Req 3 因此是大量测试和自动验证的目标 / 看见写了测试目标 is not already 已经测过 interchangeable / 已经 tested interchangeable / 已经测过交差 interchangeable / 347 req3coherence bundled interchangeable / 338 preparenondet interchangeable / req3coherence-sold-as-accept interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 796 req3-nottested interchangeable / 347 req3 item 3 interchangeable，也不是已经 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事 bundled（347 item 3 余量） interchangeable / 347 req3 item 3 interchangeable，也不是已经正确提议者的准备提案必须 Accept（794） interchangeable / 795 req3-notbyz interchangeable / 33 four gates interchangeable，也不是已经 Prepare 没有确定性要求（338） interchangeable。**  
   官方写：实践里验证者常常跑同一份代码，所以很可能**同时**踩中。这会让多数（或全部）进程 prevote `nil`，严重伤 CometBFT 的活性。正因为关键，Requirement 3 是大量测试和自动验证的目标。看见同一份代码，不是已经测过。看见 Req 3 因此是大量测试和自动验证的目标，不是已经 tested interchangeable——347 钉 bundled 三事，本页从 item 3 侧钉 not already tested 单句。看见写了测试目标，不是已经 Prepare–Process 一致性 bundled（347） interchangeable——347 钉 bundled，本页钉 item 3 第一件事。看见同一份代码库很可能同时踩中，不是已经正确提议者的准备提案必须 Accept（794） interchangeable——794 另钉 item 1。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

2. **看见会 prevote nil / 看见多数或全部进程 prevote nil / 看见严重伤活性 is not already 已经是引擎会帮你挡 interchangeable / 已经 engine-blocks interchangeable / 已经引擎挡交差 interchangeable / 347 req3coherence bundled interchangeable / 338 preparenondet-sold-as-deterministic interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 796 req3-nottested interchangeable / 347 req3 item 1 必须 Accept interchangeable / 347 req3 item 2 确定 bug interchangeable，也不是已经 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事 bundled（347 item 3 余量） interchangeable / 347 req3 item 3 interchangeable，也不是已经测过（本页第一件事） interchangeable。**  
   官方写：看见会 prevote nil，不是已经是引擎会帮你挡。看见多数或全部进程 prevote nil，不是已经 engine-blocks interchangeable——本页钉 not already engine-blocks 单句。看见严重伤活性，不是已经测过（本页第一件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

3. **看见写了测试目标 / 看见是大量测试和自动验证的目标 / 看见因此是测试目标 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经测试交差 interchangeable / 347 req3coherence bundled interchangeable / 794 req3-notany interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 796 req3-nottested interchangeable / 347 req3 item 1 / 347 req3 item 2，也不是已经 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事 bundled（347 item 3 余量） interchangeable / 347 req3 item 3 interchangeable，也不是已经测过（本页第一件事） interchangeable / 已经是引擎会帮你挡（本页第二件事） interchangeable。**  
   官方写：看见写了测试目标，不是已经交差。看见是大量测试和自动验证的目标，不是已经 settled interchangeable——本页钉 not already settled 单句。看见因此是测试目标，不是已经是引擎会帮你挡（本页第二件事） interchangeable——三件事分开钉。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。Prepare–Process 一致性 bundled（347）、正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept（347 item 1 余量 / 794）、Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题（347 item 2 余量 / 795）、Prepare 没有确定性要求（338）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **Req 3 是大量测试和自动验证的目标 not already tested ≠ 347 / 338 interchangeable：** 官方把必须测和已经测过分开。
- **会 prevote nil not already engine-blocks ≠ 已经是引擎会帮你挡 interchangeable：** 官方把会 prevote nil 和已经是引擎会挡分开。
- **写了测试目标 not already settled ≠ 已经交差 interchangeable：** 官方把写了测试目标和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Req 3 是大量测试和自动验证的目标 | 不是 already tested | 不是 Prepare 没有确定性要求 alone（338） |
| 会 prevote nil | 不是 already engine-blocks | 不是四门已经结算 alone（33） |
| 写了测试目标 | 不是 already settled | 不是必须 Accept 就已经任意块都会过 alone（794） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 3 是大量测试和自动验证的目标不是已经测过 not already tested / not already engine-blocks / not already settled 正式三事（347 余量），必须分开 Req 3 是大量测试和自动验证的目标 是不是 already tested interchangeable / 347 req3coherence bundled interchangeable / req3coherence-sold-as-accept interchangeable、会 prevote nil 是不是 already engine-blocks interchangeable、写了测试目标 是不是 already settled interchangeable。可以跳过「看见写了测试目标就已经测过 interchangeable / 就已经是引擎会帮你挡 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 3 完成（794 + 795 + 796）。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- 正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept。那是不变量 347 item 1 余量 / 794。
- Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题。那是不变量 347 item 2 余量 / 795。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
