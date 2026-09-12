# 反模式：可选模块的 EndBlocker 出错被写成局部失败

> 真值：[ISA-2025-002](../../tracks/failure-museum/isa-2025-002.md)、[不变式 71](../invariants/README.md)、[ABCI 精读](../../tracks/consensus/worked-example-prepare-process.md)。亲戚：[enable-height-sold-as-safe](enable-height-sold-as-safe.md)。

## 一句话

看见 `x/group` 或同类可选模块，就写成它的 EndBlocker 出错只红提案、不影响出块；或把能与该模块交互的用户写成「只是治理用户」。

## 正确写法

「挂在 EndBlocker 上的可选模块，出错按停链审。能与该模块交互的用户集合就是能引入停链状态的集合。」
