# 例：看见回了 Proof / 看见有 type / 看见能证存在 is not already already verified interchangeable / already same-tree interchangeable / already prove-absence interchangeable

**层次**：实现 / Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量）/ not 732 queryproof-notverified interchangeable / not 325 queryproof bundled interchangeable」，不是 Query Proofs bundled（325），也不是头上有 AppHash 不是已经是交易默克尔（731 item 1 余量）或一层 ProofOp 的根不是已经对上最终 AppHash（733 item 3 余量）。不要另写怎样编证明或怎样种树。

## 官方三件事

规范把 Requirements 里应用可以在 `QueryResponse.Proof` 里回证明、用对应块的 `AppHash` 去验、`ProofOps` 是一串只覆盖一棵指定 `type` 树里一把键的 `ProofOp` 和「已经是回了 Proof 就已经验过对上 AppHash interchangeable / 已经是有 type 就已经是同一棵树 interchangeable / 已经是能证存在就已经能证不存在 interchangeable / 已经是 Query Proofs bundled interchangeable」分开写成三件独立的实现事，不是「看见 Query 回了 Proof 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经能证不存在 interchangeable」一件事：

1. **看见回了 Proof / 看见 QueryResponse.Proof / 看见回了证明 is not already 已经验过对上 AppHash interchangeable / 已经 verified interchangeable / 已经用对应块 AppHash 验过交差 interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 732 queryproof-notverified interchangeable / 325 queryproof item 2 interchangeable，也不是已经 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事 bundled（325 item 2 余量） interchangeable / 325 queryproof item 2 interchangeable，也不是已经头上有 AppHash 不是已经是交易默克尔（731） interchangeable / 733 queryproof-notfinalapphash interchangeable / 147 apphash-this-block interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：应用可以在 `QueryResponse.Proof` 里回这份状态的证明，用对应块的 `AppHash` 去验。看见回了 Proof，不是已经 verified interchangeable——325 钉 bundled 三事，本页从 item 2 侧钉 not already verified 单句。看见 QueryResponse.Proof，不是已经 Query Proofs bundled（325） interchangeable——325 钉 bundled，本页钉 item 2 第一件事。看见回了证明，不是已经头上有 AppHash 不是已经是交易默克尔（731） interchangeable——731 另钉三种锚，本页钉回证明与验。325 queryproof vs apphash bundled unbundling 在本页 item 2 续。

2. **看见有 type / 看见 ProofOp 有 type / 看见指定了树类型 is not already 已经是同一棵树 interchangeable / 已经 same-tree interchangeable / 已经一层树交差 interchangeable / 325 queryproof bundled interchangeable / 314 querystate interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 732 queryproof-notverified interchangeable / 325 queryproof item 1 三种锚 interchangeable / 325 queryproof item 3 一层根 interchangeable，也不是已经 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事 bundled（325 item 2 余量） interchangeable / 325 queryproof item 2 interchangeable，也不是已经验过（本页第一件事） interchangeable。**  
   官方写：每一条 `ProofOp` 只证明**一棵**指定 `type` 的树里的**一把**键；`Proof` 有最小结构 `ProofOps`：一串 `ProofOp`。看见有 type，不是已经 same-tree interchangeable——有 type 不等于已经是同一棵树 / 已经是一层树。看见 ProofOp 有 type，不是已经验过（本页第一件事） interchangeable——三件事分开钉。看见指定了树类型，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉查询状态。325 queryproof vs apphash bundled unbundling 在本页 item 2 续。

3. **看见能证存在 / 看见存在证明绿了 / 看见能证这把键在 is not already 已经能证不存在 interchangeable / 已经 prove-absence interchangeable / 已经缺席证明交差 interchangeable / 325 queryproof bundled interchangeable / 38 apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 732 queryproof-notverified interchangeable / 325 queryproof item 1 / 325 queryproof item 3，也不是已经 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事 bundled（325 item 2 余量） interchangeable / 325 queryproof item 2 interchangeable，也不是已经验过（本页第一件事） interchangeable / 已经是同一棵树（本页第二件事） interchangeable。**  
   官方把能证存在和已经能证不存在分开——存在证明绿了，不等于缺席也能证。看见能证存在，不是已经 prove-absence interchangeable——本页钉 not already prove-absence 单句。看见存在证明绿了，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。看见能证这把键在，不是已经是同一棵树（本页第二件事） interchangeable——三件事分开钉。325 queryproof vs apphash bundled unbundling 在本页 item 2 完成。

怎样编 `ProofOp`、怎样种多层树、怎样从 `FinalizeBlockResponse.Data` 写出下一头是规范里的取值或做法，本页不抄。Query Proofs bundled（325）、头上有 AppHash 不是已经是交易默克尔（325 item 1 余量 / 731）、一层 ProofOp 的根不是已经对上最终 AppHash（325 item 3 余量 / 733）、本头 AppHash 已经是本高度交差（147）、只有 AppHash 可信任（38）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了 Proof not already verified ≠ 325 / 33 interchangeable：** 官方把回证明和用对应块 AppHash 去验分开。
- **有 type not already same-tree ≠ 已经是同一棵树 interchangeable：** 官方把有 type 和一条 ProofOp 只覆盖一棵树一把键分开。
- **能证存在 not already prove-absence ≠ 已经能证不存在 interchangeable：** 官方把存在证明和缺席证明分开；325 queryproof vs apphash bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了 Proof | 不是 already verified | 不是三种锚 alone（731） |
| 有 type | 不是 already same-tree | 不是 QueryState alone（314） |
| 能证存在 | 不是 already prove-absence | 不是 Only AppHash alone（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了 Proof 不是已经对上 AppHash not already verified / not already same-tree / not already prove-absence 正式三事（325 余量），必须分开回了 Proof 是不是 already verified interchangeable / 325 queryproof bundled interchangeable / queryproof-sold-as-apphash interchangeable、有 type 是不是 already same-tree interchangeable、能证存在 是不是 already prove-absence interchangeable。可以跳过「看见 Query 回了 Proof 就已经对上 AppHash interchangeable / 就已经是一层树 interchangeable / 就已经能证不存在 interchangeable」。不要另写怎样编证明。325 queryproof vs apphash bundled unbundling 在本页 item 2 续（731 + 732）；续 [`worked-example-queryproof-notfinalapphash-vs-bundled.md`](worked-example-queryproof-notfinalapphash-vs-bundled.md)（不变量 733 item 3）已写；完成见 733。

## 本页不抄

- 怎样编 `ProofOp`、怎样种多层树、怎样从 FinalizeBlockResponse.Data 写出下一头。
- Query Proofs bundled。那是不变量 325。
- 头上有 AppHash 不是已经是交易默克尔。那是不变量 325 item 1 余量 / 731。
- 一层 ProofOp 的根不是已经对上最终 AppHash。那是不变量 325 item 3 余量 / 733。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- 只有 AppHash 可信任。那是不变量 38。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
