# 反模式：插入路径的检查加法被写成心跳加余量已经安全

> 真值：[CVE-2026-34219](../../tracks/failure-museum/cve-2026-34219.md)、[不变式 121](../invariants/README.md)。亲戚：[assert-sold-as-peer-filter](assert-sold-as-peer-filter.md)、[early-return-sold-as-joined](early-return-sold-as-joined.md)。

## 一句话

看见把对等消息转成时间点时用了检查加法，或看见解析当时没崩，就写成以后心跳再加余量也不会溢出恐慌。

## 正确写法

「同一条时间线的每一处 `Instant + Duration` 必须检查。插入过了不是过期路径已经齐。」
