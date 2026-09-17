# 反模式：进了 DAG 块被写成已经在 selected chain 上

> 真值：[DAG ≠ selected chain 工作实例](../../tracks/consensus/worked-example-dag-vs-selected-chain.md)、[不变式 137](../invariants/README.md)。亲戚：[snow-sold-as-qc](snow-sold-as-qc.md)、[poh-sold-as-tower](poh-sold-as-tower.md)、[header-equals-settlement](header-equals-settlement.md)。

## 一句话

看见 Kaspa「进了一个块」或看见「也是 DAG」，就把并行块 / mergeset / 蓝写成已经在 selected chain 上，或写成已经最终，或写成 Avalanche 抽样。

## 正确写法

「并行块留下再排序，不是已经 orphan 扔掉。进了某个块不是已经在 selected chain。Selected chain 决定顺序，并且可以 reorg。Accepting block 是合并它的链块。蓝不是 QC。这和 Avalanche 问邻居不是同一句。」
