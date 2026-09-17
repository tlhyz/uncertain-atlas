# 反模式：已认证批次被写成已经写出共识序

> 真值：[Quorum Store ≠ 排序 工作实例](../../tracks/consensus/worked-example-quorum-store-vs-order.md)、[不变式 132](../invariants/README.md)。亲戚：[stm-done-sold-as-final](stm-done-sold-as-final.md)、[header-equals-settlement](header-equals-settlement.md)、[owned-sold-as-fastpath](owned-sold-as-fastpath.md)、[snow-sold-as-qc](snow-sold-as-qc.md)。

## 一句话

看见 Aptos「Quorum Store」或看见一批交易已经传开 / 已经认证，就把传播层写成已经写出 L，或把名字里的 quorum 写成已经 commit。

## 正确写法

「Quorum Store 按批次传播。已认证批次是给共识去排序的对象，不是已经排好的 L，更不是已经落盘。领袖仍提议。进了提议块不是已经持久化。」
