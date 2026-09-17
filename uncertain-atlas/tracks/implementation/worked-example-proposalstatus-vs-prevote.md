# 例：看见 UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算；看见 ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差；看见 REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决

**层次**：实现 / ProposalStatus。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ProposalStatus。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「UNKNOWN 一律是错、引擎当应用坏了会崩不是已经是四门已经结算 / ACCEPT 表示应用认为提案合法、共识会发 Prevote 不是已经交差 / REJECT 表示应用认为提案非法、共识会发 Prevote nil 不是已经能稍后改裁决」，不是四门已经结算，也不是正确提议者的准备提案必须被正确接收者 Accept。不要另写怎样写 ProposalStatus。

## 官方三件事

规范把 UNKNOWN 一律是错、ACCEPT 会发 Prevote、REJECT 会发 Prevote nil 写成三件独立的实现事，不是「看见回了 ProposalStatus 就已经是四门已经结算、已经交差、已经能稍后改裁决」一件事：

1. **看见 `UNKNOWN` 一律是错、引擎当应用坏了会崩 / 看见回了 `UNKNOWN` 不是已经是四门已经结算，也不是已经交差。**  
   官方写：`ProposalStatus` 用在 `ProcessProposal` 回包。回 `UNKNOWN` 一律是错。CometBFT 会当应用坏了，然后崩。看见回了 `UNKNOWN`，不是已经是四门齐了。看见崩了，不是已经交差。看见有枚举，不是已经选型。
2. **看见 `ACCEPT` 表示应用认为提案合法、共识会发 Prevote / 看见回了 `ACCEPT` 不是已经交差，也不是已经必须 Accept。**  
   官方写：`ACCEPT` 表示应用认为这份提案合法。共识算法收下这份提案，并给它发 Prevote。看见回了 `ACCEPT`，不是已经交差。看见会发 Prevote，不是已经是正确提议者的准备提案必须被正确接收者 Accept。看见合法，不是已经过了四门。
3. **看见 `REJECT` 表示应用认为提案非法、共识会发 Prevote nil / 看见回了 `REJECT` 不是已经能稍后改裁决，也不是已经没进块。**  
   官方写：`REJECT` 表示应用认为这份提案非法。共识算法拒掉这份提案，改发 Prevote nil。看见回了 `REJECT`，不是已经能在返回之后再改裁决。看见发了 nil，不是已经没进块。看见非法，不是已经交差。

怎样写 `ProposalStatus`、怎样挑枚举、怎样发 Prevote 是规范里的做法，本页不抄。四门已经结算是不变量 33，本页不抄。

## 官方为什么这样拆

- **UNKNOWN 一律是错、引擎当应用坏了会崩 ≠ 已经是四门已经结算：** 官方把回 UNKNOWN 会崩和四门已经结算分开。
- **ACCEPT 表示应用认为提案合法、共识会发 Prevote ≠ 已经交差：** 官方把发 Prevote 和已经交差分开。
- **REJECT 表示应用认为提案非法、共识会发 Prevote nil ≠ 已经能稍后改裁决：** 官方把发 Prevote nil 和返回之后还能再改裁决分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| UNKNOWN 一律是错、引擎当应用坏了会崩 | 不是已经是四门已经结算 | 不是四门已经结算（33） |
| ACCEPT 表示应用认为提案合法、共识会发 Prevote | 不是已经交差 | 不是正确提议者的准备提案必须被正确接收者 Accept（347） |
| REJECT 表示应用认为提案非法、共识会发 Prevote nil | 不是已经能稍后改裁决 | 不是 Process 调用是同步的就已经能在返回之后再改裁决（354） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见回了 ProposalStatus 就已经是四门已经结算、已经交差、已经能稍后改裁决」，必须分开 UNKNOWN 一律是错、引擎当应用坏了会崩是不是已经是四门已经结算、ACCEPT 表示应用认为提案合法、共识会发 Prevote 是不是已经交差、REJECT 表示应用认为提案非法、共识会发 Prevote nil 是不是已经能稍后改裁决。可以跳过「看见回了 ProposalStatus 就已经是四门已经结算」。不要另写怎样写 ProposalStatus。376 proposalstatus vs prevote bundled unbundling 完成（713 item 1 / 714 item 2 / 715 item 3）；精读 [`worked-example-propstat-notunknown-vs-bundled.md`](worked-example-propstat-notunknown-vs-bundled.md)（不变量 713 item 1）。

## 本页不抄

- 怎样写 `ProposalStatus`、怎样挑枚举、怎样发 Prevote。
- 四门已经结算。那是不变量 33。
- 正确提议者的准备提案必须被正确接收者 Accept。那是不变量 347。
- Process 调用是同步的就已经能在返回之后再改裁决。那是不变量 354。
