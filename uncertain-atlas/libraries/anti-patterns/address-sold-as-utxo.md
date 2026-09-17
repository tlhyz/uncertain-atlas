# 反模式：看见 Bech32 地址被写成链上已经有这笔输出

> 真值：[地址 ≠ 已有输出](../../tracks/implementation/worked-example-address-vs-utxo.md)、[不变式 174](../invariants/README.md)、[不变式 152](../invariants/README.md)、[不变式 170](../invariants/README.md)。亲戚：[hash-sold-as-redeem](hash-sold-as-redeem.md)、[txid-sold-as-wtxid](txid-sold-as-wtxid.md)、[type-sold-as-payload](type-sold-as-payload.md)。

## 一句话

看见 Bech32 地址或校验过了，就把链上写成已经有这笔输出，或把 173 写成 141 程序规则 / 350 后继校验，或把自动纠错写成已经改对。

## 正确写法

「看见 Bech32 地址串不是链上已经有这笔输出。校验过不是见证程序已经在链上。编出版本和程序不是已经付过款。BIP-173 不是 BIP-350，也不是 BIP-141，也不是 BIP-13。」
