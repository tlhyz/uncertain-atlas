# 反模式：电路实现被写成已经写明的陈述

> 真值：[Zcash ZIP 257](../../tracks/failure-museum/zcash-2026-orchard-circuit-not-statement.md)、[不变式 102](../invariants/README.md)。亲戚：[proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)、[fiat-shamir-sold-as-bound](fiat-shamir-sold-as-bound.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见规范段落里的 Action 陈述，或看见旧验证钥还能验历史块，就写成电路已经忠实、新电路已经安全。

## 正确写法

「陈述、电路、验证钥是三件东西。缺拷贝约束的实现不是陈述已约束。旧钥过验不是新钥已齐。」
