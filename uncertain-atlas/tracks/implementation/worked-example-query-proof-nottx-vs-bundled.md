# 例：看见头上有 AppHash is not already tx-merkle interchangeable / not already same-anchor interchangeable / not already settled interchangeable

**层次**：实现 / 头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量）/ not 947 query-proof-nottx interchangeable / not 325 query-proof-vs-apphash bundled interchangeable」，不是证明 bundled（325），也不是本头 AppHash 已经是本高度交差（147），也不是 Query 回了就已经复制（329/938）。不要另写怎样编证明或怎样种树。

## 官方三件事

1. **看见头上有 AppHash / 看见和 ValidatorsHash、DataHash 并列 这份哈希 is not already 已经是交易默克尔 interchangeable，也不是已经证明 bundled（325） interchangeable / 947 query-proof-nottx interchangeable / 948 query-proof-notmatch interchangeable / 325 query-proof item 2 Query 回了 Proof interchangeable，也不是已经头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事 bundled（325 item 1 余量） interchangeable / 325 query-proof item 1 interchangeable。**  
   官方写：头上有好几份哈希，各自锚一类证明。ValidatorsHash 用来快验验证者集合。DataHash 用来快验块里的交易。AppHash 是应用自己的。看见头上有 AppHash，不是已经是 DataHash interchangeable——本页从 325 item 1 侧钉 not already tx-merkle 单句。325 query-proof vs apphash bundled unbundling 在本页 item 1 启动。

2. **看见和另外两份并列 / 看见头上有 AppHash / 这份哈希 is not already 已经同一种锚 interchangeable，也不是已经证明 bundled（325） interchangeable / 947 query-proof-nottx interchangeable / 325 query-proof item 3 一层根 interchangeable / 949 query-proof-notfinal interchangeable，也不是已经本头 AppHash 已经是本高度交差 interchangeable / 147 apphash-commit interchangeable。**  
   官方把 ValidatorsHash、DataHash、应用自己的 AppHash 分成三种锚——325 bundled 第一件事常与 147 混成「看见头上有 AppHash 就已经是交易默克尔或已经交差 interchangeable」，本页钉 not already same-anchor 单句。

3. **看见交易在 / 看见头上有 AppHash / 这份哈希 is not already 已经交差 interchangeable，也不是已经证明 bundled（325） interchangeable / 947 query-proof-nottx interchangeable / 948 query-proof-notmatch interchangeable，也不是已经 Query 回了就已经复制 interchangeable / 329/938 query-notrepl interchangeable。**  
   官方把交易在和已经有这份分开的应用状态分开。看见交易在，不是已经交差 interchangeable。325 query-proof vs apphash bundled unbundling 在本页 item 1 启动。

怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **头上有 AppHash not already tx-merkle ≠ 已经是交易默克尔 interchangeable：** 官方把 ValidatorsHash、DataHash、应用自己的 AppHash 分成三种锚。
- **看见和另外两份并列 not already same-anchor ≠ 已经同一种锚 interchangeable：** 官方把三份哈希并列和已经同一种锚分开。
- **看见交易在 not already settled ≠ 已经交差 interchangeable：** 官方把交易在和已经有这份分开的应用状态分开；325 query-proof vs apphash bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 头上有 AppHash | 不是已经是交易默克尔 | 不是本头 AppHash 已经是本高度交差（147） |
| 看见和另外两份并列 | 不是已经同一种锚 | 不是 Query 回了就已经复制（329/938） |
| 看见交易在 | 不是已经交差 | 不是 Query 回了 Proof 就已经对上（948） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash not already tx-merkle / not already same-anchor / not already settled 正式三事（325 余量），必须分开是不是已经是交易默克尔、是不是已经同一种锚、是不是已经交差。可以跳过「看见头上有 AppHash 就已经能验应用」。不要另写怎样编证明或怎样种树。325 query-proof vs apphash bundled unbundling 在本页 item 1 启动；续 [`worked-example-query-proof-notmatch-vs-bundled.md`](worked-example-query-proof-notmatch-vs-bundled.md)（不变量 948 item 2）。

## 本页不抄

- 怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头。
- 证明 bundled。那是不变量 325。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- Query 回了就已经复制。那是不变量 329/938。
