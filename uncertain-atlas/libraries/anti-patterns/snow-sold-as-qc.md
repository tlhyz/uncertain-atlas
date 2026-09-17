# 反模式：抽样 α 多数被写成已经有一张可转发的 QC

> 真值：[Snow 抽样 ≠ QC 工作实例](../../tracks/consensus/worked-example-snow-sample-vs-qc.md)、[不变式 131](../invariants/README.md)。亲戚：[sample-sold-as-full-set](sample-sold-as-full-set.md)、[justified-sold-as-finalized](justified-sold-as-finalized.md)、[header-equals-settlement](header-equals-settlement.md)、[two-finality-sold-as-one](two-finality-sold-as-one.md)。

## 一句话

看见 Avalanche「也是 BFT」，或看见某一轮抽样已经 α 多数，就把本节点的连续置信写成可转发的 +2/3 证书，或把出块窗里的指定人写成已经替全网决定。

## 正确写法

「Snow 是反复子抽样。α 是这一撮样本里的多数，β 是本节点连续成功次数，都不是全集 QC。Preference 不是 LastAccepted。Snowman++ 出块窗是节奏，不是 Snowball 已经决定。」
