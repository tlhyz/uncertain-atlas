# 例：看见头上有 AppHash 不是已经是交易默克尔；看见 Query 回了 Proof 不是已经对上 AppHash；看见一层 ProofOp 的根不是已经对上最终 AppHash

**层次**：实现 / Query Proofs。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「头上有 AppHash 不是已经是交易默克尔 / Query 回了 Proof 不是已经对上 AppHash / 一层 ProofOp 的根不是已经对上最终 AppHash」，不是本头 AppHash 已经是本高度交差，也不是 QueryState 已经是 ExecuteTxState。不要另写怎样编证明或怎样种树。 325 queryproof vs apphash bundled unbundling 启动（731）；精读 [`worked-example-queryproof-nottxmerkle-vs-bundled.md`](worked-example-queryproof-nottxmerkle-vs-bundled.md)（不变量 731 item 1）。

## 官方三件事

规范把查询证明写成三件独立的实现事，不是「看见头上有 AppHash 就已经能验应用、已经对上、已经走完多层」一件事：

1. **看见头上有 AppHash / 看见和 ValidatorsHash、DataHash 并列 不是已经是交易默克尔，也不是已经是验证者集合。**  
   官方写：头上有好几份哈希，各自锚一类证明。`ValidatorsHash` 用来快验验证者集合。`DataHash` 用来快验块里的交易。`AppHash` **是应用自己的**：给应用状态做应用自己的默克尔证明。有的应用把相关状态就放在交易里（官方举 Bitcoin UTXO）；有的应用另有一份从交易**确定算出来、但不在交易里**的状态（官方举 Ethereum 合约和账户）。后一种才靠 `AppHash` 给轻客户端更省地验。看见头上有 AppHash，不是已经是 DataHash。看见和另外两份并列，不是已经同一种锚。看见交易在，不是已经有这份分开的应用状态。
2. **看见 Query 回了 Proof / 看见 QueryResponse.Proof 不是已经对上 AppHash，也不是已经是一层树。**  
   官方写：应用可以在 `QueryResponse.Proof` 里回这份状态的证明，用对应块的 `AppHash` 去验。`Proof` 有最小结构 `ProofOps`：一串 `ProofOp`。每一条 `ProofOp` 只证明**一棵**指定 `type` 的树里的**一把**键。看见回了 Proof，不是已经验过。看见有 type，不是已经是同一棵树。看见能证存在，不是已经能证不存在。
3. **看见一层 ProofOp 的根 / 看见对上了 不是已经是下一层要验的值，也不是已经对上最终 AppHash。**  
   官方写：验整份证明时，**这一条 ProofOp 的根，是下一条要验的值**。最后一条的根，才该对上正在验的 `AppHash`。看见一层对上，不是已经交给下一层。看见中间根对了，不是已经对上 AppHash。看见能证缺席，不是已经比对着块哈希。

怎样编 `ProofOp`、怎样种多层树、怎样从 `FinalizeBlockResponse.Data` 写出下一头是规范里的取值或做法，本页不抄。本头 AppHash 已经是本高度交差是不变量 147，本页不抄。

## 官方为什么这样拆

- **头上有 AppHash ≠ 已经是交易默克尔：** 官方把 ValidatorsHash、DataHash、应用自己的 AppHash 分成三种锚。
- **Query 回了 Proof ≠ 已经对上 AppHash：** 官方把回证明和用对应块的 AppHash 去验分开；一条 ProofOp 只覆盖一棵树的一把键。
- **一层 ProofOp 的根 ≠ 已经对上最终 AppHash：** 官方把多层根接值和最后一条对 AppHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 头上有 AppHash | 不是已经是交易默克尔 | 不是本头 AppHash 已经是本高度交差（147） |
| Query 回了 Proof | 不是已经对上 AppHash | 不是 QueryState 已经是 ExecuteTxState（314） |
| 一层 ProofOp 的根 | 不是已经对上最终 AppHash | 不是只有 AppHash 可信任（38） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「查询已经带证明」，必须分开头上有 AppHash 是不是已经是交易默克尔、Query 回了 Proof 是不是已经对上 AppHash、一层 ProofOp 的根是不是已经对上最终 AppHash。可以跳过「看见头上有 AppHash 就已经能验应用」。不要另写怎样编证明或怎样种树。 325 queryproof vs apphash bundled unbundling 启动（731 item 1）。

## 本页不抄

- 怎样编 `ProofOp`、怎样种多层树、怎样从 Finalize 写出下一头。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
- 只有 AppHash 可信任。那是不变量 38。
