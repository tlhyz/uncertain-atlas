# 反模式：部分签名包被写成已经是网上能广播的交易

> 真值：[工作包 ≠ 已广播](../../tracks/implementation/worked-example-psbt-vs-broadcast.md)、[不变式 179](../invariants/README.md)、[不变式 174](../invariants/README.md)、[不变式 166](../invariants/README.md)。亲戚：[address-sold-as-utxo](address-sold-as-utxo.md)、[rbf-sold-as-replaced](rbf-sold-as-replaced.md)、[txid-sold-as-wtxid](txid-sold-as-wtxid.md)。

## 一句话

看见钱包导出一份部分签名包，就把它写成已经是网上能广播的完整交易，或把里面有几张签写成这一输入已经凑齐，或把 174 写成 173。

## 正确写法

「看见部分签名包不是已经是网上能广播的完整交易。里面有几张签不是这一输入已经凑齐。两份包能合并不是已经抽出网络序列化。抽出完整交易不是已经广播。BIP-174 不是 BIP-173，也不是 BIP-125。」
