# 例：看见 ProofOp.data 是这把键的编码证明 is not already proof_ops interchangeable / not already AppHash matched interchangeable / not already settled interchangeable

**层次**：实现 / ProofOp.data not proof_ops / not already AppHash matched / not already settled 正式三事（390 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProofOp.data not proof_ops / not already AppHash matched / not already settled 正式三事（390 余量）/ not 744 proofop-notproofops interchangeable / not 390 proofop-vs-key bundled interchangeable」，不是 ProofOp 键 bundled（390），也不是 Query 回了 Proof 就已经对上 AppHash（325）。不要另写怎样写 ProofOp 键。

## 官方三件事

1. **看见 ProofOp `data` 是这把键的编码证明 / 看见填了 data / 一层编码证明 is not already 已经是 Query 回包那串 `proof_ops` interchangeable / 325 queryproof interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 744 proofop-notproofops interchangeable / 743 proofop-notquerykey interchangeable / 390 proofop item 1 key interchangeable，也不是已经 data not proof_ops / not already AppHash matched / not already settled 正式三事 bundled（390 item 2 余量） interchangeable / 390 proofop item 2 interchangeable。**  
   官方写：`data` 是这把键的编码默克尔证明。看见填了 data，不是已经是 Query 回包那串 `proof_ops` interchangeable——本页从 390 item 2 侧钉 not proof_ops 单句。390 proofop vs key bundled unbundling 在本页 item 2 续。

2. **看见填了 data / 看见有编码证明 / 一层编码证明 is not already 已经一层根对上最终 AppHash interchangeable / 325 queryproof interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 744 proofop-notproofops interchangeable / 390 proofop item 3 CheckTx log interchangeable / 745 proofop-notquerylog interchangeable。**  
   官方把一层编码证明和已经对上最终 AppHash 分开——390 bundled 第二件事常与 325 混成「看见填了 data 就已经对上 AppHash interchangeable」，本页钉 not already AppHash matched 单句。

3. **看见填了 data / 看见能回 / 一层编码证明 is not already 已经交差 interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 744 proofop-notproofops interchangeable / 743 proofop-notquerykey interchangeable。**  
   官方把能回 data 和已经交差分开。看见能回，不是已经交差 interchangeable。390 proofop vs key bundled unbundling 在本页 item 2 续。

怎样写 ProofOp 键、怎样填 key、怎样编 data 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **data not proof_ops ≠ 325 interchangeable：** 官方把一层编码证明和回包里的证明序列分开。
- **data not already AppHash matched ≠ 325 interchangeable：** 官方把有编码证明和已经对上最终 AppHash 分开。
- **data not already settled ≠ 已经交差 interchangeable：** 官方把能回 data 和已经交差分开；390 proofop vs key bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProofOp.data 是这把键的编码证明 | 不是已经是 proof_ops（325） | 不是 key（743/390 item 1） |
| 看见填了 data | 不是已经对上 AppHash（325） | 不是 ProofOp 键 bundled（390） |
| 看见能回 | 不是已经交差 | 不是 CheckTx log（745/390 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProofOp.data not proof_ops / not already AppHash matched / not already settled 正式三事（390 余量），必须分开 data 是不是已经是 proof_ops interchangeable / 325、是不是已经对上 AppHash interchangeable / 325、是不是已经交差。可以跳过「看见填了 data 就已经是 proof_ops」。不要另写怎样写 ProofOp 键。390 proofop vs key bundled unbundling 在本页 item 2 续；完成 [`worked-example-proofop-notquerylog-vs-bundled.md`](worked-example-proofop-notquerylog-vs-bundled.md)（不变量 745 item 3）。

## 本页不抄

- 怎样写 ProofOp 键、怎样填 key、怎样编 data。
- ProofOp 键 bundled。那是不变量 390。
- ProofOp.key。那是不变量 390 item 1 余量 / 743。
- CheckTx 回包 log。那是不变量 390 item 3 余量 / 745。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
