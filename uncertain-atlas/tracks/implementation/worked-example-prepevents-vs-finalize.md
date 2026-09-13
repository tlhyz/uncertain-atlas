# 例：看见 Prepare 执行准备提案时 MAY 产出块事件或交易事件不是已经 PrepareProposalResponse 里交回；看见应用 MUST 把这些事件留到块决定之后不是已经 Process 时就交出去；看见经 FinalizeBlockResponse 交给 CometBFT 不是已经 CheckTxResponse.events / ExecTxResult.events

**层次**：实现 / Prepare 事件保留路径正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Prepare 执行准备提案时 MAY 产出块事件或交易事件不是已经 PrepareProposalResponse 里交回 / 应用 MUST 把这些事件留到块决定之后不是已经 Process 时就交出去 / 经 FinalizeBlockResponse 交给 CometBFT 不是已经 CheckTxResponse.events / ExecTxResult.events」，不是 Prepare 回包校验那套已经验过重复，也不是 FinalizeBlockResponse.events 只是索引栏就已经印进本头。不要另写怎样攒 Prepare 事件。

## 官方三件事

规范把 Prepare 执行准备提案时 MAY 产出事件、MUST 留到块决定之后、再经 FinalizeBlockResponse 交回写成三件独立的实现事，不是「看见 Prepare 里产出了事件就已经交给引擎、已经索引、已经印进 LastResultsHash」一件事：

1. **看见 Prepare 执行准备提案时 MAY 产出块事件或交易事件 / 看见先跑了 不是已经在 PrepareProposalResponse 里交回，也不是已经 Prepare 返回时引擎就已经收到。**  
   官方写：As a result of executing the prepared proposal, the Application may produce block events or transaction events。`PrepareProposalResponse` 只有 `txs`。看见 MAY 产出，不是已经在回包里。看见先跑了，不是已经 Prepare 返回时就交给 CometBFT。
2. **看见应用 MUST 把这些事件留到块决定之后 / 看见留着 不是已经 Process 时就交出去，也不是已经 prevote nil / REJECT 时就丢掉可以不算。**  
   官方写：The Application must keep those events until a block is decided。看见必须留着，不是已经 Process 时就索引。看见块还没决定，不是已经因为 Prepare 过了就交差。看见另一块被决定，不是已经 Prepare 时产出的那份就可以不管。
3. **看见然后经 FinalizeBlockResponse 交给 CometBFT / 看见 Finalize 回了 events 不是已经是 CheckTxResponse.events 那种池门回包，也不是已经是 ExecTxResult.events 那种逐笔 tx_results。**  
   官方写：then pass them on to CometBFT via `FinalizeBlockResponse`。看见经 Finalize 交回，不是已经 CheckTx 回包 events interchangeable。看见块级 events，不是已经 ExecTxResult 里逐笔 events。看见给了 CometBFT，不是已经像 Code/Data 那样印进 LastResultsHash。

怎样攒 Prepare 事件、怎样等块决定、怎样在 Finalize 交回是规范里的做法，本页不抄。Prepare 回包校验（357）是引擎没有再验重复 / 回包验不过崩溃 / 事件不是已经交给引擎那套另一切片，FinalizeBlockResponse.events 栏（431）是索引栏不是已经印进本头那套另一切片，本页不抄。

## 官方为什么这样拆

- **Prepare MAY 产出块/tx 事件 ≠ 已经在 PrepareProposalResponse 里交回：** 官方把先产出和回包只有 txs 分开。
- **MUST 留到块决定之后 ≠ 已经 Process 时就交出去：** 官方把保留到决定和 Process 时就索引分开。
- **经 FinalizeBlockResponse 交回 ≠ 已经是 CheckTx / ExecTxResult events：** 官方把 Prepare→Finalize 保留路径和池门 / 逐笔回包 events 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Prepare MAY 产出块/tx 事件 | 不是已经在 PrepareProposalResponse 里交回 | 不是 Prepare 回包校验就已经验过重复（357） |
| MUST 留到块决定之后 | 不是已经 Process 时就交出去 | 不是 Prepare 里产出了事件就已经交给引擎（357 第三件） |
| 经 FinalizeBlockResponse 交回 | 不是已经是 CheckTx / ExecTxResult events | 不是 FinalizeBlockResponse.events 就已经印进本头（431） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里产出了事件就已经交给引擎、已经索引、已经印进 LastResultsHash」，必须分开 Prepare MAY 产出块/tx 事件是不是已经在 PrepareProposalResponse 里交回、MUST 留到块决定之后是不是已经 Process 时就交出去、经 FinalizeBlockResponse 交回是不是已经是 CheckTxResponse.events / ExecTxResult.events。可以跳过「看见 Prepare 里产出了事件就已经交给引擎」。不要另写怎样攒 Prepare 事件。

## 本页不抄

- 怎样攒 Prepare 事件、怎样等块决定、怎样在 Finalize 交回。
- 引擎没有再验重复 / Prepare 回包验不过崩溃。那是不变量 357 的另两件。
- FinalizeBlockResponse.events 是给索引用的类型键值事件。那是不变量 431。
- CheckTx 回包 events / ExecTxResult.events。那是不变量 381 / 446。
- Code / Data 就已经印进本头。那是不变量 316。
