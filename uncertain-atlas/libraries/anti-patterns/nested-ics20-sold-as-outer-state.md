# 反模式：内层预编译改过账被写成外层已经看见

> 真值：[ASA-2026-002](../../tracks/failure-museum/asa-2026-002.md)、[不变式 118](../invariants/README.md)。亲戚：[precompile-oog-sold-as-reverted](precompile-oog-sold-as-reverted.md)、[cancel-sold-as-no-debit](cancel-sold-as-no-debit.md)。

## 一句话

看见 ICS20 预编译在内层跑完，或看见已经关掉该预编译，就写成外层余额已经更新，同一笔不能再花。

## 正确写法

「嵌套执行的内层更新必须对外层同一对象可见。关掉预编译不是嵌套写回已经齐。」
