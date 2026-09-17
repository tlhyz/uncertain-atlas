# 反模式：类型信封被写成已经解开内层

> 真值：[信封 ≠ 内层](../../tracks/implementation/worked-example-typed-vs-legacy.md)、[不变式 167](../invariants/README.md)、[不变式 161](../invariants/README.md)、[不变式 158](../invariants/README.md)。亲戚：[chainid-sold-as-signed](chainid-sold-as-signed.md)、[basefee-sold-as-tip](basefee-sold-as-tip.md)。

## 一句话

看见交易带了类型号或旧式字段列表，就把类型字节写成已经解开内层，或把旧式列表写成已经是信封，或把 2718 写成 1559。

## 正确写法

「类型字节不是已经解开内层字段。旧式 RLP 列表不是已经是类型信封。EIP-2718 不是 EIP-1559，也不是 EIP-155。看见收据不是收据类型已经对上。」
