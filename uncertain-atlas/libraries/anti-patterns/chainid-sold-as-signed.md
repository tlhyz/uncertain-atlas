# 反模式：看见 chainId 被写成签名已经罩住这条链

> 真值：[chainId ≠ 已签](../../tracks/crypto/worked-example-chainid-vs-signed.md)、[不变式 161](../invariants/README.md)、[不变式 6](../invariants/README.md)。亲戚：[basefee-sold-as-tip](basefee-sold-as-tip.md)、[txid-sold-as-wtxid](txid-sold-as-wtxid.md)。

## 一句话

看见钱包写了 chainId 或规范编号 155，就把 JSON 字段写成已经编进签名哈希，或把旧六字段签写成已经防跨链重放，或把本页写成 1559 费用市场。

## 正确写法

「JSON 里的 chainId 不是已经编进签名哈希。旧六字段签不是已经防跨链重放。EIP-155 不是 EIP-1559。用户交易的链绑定不是投票域。」
