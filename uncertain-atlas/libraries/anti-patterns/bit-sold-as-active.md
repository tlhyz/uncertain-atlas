# 反模式：版本位被置上被写成已经锁定或已经激活

> 真值：[置位 ≠ 已激活](../../tracks/implementation/worked-example-versionbit-vs-active.md)、[不变式 171](../invariants/README.md)、[不变式 165](../invariants/README.md)、[不变式 41](../invariants/README.md)。亲戚：[csv-sold-as-absolute](csv-sold-as-absolute.md)、[hash-sold-as-redeem](hash-sold-as-redeem.md)。

## 一句话

看见矿工把头上某一位置上或文案写 LOCKED_IN，就把软分叉写成已经锁定或已经强制新规则，或把 9 写成 34 整数版本 / 被部署的那条规则。

## 正确写法

「版本位被置上不是已经锁定。锁定不是已经激活。超时未锁定不是已经可以当激活。BIP-9 不是 BIP-34 比整数版本，也不是被部署的那条新规则。」
