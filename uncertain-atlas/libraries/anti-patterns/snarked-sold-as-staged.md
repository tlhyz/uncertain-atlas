# 反模式：SNARKed 被写成最新 staged

> 真值：[snarked ≠ staged 工作实例](../../tracks/light-clients/worked-example-snarked-vs-staged.md)、[不变式 123](../invariants/README.md)。亲戚：[proof-size-equals-chain](proof-size-equals-chain.md)、[header-equals-settlement](header-equals-settlement.md)、[l2-accepted-sold-as-l1](l2-accepted-sold-as-l1.md)、[proof-ok-equals-no-inflation](proof-ok-equals-no-inflation.md)。

## 一句话

看见递归证明验绿，或看见「整条历史已被证明」，就写成最新账户态已经被这枚证明保证，或把 Pickles 写成 Kimchi，或把进块写成已经进入 SNARKed ledger。

## 正确写法

「区块链 SNARK 点名的是 SNARKed ledger。staged 是已 Apply、尚未被该证明保证的当前账户态。验 π 不是已经有自己的账户与路径。Pickles 不是 Kimchi。」
