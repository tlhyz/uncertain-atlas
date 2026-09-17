# 反模式：带回剩余气的回滚被写成已经把气烧光

> 真值：[回滚 ≠ 烧光](../../tracks/implementation/worked-example-revert-vs-invalid.md)、[不变式 177](../invariants/README.md)、[不变式 103](../invariants/README.md)、[不变式 176](../invariants/README.md)。亲戚：[oog-sold-as-reverted](oog-sold-as-reverted.md)、[initcode-sold-as-runtime](initcode-sold-as-runtime.md)、[transient-sold-as-storage](transient-sold-as-storage.md)。

## 一句话

看见「执行失败」，就把带回剩余气的回滚写成已经像非法指令那样把气烧光，或把不够付这道回滚自己的费写成已经留下剩余气，或把 140 写成空账户 OOG。

## 正确写法

「带回剩余气的回滚不是已经像非法指令那样把剩余气烧光。不够付这道回滚自己的费不是已经按回滚语义留下剩余气。创建里回滚不是已经部署。EIP-140 不是空账户 OOG 回滚，也不是另一条链的 REVERTED 档。」
