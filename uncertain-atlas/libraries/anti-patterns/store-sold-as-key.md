# 反模式：`store` 被写成已经是顶层资源

> 真值：[能力 ≠ 资源](../../tracks/state-models/worked-example-ability-vs-resource.md)、[不变式 151](../invariants/README.md)、[不变式 128](../invariants/README.md)。亲戚：[owned-sold-as-fastpath](owned-sold-as-fastpath.md)。

## 一句话

看见类型写了 `has store` 或结构体声明了 `has copy`，就把 `store` 写成已经是顶层资源，或把声明写成这个实例能复制，或把整数字段写成外层钱能复制。

## 正确写法

「`store` 不是已经是顶层资源。`key` 操作只在定义模块。结构体写了 `has copy` 不是这个实例能复制。字段是整数不是外层资源能复制。」
