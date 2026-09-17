# 例：看见同一高度回了不同码不是已经有了 CheckTxCode；看见还在振荡不是已经过了 h_stable；看见本地不再振荡不是已经各节点同一份 b

**层次**：实现 / CheckTx 最终不再振荡。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「同一高度回了不同码不是已经有了 CheckTxCode / 还在振荡不是已经过了 h_stable / 本地不再振荡不是已经各节点同一份 b」，不是 CheckTxState 已经是 ExecuteTxState，也不是提案收了已经从池里删掉。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 官方三件事

规范把同一高度上的 CheckTx 码和最终不再振荡写成三件独立的实现事，不是「看见过了就已经稳定、已经离池、已经全网同一份」一件事：

1. **看见同一高度 CheckTx 回了不同码 / 看见 CheckTxCodes 是集合 不是已经有了 CheckTxCode，也不是已经能说 OK。**  
   官方写：高度 *h* 上对同一笔 *tx* 的 `CheckTxResponse` 码收成集合 *CheckTxCodes*。集合可以有多个码。只有它是单元素时，才定义 *CheckTxCode*。不是单元素，*CheckTxCode* **没有定义**。`OK(CheckTxCode)` 也就没有定义。看见回了两次，不是已经有这个码。看见集合在，不是已经能说成功。
2. **看见还在振荡 / 看见还在池里 不是已经过了 h_stable，也不是已经离池。**  
   官方写：对任意 *tx*，存在布尔 *b* 和高度 *h_stable*，使得任意正确进程在 *h ≥ h_stable* 上都有定义好的 *CheckTxCode*，且 `OK = b`。Requirement 13 保证：这笔若在本节点池里待得够久，会**最终**不再在成功和失败之间来回。于是各全节点的池最终会把它清掉：要么到处因 CheckTx 失败被扔掉，要么一直合法、够流言、够被提案、够被决定。看见还在振荡，不是已经过了 *h_stable*。看见还在池里，不是已经离池。看见最终不再振荡，不是已经进了块。
3. **看见本地 h_p,stable / 看见本节点不再振荡 不是已经是全局同一高度，也不是已经各节点同一份 b。**  
   官方写：Requirement 13 写的是全局 *h_stable*，实现者也可以把它看成只属于进程 *p* 的 *h_p,stable*，一般性不丢。**相反**，*b* **必须**各正确进程相同。看见本节点稳住了，不是已经全网同一高度。看见本地不再振荡，不是已经同一份 *b*。

怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔是规范里的取值或做法，本页不抄。CheckTxState 不是 ExecuteTxState 是不变量 312，本页不抄。

## 官方为什么这样拆

- **同一高度回了不同码 ≠ 已经有了 CheckTxCode：** 官方把集合和单元素才定义的那个码分开。
- **还在振荡 ≠ 已经过了 h_stable：** 官方把「最终不再振荡」写成存在以后的高度，不是看见此刻来回就已经齐。
- **本地不再振荡 ≠ 已经各节点同一份 b：** 官方把可以本地的稳定高度和必须全网同一份 *b* 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一高度回了不同码 | 不是已经有了 CheckTxCode | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 还在振荡 | 不是已经过了 h_stable | 不是提案收了已经从池里删掉（301） |
| 本地不再振荡 | 不是已经各节点同一份 b | 不是索引器已经保证不重放（313）；不是四门已经结算（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「CheckTx 过了就已经稳定、已经离池、已经全网同一份」，必须分开同一高度回了不同码是不是已经有了 CheckTxCode、还在振荡是不是已经过了 h_stable、本地不再振荡是不是已经各节点同一份 b。可以跳过「看见过了就已经稳定」。不要另写怎样实现 CheckTx 或怎样挑稳定高度。

## 本页不抄

- 怎样实现 CheckTx、怎样挑稳定高度、怎样写布尔。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- 提案收了已经从池里删掉。那是不变量 301。
- 索引器已经保证不重放。那是不变量 313。
- 四门已经结算。那是不变量 33。
