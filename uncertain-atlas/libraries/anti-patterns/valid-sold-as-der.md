# 反模式：ECDSA 验得过被写成已经是严格 DER

> 真值：[验过 ≠ 已是 DER](../../tracks/implementation/worked-example-valid-vs-der.md)、[不变式 172](../invariants/README.md)、[不变式 144](../invariants/README.md)、[不变式 3](../invariants/README.md)。亲戚：[noncanonical-accepted](noncanonical-accepted.md)、[policy-sold-as-consensus](policy-sold-as-consensus.md)、[txid-sold-as-wtxid](txid-sold-as-wtxid.md)。

## 一句话

看见密码库收下一条签或转发策略已经要 DER，就把共识写成已经收下，或把 66 写成 62 延展菜谱 / 146 低 S / 34 整数版本。

## 正确写法

「ECDSA 数学上验得过不是已经是严格 DER。库接受某种变形不是共识已经接受。转发策略已经要 DER 不是共识已经要。BIP-66 不是 BIP-62，也不是 BIP-146，也不是 BIP-34。」
