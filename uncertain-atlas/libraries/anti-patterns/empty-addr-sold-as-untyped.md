# 反模式：空地址被写成还没有账户类型

> 真值：[Barberry](../../tracks/failure-museum/barberry.md)、[不变式 83](../invariants/README.md)。亲戚：[blocked-sold-as-initialized](blocked-sold-as-initialized.md)、[authz-sold-as-validated](authz-sold-as-validated.md)。

## 一句话

看见地址还空着，就写成别人不能先指定账户类型；或把入金写成一定还能取出。

## 正确写法

「账户类型必须由权利人或创世初始化。外人把空地址写成只进不出，入金就取不出来。空地址不是还没有类型。」
