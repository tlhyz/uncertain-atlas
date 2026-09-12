# 反模式：源链托管被写成对岸已经铸出原币

> 真值：[托管 ≠ 对岸铸券](../../tracks/economic/worked-example-escrow-vs-voucher.md)、[不变式 155](../invariants/README.md)、[不变式 146](../invariants/README.md)。亲戚：[client-sold-as-packet](client-sold-as-packet.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见本链托管进账或对岸多了一笔同名余额，就把源链托管写成对岸已经铸出原币，或把对岸券写成源链已经解锁，或把带通道前缀的 denom 写成原来的名字。

## 正确写法

「源链托管不是对岸已经铸券。对岸券不是源链已解锁的原币。带端口/通道前缀的 denom 不是原来的 denom。」
