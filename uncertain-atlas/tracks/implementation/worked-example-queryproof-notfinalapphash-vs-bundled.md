# 例：看见一层对上 / 看见中间根对了 / 看见能证缺席 is not already already next-layer interchangeable / already final-apphash interchangeable / already blockhash-compared interchangeable

**层次**：实现 / 一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量）/ not 733 queryproof-notfinalapphash interchangeable / not 325 queryproof bundled interchangeable」，不是 Query Proofs bundled（325），也不是头上有 AppHash 不是已经是交易默克尔（731 item 1 余量）或 Query 回了 Proof 不是已经对上 AppHash（732 item 2 余量）。不要另写怎样编证明或怎样种树。

## 官方三件事

规范把 Requirements 里验整份证明时这一条 ProofOp 的根是下一条要验的值、最后一条的根才该对上正在验的 `AppHash` 和「已经是一层对上就已经交给下一层 interchangeable / 已经是中间根对了就已经对上最终 AppHash interchangeable / 已经是能证缺席就已经比对着块哈希 interchangeable / 已经是 Query Proofs bundled interchangeable」分开写成三件独立的实现事，不是「看见一层 ProofOp 的根对上了就已经走完多层 interchangeable / 就已经对上最终 AppHash interchangeable / 就已经比对着块哈希 interchangeable」一件事：

1. **看见一层对上 / 看见这一条 ProofOp 的根对了 / 看见一层根绿了 is not already 已经交给下一层 interchangeable / 已经 next-layer interchangeable / 已经是下一条要验的值交差 interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 733 queryproof-notfinalapphash interchangeable / 325 queryproof item 3 interchangeable，也不是已经一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事 bundled（325 item 3 余量） interchangeable / 325 queryproof item 3 interchangeable，也不是已经头上有 AppHash 不是已经是交易默克尔（731） interchangeable / 732 queryproof-notverified interchangeable / 147 apphash-this-block interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：验整份证明时，**这一条 ProofOp 的根，是下一条要验的值**。看见一层对上，不是已经 next-layer interchangeable——325 钉 bundled 三事，本页从 item 3 侧钉 not already next-layer 单句。看见这一条 ProofOp 的根对了，不是已经 Query Proofs bundled（325） interchangeable——325 钉 bundled，本页钉 item 3 第一件事。看见一层根绿了，不是已经 Query 回了 Proof 不是已经对上（732） interchangeable——732 另钉回证明与验，本页钉多层根接值。325 queryproof vs apphash bundled unbundling 在本页 item 3 完成。

2. **看见中间根对了 / 看见对上了 / 看见某层根绿了 is not already 已经对上最终 AppHash interchangeable / 已经 final-apphash interchangeable / 已经最后一条对 AppHash 交差 interchangeable / 325 queryproof bundled interchangeable / 38 apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 733 queryproof-notfinalapphash interchangeable / 325 queryproof item 1 三种锚 interchangeable / 325 queryproof item 2 回证明 interchangeable，也不是已经一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事 bundled（325 item 3 余量） interchangeable / 325 queryproof item 3 interchangeable，也不是已经交给下一层（本页第一件事） interchangeable。**  
   官方写：最后一条的根，才该对上正在验的 `AppHash`。看见中间根对了，不是已经 final-apphash interchangeable——本页钉 not already final-apphash 单句。看见对上了，不是已经交给下一层（本页第一件事） interchangeable——三件事分开钉。看见某层根绿了，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。325 queryproof vs apphash bundled unbundling 在本页 item 3 完成。

3. **看见能证缺席 / 看见缺席证明绿了 / 看见能证这把键不在 is not already 已经比对着块哈希 interchangeable / 已经 blockhash-compared interchangeable / 已经对着块哈希交差 interchangeable / 325 queryproof bundled interchangeable / 147 apphash-this-block interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 733 queryproof-notfinalapphash interchangeable / 325 queryproof item 1 / 325 queryproof item 2，也不是已经一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事 bundled（325 item 3 余量） interchangeable / 325 queryproof item 3 interchangeable，也不是已经交给下一层（本页第一件事） interchangeable / 已经对上最终 AppHash（本页第二件事） interchangeable。**  
   官方把能证缺席和已经比对着块哈希分开——缺席证明绿了，不等于已经对着块哈希。看见能证缺席，不是已经 blockhash-compared interchangeable——本页钉 not already blockhash-compared 单句。看见缺席证明绿了，不是已经本头 AppHash 已经是本高度交差（147） interchangeable——147 另钉本头交差。看见能证这把键不在，不是已经对上最终 AppHash（本页第二件事） interchangeable——三件事分开钉。325 queryproof vs apphash bundled unbundling 在本页 item 3 完成。

怎样编 `ProofOp`、怎样种多层树、怎样从 `FinalizeBlockResponse.Data` 写出下一头是规范里的取值或做法，本页不抄。Query Proofs bundled（325）、头上有 AppHash 不是已经是交易默克尔（325 item 1 余量 / 731）、Query 回了 Proof 不是已经对上 AppHash（325 item 2 余量 / 732）、本头 AppHash 已经是本高度交差（147）、只有 AppHash 可信任（38）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **一层对上 not already next-layer ≠ 325 / 33 interchangeable：** 官方把一层根对上和已经交给下一层分开。
- **中间根对了 not already final-apphash ≠ 已经对上最终 AppHash interchangeable：** 官方把中间根和最后一条对 AppHash 分开。
- **能证缺席 not already blockhash-compared ≠ 已经比对着块哈希 interchangeable：** 官方把缺席证明和对着块哈希分开；325 queryproof vs apphash bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一层对上 | 不是 already next-layer | 不是回证明 alone（732） |
| 中间根对了 | 不是 already final-apphash | 不是 Only AppHash alone（38） |
| 能证缺席 | 不是 already blockhash-compared | 不是本头交差 alone（147） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根不是已经对上最终 AppHash not already next-layer / not already final-apphash / not already blockhash-compared 正式三事（325 余量），必须分开一层对上 是不是 already next-layer interchangeable / 325 queryproof bundled interchangeable / queryproof-sold-as-apphash interchangeable、中间根对了 是不是 already final-apphash interchangeable、能证缺席 是不是 already blockhash-compared interchangeable。可以跳过「看见一层 ProofOp 的根对上了就已经走完多层 interchangeable / 就已经对上最终 AppHash interchangeable / 就已经比对着块哈希 interchangeable」。不要另写怎样编证明。325 queryproof vs apphash bundled unbundling 在本页 item 3 完成（731 + 732 + 733）。

## 本页不抄

- 怎样编 `ProofOp`、怎样种多层树、怎样从 FinalizeBlockResponse.Data 写出下一头。
- Query Proofs bundled。那是不变量 325。
- 头上有 AppHash 不是已经是交易默克尔。那是不变量 325 item 1 余量 / 731。
- Query 回了 Proof 不是已经对上 AppHash。那是不变量 325 item 2 余量 / 732。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- 只有 AppHash 可信任。那是不变量 38。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
