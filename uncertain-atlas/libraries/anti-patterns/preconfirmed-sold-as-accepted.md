# 反模式：排序者回执被写成已经 ACCEPTED_ON_L2 / L1

> 真值：[L2 档 ≠ L1 工作实例](../../tracks/finality/worked-example-l2-status-vs-l1.md)、[不变式 138](../invariants/README.md)、[不变式 28](../invariants/README.md)。亲戚：[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)、[justified-sold-as-finalized](justified-sold-as-finalized.md)、[poh-sold-as-tower](poh-sold-as-tower.md)。

## 一句话

看见 Starknet `CANDIDATE` / `PRE_CONFIRMED` 或看见「ZK」，就把排序者已写哈希或已打回执写成已经 `ACCEPTED_ON_L2`，或写成已经 `ACCEPTED_ON_L1`。

## 正确写法

「`CANDIDATE` 还没执行。`PRE_CONFIRMED` 是排序者回执，不是已经共识最终。`ACCEPTED_ON_L2` 不是已经 `ACCEPTED_ON_L1`。验的是当前登记的 program hash，不是物理定律。」
