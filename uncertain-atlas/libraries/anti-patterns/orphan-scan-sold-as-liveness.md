# 反模式：不可中断的孤儿扫描被写成节点仍活着

> 真值：[孤儿精读](../../tracks/mempool/worked-example-orphan-resolution.md)、[CVE-2024-52914](../../tracks/failure-museum/cve-2024-52914.md)、[不变式 32](../invariants/README.md#32-孤儿解析必须可中断且验代价有配额)。

## 一句话

节点因解析未确认依赖而数小时不读网，文案仍写「全节点在线 / 已同步」。

## 正确写法

「孤儿解析必须让出事件循环。卡住是实现活性事故，不是共识重组。」
