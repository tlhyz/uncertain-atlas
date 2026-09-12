# 反模式：VRF 抽中被写成这块已经认证

> 真值：[VRF 抽签 ≠ 已认证 工作实例](../../tracks/consensus/worked-example-vrf-sortition-vs-certified.md)、[不变式 134](../invariants/README.md)。亲戚：[snow-sold-as-qc](snow-sold-as-qc.md)、[poh-sold-as-tower](poh-sold-as-tower.md)、[stake-sold-as-validator-quorum](stake-sold-as-validator-quorum.md)、[babe-sold-as-grandpa](babe-sold-as-grandpa.md)。

## 一句话

看见 Algorand「密码抽签」或看见某账户出示 VRF 证明，就把抽中 / 最低哈希 / soft vote 写成已经 certify，或把抽签写成 Avalanche 问邻居。

## 正确写法

「VRF 抽的是本步谁能提议或投票。抽中不是已经认证。最低 VRF 只用来收成一份提案。Soft vote 和 certify 是两步、两个委员会。参与钥不是花费钥。按 Algo 抽签不是一人一票，也不是问邻居。」
