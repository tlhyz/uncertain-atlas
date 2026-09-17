# 反模式：谓词通过被写成脚本已经跑完

> 真值：[谓词 ≠ 脚本工作实例](../../tracks/parallelism/worked-example-utxo-access-list.md)、[不变式 143](../invariants/README.md)、[不变式 122](../invariants/README.md)。亲戚：[stm-done-sold-as-final](stm-done-sold-as-final.md)、[owned-sold-as-fastpath](owned-sold-as-fastpath.md)、[order-sold-as-state](order-sold-as-state.md)、[batch-sold-as-ordered](batch-sold-as-ordered.md)。

## 一句话

看见「UTXO 并行」或看见「也是声明依赖」，就把谓词通过写成脚本已经跑完，或把只读重叠写成必须串行，或把并行验证写成已经不需要顺序 L。

## 正确写法

「谓词通过不是脚本已经跑完。只读访问集重叠不是写冲突。写集相交必须拓扑序。并行验证不是已经不需要顺序副作用。有持久存储的是作为输入的合约，不是脚本。」
