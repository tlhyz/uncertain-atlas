# 例：看见 Query 回了 Proof is not already matched interchangeable / not already one-tree interchangeable / not already settled interchangeable

**层次**：实现 / Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量）/ not 948 query-proof-notmatch interchangeable / not 325 query-proof-vs-apphash bundled interchangeable」，不是证明 bundled（325），也不是 QueryState 已经是 ExecuteTxState（314），也不是只有 AppHash 可信任（38）。不要另写怎样编证明或怎样种树。

## 官方三件事

1. **看见 Query 回了 Proof / 看见 QueryResponse.Proof 这份证明 is not already 已经对上 AppHash interchangeable，也不是已经证明 bundled（325） interchangeable / 948 query-proof-notmatch interchangeable / 947 query-proof-nottx interchangeable / 325 query-proof item 1 头上有 AppHash interchangeable，也不是已经 Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事 bundled（325 item 2 余量） interchangeable / 325 query-proof item 2 interchangeable。**  
   官方写：应用可以在 QueryResponse.Proof 里回这份状态的证明，用对应块的 AppHash 去验。看见回了 Proof，不是已经验过 interchangeable——本页从 325 item 2 侧钉 not already matched 单句。325 query-proof vs apphash bundled unbundling 在本页 item 2 续。

2. **看见有 type / 看见回了 Proof / 这份证明 is not already 已经是同一棵树 interchangeable，也不是已经证明 bundled（325） interchangeable / 948 query-proof-notmatch interchangeable / 325 query-proof item 3 一层根 interchangeable / 949 query-proof-notfinal interchangeable，也不是已经 QueryState 已经是 ExecuteTxState interchangeable / 314 querystate interchangeable。**  
   官方写：每一条 ProofOp 只证明一棵指定 type 的树里的一把键。看见有 type，不是已经是同一棵树 interchangeable。本页钉 not already one-tree 单句。

3. **看见能证存在 / 看见回了 Proof / 这份证明 is not already 已经交差 interchangeable，也不是已经证明 bundled（325） interchangeable / 948 query-proof-notmatch interchangeable / 947 query-proof-nottx interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把能证存在和已经能证不存在分开。看见能证存在，不是已经交差 interchangeable。325 query-proof vs apphash bundled unbundling 在本页 item 2 续。

怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **Query 回了 Proof not already matched ≠ 已经对上 AppHash interchangeable：** 官方把回证明和用对应块的 AppHash 去验分开。
- **看见有 type not already one-tree ≠ 已经是同一棵树 interchangeable：** 官方把一条 ProofOp 只覆盖一棵树的一把键分开。
- **看见能证存在 not already settled ≠ 已经交差 interchangeable：** 官方把能证存在和已经能证不存在分开；325 query-proof vs apphash bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回了 Proof | 不是已经对上 AppHash | 不是 QueryState 已经是 ExecuteTxState（314） |
| 看见有 type | 不是已经是同一棵树 | 不是只有 AppHash 可信任（38） |
| 看见能证存在 | 不是已经交差 | 不是一层根就已经对上最终 AppHash（949） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof not already matched / not already one-tree / not already settled 正式三事（325 余量），必须分开是不是已经对上 AppHash、是不是已经是同一棵树、是不是已经交差。可以跳过「看见头上有 AppHash 就已经能验应用」。不要另写怎样编证明或怎样种树。325 query-proof vs apphash bundled unbundling 在本页 item 2 续；续 [`worked-example-query-proof-notfinal-vs-bundled.md`](worked-example-query-proof-notfinal-vs-bundled.md)（不变量 949 item 3）。

## 本页不抄

- 怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头。
- 证明 bundled。那是不变量 325。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- 只有 AppHash 可信任。那是不变量 38。
