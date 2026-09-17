# 反模式：变异块被写成已经处理完这块，或一个对等节点能清掉别人的下载

> 真值：[CVE-2024-52921](../../tracks/failure-museum/cve-2024-52921.md)、[compact 精读](../../tracks/network/worked-example-compact-block.md)、[不变式 39](../invariants/README.md#39-对等节点的块下载状态必须隔离)。

## 一句话

未请求的变异块（根或 witness 承诺对不上交易）被当成「这块处理完了」，从而忘掉正在向其他对等节点做的 compact 重建。

## 正确写法

「下载状态按 (对等节点, 对象) 隔离。变异是传播垃圾，不是共识已经拒绝了合法块。」
