# 反模式：停链被写成一种事故

> 真值：[停链面地图](../../tracks/failure-museum/worked-example-halt-surfaces.md)、[不变式 84](../invariants/README.md)。亲戚：[halt-msg-sold-as-halt](halt-msg-sold-as-halt.md)、[endblocker-error-sold-as-skippable](endblocker-error-sold-as-skippable.md)。

## 一句话

看见高度不涨，就写成「停链」一个词交差；或把说明书停、EndBlocker 错、非确定、版本差、本节点崩溃糊成同一谓词。

## 正确写法

「停必须点名路径。交易内 panic 可被恢复。EndBlocker 出错会停。非确定会停。版本不一致会停。锁钱不是停。+⅓ 打补丁变成可见停，不是已经安全。」
