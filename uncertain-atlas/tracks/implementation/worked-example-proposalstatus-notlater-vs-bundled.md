# 例：看见回了 REJECT / 看见发了 nil / 看见非法 is not already already later interchangeable / already outofblock interchangeable / already settled interchangeable

**层次**：实现 / REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量）/ not 877 proposalstatus-notlater interchangeable / not 376 proposalstatus bundled interchangeable」，不是 proposalstatus bundled（376），也不是 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算（875 item 1 余量）或 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差（876 item 2 余量）。不要另写怎样写 ProposalStatus。

## 官方三件事

规范把 Methods 里 REJECT 表示应用认为提案非法、共识会发 Prevote nil 和「已经是回了 REJECT 就已经能稍后改裁决 interchangeable / 已经是发了 nil 就已经没进块 interchangeable / 已经是非法就已经交差 interchangeable / 已经是 proposalstatus bundled interchangeable」分开写成三件独立的实现事，不是「看见回了 REJECT 就已经能稍后改裁决 interchangeable / 就已经没进块 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见回了 REJECT / 看见 REJECT 表示应用认为提案非法、共识会发 Prevote nil / 看见回了 REJECT 状态 is not already 已经能稍后改裁决 interchangeable / 已经 later interchangeable / 已经能稍后改裁决交差 interchangeable / 376 proposalstatus bundled interchangeable / 354 processwhen interchangeable / proposalstatus-sold-as-prevote interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 877 proposalstatus-notlater interchangeable / 376 proposalstatus item 3 interchangeable，也不是已经 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事 bundled（376 item 3 余量） interchangeable / 376 proposalstatus item 3 interchangeable，也不是已经回了 UNKNOWN 就已经是四门已经结算（875） interchangeable / 回了 ACCEPT 就已经交差（876） interchangeable / 33 four gates interchangeable，也不是已经 Process 调用是同步的就已经能在返回之后再改裁决（354） interchangeable。**  
   官方写：`REJECT` 表示应用认为这份提案非法。共识算法拒掉这份提案，改发 Prevote nil。看见回了 `REJECT`，不是已经能在返回之后再改裁决。看见回了 REJECT，不是已经 later interchangeable——376 钉 bundled 三事，本页从 item 3 侧钉 not already later 单句。看见 REJECT 表示应用认为提案非法、共识会发 Prevote nil，不是已经 proposalstatus bundled（376） interchangeable——376 钉 bundled，本页钉 item 3 第一件事。看见回了 REJECT 状态，不是已经 Process 调用是同步的就已经能在返回之后再改裁决（354） interchangeable——354 另钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成。

2. **看见发了 nil / 看见共识会发 Prevote nil / 看见发了 Prevote nil is not already 已经没进块 interchangeable / 已经 outofblock interchangeable / 已经没进块交差 interchangeable / 376 proposalstatus bundled interchangeable / 354 processwhen interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 877 proposalstatus-notlater interchangeable / 376 proposalstatus item 1 回了 UNKNOWN interchangeable / 376 proposalstatus item 2 回了 ACCEPT interchangeable，也不是已经 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事 bundled（376 item 3 余量） interchangeable / 376 proposalstatus item 3 interchangeable，也不是已经能稍后改裁决（本页第一件事） interchangeable。**  
   官方写：看见发了 nil，不是已经没进块。看见共识会发 Prevote nil，不是已经 outofblock interchangeable——本页钉 not already outofblock 单句。看见发了 Prevote nil，不是已经能稍后改裁决（本页第一件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成。

3. **看见非法 / 看见应用认为提案非法 / 看见非法状态 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 376 proposalstatus bundled interchangeable / 876 proposalstatus-notsettled interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 877 proposalstatus-notlater interchangeable / 376 proposalstatus item 1 / 376 proposalstatus item 2，也不是已经 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事 bundled（376 item 3 余量） interchangeable / 376 proposalstatus item 3 interchangeable，也不是已经能稍后改裁决（本页第一件事） interchangeable / 已经没进块（本页第二件事） interchangeable。**  
   官方写：看见非法，不是已经交差。看见应用认为提案非法，不是已经 settled interchangeable——本页钉 not already settled 单句。看见非法状态，不是已经没进块（本页第二件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成。

怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。proposalstatus bundled（376）、UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算（376 item 1 余量 / 875）、ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差（376 item 2 余量 / 876）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、Process 调用是同步的就已经能在返回之后再改裁决（354）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 REJECT not already later ≠ 376 / 354 interchangeable：** 官方把发 Prevote nil 和返回之后还能再改裁决分开。
- **发了 nil not already outofblock ≠ 已经没进块 interchangeable：** 官方把发了 nil 和已经没进块分开。
- **非法 not already settled ≠ 已经交差 interchangeable：** 官方把非法和已经交差分开；376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 REJECT | 不是 already later | 不是 Process 同步就能稍后改裁决 alone（354） |
| 发了 nil | 不是 already outofblock | 不是回了 ACCEPT already settled alone（876） |
| 非法 | 不是 already settled | 不是回了 UNKNOWN already fourgates alone（875） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决 not already later / not already outofblock / not already settled 正式三事（376 余量），必须分开回了 REJECT 是不是 already later interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable、发了 nil 是不是 already outofblock interchangeable、非法 是不是 already settled interchangeable。可以跳过「看见回了 REJECT 就已经能稍后改裁决 interchangeable / 就已经没进块 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 ProposalStatus。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 3 完成（875 + 876 + 877）。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- proposalstatus bundled。那是不变量 376。
- UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算。那是不变量 376 item 1 余量 / 875。
- ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差。那是不变量 376 item 2 余量 / 876。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Process 调用是同步的就已经能在返回之后再改裁决。那是不变量 354。
