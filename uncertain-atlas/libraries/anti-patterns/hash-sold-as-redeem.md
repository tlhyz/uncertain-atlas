# 反模式：付给脚本哈希被写成已经揭开赎回脚本

> 真值：[哈希 ≠ 已揭开赎回](../../tracks/state-models/worked-example-p2sh-hash-vs-redeem.md)、[不变式 170](../invariants/README.md)、[不变式 153](../invariants/README.md)、[不变式 144](../invariants/README.md)。亲戚：[keypath-sold-as-tree](keypath-sold-as-tree.md)、[policy-sold-as-consensus](policy-sold-as-consensus.md)。

## 一句话

看见输出写了脚本哈希或旧节点 HASH160 EQUAL 通过，就把赎回写成已经揭开，或把新节点写成已经再跑，或把 16 写成 13 地址 / 11 多重签 / Taproot 钥匙路径。

## 正确写法

「付给脚本哈希不是已经揭开赎回脚本。旧节点 HASH160 EQUAL 通过不是新节点已经再跑赎回。哈希对上不是内层已经验过。BIP-16 不是 BIP-13 地址，也不是 BIP-11 多重签，也不是 Taproot 钥匙路径。」
