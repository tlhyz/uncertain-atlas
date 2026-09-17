# 反模式：实现调整钟被写成共识门槛

> 真值：[CVE-2024-52912](../../tracks/failure-museum/cve-2024-52912.md)、[调整钟精读](../../tracks/network/worked-example-adjusted-time.md)、[不变式 29](../invariants/README.md#29-网络调整钟不得绕过上限)。

## 一句话

节点因对等偏移拒收规范新块，文案写成「链认为这些块非法」或「我们改了 MTP」。

## 正确写法

「本实现的调整时间被带偏，块时间检查用错了尺子；共识规则未改。」
