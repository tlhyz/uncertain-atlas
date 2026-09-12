# 反模式：排序者 unsafe / 同名 RPC `safe` 被写成已经从 L1 推导或已经 Gasper

> 真值：[推导头工作实例](../../tracks/finality/worked-example-unsafe-vs-derived.md)、[不变式 141](../invariants/README.md)、[不变式 9](../invariants/README.md)。亲戚：[justified-sold-as-finalized](justified-sold-as-finalized.md)、[preconfirmed-sold-as-accepted](preconfirmed-sold-as-accepted.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)。

## 一句话

看见 OP Stack / Base 的 `latest` / `safe` / `finalized`，就把排序者尚未从 L1 推导的块写成已经 `safe`，或把 OP `safe` 写成 Gasper justified，或把 Standard Bridge 等待写成 L2 交易还没 finalized。

## 正确写法

「`unsafe` / `latest` 还没从 L1 推导。OP `safe` 是当前 canonical L1 可反推，不是 justified，也不是已经 `finalized`。L2 `finalized` 不是桥已经兑付。」
