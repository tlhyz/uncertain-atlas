# 例：看见 ProofOp.key 是这棵默克尔树里这把键不是已经是 Query 回包键；看见 ProofOp.data 是这把键的编码证明不是已经是 proof_ops；看见 CheckTx 回包 log 是应用日志输出不是已经是 Query 日志

**层次**：实现 / ProofOp 键。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProofOp / CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ProofOp.key 是这棵默克尔树里这把键不是已经是 Query 回包键 / ProofOp.data 是这把键的编码证明不是已经是 proof_ops / CheckTx 回包 log 是应用日志输出不是已经是 Query 日志」，不是 Query 回了 Proof 就已经对上 AppHash，也不是 Query 回包 key 就已经是 Query 高度。不要另写怎样写 ProofOp 键。

## 官方三件事

规范把 ProofOp `key` 是这棵默克尔树里这把键、ProofOp `data` 是这把键的编码证明、CheckTx 回包 `log` 是应用日志输出写成三件独立的实现事，不是「看见填了 ProofOp 键就已经是 Query 回包键、已经是 proof_ops、已经是 Query 日志」一件事：

1. **看见 ProofOp `key` 是这棵默克尔树里这把键 / 看见填了 key 不是已经是 Query 回包键，也不是已经是 ProofOp 类型。**  
   官方写：`key` 是这棵默克尔树里这把证明对应的键。看见填了 key，不是已经是 Query 回包那份键。看见有键，不是已经是 `type` 那种编码种类。看见能填，不是已经交差。
2. **看见 ProofOp `data` 是这把键的编码证明 / 看见填了 data 不是已经是 proof_ops，也不是已经对上最终 AppHash。**  
   官方写：`data` 是这把键的编码默克尔证明。看见填了 data，不是已经是 Query 回包那串 `proof_ops`。看见有编码证明，不是已经一层根对上最终 AppHash。看见能回，不是已经交差。
3. **看见 CheckTx 回包 `log` 是应用日志输出 / 看见回了日志 不是已经是 Query 日志，也不是已经被引擎用了 Data。**  
   官方写：`log` 是应用日志的输出。看见回了日志，不是已经是 Query 回包那份日志。看见有日志，不是已经是 CheckTx 的 Data 被引擎用了。看见能回，不是已经交差。

怎样写 ProofOp 键、怎样填 key、怎样编 data 是规范里的做法，本页不抄。Query 回了 Proof 就已经对上 AppHash 是不变量 325，本页不抄。

## 官方为什么这样拆

- **ProofOp.key 是这棵默克尔树里这把键 ≠ 已经是 Query 回包键：** 官方把一层证明里的键和 Query 回包那份键分开。
- **ProofOp.data 是这把键的编码证明 ≠ 已经是 proof_ops：** 官方把一层编码证明和回包里的证明序列分开。
- **CheckTx 回包 log 是应用日志输出 ≠ 已经是 Query 日志：** 官方把 CheckTx 这份日志和 Query 那份日志分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ProofOp.key 是这棵默克尔树里这把键 | 不是已经是 Query 回包键 | 不是 Query 回包 key 就已经是 Query 高度（380） |
| ProofOp.data 是这把键的编码证明 | 不是已经是 proof_ops | 不是 Query 回了 Proof 就已经对上 AppHash（325） |
| CheckTx 回包 log 是应用日志输出 | 不是已经是 Query 日志 | 不是 Query 回包 log 就已经新鲜（384） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ProofOp 键就已经是 Query 回包键、已经是 proof_ops、已经是 Query 日志」，必须分开 ProofOp.key 是这棵默克尔树里这把键是不是已经是 Query 回包键、ProofOp.data 是这把键的编码证明是不是已经是 proof_ops、CheckTx 回包 log 是应用日志输出是不是已经是 Query 日志。可以跳过「看见填了 ProofOp 键就已经是 Query 回包键」。不要另写怎样写 ProofOp 键。

## 本页不抄

- 怎样写 ProofOp 键、怎样填 key、怎样编 data。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
- Query 回包 key 就已经是 Query 高度。那是不变量 380。
- Query 回包 log 就已经新鲜。那是不变量 384。
