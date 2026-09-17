# 反模式：访问列表被写成已经访问过

> 真值：[列入 ≠ 已访问](../../tracks/implementation/worked-example-listed-vs-accessed.md)、[不变式 168](../invariants/README.md)、[不变式 167](../invariants/README.md)、[不变式 158](../invariants/README.md)。亲戚：[type-sold-as-payload](type-sold-as-payload.md)、[basefee-sold-as-tip](basefee-sold-as-tip.md)、[predicate-sold-as-script](predicate-sold-as-script.md)。

## 一句话

看见交易带了访问列表或预付了列表费，就把列入写成已经访问过，或把列表外写成已经不能碰，或把 2930 写成 2718 / 1559。

## 正确写法

「列出地址或槽不是已经访问过。列表外不是已经不能碰。预付列表费不是已经跑完读取。EIP-2930 不是 EIP-2718 信封本身，也不是 EIP-1559。」
