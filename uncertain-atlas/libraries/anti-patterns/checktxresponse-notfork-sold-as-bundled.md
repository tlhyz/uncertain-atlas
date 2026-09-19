# 反模式：把各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量）说成已经分叉 / 已经违规 / 已经是 ExecuteTxState

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[各节点 Data 不一样 not already fork ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notfork-vs-bundled.md)。

## 卖法

把各节点 Data 不一样 / 节点间 Data 不同 / CheckTx Data 各异 写成已经分叉 interchangeable / 已经 fork interchangeable / 已经共识分叉 interchangeable / 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable；把 Data 不确定 / 不必确定 / 不确定字段 写成已经违规 interchangeable / 已经 violation interchangeable / 已经必须确定 interchangeable；把 CheckTxState 不同 / 各节点 CheckTxState 不一样 写成已经和 ExecuteTxState 同一份 interchangeable / 已经 ExecuteTxState interchangeable / 已经和 Finalize 同一把确定性尺子 interchangeable，或已经和 317 checktxresponse bundled / checktxresponse-sold-as-exec interchangeable / 711 checktxresponse-notfork interchangeable。

## 为什么错

官方把各节点 Data 不一样单句、already fork、already violation、already ExecuteTxState 写成三件独立的实现事。把它们卖成 already fork interchangeable / already violation interchangeable / already ExecuteTxState interchangeable，会把 not already fork、not already violation、not already ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量），必须分开 not already fork、not already violation、not already ExecuteTxState 三件事，不要和 317 / 33 / 710 / 712 / 312 / 316 糊成一句。

## 和相邻反模式

- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTxResponse vs exec bundled 全段，不是本页各节点不一样 item 2 单句边界。
- [checktxresponse-notused-sold-as-bundled](checktxresponse-notused-sold-as-bundled.md) 是回了字节被引擎用 item 1，不是本页分叉边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ ExecuteTxState 全段，不是本页 Data 不确定单句边界。
