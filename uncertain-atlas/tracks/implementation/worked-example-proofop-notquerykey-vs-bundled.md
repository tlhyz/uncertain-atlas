# 例：看见 ProofOp.key 是这棵默克尔树里这把键 is not already Query response key interchangeable / not already ProofOp type interchangeable / not already settled interchangeable

**层次**：实现 / ProofOp.key not Query response key / not ProofOp type / not already settled 正式三事（390 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ProofOp.key not Query response key / not ProofOp type / not already settled 正式三事（390 余量）/ not 743 proofop-notquerykey interchangeable / not 390 proofop-vs-key bundled interchangeable」，不是 ProofOp 键 bundled（390），也不是 Query 回包 key 就已经是 Query 高度（380）。不要另写怎样写 ProofOp 键。

## 官方三件事

1. **看见 ProofOp `key` 是这棵默克尔树里这把键 / 看见填了 key / 一层证明里的键 is not already 已经是 Query 回包那份键 interchangeable / 380 querykey interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 743 proofop-notquerykey interchangeable / 744 proofop-notproofops interchangeable / 390 proofop item 2 data interchangeable，也不是已经 key not Query response key / not ProofOp type / not already settled 正式三事 bundled（390 item 1 余量） interchangeable / 390 proofop item 1 interchangeable。**  
   官方写：`key` 是这棵默克尔树里这把证明对应的键。看见填了 key，不是已经是 Query 回包那份键 interchangeable——本页从 390 item 1 侧钉 not Query response key 单句。390 proofop vs key bundled unbundling 在本页 item 1 启动。

2. **看见填了 key / 看见有键 / 一层证明里的键 is not already 已经是 `type` 那种编码种类 interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 743 proofop-notquerykey interchangeable / 390 proofop item 3 CheckTx log interchangeable / 745 proofop-notquerylog interchangeable。**  
   官方把一层证明里的键和编码种类分开——390 bundled 第一件事常与 type 混成「看见填了 key 就已经是 ProofOp 类型 interchangeable」，本页钉 not ProofOp type 单句。

3. **看见填了 key / 看见能填 / 一层证明里的键 is not already 已经交差 interchangeable，也不是已经 ProofOp 键 bundled（390） interchangeable / 743 proofop-notquerykey interchangeable / 744 proofop-notproofops interchangeable。**  
   官方把能填 key 和已经交差分开。看见能填，不是已经交差 interchangeable。390 proofop vs key bundled unbundling 在本页 item 1 启动。

怎样写 ProofOp 键、怎样填 key、怎样编 data 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **key not Query response key ≠ 380 interchangeable：** 官方把一层证明里的键和 Query 回包那份键分开。
- **key not ProofOp type ≠ type interchangeable：** 官方把键和编码种类分开。
- **key not already settled ≠ 已经交差 interchangeable：** 官方把能填 key 和已经交差分开；390 proofop vs key bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProofOp.key 是这棵默克尔树里这把键 | 不是已经是 Query 回包键（380） | 不是 data（744/390 item 2） |
| 看见填了 key | 不是已经是 ProofOp 类型 | 不是 ProofOp 键 bundled（390） |
| 看见能填 | 不是已经交差 | 不是 CheckTx log（745/390 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProofOp.key not Query response key / not ProofOp type / not already settled 正式三事（390 余量），必须分开 key 是不是已经是 Query 回包键 interchangeable / 380、是不是已经是 ProofOp 类型、是不是已经交差。可以跳过「看见填了 key 就已经是 Query 回包键」。不要另写怎样写 ProofOp 键。390 proofop vs key bundled unbundling 在本页 item 1 启动；续 [`worked-example-proofop-notproofops-vs-bundled.md`](worked-example-proofop-notproofops-vs-bundled.md)（不变量 744 item 2）。

## 本页不抄

- 怎样写 ProofOp 键、怎样填 key、怎样编 data。
- ProofOp 键 bundled。那是不变量 390。
- ProofOp.data。那是不变量 390 item 2 余量 / 744。
- CheckTx 回包 log。那是不变量 390 item 3 余量 / 745。
- Query 回包 key 就已经是 Query 高度。那是不变量 380。
