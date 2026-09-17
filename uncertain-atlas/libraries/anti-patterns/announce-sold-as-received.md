# 反模式：对等节点宣布了新块，被写成已经收到

> 真值：[CVE-2024-52922](../../tracks/failure-museum/cve-2024-52922.md)、[官方披露](https://bitcoincore.org/en/2024/11/05/cb-stall-hindering-propagation/)、[不变式 36](../invariants/README.md#36-新块宣布后的索取不得被单一宣布者独占)。

## 一句话

看见 headers / compact block 宣布，就写成「节点已跟上尖」，或把「本节点还没拼出块」写成链非法 / 链停。

## 正确写法

「宣布 ≠ 交付。块索取必须能换对等节点。还没收到是网络/实现，不是共识改写历史。」
