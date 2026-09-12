# 反模式：本笔第一次碰被写成已经热

> 真值：[第一次 ≠ 已热](../../tracks/implementation/worked-example-cold-vs-warm.md)、[不变式 169](../invariants/README.md)、[不变式 168](../invariants/README.md)、[不变式 101](../invariants/README.md)。亲戚：[listed-sold-as-accessed](listed-sold-as-accessed.md)、[gas-sold-as-wallclock](gas-sold-as-wallclock.md)。

## 一句话

看见发送者已在集合或本笔读过一次，就把第一次碰写成已经热，或把下一笔写成还热，或把 2929 写成 2930 / 墙钟。

## 正确写法

「本笔第一次碰不是已经热。本笔再碰不是又是一次冷访问。发送者开跑已在集合不是任意地址已经热。EIP-2929 不是 EIP-2930 名单，也不是 gas 已经等于墙钟。」
