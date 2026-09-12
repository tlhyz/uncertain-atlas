# 反模式：justified 或 head 被写成已经 finalized

> 真值：[head ≠ justified ≠ finalized 工作实例](../../tracks/finality/worked-example-head-vs-justified-vs-finalized.md)、[不变式 127](../invariants/README.md)。亲戚：[babe-sold-as-grandpa](babe-sold-as-grandpa.md)、[two-finality-sold-as-one](two-finality-sold-as-one.md)、[header-equals-settlement](header-equals-settlement.md)、[stale-checkpoint-sold-as-genesis](stale-checkpoint-sold-as-genesis.md)、[sample-sold-as-full-set](sample-sold-as-full-set.md)。

## 一句话

看见出块、钱包绿勾、RPC `latest` / `safe`、或「已经 justified」，就写成不可逆，或把 `safe` 写成官方的 justified / finalized。

## 正确写法

「LMD-GHOST 的头可以摆。justified 是检查点第一步，官方写在某些条件下仍可回滚。finalized 是再过一档检查点之后的第二步。`latest` / `safe` / `finalized` 是三个 RPC 标签；官方没有把 `safe` 写成 justified。」
