# 反模式：轻验 AppHash 被写成提议者日程已对齐

> 真值：[ASA-2024-009](../../tracks/failure-museum/asa-2024-009.md)、[不变式 56](../invariants/README.md)、[state sync 精读](../../tracks/implementation/worked-example-statesync.md)。亲戚：[statesync-sold-as-genesis](statesync-sold-as-genesis.md)。

## 一句话

看见 state sync 对上了 AppHash，就写成新生验证者已经和全网认同一个「下一轮谁提议」。

## 正确写法

「轻验 AppHash 只锚定应用根。提议者选择状态（咨询点名 `ProposerPriority`）必须另做交叉核对；对不上则同步必须失败。」
