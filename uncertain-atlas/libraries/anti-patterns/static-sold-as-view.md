# 反模式：静态帧被写成已经是高级语言的只读函数

> 真值：[静态 ≠ view](../../tracks/implementation/worked-example-static-vs-view.md)、[不变式 178](../invariants/README.md)、[不变式 177](../invariants/README.md)、[不变式 159](../invariants/README.md)。亲戚：[revert-sold-as-invalid](revert-sold-as-invalid.md)、[transient-sold-as-storage](transient-sold-as-storage.md)、[selfdestruct-sold-as-deleted](selfdestruct-sold-as-deleted.md)。

## 一句话

看见「只读」或 `view`，就把虚拟机静态帧写成已经是高级语言只读，或把没转账写成已经静态，或把 214 写成 140。

## 正确写法

「静态帧不是已经是高级语言的只读函数。没转账的普通调用不是已经是静态帧。静态帧里改状态不是已经改成。CALLCODE 带非零值不是已经算改状态。EIP-214 不是 EIP-140，也不是瞬时店禁写单独成页。」
