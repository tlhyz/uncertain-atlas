# 反模式：把后继校验和写成已经是旧地址方案

## 一句话

把 `Bech32m` 写成已经是 `Bech32`，或把后继版本用旧校验和编出来的串写成已经合法。

## 看起来像什么

- 「后继地址也是 Bech32。」
- 「校验过了，就是 173 那一套。」
- 「用旧方案编后继版本也可以。」
- 「看见后继地址，就是已经有一笔 UTXO。」

## 为什么错

[BIP-350](https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki) 把后继见证版本改到新校验和，并要求解码器按版本选校验和。旧方案继续只服务 `v0`。校验过了只说明这一版校验和过了，不说明已经是另一版方案，也不说明已经有 UTXO。

## 正确分法

1. 先点名校验和版本。
2. 再点名见证版本。
3. 再问版本和校验和是否配对。
4. 最后才问这一串是不是已经对应 UTXO。

## 和相邻坑的差别

- 和 [`bech32-sold-as-utxo.md`](bech32-sold-as-utxo.md) 不同：那一条把地址写成已经有 UTXO；本条把后继校验和写成已经是旧方案。
- 和 [`psbt-sold-as-broadcast.md`](psbt-sold-as-broadcast.md) 不同：那一条把未完成交易对象写成已经能广播。
- 和 [`segwit-sold-as-txid.md`](segwit-sold-as-txid.md) 不同：那一条把隔离见证标识写成已经是旧交易标识。
