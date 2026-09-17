# 反模式：子群检查被写成点已经在曲线上

> 真值：[CVE-2025-30147](../../tracks/failure-museum/cve-2025-30147.md)、[不变式 116](../invariants/README.md)。亲戚：[circuit-impl-sold-as-statement](circuit-impl-sold-as-statement.md)、[identity-rk-sold-as-handled](identity-rk-sold-as-handled.md)。

## 一句话

看见库做了子群成员检查，或看见原生预编译更快，就写成未信任点已经在曲线上，两家客户端已经同根。

## 正确写法

「未信任点必须先在曲线上、再在子群里。子群检查不是曲线检查。原生加速不是两家已经同根。」
