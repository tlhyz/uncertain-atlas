# 反模式：initcode 的界被写成已经是部署代码的界

> 真值：[initcode ≠ 运行时代码](../../tracks/implementation/worked-example-initcode-vs-runtime.md)、[不变式 176](../invariants/README.md)、[不变式 175](../invariants/README.md)、[不变式 169](../invariants/README.md)。亲戚：[max-sold-as-next-nonce](max-sold-as-next-nonce.md)、[first-access-sold-as-warm](first-access-sold-as-warm.md)、[selfdestruct-sold-as-deleted](selfdestruct-sold-as-deleted.md)。

## 一句话

看见「合约有大小限制」，就把 initcode 写成已经受 170 那道界管，或把按字分析费写成已经创建，或把 3860 写成 1014 的哈希费。

## 正确写法

「initcode 超界不是已经是部署代码超界。创建交易超界不是已经是 CREATE 指令失败。按字收跳转分析费不是已经跑完 initcode。EIP-3860 不是 EIP-170，也不是 EIP-1014，也不是 EIP-2681。」
