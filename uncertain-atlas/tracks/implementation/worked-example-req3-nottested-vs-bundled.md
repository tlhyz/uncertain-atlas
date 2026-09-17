# 例：看见 Req 3 是大量测试和自动验证的目标 is not already tested interchangeable / not already engine blocks interchangeable / not already settled interchangeable

**层次**：实现 / Req 3 是大量测试和自动验证的目标 not already tested / not already engine blocks / not already settled 正式三事（347 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Req 3 是大量测试和自动验证的目标 not already tested / not already engine blocks / not already settled 正式三事（347 余量）/ not 874 req3-nottested interchangeable / not 347 req3-coherence-vs-accept bundled interchangeable」，不是 Prepare–Process 一致性 bundled（347），也不是 Prepare 没有确定性要求（338），也不是四门已经结算（33）。不要另写怎样写 Prepare 或 Process。

## 官方三件事

1. **看见同一份代码库很可能同时踩中、多数 prevote nil / 看见 Req 3 因此是大量测试和自动验证的目标 这份目标 is not already 已经测过 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 874 req3-nottested interchangeable / 872 req3-notany interchangeable / 347 req3 item 1 必须 Accept interchangeable，也不是已经 Req 3 是大量测试和自动验证的目标 not already tested / not already engine blocks / not already settled 正式三事 bundled（347 item 3 余量） interchangeable / 347 req3 item 3 interchangeable。**  
   官方写：实践里验证者常常跑同一份代码，所以很可能同时踩中。这会让多数（或全部）进程 prevote `nil`，严重伤 CometBFT 的活性。正因为关键，Requirement 3 是大量测试和自动验证的目标。看见同一份代码，不是已经测过 interchangeable——本页从 347 item 3 侧钉 not already tested 单句。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

2. **看见会 prevote nil / 看见写了测试目标 / 这份目标 is not already 已经是引擎会帮你挡 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 874 req3-nottested interchangeable / 347 req3 item 2 确定 bug interchangeable / 873 req3-notbyz interchangeable，也不是已经 Prepare 没有确定性要求 interchangeable / 338 preparenondet interchangeable。**  
   官方把会 prevote nil 和已经是引擎会帮你挡分开——347 bundled 第三件事常与 338 混成「看见写了测试目标就已经测过或已经是引擎会挡 interchangeable」，本页钉 not already engine blocks 单句。

3. **看见会 prevote nil / 看见写了测试目标 / 这份目标 is not already 已经交差 interchangeable，也不是已经 Prepare–Process 一致性 bundled（347） interchangeable / 874 req3-nottested interchangeable / 872 req3-notany interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把写了测试目标和已经交差分开。看见写了测试目标，不是已经交差 interchangeable。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

怎样写 Prepare / Process、怎样测、怎样写测试向量是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Req 3 是大量测试和自动验证的目标 not already tested ≠ 已经测过 interchangeable：** 官方把必须测和已经测过分开。
- **看见会 prevote nil not already engine blocks ≠ 已经是引擎会帮你挡 interchangeable：** 官方把会 prevote nil 和已经是引擎会挡分开。
- **看见写了测试目标 not already settled ≠ 已经交差 interchangeable：** 官方把写了测试目标和已经交差分开；347 req3 vs accept bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Req 3 是大量测试和自动验证的目标 | 不是已经测过 | 不是 Prepare 没有确定性要求（338） |
| 看见会 prevote nil | 不是已经是引擎会帮你挡 | 不是四门已经结算（33） |
| 看见写了测试目标 | 不是已经交差 | 不是必须 Accept 就已经任意块都会过（872） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Req 3 是大量测试和自动验证的目标 not already tested / not already engine blocks / not already settled 正式三事（347 余量），必须分开是不是已经测过、是不是已经是引擎会帮你挡、是不是已经交差。可以跳过「看见写了测试目标就已经测过」。不要另写怎样写 Prepare 或 Process。347 req3 vs accept bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Prepare / Process、怎样测、怎样写测试向量。
- Prepare–Process 一致性 bundled。那是不变量 347。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347 item 1 余量 / 872。
- Prepare 没有确定性要求。那是不变量 338。
- 四门已经结算。那是不变量 33。
