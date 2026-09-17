# 反模式：应用快照同步被写成从创世重放，或 snapshot.hash 被写成 AppHash

> 真值：[state sync 精读](../../tracks/implementation/worked-example-statesync.md)、[ABCI++ OfferSnapshot](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md)、[不变式 38](../invariants/README.md#38-应用快照必须点名跳过了历史重放且锚是轻验-apphash)。亲戚：[apphash-sold-as-proposer](apphash-sold-as-proposer.md)（轻验 AppHash ≠ 提议者日程）。

## 一句话

看见节点「几分钟跟上」，就写成「已从创世执行每一块」，或把对等节点快照元数据的 `hash` 当成轻客户端验过的链上 `AppHash`。

## 正确写法

| 路径 | 能说的句子 |
|------|------------|
| state sync 完成 | 「应用状态装到高度 H；AppHash 对上轻验过头；历史块未重放」 |
| assumeutxo 背景未完 | 「尖可用；UTXO 历史仍在背景验」 |
| 从创世 | 「每一高度 Finalize / 脚本已在本节点执行或验证」 |

## 对不确定的意义（建议）

缺「跳过了什么 / 锚是哪个哈希 / 信任期」的「快速同步」，这条就红。
