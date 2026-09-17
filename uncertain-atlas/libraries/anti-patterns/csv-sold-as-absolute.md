# 反模式：脚本里的 CSV 被写成已经是绝对锁或已经是部署名

> 真值：[CSV ≠ 绝对锁](../../tracks/state-models/worked-example-csv-vs-cltv.md)、[不变式 165](../invariants/README.md)、[不变式 164](../invariants/README.md)、[不变式 41](../invariants/README.md)。亲戚：[cltv-sold-as-nlocktime](cltv-sold-as-nlocktime.md)。

## 一句话

看见文案写「CSV 之后」或输入填了 nSequence，就把相对锁写成已经是 CLTV，或把部署名写成已经在讲操作码，或把有序号写成输出已经相对锁住。

## 正确写法

「脚本里的 CSV 不是 nSequence 已经把输出相对锁住。相对锁不是绝对锁。CSV 软分叉部署不是已经在讲 CHECKSEQUENCEVERIFY 操作码。nSequence 有数不是已经是相对锁。」
