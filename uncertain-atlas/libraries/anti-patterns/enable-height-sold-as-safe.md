# 反模式：治理改扩展启用高度被写成节点已经能吃

> 真值：[ASA-2024-001](../../tracks/failure-museum/asa-2024-001.md)、[不变式 58](../invariants/README.md)、[扩展精读](../../tracks/consensus/worked-example-vote-extension.md)。

## 一句话

看见治理提案改了 `VoteExtensionsEnableHeight` 且已通过，就写成所有节点会按新高度启用扩展；或把验证失败写成「治理否决」，其实进程已经 panic。

## 正确写法

「可治理的启用高度必须先有合法转移谓词。过不了必须拒参数，不得崩进程。治理通过 ≠ 实现已经能吃这个值。」
