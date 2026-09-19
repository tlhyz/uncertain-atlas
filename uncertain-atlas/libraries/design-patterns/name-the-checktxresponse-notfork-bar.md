# 模式：把各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Specifics of `CheckTxResponse`。  
**例**：[各节点 Data 不一样 not already fork ≠ bundled（317）](../../tracks/implementation/worked-example-checktxresponse-notfork-vs-bundled.md)。

## 三个名字

1. **各节点 Data 不一样 不是 already fork：** 看见节点间 Data 不同 / CheckTx Data 各异，不是已经分叉 interchangeable / 已经共识分叉 interchangeable，不是 317 checktxresponse bundled interchangeable / 33 four gates interchangeable / checktxresponse-sold-as-exec interchangeable。

2. **Data 不确定 不是 already violation：** 看见不必确定 / 不确定字段，不是已经违规 interchangeable / 已经必须确定 interchangeable，不是 317 checktxresponse item 1 interchangeable / 710 checktxresponse-notused interchangeable。

3. **CheckTxState 不同 不是 already ExecuteTxState：** 看见各节点 CheckTxState 不一样 / CheckTx 验时状态不同，不是已经和 ExecuteTxState 同一份 interchangeable / 已经和 Finalize 同一把确定性尺子 interchangeable，不是 317 checktxresponse item 3 interchangeable / 712 checktxresponse-notpriority interchangeable。

官方把各节点 Data 不一样单句、already fork、already violation、already ExecuteTxState 写成三个名字。把它们叫成一个「看见不确定就已经分叉 interchangeable / 就已经违规 interchangeable / 就已经和 Finalize 同一把确定性尺子 interchangeable」，会把 not already fork、not already violation、not already ExecuteTxState 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看各节点 Data 不一样不是已经分叉 not already fork / not already violation / not already ExecuteTxState 正式三事（317 余量），先数清问的是各节点 Data 不一样 是不是 already fork / 317 / checktxresponse-sold-as-exec，是不是 Data 不确定 是不是 already violation，还是 CheckTxState 不同 是不是 already ExecuteTxState，再决定要不要同一次发布。317 checktxresponse vs exec bundled unbundling 在本页 item 2 完成。
