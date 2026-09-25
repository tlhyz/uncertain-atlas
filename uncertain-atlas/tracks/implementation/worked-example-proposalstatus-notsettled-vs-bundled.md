# 例：看见回了 ACCEPT / 看见会发 Prevote / 看见合法 is not already already settled interchangeable / already mustaccept interchangeable / already fourgates interchangeable

**层次**：实现 / ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量）/ not 876 proposalstatus-notsettled interchangeable / not 376 proposalstatus bundled interchangeable」，不是 proposalstatus bundled（376），也不是 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算（875 item 1 余量）或 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决（376 item 3 余量）。不要另写怎样写 ProposalStatus。

## 官方三件事

规范把 Methods 里 ACCEPT 表示应用认为提案合法、共识会发 Prevote 和「已经是回了 ACCEPT 就已经交差 interchangeable / 已经是会发 Prevote 就已经必须 Accept interchangeable / 已经是合法就已经过了四门 interchangeable / 已经是 proposalstatus bundled interchangeable」分开写成三件独立的实现事，不是「看见回了 ACCEPT 就已经交差 interchangeable / 就已经必须 Accept interchangeable / 就已经过了四门 interchangeable」一件事：

1. **看见回了 ACCEPT / 看见 ACCEPT 表示应用认为提案合法、共识会发 Prevote / 看见回了 ACCEPT 状态 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 376 proposalstatus bundled interchangeable / 347 must Accept interchangeable / proposalstatus-sold-as-prevote interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 876 proposalstatus-notsettled interchangeable / 376 proposalstatus item 2 interchangeable，也不是已经 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事 bundled（376 item 2 余量） interchangeable / 376 proposalstatus item 2 interchangeable，也不是已经回了 UNKNOWN 就已经是四门已经结算（875） interchangeable / 33 four gates interchangeable / 回了 REJECT 就能稍后改裁决（376 item 3） interchangeable，也不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable。**  
   官方写：`ACCEPT` 表示应用认为这份提案合法。共识算法收下这份提案，并给它发 Prevote。看见回了 `ACCEPT`，不是已经交差。看见回了 ACCEPT，不是已经 settled interchangeable——376 钉 bundled 三事，本页从 item 2 侧钉 not already settled 单句。看见 ACCEPT 表示应用认为提案合法、共识会发 Prevote，不是已经 proposalstatus bundled（376） interchangeable——376 钉 bundled，本页钉 item 2 第一件事。看见回了 ACCEPT 状态，不是已经正确提议者的准备提案必须被正确接收者 Accept（347） interchangeable——347 另钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续。

2. **看见会发 Prevote / 看见共识会发 Prevote / 看见发了 Prevote is not already 已经必须 Accept interchangeable / 已经 mustaccept interchangeable / 已经必须 Accept 交差 interchangeable / 376 proposalstatus bundled interchangeable / 347 must Accept interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 876 proposalstatus-notsettled interchangeable / 376 proposalstatus item 1 回了 UNKNOWN interchangeable / 376 proposalstatus item 3 回了 REJECT interchangeable，也不是已经 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事 bundled（376 item 2 余量） interchangeable / 376 proposalstatus item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable。**  
   官方写：看见会发 Prevote，不是已经是正确提议者的准备提案必须被正确接收者 Accept。看见共识会发 Prevote，不是已经 mustaccept interchangeable——本页钉 not already mustaccept 单句。看见发了 Prevote，不是已经交差（本页第一件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续。

3. **看见合法 / 看见应用认为提案合法 / 看见合法状态 is not already 已经过了四门 interchangeable / 已经 fourgates interchangeable / 已经过了四门交差 interchangeable / 376 proposalstatus bundled interchangeable / 33 four gates interchangeable，也不是已经 proposalstatus bundled（376） interchangeable / 876 proposalstatus-notsettled interchangeable / 376 proposalstatus item 1 / 376 proposalstatus item 3，也不是已经 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事 bundled（376 item 2 余量） interchangeable / 376 proposalstatus item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable / 已经必须 Accept（本页第二件事） interchangeable。**  
   官方写：看见合法，不是已经过了四门。看见应用认为提案合法，不是已经 fourgates interchangeable——本页钉 not already fourgates 单句。看见合法状态，不是已经必须 Accept（本页第二件事） interchangeable——三件事分开钉。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续。

怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。proposalstatus bundled（376）、UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算（376 item 1 余量 / 875）、REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决（376 item 3 余量）、四门已经结算（33）、正确提议者的准备提案必须被正确接收者 Accept（347）、Process 调用是同步的就已经能在返回之后再改裁决（354）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 ACCEPT not already settled ≠ 376 / 347 interchangeable：** 官方把发 Prevote 和已经交差分开。
- **会发 Prevote not already mustaccept ≠ 已经必须 Accept interchangeable：** 官方把会发 Prevote 和已经必须 Accept 分开。
- **合法 not already fourgates ≠ 已经过了四门 interchangeable：** 官方把合法和已经过了四门分开；376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 ACCEPT | 不是 already settled | 不是正确提议者的准备提案必须被正确接收者 Accept alone（347） |
| 会发 Prevote | 不是 already mustaccept | 不是回了 UNKNOWN already fourgates alone（875） |
| 合法 | 不是 already fourgates | 不是四门已经结算 alone（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 not already settled / not already mustaccept / not already fourgates 正式三事（376 余量），必须分开回了 ACCEPT 是不是 already settled interchangeable / 376 proposalstatus bundled interchangeable / proposalstatus-sold-as-prevote interchangeable、会发 Prevote 是不是 already mustaccept interchangeable、合法 是不是 already fourgates interchangeable。可以跳过「看见回了 ACCEPT 就已经交差 interchangeable / 就已经必须 Accept interchangeable / 就已经过了四门 interchangeable」。不要另写怎样写 ProposalStatus。376 proposalstatus-vs-prevote bundled unbundling 在本页 item 2 续（875 + 876）。

## 本页不抄

- 怎样写 ProposalStatus、怎样挑枚举、怎样发 Prevote。
- proposalstatus bundled。那是不变量 376。
- UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算。那是不变量 376 item 1 余量 / 875。
- REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决。那是不变量 376 item 3 余量。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Process 调用是同步的就已经能在返回之后再改裁决。那是不变量 354。
