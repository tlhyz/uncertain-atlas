# 例：看见回了 UNKNOWN / 看见崩了 / 看见有枚举 is not already already fourgates interchangeable / already settled interchangeable / already selected interchangeable

**层次**：实现 / UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量）/ not 875 proposalstatus-notfourgates interchangeable / not 376 proposalstatus bundled interchangeable」，不是 proposalstatus bundled（376），也不是 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差（376 item 2 余量）或 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决（376 item 3 余量）。不要另写怎样写 ProposalStatus。

## 官方三件事

规范把 Methods 里 UNKNOWN 一律是错、引擎当应用坏了会崩 和「已经是回了 UNKNOWN 就已经是四门已经结算 interchangeable / 已经是崩了就已经交差 interchangeable / 已经是有枚举就已经选型 interchangeable / 已经是 proposalstatus bundled interchangeable」分开写成三件独立的实现事，不是「看见回了 UNKNOWN 就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经选型 interchangeable」一件事：

1. **看见回了 UNKNOWN / 看见 UNKNOWN 一律是错、引擎当应用坏了会崩 / 看见回了 UNKNOWN 状态 is not already 已经是四门已经结算 interchangeable / 已经 fourgates interchangeable / 已经是四门已经结算交差 interchangeable / 376 proposalstatus bundled interchangeable / 33 four gates interchangeable / proposalstatus-sold-as-prevote interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 875 proposalstatus-notfourgates interchangeable / 376 proposalstatus item 1 interchangeable，也不是已经 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事 bundled（376 item 1 余量） interchangeable / 376 proposalstatus item 1 interchangeable，也不是已经回了 ACCEPT 就已经交差（376 item 2） interchangeable / 回了 REJECT 就能稍后改裁决（376 item 3） interchangeable / 347 must Accept interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`ProposalStatus` 用在 `ProcessProposal` 回包。回 `UNKNOWN` 一律是错。CometBFT 会当应用坏了，然后崩。看见回了 `UNKNOWN`，不是已经是四门齐了。看见回了 UNKNOWN，不是已经 fourgates interchangeable——376 钉 bundled 三事，本页从 item 1 侧钉 not already fourgates 单句。看见 UNKNOWN 一律是错、引擎当应用坏了会崩，不是已经 proposalstatus bundled（376） interchangeable——376 钉 bundled，本页钉 item 1 第一件事。看见回了 UNKNOWN 状态，不是已经四门已经结算（33） interchangeable——33 另钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动。

2. **看见崩了 / 看见引擎当应用坏了会崩 / 看见崩 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 376 proposalstatus bundled interchangeable / 33 four gates interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 875 proposalstatus-notfourgates interchangeable / 376 proposalstatus item 2 回了 ACCEPT interchangeable / 376 proposalstatus item 3 回了 REJECT interchangeable，也不是已经 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事 bundled（376 item 1 余量） interchangeable / 376 proposalstatus item 1 interchangeable，也不是已经是四门已经结算（本页第一件事） interchangeable。**  
   官方写：看见崩了，不是已经交差。看见引擎当应用坏了会崩，不是已经 settled interchangeable——本页钉 not already settled 单句。看见崩，不是已经是四门已经结算（本页第一件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动。

3. **看见有枚举 / 看见 ProposalStatus 枚举 / 看见有 UNKNOWN/ACCEPT/REJECT is not already 已经选型 interchangeable / 已经 selected interchangeable / 已经选型交差 interchangeable / 376 proposalstatus bundled interchangeable / 354 processwhen interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 875 proposalstatus-notfourgates interchangeable / 376 proposalstatus item 2 / 376 proposalstatus item 3，也不是已经 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事 bundled（376 item 1 余量） interchangeable / 376 proposalstatus item 1 interchangeable，也不是已经是四门已经结算（本页第一件事） interchangeable / 已经交差（本页第二件事） interchangeable。**  
   官方写：看见有枚举，不是已经选型。看见 ProposalStatus 枚举，不是已经 selected interchangeable——本页钉 not already selected 单句。看见有 UNKNOWN/ACCEPT/REJECT，不是已经交差（本页第二件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动。

怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。proposalstatus bundled（376）、ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差（376 item 2 余量）、REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决（376 item 3 余量）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、Process 调用是同步的就已经能在返回之后再改裁决（354）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 UNKNOWN not already fourgates ≠ 376 / 33 interchangeable：** 官方把回 UNKNOWN 会崩和四门已经结算分开。
- **崩了 not already settled ≠ 已经交差 interchangeable：** 官方把崩了和已经交差分开。
- **有枚举 not already selected ≠ 已经选型 interchangeable：** 官方把有枚举和已经选型分开；376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 UNKNOWN | 不是 already fourgates | 不是四门已经结算 alone（33） |
| 崩了 | 不是 already settled | 不是 ACCEPT 就已经交差 alone（376 item 2） |
| 有枚举 | 不是 already selected | 不是 Process 同步就能稍后改裁决 alone（354） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 not already fourgates / not already settled / not already selected 正式三事（376 余量），必须分开回了 UNKNOWN 是不是 already fourgates interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable、崩了 是不是 already settled interchangeable、有枚举 是不是 already selected interchangeable。可以跳过「看见回了 UNKNOWN 就已经是四门已经结算 interchangeable / 就已经交差 interchangeable / 就已经选型 interchangeable」。不要另写怎样写 ProposalStatus。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 1 启动（875）。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- proposalstatus bundled。那是不变量 376。
- ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差。那是不变量 376 item 2 余量。
- REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决。那是不变量 376 item 3 余量。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Process 调用是同步的就已经能在返回之后再改裁决。那是不变量 354。
