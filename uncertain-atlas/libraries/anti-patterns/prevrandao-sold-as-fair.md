# 反模式：PREVRANDAO 被写成无偏应用随机

> 真值：[DIFFICULTY ≠ 工作量](../../tracks/crypto/worked-example-prevrandao-vs-difficulty.md)、[不变式 157](../invariants/README.md)、[不变式 3](../invariants/README.md)。亲戚：[parent-root-sold-as-head](parent-root-sold-as-head.md)、[processed-sold-as-head](processed-sold-as-head.md)。

## 一句话

看见合约还在调 `DIFFICULTY` 或头上有 `prevRandao`，就把合并后的难度字段写成工作量，或把 `PREVRANDAO` 写成本块刚掷的公平骰子，或把信标 RANDAO 写成应用级无偏随机。

## 正确写法

「合并后的 `difficulty` 不是工作量。`PREVRANDAO` 不是本块刚掷的骰子。信标 RANDAO 不是应用级无偏随机。」
