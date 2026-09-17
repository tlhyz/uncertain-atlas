# 例：看见不该验排序相关有效性不是已经该在 CheckTx 里验；看见拜占庭能提案一满块无效交易不是已经被池子挡住；看见 ProcessProposal 对付这种行为不是已经是 CheckTx

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Mempool Connection / CheckTx。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「不该验排序相关有效性不是已经该在 CheckTx 里验 / 拜占庭能提案一满块无效交易不是已经被池子挡住 / ProcessProposal 对付这种行为不是已经是 CheckTx」，不是 CheckTxState 已经是 ExecuteTxState，也不是四门已经结算。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。

## 官方三件事

规范把 CheckTx 的弱过滤器写成三件独立的实现事，不是「看见过了 CheckTx 就已经验完、已经被池子挡住、已经是 ProcessProposal」一件事：

1. **看见 CheckTx 不该验所有有效性 / 看见有效性依赖排序 不是已经该在 CheckTx 里验排序，也不是已经按将要执行的那份验过。**  
   官方写：CheckTx 只是弱过滤器，用来把无效交易挡在内存池外，最终也挡在链外。交易不能保证按以后作为（可能的）决定块去执行时那一份状态来验，因此 CheckTx **不该**把影响有效性的每件事都验完，尤其是那些有效性可能依赖交易排序的检查。看见不该验所有，不是已经该把排序相关的那部分写进 CheckTx。看见排序会改有效性，不是已经按将要执行的那份验过。看见过了 CheckTx，不是已经交差。
2. **看见拜占庭可以不在乎 CheckTx / 看见能提案一满块无效交易 不是已经被池子挡住，也不是已经进不了共识。**  
   官方写：CheckTx 弱，是因为拜占庭节点可以不在乎 CheckTx；它想的话就能提案一满块无效交易。看见池子会挡，不是拜占庭已经被挡住。看见能提案无效交易，不是已经进不了块。看见诚实节点过了 CheckTx，不是对手已经守同一把尺。
3. **看见从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 看见规范点名 ProcessProposal 不是已经是 CheckTx，也不是已经是 Finalize。**  
   官方写：从 ABCI 1.0 起，对付这种行为的机制是 `ProcessProposal`。看见有 ProcessProposal，不是已经是 CheckTx。看见点名了这道门，不是已经 Finalize。看见会拒提案，不是已经在池子里挡完。

怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal` 是规范里的做法，本页不抄。CheckTxState 已经是 ExecuteTxState 是不变量 312，本页不抄。

## 官方为什么这样拆

- **不该验排序相关有效性 ≠ 已经该在 CheckTx 里验：** 官方把「不该验所有、尤其是排序相关」和「按将要执行的那份验过」分开。
- **拜占庭能提案一满块无效交易 ≠ 已经被池子挡住：** 官方把池子弱过滤器和拜占庭可以不守分开。
- **ProcessProposal 对付这种行为 ≠ 已经是 CheckTx：** 官方把这道门写成对付拜占庭不守 CheckTx 的机制，不是 CheckTx 自己，也不是 Finalize。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 不该验排序相关有效性 | 不是已经该在 CheckTx 里验 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 拜占庭能提案一满块无效交易 | 不是已经被池子挡住 | 不是四门已经结算（33） |
| ProcessProposal 对付这种行为 | 不是已经是 CheckTx | 不是索引器已经保证不重放（313） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见过了 CheckTx 就已经验完、已经被池子挡住、已经是 ProcessProposal」，必须分开不该验排序相关有效性是不是已经该在 CheckTx 里验、拜占庭能提案一满块无效交易是不是已经被池子挡住、ProcessProposal 对付这种行为是不是已经是 CheckTx。可以跳过「看见过了 CheckTx 就已经验完」。不要把「不验排序」当不确定已经验完。不要另写怎样写 CheckTx 或怎样写 ProcessProposal。339 checktx-weak vs process bundled unbundling 完成（929 item 1 / 930 item 2 / 931 item 3）；精读 [`worked-example-checktx-weak-notsort-vs-bundled.md`](worked-example-checktx-weak-notsort-vs-bundled.md)（不变量 929 item 1）。

## 本页不抄

- 怎样写 `CheckTx`、怎样挑哪些检查留给 Process、怎样写 `ProcessProposal`。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 四门已经结算。那是不变量 33。
- 索引器已经保证不重放。那是不变量 313。
