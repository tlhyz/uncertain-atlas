# 反模式：钥匙路径被写成已经揭开脚本树

> 真值：[钥匙路径 ≠ 已经揭开脚本树](../../tracks/implementation/worked-example-keypath-vs-scriptpath.md)、[不变式 153](../invariants/README.md)、[不变式 152](../invariants/README.md)。亲戚：[txid-sold-as-wtxid](txid-sold-as-wtxid.md)、[btc-lock-sold-as-commit](btc-lock-sold-as-commit.md)。

## 一句话

看见一笔只有签名的 Taproot 花费或一个 Taproot 输出，就把钥匙路径写成已经揭开有没有脚本树，或把脚本路径写成已经揭开全部脚本，或把输出本身写成已经能分辨付款给钥还是付款给脚本。

## 正确写法

「钥匙路径不是已经揭开有没有脚本树。脚本路径不是已经揭开全部脚本。看见 Taproot 输出不是已经知道它是付款给钥还是付款给脚本。」
