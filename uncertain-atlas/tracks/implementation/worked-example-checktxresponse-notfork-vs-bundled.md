# 例：看见各节点 Data 不一样 / Data 不确定 / CheckTxState 不同 is not already already fork interchangeable / already violation interchangeable / already ExecuteTxState interchangeable

**层次**：实现 / 各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量）/ not 711 checktxresponse-notfork interchangeable / not 317 checktxresponse bundled interchangeable」，不是 CheckTxResponse vs exec bundled（317），也不是 CheckTx Data 不是已经被引擎用了（710 item 1 余量）或 Priority 不是已经是共识顺序（712 item 3 余量）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

规范把 Requirements 里这份 Data **不必确定**、同一笔交易各节点用 CheckTx 验时 *CheckTxState* 可以不一样、看见各节点 Data 不一样不是已经分叉、看见不确定不是已经违规、看见 CheckTxState 不同不是已经和 ExecuteTxState 同一份 和「已经是各节点不一样就已经分叉 interchangeable / 已经是不确定就已经违规 interchangeable / 已经是 CheckTxState 不同就已经是 ExecuteTxState interchangeable / 已经是 CheckTxResponse vs exec bundled interchangeable」分开写成三件独立的实现事，不是「看见 Data 不确定 就已经分叉 interchangeable / 就已经违规 interchangeable / 就已经和 Finalize 同一把确定性尺子 interchangeable」一件事：

1. **看见各节点 Data 不一样 / 看见节点间 Data 不同 / 看见 CheckTx Data 各异 is not already 已经分叉 interchangeable / 已经 fork interchangeable / 已经共识分叉 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 711 checktxresponse-notfork interchangeable / 317 checktxresponse item 2 interchangeable，也不是已经各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事 bundled（317 item 2 余量） interchangeable / 317 checktxresponse item 2 interchangeable，也不是已经 CheckTx Data 不是已经被引擎用了（710） interchangeable / 712 checktxresponse-notpriority interchangeable / 312 checktxstate interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：这个字段**不必确定**。同一笔交易，各节点的应用收到它、用 CheckTx 验的时候，*CheckTxState* 可以不一样。看见各节点 Data 不一样，不是已经分叉 interchangeable——317 钉 bundled 三事，本页从 item 2 侧钉 not already fork 单句。看见节点间 Data 不同，不是已经 CheckTxResponse vs exec bundled（317） interchangeable——317 钉 bundled，本页钉 item 2 第一件事。看见 CheckTx Data 各异，不是已经 CheckTx Data 不是已经被引擎用了（710） interchangeable——710 另钉 item 1，本页钉 item 2 第一件事。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。

2. **看见 Data 不确定 / 看见不必确定 / 看见不确定字段 is not already 已经违规 interchangeable / 已经 violation interchangeable / 已经必须确定 interchangeable / 317 checktxresponse bundled interchangeable / 316 exectxresult interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 711 checktxresponse-notfork interchangeable / 317 checktxresponse item 1 被引擎用 interchangeable / 317 checktxresponse item 3 Priority interchangeable，也不是已经各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事 bundled（317 item 2 余量） interchangeable / 317 checktxresponse item 2 interchangeable，也不是已经分叉（本页第一件事） interchangeable。**  
   官方把不必确定和已经违规路径分开——不确定，不等于已经违规。看见 Data 不确定，不是已经违规 interchangeable——本页钉 not already violation 单句。看见不必确定，不是已经 Priority 不是已经是共识顺序（712） interchangeable——712 另钉 item 3，本页钉 item 2 第二件事。看见不确定字段，不是已经和 Finalize 的 Data 同一把确定性尺子（316） interchangeable——316 另钉 Finalize 侧，本页钉 item 2 第二件事。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。

3. **看见 CheckTxState 不同 / 看见各节点 CheckTxState 不一样 / 看见 CheckTx 验时状态不同 is not already 已经和 ExecuteTxState 同一份 interchangeable / 已经 ExecuteTxState interchangeable / 已经和 Finalize 同一把确定性尺子 interchangeable / 317 checktxresponse bundled interchangeable / 312 checktxstate interchangeable，也不是已经 CheckTxResponse vs exec bundled（317） interchangeable / 711 checktxresponse-notfork interchangeable / 317 checktxresponse item 1 / 317 checktxresponse item 3，也不是已经各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事 bundled（317 item 2 余量） interchangeable / 317 checktxresponse item 2 interchangeable，也不是已经分叉（本页第一件事） interchangeable / 已经违规（本页第二件事） interchangeable。**  
   官方把 CheckTxState 可以不一样和已经是 ExecuteTxState 路径分开——CheckTxState 不同，不等于已经和 ExecuteTxState 同一份。看见 CheckTxState 不同，不是已经 ExecuteTxState interchangeable——本页钉 not already ExecuteTxState 单句。看见各节点 CheckTxState 不一样，不是已经分叉（本页第一件事） interchangeable——三件事分开钉。看见 CheckTx 验时状态不同，不是已经 CheckTxState vs execute bundled（312） interchangeable——312 另钉。317 checktxresponse vs exec bundled unbundling 在本页 item 2 完成。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。CheckTxResponse vs exec bundled（317）、CheckTx Data 不是已经被引擎用了（317 item 1 余量 / 710）、Priority 不是已经是共识顺序（317 item 3 余量 / 712）、CheckTxState vs execute（312）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **各节点 Data 不一样 not already fork ≠ 317 / 33 interchangeable：** 官方把 CheckTxState 可以不同单句和已经分叉路径分开。
- **Data 不确定 not already violation ≠ 已经违规 interchangeable：** 官方把不必确定单句和已经违规路径分开。
- **CheckTxState 不同 not already ExecuteTxState ≠ 已经和 Finalize 同一把确定性尺子 interchangeable：** 官方把 CheckTxState 可以不一样单句和已经是 ExecuteTxState 路径分开；317 checktxresponse vs exec bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 各节点 Data 不一样 | 不是 already fork | 不是被引擎用 alone（710） |
| Data 不确定 | 不是 already violation | 不是 Priority 共识 alone（712） |
| CheckTxState 不同 | 不是 already ExecuteTxState | 不是 CheckTxState bundled alone（312） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量），必须分开各节点 Data 不一样 是不是 already fork interchangeable / 317 checktxresponse bundled interchangeable / checktxresponse-sold-as-exec interchangeable、Data 不确定 是不是 already violation interchangeable、CheckTxState 不同 是不是 already ExecuteTxState interchangeable。可以跳过「看见不确定就已经分叉 interchangeable / 就已经违规 interchangeable / 就已经和 Finalize 同一把确定性尺子 interchangeable」。不要另写怎样编 Data。317 checktxresponse vs exec bundled unbundling 在本页 item 2 完成；续 [`worked-example-checktxresponse-notpriority-vs-bundled.md`](worked-example-checktxresponse-notpriority-vs-bundled.md)（不变量 712 item 3，待写）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse vs exec bundled。那是不变量 317。
- CheckTx Data 不是已经被引擎用了。那是不变量 317 item 1 余量 / 710。
- Priority 不是已经是共识顺序。那是不变量 317 item 3 余量 / 712。
- CheckTxState vs execute。那是不变量 312。
- 四门已经结算。那是不变量 33。
