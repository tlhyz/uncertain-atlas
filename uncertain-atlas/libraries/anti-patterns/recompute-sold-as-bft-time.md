# 反模式：中位数复算被写成故障者不能改时间

> 真值：[CSA-2026-001 Tachyon](../../tracks/failure-museum/csa-2026-001.md)、[不变式 61](../invariants/README.md)、[块时间精读](../../tracks/consensus/worked-example-pbts.md)。

## 一句话

看见实现能从 `LastCommit` 复算出与头相同的中位数，就写成 BFT Time 的拜占庭保证已成立。

## 正确写法

「复算用的时间戳集合必须等于已验收的 commit 签名集合。咨询原文：故障进程不能任意抬高 Time。两条路径不一致，这句话就不成立。」
