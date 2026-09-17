# 反模式：一家收下无效 ephemeralKey 被写成规范已经允许

> 真值：[Zcash ZIP 256](../../tracks/failure-museum/zcash-2026-ephemeralkey-split.md)、[不变式 108](../invariants/README.md)。亲戚：[normalize-sold-as-encoded](normalize-sold-as-encoded.md)、[identity-rk-sold-as-handled](identity-rk-sold-as-handled.md)、[noncanonical-accepted](noncanonical-accepted.md)。

## 一句话

看见一家节点收下某 32 字节，或看见它和 `rk` 画在同一条曲线上，就写成规范已经允许、两个字段已经共用一条解码谓词。

## 正确写法

「规范要求合法非零点的字段，无效编码必须两家同拒。先拒零点不是全部无效字节已挡。`ephemeralKey` 不是 `rk`。」
