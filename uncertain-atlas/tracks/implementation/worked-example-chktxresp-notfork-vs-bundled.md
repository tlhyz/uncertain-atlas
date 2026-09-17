# 例：看见各节点 Data 不一样 is not already forked interchangeable / not already illegal interchangeable / not already same-state interchangeable

**层次**：实现 / 各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of CheckTxResponse。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量）/ not 1017 chktxresp-notfork interchangeable / not 317 checktxresponse-vs-exec bundled interchangeable」，不是 CheckTxResponse bundled（317），也不是 CheckTxState 已经是 ExecuteTxState（312），也不是 CheckTx 振荡就已经是永远绿（328）。不要另写怎样实现 Priority 或怎样编 Data。

## 官方三件事

1. **看见 Data 不确定 / 看见各节点 Data 不一样 这份回执 is not already 已经分叉 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1017 chktxresp-notfork interchangeable / 1016 chktxresp-notused interchangeable / 317 checktx item 1 Data interchangeable，也不是已经各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事 bundled（317 item 2 余量） interchangeable / 317 checktx item 2 interchangeable。**  
   官方写：这个字段不必确定。同一笔交易，各节点的应用收到它、用 CheckTx 验的时候，CheckTxState 可以不一样。看见各节点 Data 不一样，不是已经分叉 interchangeable——本页从 317 item 2 侧钉 not already forked 单句。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。

2. **看见不确定 / 看见各节点不一样 / 这份回执 is not already 已经违规 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1017 chktxresp-notfork interchangeable / 317 checktx item 3 Priority interchangeable / 1018 chktxresp-notprio interchangeable，也不是已经 CheckTxState 已经是 ExecuteTxState interchangeable / 312 checktxstate interchangeable。**  
   官方把不确定和已经违规分开。看见不确定，不是已经违规 interchangeable。本页钉 not already illegal 单句。

3. **看见 CheckTxState 不同 / 看见各节点不一样 / 这份回执 is not already 已经和 ExecuteTxState 同一份 interchangeable，也不是已经 CheckTxResponse bundled（317） interchangeable / 1017 chktxresp-notfork interchangeable / 1016 chktxresp-notused interchangeable，也不是已经 CheckTx 振荡就已经是永远绿 interchangeable / 328 oscillate interchangeable。**  
   官方把 CheckTxState 不同和已经和 ExecuteTxState 同一份分开。看见 CheckTxState 不同，不是已经和 ExecuteTxState 同一份 interchangeable。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。

怎样实现 Priority、怎样给内存池排序、怎样编 Data 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **各节点 Data 不一样 not already forked ≠ 已经分叉 interchangeable：** 官方把 CheckTxState 可以不同和共识 Agreement 分开。
- **看见不确定 not already illegal ≠ 已经违规 interchangeable：** 官方把不确定和已经违规分开。
- **看见 CheckTxState 不同 not already same-state ≠ 已经和 ExecuteTxState 同一份 interchangeable：** 官方把 CheckTxState 不同和已经和 ExecuteTxState 同一份分开；317 checktxresponse vs exec bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Data 不必确定 | 不是已经分叉 | 不是 CheckTxState 已经是 ExecuteTxState（312） |
| 看见不确定 | 不是已经违规 | 不是 CheckTx 振荡就已经是永远绿（328） |
| 看见 CheckTxState 不同 | 不是已经和 ExecuteTxState 同一份 | 不是 Priority 就已经是共识顺序（1018） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样 not already forked / not already illegal / not already same-state 正式三事（317 余量），必须分开是不是已经分叉、是不是已经违规、是不是已经和 ExecuteTxState 同一份。可以跳过「看见回了就已经被引擎用了」。不要另写怎样实现 Priority 或怎样编 Data。317 checktxresponse vs exec bundled unbundling 在本页 item 2 续；续 [`worked-example-chktxresp-notprio-vs-bundled.md`](worked-example-chktxresp-notprio-vs-bundled.md)（不变量 1018 item 3）。

## 本页不抄

- 怎样实现 Priority、怎样给内存池排序、怎样编 Data。
- CheckTxResponse bundled。那是不变量 317。
- CheckTxState 已经是 ExecuteTxState。那是不变量 312。
- CheckTx 振荡就已经是永远绿。那是不变量 328。
