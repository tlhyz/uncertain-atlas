# 反模式：超时挂钩被写成 ICS-20 已经原子

> 真值：[ASA-2024-007](../../tracks/failure-museum/asa-2024-007.md)、[不变式 78](../invariants/README.md)。亲戚：[ack-json-sold-as-deterministic](ack-json-sold-as-deterministic.md)。

## 一句话

看见 ibc-hooks 包着 transfer，就写成超时只会退一次钱；或把许可上传写成重入已经不可能。

## 正确写法

「超时回调必须在包承诺删除之后才能再进同一条路。OnTimeout 里不得再执行同一 MsgTimeout。挂钩不是 ICS-20 已原子。」
